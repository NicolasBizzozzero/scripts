from os import system as exec
from sys import argv


path_to_WC_utility = r"C:\Program Files\wallpaperchanger\WallpaperChanger.exe"
backgrounds = []


def change_background(image: str, style: int = 2) -> None:
    """ Change the background of the computer. This function
        execute the open source utility "WallpaperChanger".
        You can find more informations about it here :
        https://github.com/philhansen/WallpaperChanger
    """
    global path_to_WC_utility
    exec("{} {} {}".format(path_to_WC_utility, image, style))


def print_usage() -> None:
    """ Print how to use this programm. """
    print("Usage: python switch_bg_date.py [image] [style]")


def main(image: str, style: int = 2):
    pass


if __name__ == '__main__':
    argc = len(argv)
    if argc <= 1:
        print("Error, you should pass at least one argument.")
        print_usage()
    elif argc == 2:
        main(argv[1])
    elif argc == 3:
        main(argv[1], argv[2])
    else:
        print("Error, too many arguments.")
        print_usage()
