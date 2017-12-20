""" Infinitely click at a given coordinate until the next `KeyboardInterrupt`.
This script will click at the coordinate given as params, then click
infinitely until you stop the process. You can configure the waiting time
between each click.

Dependencies:
* pyautogui

Known bugs:

Error codes:
0 - Success
1 - Wrong number of arguments
"""
from __future__ import print_function
from sys import argv
import pyautogui
import time


_DEFAULT_SLEEPING_TIME = 0.5

_STR_USAGE = ("Usage: python infinite_click.py <X> <Y> "
              "[-t --sleeping-time <TIME>]")
_STR_WRONG_NUMBER_ARGUMENTS = "Error: Wrong number of arguments"

_CODE_SUCCESS = 0
_CODE_WRONG_NUMBER_ARGUMENT = 1


def main():
    if len(argv) <= 2:
        print(_STR_WRONG_NUMBER_ARGUMENTS)
        print(_STR_USAGE)
        exit(_CODE_WRONG_NUMBER_ARGUMENT)

    coordinates, sleeping_time = _parse_args(argv)

    _infinite_click(coordinates=coordinates, sleeping_time=sleeping_time)

    exit(_CODE_SUCCESS)


def _parse_args(argv):
    global _DEFAULT_SLEEPING_TIME

    coordinate_x = None
    coordinate_y = None
    sleeping_time = _DEFAULT_SLEEPING_TIME

    parse_sleeping_time = False
    for param in argv[1:]:
        if parse_sleeping_time:
            sleeping_time = float(param)
            break
        if param in ("-t", "--sleeping-time"):
            parse_sleeping_time = True
            continue
        else:
            # parsing coordinates
            if coordinate_x is None:
                coordinate_x = int(param)
            elif coordinate_y is None:
                coordinate_y = int(param)
            else:
                # I don't know what I just parsed
                pass
    return (coordinate_x, coordinate_y), sleeping_time


def _infinite_click(coordinates, sleeping_time):
    try:
        while True:
            pyautogui.click(*coordinates)
            time.sleep(sleeping_time)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
