#!/bin/python
""" Extract files from most of common archive formats. """

import shutil
import argparse
import os


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("archive", type=str,
                        help='Archive file from which to extract.')
    parser.add_argument("-d", "--dir-dest", type=str, default=".",
                        help='Direction into which extract all files.')
    parser.add_argument("-k", "--keep", action='store_true',
                        help='Keep archive file after extraction.')
    args = parser.parse_args()

    extract(
        archive=args.archive,
        dir_dest=args.dir_dest,
        keep=args.keep
    )


def extract(archive, dir_dest, keep):
    shutil.unpack_archive(archive, dir_dest)
    if not keep:
        os.remove(archive)


if __name__ == '__main__':
    main()
