""" Alter Github commit history.

Dependencies :
* https://github.com/NicolasBi/scripts/git_time.sh
"""

import subprocess
import datetime
import random


_RANGE_NUMBER_COMMIS = (1, 4)

_MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
           "Oct", "Nov", "Dec")
_FORMAT_TIME = "{month} {day} {hour}:{minute}:{second} {year} +0100"

_GIT_TIME_SCRIPT = "./git_time.sh"

_STR_WRONG_NUMBER_ARGUMENTS = "Error: Wrong number of arguments"
_STR_WRONG_TIME_FORMAT = ("Error, the time \"{time}\"must respect the ffmpeg "
                          "time format")

_CODE_SUCCESS = 0
_CODE_WRONG_NUMBER_ARGUMENT = 1
_CODE_WRONG_TIME_FORMAT = 2


def main():
    github_history_cheat()


def github_history_cheat():
    for month in _MONTHS[:-1]:
        for day in range(1, 28):
            today = datetime.datetime.now()
            commit_time = _FORMAT_TIME.format(month=month,
                                              day=day,
                                              hour=today.hour,
                                              minute=today.minute,
                                              second=today.second,
                                              year=today.year)

            # Let's commit
            for _ in range(random.randint(*_RANGE_NUMBER_COMMIS)):
                _execute_command(_GIT_TIME_SCRIPT, [commit_time])

    # Force push changes
    _execute_command("git", ["push", "origin", "master", "--force"])
    exit(_CODE_SUCCESS)


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
