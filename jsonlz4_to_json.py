""" Decompress JSONlz4 files into human-readable JSON files.

\b
Dependencies:
* lz4 >= 2.1.6

\b
Source:
* https://unix.stackexchange.com/a/497861
"""

import ntpath
import os
import json
import glob
import argparse

import lz4.block as lz4block


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("jsonlz4_files", type=str, nargs="*",
                        help='jsonlz4 files to convert.')
    parser.add_argument("--dir-dest", type=str, default=".",
                        help="Save all CSV files into this directory.")
    parser.add_argument("--encoding", type=str, default=None,
                        help="Encoding used to load the jsonlz4 files.")
    parser.add_argument("-i", "--indent", type=int, default=4,
                        help="Number of spaces acting as indentation for output files.")
    args = parser.parse_args()

    jsonlz4_to_json(
        jsonlz4_files=args.jsonlz4_files,
        dir_dest=args.dir_dest,
        encoding=args.encoding,
        indent=args.indent
    )


def jsonlz4_to_json(jsonlz4_files, dir_dest, encoding, indent):
    # Unpacking star-like filepath (for windows cmd shell)
    # Also removing duplicate filenames.
    files = set()
    for file in jsonlz4_files:
        for subfile in glob.glob(file):
            files.add(subfile)

    for file_path in files:
        file_name = os.path.splitext(ntpath.basename(file_path))[0]
        file_path_dest = os.path.join(dir_dest, file_name + ".json")

        content = load_jsonlz4_file(file_path, encoding=encoding)
        save_json_file(content, destination=file_path_dest, indent=indent)


def load_jsonlz4_file(file_path: str, encoding: str) -> dict:
    with open(file_path, "rb") as bytestream:
        bytestream.read(8)  # Skip past the b"mozLz40\0" header
        content = lz4block.decompress(bytestream.read()).decode(encoding)
        return json.loads(content)


def save_json_file(content: dict, destination: str, indent: int) -> None:
    if indent <= 0:
        indent = None
    with open(destination, "w") as file:
        json.dump(content, file, ensure_ascii=False, indent=indent)


if __name__ == '__main__':
    main()
