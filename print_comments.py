from re import match, compile, findall
from enum import Enum
from sys import argv


class Language(Enum):
    NOT_SUPPORTED = 0
    C = 1


def get_language(filename: str) -> Language:
    extension = filename.split('.')[-1].lower()

    if extension in ('c', 'h'):
        return Language.C
    else:
        return Language.NOT_SUPPORTED


def get_file_content(filename: str) -> str:
    with open(filename) as file:
        content = file.readlines()
    content = "".join(content)
    return content


def get_comments(file_content: str, language: Language) -> list:
    regex = None
    if language == Language.C:
        regex = r"(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)"

    regex = compile(regex)
    results = findall(regex, file_content)
    return results


def print_comments(comments: list) -> None:
    for comment in comments:
        print(comment)


def main():
    for file in argv[1:]:
        print_comments(get_comments(
            get_file_content(file), get_language(file)))


if __name__ == '__main__':
    main()
