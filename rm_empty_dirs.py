""" Remove empty folders recursively.

Inspired by :
* https://gist.github.com/jacobtomlinson/9031697

Known Bugs :

Error codes :
0 - Success
1 - Wrong number of arguments
2 - The root directory does not exists
"""
from sys import argv
from os import listdir, rmdir
from os.path import isdir, join


_STR_USAGE = "Usage: rm_empty_dirs.py <ROOT_DIR>"
_STR_WRONG_NUMBER_ARGUMENTS = "Error: Wrong number of arguments"
_STR_ROOT_DIRECTORY_NOT_EXISTS = "Error: Not such directory \"{dir}\""


_CODE_SUCCESS = 0
_CODE_WRONG_NUMBER_ARGUMENT = 1
_CODE_ROOT_DIRECTORY_NOT_EXISTS = 2


def main():
    if len(argv) != 2:
        print(_STR_WRONG_NUMBER_ARGUMENTS)
        print(_STR_USAGE)
        exit(_CODE_WRONG_NUMBER_ARGUMENT)

    # Unpacking arguments
    root_directory = argv[1]

    if not isdir(root_directory):
        print(_STR_ROOT_DIRECTORY_NOT_EXISTS)
        exit(_CODE_ROOT_DIRECTORY_NOT_EXISTS)

    _rm_empty_dir(root_directory)


def _rm_empty_dir(root_directory):
    """ Remove empty folders recursively. """
    if not isdir(root_directory):
        return

    # Remove empty subfolders
    for file in listdir(root_directory):
        fullpath = join(root_directory, file)
        if isdir(fullpath):
            _rm_empty_dir(fullpath)

    # if the root folder is empty, delete it
    nonempty_files = listdir(root_directory)
    if len(nonempty_files) == 0:
        rmdir(root_directory)


if __name__ == "__main__":
    main()
