from os import system as execute
from sys import argv


def get_websites_from_command_line() -> list:
    return argv[1:]


def get_websites_from_a_file() -> list:
    pass


def build_command(websites: list) -> str:
    command = "start chrome"
    for website in websites:
        command = "{} \"{}\"".format(command, website)
    return command


def main():
    # Get the websites from the command-line
    websites = get_websites_from_command_line()

    # Build and launch the command
    command = build_command(websites)
    execute(command)


if __name__ == '__main__':
    main()
