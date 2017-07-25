""" Provide an iterator recursivey walking through each html file of a webpage. """
import re
import sys

_CODE_SUCCESS = 0
_CODE_ERROR_WRONG_NUMBER_ARGS = 1

_REGEX_URL = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

_TEMP_FILE_PATH = "~url_crawler.txt"


def main() -> None:
    global _CODE_SUCCESS

    url_adress = _parse_args(sys.argv)
    command = _format_command(url_adress, _TEMP_FILE_PATH)
    text_result = _launch_command(command)

    print(text_result)

    urls = _retrieve_urls(text_result)

    print(urls)
    exit(_CODE_SUCCESS)


def _parse_args(argv: List[str]) -> str:
    global _CODE_ERROR_WRONG_NUMBER_ARGS

    if len(argv) != 2:
        _print_usage()
        exit(_CODE_ERROR_WRONG_NUMBER_ARGS)
    else:
        return sys.argv[1]


def _format_command(url_adress: str, temp_file_path: str) -> List[str]:
    return [wget, "--spider", "--force-html", "--recursive",
            "--no-check-certificate", url_adress, "--output-file",
            temp_file_path]


def _launch_command(command: List[str]) -> str:
    pass


def _retrieve_urls(text: str) -> List[str]:
    global _REGEX_URL


if __name__ == '__main__':
    main()
