""" Flatten a root directory.
Flattening a directory means moving all files from its subdirectories into the
root direcotry, then delete the empties directories.
"""
import argparse
import os
import pathlib
import shutil
import sys
import uuid


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root_directory', metavar='DIR', type=str,
                        help='Directory to flatten')
    args = parser.parse_args()

    flatten_directory(args.root_directory)
    remove_empty_dirs(args.root_directory)


def flatten_directory(root_directory):
    if not os.path.isdir(root_directory):
        return
    for file in pathlib.Path(root_directory).rglob("*"):
        if os.path.isfile(file):
            basename = os.path.basename(file)
            move_file(path_src=file,
                      path_dest=os.path.join(root_directory, basename))


def remove_empty_dirs(root_directory):
    """ Remove empty folders recursively. """
    if not os.path.isdir(root_directory):
        return
    for directory in pathlib.Path(root_directory).rglob("*"):
        if os.path.isdir(directory) and (len(os.listdir(directory)) == 0):
            os.rmdir(directory)


def move_file(path_src, path_dest, existing_strategy="uuid"):
    """ Move a file located at `path_src` into `path_dest`.
    If a file with the same name already exists at `path_dest`, one of the
    strategy specified with `existing_strategy` is used :
    - 'uuid': Append a "-" char followed by a UUID before the extension.
    - 'int': Append a "-" char followed by a unique integer before the
    extension.
    A file extension is defined as the last string behind a '.' character.
    Thus, the filename "file.png.txt" as for extension "txt". If no '.'
    character is presents in the filename, the file is considered without an
    extension.
    """
    if os.path.abspath(path_src) == os.path.abspath(path_dest):
        return
    if not os.path.isfile(path_dest):
        shutil.move(path_src, path_dest)
    else:
        basename = os.path.basename(path_dest)
        dirname = os.path.dirname(path_dest)
        split = basename.split(".")
        basename_without_ext, ext = ".".join(split[:-1]), split[-1]
        if existing_strategy == "uuid":
            str_uuid = uuid.uuid4().hex
            new_basename = basename_without_ext + "-" + str_uuid + "." + ext
        elif existing_strategy == "int":
            pass
        else:
            print("'existing_strategy'", existing_strategy, "does not exists.",
                  "File", path_src, "has not been moved.", file=sys.stderr)
        path_dest = os.path.join(dirname, new_basename)
        shutil.move(path_src, path_dest)


if __name__ == "__main__":
    main()
