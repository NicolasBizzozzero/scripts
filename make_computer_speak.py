from os import system
from sys import argv


script_location = r'"C:\Program Files\Jampal\ptts.vbs"'
filename = r"file_to_read.txt"


def string_concatenation(*strings: str) -> str:
    result = ""
    for string in strings:
        result = "{}{}".format(result, string)
    return result


def put_text_into_file(filename: str, text: str):
    with open(filename, 'w') as file:
        file.write(text)


def format_command(filename: str = "file_to_read.txt") -> str:
    return string_concatenation("cscript ", script_location, ' -u ', filename)


def run_command(command: str):
    system(command)


def main():
    if len(argv) > 1:
        # User has specified a text to read
        # overwrite the previous file
        put_text_into_file(filename, argv[1])

    # Read the file created
    command = format_command(filename)
    run_command(command)


if __name__ == '__main__':
    main()
