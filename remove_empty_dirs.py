""" Remove empty folders recursively. """
import argparse
import os
import pathlib


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root_directories', metavar='DIR', type=str, nargs='+',
                        help='Directories from which to delete all empty dirs')
    args = parser.parse_args()

    for root_directory in args.root_directories:
        remove_empty_dirs(root_directory)


def remove_empty_dirs(root_directory):
    """ Remove empty folders recursively. """
    if not os.path.isdir(root_directory):
        return
    for directory in pathlib.Path(root_directory).rglob("*"):
        if os.path.isdir(directory) and (len(os.listdir(directory)) == 0):
            os.rmdir(directory)


if __name__ == "__main__":
    main()
