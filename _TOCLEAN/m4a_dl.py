""" Extract the M4A audio flux from a video located at a webpage.
The script can also download mutliple URLs from a file.
The file containing the URls must match the following format :
* One URL per line.
* Line not containing URL (not matched by the REGEX) are ignored.

Dependencies:
* youtube-dl

Error codes :
0 - Success
1 - Wrong number of arguments
2 - The file does not exists
"""
import sys
from os import system as run_command
import re


_DEFAULT_URL_REGEX = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+%")

_MAIN_COMMAND = "youtube-dl"
_PARAM_EXTRACT_AUDIO = "-f 140"
_PARAM_IGNORE_ERRORS = "--ignore-errors"
_PARAM_LIMIT_RATE = "--limit-rate {limit}K"  # In kilo-octet per seconds

_STR_USAGE = "Usage: python m4a_dl.py <URL> ... [-f --file <FILE>] [-r --regex <REGEX>] [-e --encoding <ENCODING>]"
_STR_WRONG_NUMBER_ARGUMENTS = "Error: Wrong number of arguments"
_STR_FILE_DOES_NOT_EXISTS = "Error: Not such file \"{file}\""

_CODE_SUCCESS = 0
_CODE_WRONG_NUMBER_ARGUMENT = 1
_CODE_FILE_DOES_NOT_EXISTS = 2


def main():
    if len(argv) <= 1:
        print(_STR_WRONG_NUMBER_ARGUMENTS)
        print(_STR_USAGE)
        exit(_CODE_WRONG_NUMBER_ARGUMENT)

    # Unpack parameters
    urls, url_regex, input_file, encoding = _parse_args(sys.argv)

    # Download URLs from command-line
    for url in urls:
        m4a_dl(url=url, url_regex=url_regex)

    # Download URLs from file
    if input_file:
        m4a_dl_file(file=input_file, url_regex=url_regex, encoding=encoding)

    exit(_CODE_SUCCESS)


def _parse_args(argv):
    global _DEFAULT_URL_REGEX

    urls = []
    url_regex = _DEFAULT_URL_REGEX
    input_file = None
    encoding = None

    parse_url_regex = False
    parse_input_file = False
    parse_encoding = False
    for param in argv[1:]:
        if parse_url_regex:
            parse_url_regex = False
            intensity = re.compile(param)
            continue
        if parse_input_file:
            parse_input_file = False
            input_file = param
            continue
        if parse_encoding:
            parse_encoding = False
            encoding = param
            continue

        if param in ("-r", "--regex"):
            parse_url_regex = True
            continue

        if param in ("-f", "--file"):
            parse_input_file = True
            continue

        if param in ("-e", "--encoding"):
            parse_encoding = True
            continue

        else:
            urls.append(param)
    return urls, url_regex, input_file, encoding


def m4a_dl(*, url, url_regex):
    """ Download the M4A flux from a video located at an URL. """
    pass


def m4a_dl_file(*, file, url_regex, encoding):
    """ Download the M4A flux of all the URLs stored in `file`. """
    for line in _iter_lines(file):
        if _is_url(line, url_regex=url_regex):
            pass


def _iter_lines(file, encoding="utf8"):
    """ Iterator yielding the content of a file line by line. """
    with open(file, encoding=encoding):
        for line in file:
            yield line


def _is_url(string, url_regex):


def _download_all_urls_from_file(path, encoding="utf8"):
    with open(path, encoding=encoding) as file:
        for url in file:
            if url:  # Prevent empty lines to produce wrong commands
                _download_audio(url)


def _download_audio(url):
    command = _format_command(url, PARAM_AUDIO_M4A)
    run_command(command)


def _check_errors(argv):
    if (len(argv) != 2):
        print("You need to pass at least one argument.\n", USAGE)
        exit(1)


def _format_command(url, *params):
    command = MAIN_COMMAND
    for param in params:
        command = "{} {}".format(command, param)
    return "{} {}".format(command, url)


if __name__ == '__main__':
    main()
