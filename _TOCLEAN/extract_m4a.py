# ffmpeg -ss 1:01:42 -i c:\Data\temp\in.m4a -vn -c copy -t 1:00:00 out.m4a

import re
import subprocess
import click


COMMAND_NAME = "ffmpeg"
DEFAULT_DURATION = "99:59:59"


@click.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_file", type=click.Path(exists=False))
@click.argument("timestamp")
@click.argument("duration")
def entrypoint_with_duration(input_file, output_file, timestamp,
                             duration) -> None:
    _assert_inputs(input_file, output_file, timestamp, duration)
    parameters = _compute_parameters(input_file, output_file, timestamp,
                                     duration)
    _execute_command(COMMAND_NAME, parameters)


@click.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_file", type=click.Path(exists=False))
@click.argument("timestamp")
def entrypoint_without_duration(input_file, output_file, timestamp) -> None:
    _assert_inputs(input_file, output_file, timestamp)
    parameters = _compute_parameters(input_file, output_file, timestamp,
                                     DEFAULT_DURATION)
    _execute_command(COMMAND_NAME, parameters)


def _assert_inputs(input_file: str, output_file: str, timestamp: str,
                   duration: str) -> None:
    assert input_file != output_file
    _assert_timeformat(timestamp)
    _assert_timeformat(duration)


# TODO: Write doctests
def _assert_timeformat(time: str) -> bool:
    time_format = r"\d\d:\d\d:\d\d"
    assert re.match(time_format, time)


def _compute_parameters(input_file: str, output_file: str, timestamp: str,
                        duration: str) -> str:
    return ["-ss", timestamp, "-i", input_file, "-vn", "-c", "copy", "-t",
            duration, output_file]


def _execute_command(command: str, *parameters: str, stdin=None, stdout=None,
                     stderr=None) -> int:
    """ Execute `command` in a subprocess and return the result code of the
    command.
    """
    result = subprocess.run([command, *parameters], stdin=stdin, input=None,
                            stdout=stdout, stderr=stderr, shell=False,
                            timeout=None, check=False)
    return_code = result.returncode
    return return_code


if __name__ == '__main__':
    pass
