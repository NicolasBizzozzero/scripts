""" Module to remove empty folders recursively. Can be used as standalone
script or be imported into existing script.

Inspired by :
https://gist.github.com/jacobtomlinson/9031697
"""
import os
import sys


def remove_empty_folders(path, remove_root=True):
    """ Function to remove empty folders """
    if not os.path.isdir(path):
        return

    # remove empty subfolders
    files = os.listdir(path)
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                remove_empty_folders(fullpath)

    # if folder empty, delete it
    files = os.listdir(path)
    if len(files) == 0 and remove_root:
        print("Removing empty folder:", path)
        os.rmdir(path)


def usage_string():
    """ Return usage string to be output in error cases """
    return 'Usage: %s directory [remove_root]' % sys.argv[0]


def main():
    remove_root = True

    if len(sys.argv) < 1:
        print("Not enough arguments")
        sys.exit(usage_string())

    if not os.path.isdir(sys.argv[1]):
        print("No such directory %s" % sys.argv[1])
        sys.exit(usage_string())

    if len(sys.argv) == 3 and sys.argv[2] != "False":
        print("remove_root must be 'False' or not set")
        sys.exit(usage_string())
    else:
        remove_root = False

    remove_empty_folders(sys.argv[1], remove_root)


if __name__ == "__main__":
    main()
