""" Change the extension of all files present in the directory.
This script will crawl through all the files present in the current directory,
and change their extension to the one passed by argument.

Known Bugs :
* If two files with the same base name but a different extension are in the
same directory, Python will raise an FileExistsError. More generally, Python
will never erase a file by itself. This'll be kept as a feature for safety
reasons.

Error codes :
0 - Success
1 - Wrong number of arguments
2 - An extension swapping as failed because the new file already exists
"""
from __future__ import print_function
from os import rename, listdir
from os.path import basename, splitext
from sys import argv


_STR_USAGE = "Usage: python extension_cwd.py <EXTENSION>"
_STR_WRONG_NUMBER_ARGUMENTS = "Error: Wrong number of arguments"
_STR_FILE_EXISTS = ("Error: Can't change the extension of \"{old_name}\" "
                    "with \"{extension}\" without erasing the file "
                    "\"{existing_file}\"")

_CODE_SUCCESS = 0
_CODE_WRONG_NUMBER_ARGUMENT = 1
_CODE_FILE_EXISTS = 2


def main():
    if len(argv) <= 1:
        print(_STR_WRONG_NUMBER_ARGUMENTS)
        print(_STR_USAGE)
        exit(_CODE_WRONG_NUMBER_ARGUMENT)

    # Unpacking arguments
    extension = argv[1]

    _extension_cwd(extension=extension)

    exit(_CODE_SUCCESS)


def _extension_cwd(extension):
    """ Crawl through all the files present in the current directory, and
    change their extension to the one passed by argument.
    Will intentionaly ignore one file name (the name of the script itself).
    """
    script_name = basename(__file__)
    for old_name in listdir("."):
        # Doesn't rename the script itself
        if old_name != script_name:
            new_name = _change_extension(file=old_name, extension=extension)
            try:
                rename(old_name, new_name)
            except FileExistsError:
                print(_STR_FILE_EXISTS.format(old_name=old_name,
                                              extension=extension,
                                              existing_file=new_name))
                exit(_CODE_FILE_EXISTS)


def _change_extension(file, extension):
    """ Return `file` with its previous extension swapped with `extension`.
    """
    file_name = splitext(basename(file))[0]
    return _strcnt(file_name, ".", extension)


def _strcnt(*strings):
    """ Return the concatenation of all the strings passed as argument. """
    result = ""
    for string in strings:
        result = "{result}{string}".format(result=result, string=string)
    return result


if __name__ == '__main__':
    main()
