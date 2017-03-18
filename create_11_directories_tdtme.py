from sys import argv
from os import mkdir


def get_usage() -> str:
    return "Usage : python create_11_directories_tdtme.py directory"


def create_directory(path: str, dirname: str):
    directory_full_name = string_concatenation(path, '/', dirname)
    mkdir(directory_full_name)
    print("Created directory :" + directory_full_name)


def create_directories(path: str,
                       dirname: str = "TD-TME",
                       separator: str = ' ',
                       number_of_directories: int = 11):
    for dir_counter in range(1, number_of_directories + 1):
        create_directory(path, string_concatenation(dirname,
                                                    separator,
                                                    str(dir_counter)))


def string_concatenation(*strings: str) -> str:
    result = ""
    for string in strings:
        result = "{}{}".format(result, string)
    return result


def main():
    if len(argv) <= 1:
        print("You need to pass at least one argument.")
        print(get_usage())
        exit(1)

    path = argv[1]
    create_directories(path)


if __name__ == '__main__':
    main()
