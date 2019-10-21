""" Extract parts of a m4a file using ffmpeg.

Dependencies :
* ffmpeg
"""

import re
import subprocess
import argparse


_FORMAT_TIME = r"\d\d:\d\d:\d\d"

_MAIN_COMMAND = "ffmpeg"
_PARAM_START = "-ss"
_PARAM_INPUT = "-i"
_PARAM_DURATION = "-t"
_PARAM_NO_VIDEO = "-vn"
_PARAM_CODEC = "-c"
_PARAM_CODEC_COPY = "copy"

_STR_WRONG_NUMBER_ARGUMENTS = "Error: Wrong number of arguments"
_STR_WRONG_TIME_FORMAT = ("Error, the time \"{time}\"must respect the ffmpeg "
                          "time format")

_CODE_SUCCESS = 0
_CODE_WRONG_NUMBER_ARGUMENT = 1
_CODE_WRONG_TIME_FORMAT = 2


def main() -> None:
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("input_file", type=str,
                        help='File from which to extract the audio')
    parser.add_argument("output_file", type=str,
                        help='File from which to write the audio')
    parser.add_argument("timestamp", type=str,
                        help='Timestamp from where to start extracting the audio')
    parser.add_argument("--duration", type=str, default="99:59:59",
                        help='The duration of the slicing.')
    args = parser.parse_args()

    m4a_slicing(
        input_file=args.input_file,
        output_file=args.output_file,
        timestamp=args.timestamp,
        duration=args.duration
    )


def m4a_slicing(input_file, output_file, timestamp, duration) -> None:
    _assert_timeformat(timestamp)
    _assert_timeformat(duration)

    parameters = _format_params(input_file, output_file, timestamp,
                                duration)
    print(parameters)
    _execute_command(_MAIN_COMMAND, parameters)
    exit(_CODE_SUCCESS)


def _assert_timeformat(time: str) -> None:
    """ Exit the script with the proper error message and time code if the
    timestamp passed as parameter does not match the format required by
    'ffmpeg'.
    """
    if not re.match(_FORMAT_TIME, time):
        click.echo(_STR_WRONG_TIME_FORMAT)
        exit(_CODE_WRONG_TIME_FORMAT)


def _format_params(input_file: str, output_file: str, timestamp: str,
                   duration: str) -> str:
    """ Format the parameters to match the syntax required by 'ffmpeg'. """
    global _PARAM_START, _PARAM_INPUT, _PARAM_NO_VIDEO, _PARAM_CODEC,\
        _PARAM_CODEC_COPY, _PARAM_DURATION

    return [_PARAM_START, timestamp, _PARAM_INPUT, input_file,
            _PARAM_NO_VIDEO, _PARAM_CODEC, _PARAM_CODEC_COPY, _PARAM_DURATION,
            duration, output_file]


def _execute_command(command: str, parameters: str, stdin=None, stdout=None,
                     stderr=None) -> int:
    """ Execute `command` in a subprocess and return the result code of the
    command.
    """
    result = subprocess.run([command, *parameters], stdin=stdin, input=None,
                            stdout=stdout, stderr=stderr, shell=False,
                            timeout=None, check=False)
    return result.returncode


if __name__ == '__main__':
    main()
