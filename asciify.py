""" Convert all non-ASCII characters of the file passed by argument to their
ASCII counterpart (or a default symbol).

Known Bugs :

Error codes :
0 - Success
1 - Wrong number of arguments
2 - Renaming a file as failed because the new file already exists
3 - A file passed by argument has not been found
"""
from __future__ import print_function
from sys import argv
from os import rename
import unicodedata


_DEFAULT_CHAR = "_"

_STR_USAGE = "Usage: python asciify.py <FILES> ... [-d --default-char <CHAR>]"
_STR_WRONG_NUMBER_ARGUMENTS = "Error: Wrong number of arguments"
_STR_FILE_EXISTS = ("Error: Can't rename \"{old_name}\" into \"{new_name}\" "
                    "without erasing an existing file")
_STR_FILE_NOT_FOUND = "Error: Can't find the file \"{file}\""

_CODE_SUCCESS = 0
_CODE_WRONG_NUMBER_ARGUMENT = 1
_CODE_FILE_EXISTS = 2
_CODE_FILE_NOT_FOUND = 3


def main():
    if len(argv) <= 1:
        print(_STR_WRONG_NUMBER_ARGUMENTS)
        print(_STR_USAGE)
        exit(_CODE_WRONG_NUMBER_ARGUMENT)

    files, default_char = _parse_args(argv)

    asciify(files=files, default_char=default_char)

    exit(_CODE_SUCCESS)


def _parse_args(argv):
    global _DEFAULT_CHAR

    default_char = _DEFAULT_CHAR
    files = []

    parse_default_char = False
    for param in argv[1:]:
        if parse_default_char:
            parse_default_char = False
            default_char = param
            continue
        if param in ("-d", "--default-char"):
            parse_default_char = True
            continue
        else:
            files.append(param)
    return files, default_char


def asciify(*, files, default_char):
    for file in files:
        if not _is_ASCII(file):
            new_name = _convert_to_ascii(string=file,
                                         default_char=default_char)
            try:
                rename(file, new_name)
            except FileExistsError:
                print(_STR_FILE_EXISTS.format(old_name=file,
                                              new_name=new_name))
                exit(_CODE_FILE_EXISTS)
            except FileNotFoundError:
                print(_STR_FILE_NOT_FOUND.format(file=file))


def _is_ASCII(string):
    """ Return True if string contain only ASCII characters. Extended-ASCII
    characters are not considered as ASCII characters.
    """
    try:
        string.encode("ascii")
    except UnicodeEncodeError:
        return False
    return True


def _convert_to_ascii(string, default_char):
    """ Convert all non-ASCII chars contained in a string to their ASCII
    counterpart or to a default character.
    """
    string_ASCII = ""
    for char in string:
        if not _is_ASCII(char):
            string_ASCII = _strcnt(string_ASCII, _get_ASCII_char(char,
                                                                 default_char))
        else:
            string_ASCII = _strcnt(string_ASCII, char)
    return string_ASCII


def _strcnt(*strings):
    """ Return the concatenation of all the strings passed as argument. """
    result = ""
    for string in strings:
        result = "{result}{string}".format(result=result, string=string)
    return result


def _get_ASCII_char(char, default_char):
    """ Return the ASCII counterpart of `char`, or `default_char` if it does
    not exists.
    """
    try:
        cleaned_char = unicodedata.normalize("NFKD", char)[0]
        if not _is_ASCII(cleaned_char):
            return default_char
        return cleaned_char
    except IndexError:
        # The char is too complex to be interpreted as ASCII
        return default_char


if __name__ == '__main__':
    main()
