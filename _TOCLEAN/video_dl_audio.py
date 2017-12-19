import sys
from os import system as run_command


USAGE = "Usage : video_dl_audio.py [file]"

MAIN_COMMAND = "youtube-dl"
PARAM_AUDIO_M4A = "-f 140"
PARAM_IGNORE_ERRORS = "--ignore-errors"
PARAM_LIMIT_RATE = "--limit-rate {limit}K"


def main_entry_point() -> None:
    _check_errors(sys.argv)

    downloads_file = sys.argv[1]
    _download_all_urls_from_file(path=downloads_file)


def _download_all_urls_from_file(path: str, encoding: str = "utf8") -> None:
    with open(path, encoding=encoding) as file:
        for url in file:
            if url:  # Prevent empty lines to produce wrong commands
                _download_audio(url)


def _download_audio(url: str) -> str:
    command = _format_command(url, PARAM_AUDIO_M4A)
    run_command(command)


def _check_errors(argv: dict) -> None:
    if (len(argv) != 2):
        print("You need to pass at least one argument.\n", USAGE)
        exit(1)


def _format_command(url: str, *params) -> str:
    command = MAIN_COMMAND
    for param in params:
        command = "{} {}".format(command, param)
    return "{} {}".format(command, url)


if __name__ == '__main__':
    main_entry_point()
