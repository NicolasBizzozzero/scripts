from os import getcwd
from sys import argv


def get_working_directory() -> str:
    return getcwd()


def create_a_lot_of_files(filepath: str, extension: str, number: int,
                          content: str = "") -> None:
    if extension[0] == '.':
        extension = extension[1:]
    while number > 0:
        create_file("{}{}.{}".format(filepath, number, extension), content)
        number -= 1


def create_file(filepath: str, content: str = "") -> None:
    with open(filepath, 'w') as file:
        file.write(content)


def print_usage() -> None:
    print("Usage: pourrir_repertoire.py filename number_of_files [content]")


def main(filename: str, number_of_files: int, content: str = "") -> None:
    working_directory = get_working_directory()
    create_a_lot_of_files("{}/{}".format(working_directory,
                                         filename),
                          "txt", number_of_files, content)


if __name__ == "__main__":
    if len(argv) <= 2:
        print("You need to pass at least 2 arguments.")
        print_usage()
    elif len(argv) == 3:
        main(argv[1], int(argv[2]))
    elif len(argv) == 4:
        main(argv[1], int(argv[2]), argv[3])
    else:
        print("Too many arguments.")
        print_usage()
