""" Remove suffixes from all files matching a REGEX. """

import re
import os
import glob
import argparse
import sys
import shutil
import ntpath


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("path_dir", type=str,
                        help='Directory from which to process files')
    parser.add_argument("suffix", type=str,
                        help="REGEX applied to all files, including their extension. If this REGEX match on a file, "
                             "all match present in this file will be deleted.")
    parser.add_argument("-r", "--recursive", action='store_true',
                        help='Also process files from subdirectories')
    parser.add_argument("-s", "--existing-file-strategy", choices=["error", "warning", "unique_name", "erase"],
                        default="warning",
                        help="How to handle already existing files before renaming them. Choices are :\n"
                             "* 'error': Raise an error and stop the script.\n"
                             "* 'warning': Raises a warning to stderr and continue the script.\n"
                             "* 'unique_name': Create a guaranted unique name for the new file "
                             "by appending a number to it.\n"
                             "* 'erase': Erase the already existing file.")
    args = parser.parse_args()

    remove_suffix(
        path_dir=args.path_dir,
        suffix=args.suffix,
        existing_file_srategy=args.existing_file_srategy,
        recursive=args.recursive
    )


def remove_suffix(path_dir: str, suffix: str, existing_file_srategy: str = "warning", recursive: bool = False):
    for file in iter_files(path_dir=path_dir, recursive=recursive, sort=False):
        dirname, filename = os.path.dirname(file), os.path.basename(file)

        # Check if filename contains the pattern
        res = re.sub(suffix, "", filename)
        if res != filename:
            rename_file(file, os.path.join(dirname, res),
                        existing_file_srategy=existing_file_srategy)


def iter_files(path_dir: str, recursive: bool = False, sort: bool = False) -> str:
    if recursive:
        glob_expr = "./**/*"
    else:
        glob_expr = "./*"

    if sort:
        iterable = sorted(glob.glob(glob_expr, recursive=recursive))
    else:
        iterable = glob.glob(glob_expr, recursive=recursive)

    for file in iterable:
        if os.path.isfile(file):
            yield file


def rename_file(path_file_src: str, path_file_dest: str, strategy: str = "warning"):
    if os.path.exists(path_file_dest):
        if strategy == "error":
            raise OSError("Cannot rename \"{}\" into \"{}\", file already "
                          "exists.".format(path_file_src, path_file_dest))
            exit(2)
        elif strategy == "warning":
            print("Cannot rename \"{}\" into \"{}\", file already "
                  "exists.".format(path_file_src, path_file_dest), file=sys.stderr)
        elif strategy == "unique_name":
            new_path_file_dest = generate_unique_filename(path_file_dest)
            shutil.move(path_file_src, new_path_file_dest)
        elif strategy == "erase":
            shutil.move(path_file_src, path_file_dest)
    else:
        shutil.move(path_file_src, path_file_dest)


def generate_unique_filename(filepath: str, separator: str = "_") -> str:
    if os.path.isfile(filepath):
        dir_name = ntpath.dirname(filepath)
        dir_name = "." if dir_name == "" else dir_name
        base_name = get_file_basename(filepath)
        ext = get_file_extension(filepath)
        ext = "." + ext if ext != "" else ext

        suffix = 1
        new_filename = "{}{}{}{}".format(
            base_name,
            separator,
            str(suffix),
            ext
        )
        new_filepath = os.path.join(dir_name, new_filename)
        while os.path.isfile(new_filepath):
            suffix += 1
            new_filename = "{}{}{}{}".format(
                separator.join(new_filename.split(separator)[:-1]),
                separator,
                str(suffix),
                ext
            )
            new_filepath = os.path.join(dir_name, new_filename)
        return new_filepath
    else:
        return filepath


def get_file_basename(file_name: str) -> str:
    file_name = ntpath.basename(file_name)
    assert len(file_name) > 0,\
        "Your file name must contains at least one character."

    if file_name[0] != "." and '.' in file_name:
        return ".".join(os.path.basename(file_name).split(".")[:-1])
    elif file_name[0] == "." and '.' in file_name[1:]:
        return ".".join(os.path.basename(file_name).split(".")[:-1])
    else:
        return file_name


def get_file_extension(file_name: str) -> str:
    file_name = ntpath.basename(file_name)
    assert len(file_name) > 0,\
        "Your file name must contains at least one character."

    if file_name[0] != "." and '.' in file_name:
        return file_name.split(".")[-1]
    elif file_name[0] == "." and '.' in file_name[1:]:
        return file_name.split(".")[-1]
    else:
        return ""


if __name__ == '__main__':
    main()
