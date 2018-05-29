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
import os
import re


_DEFAULT_URL_REGEX = re.compile(
    r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

_MAIN_COMMAND = "youtube-dl"
_PARAM_EXTRACT_AUDIO = "-f 140"
_PARAM_IGNORE_ERRORS = "--ignore-errors"
_PARAM_LIMIT_RATE = "--limit-rate {limit}K"  # In kilo-octet per seconds

_STR_USAGE = ("Usage: python m4a_dl.py <URL> ... "
              "[-f --file <FILE>] "
              "[-r --regex <REGEX>] "
              "[-e --encoding <ENCODING>] "
              "[-l --limit-rate <LIMIT>]")
_STR_WRONG_NUMBER_ARGUMENTS = "Error: Wrong number of arguments"
_STR_FILE_DOES_NOT_EXISTS = "Error: Not such file \"{file}\""
_STR_NOT_URL = "The following parameter is not a valid URL : \"{string}\""

_CODE_SUCCESS = 0
_CODE_WRONG_NUMBER_ARGUMENT = 1
_CODE_FILE_DOES_NOT_EXISTS = 2


def main():
    if len(sys.argv) <= 1:
        print(_STR_WRONG_NUMBER_ARGUMENTS)
        print(_STR_USAGE)
        exit(_CODE_WRONG_NUMBER_ARGUMENT)

    # Unpack parameters
    urls, url_regex, input_file, encoding, limit_rate = _parse_args(sys.argv)

    # Download URLs from command-line
    for url in urls:
        m4a_dl(url=url, url_regex=url_regex, limit_rate=limit_rate)

    # Download URLs from file
    if input_file:
        m4a_dl_file(file=input_file, url_regex=url_regex, encoding=encoding,
                    limit_rate=limit_rate)

    exit(_CODE_SUCCESS)


def _parse_args(argv):
    global _DEFAULT_URL_REGEX

    urls = []
    url_regex = _DEFAULT_URL_REGEX
    input_file = None
    encoding = None
    limit_rate = None

    parse_url_regex = False
    parse_input_file = False
    parse_encoding = False
    parse_limit_rate = False
    for param in argv[1:]:
        if parse_url_regex:
            parse_url_regex = False
            url_regex = re.compile(param)
            continue
        if parse_input_file:
            parse_input_file = False
            input_file = param
            continue
        if parse_encoding:
            parse_encoding = False
            encoding = param
            continue
        if parse_limit_rate:
            parse_limit_rate = False
            limit_rate = float(param)
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

        if param in ("-l", "--limit-rate"):
            parse_limit_rate = True
            continue

        else:
            urls.append(param)
    return urls, url_regex, input_file, encoding, limit_rate


def m4a_dl(*, url, url_regex, limit_rate):
    """ Download the M4A flux from a video located at an URL. """
    if _is_url(url, url_regex):
        _download(url=url, limit_rate=limit_rate)
    else:
        print(_STR_NOT_URL.format(string=url))


def m4a_dl_file(*, file, url_regex, encoding, limit_rate):
    """ Download the M4A flux of all the URLs stored in `file`. """
    if not os.path.isfile(file):
        print(_STR_FILE_DOES_NOT_EXISTS)
        exit(_CODE_FILE_DOES_NOT_EXISTS)

    for line in _iter_lines(file):
        if _is_url(line, url_regex=url_regex):
            _download(url=line, limit_rate=limit_rate)


def _iter_lines(file, encoding="utf8"):
    """ Iterator yielding the content of a file line by line. """
    with open(file, encoding=encoding) as file:
        for line in file:
            yield line


def _is_url(string, url_regex):
    """ Return a boolean corresponding to the matching of `string` by the
    URL's REGEX provided.
    """
    return True if re.match(url_regex, string) else False


def _download(url, limit_rate):
    command = _format_command(url, limit_rate)
    os.system(command)


def _format_command(url, limit_rate):
    """ Format a 'youtube-dl' command which'll be called by a terminal. """
    global _MAIN_COMMAND, _PARAM_EXTRACT_AUDIO, _PARAM_IGNORE_ERRORS,\
        _PARAM_LIMIT_RATE

    command = "{} {}".format(
        _MAIN_COMMAND, _PARAM_EXTRACT_AUDIO, _PARAM_IGNORE_ERRORS)
    if limit_rate:
        command = "{} {}".format(
            command, _PARAM_LIMIT_RATE.format(limit=limit_rate))
    return "{} {}".format(command, url)


if __name__ == '__main__':
    main()
