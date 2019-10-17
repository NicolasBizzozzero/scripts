#!/usr/bin/env python3
""" Convert a JSON file to a Pretty-Printed version. """
import json
import collections
import argparse


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("path_files", type=str, nargs="+",
                        help='JSON files to Pretty-Print')
    parser.add_argument("-s", "--sort-keys", action='store_true',
                        help="Sort the keys before rewritting the JSON file")
    parser.add_argument("-i", "--indent", type=int, default=4,
                        help="Number of spaces to add for each indentation level")
    parser.add_argument("--item-separator", type=str, default=",",
                        help="Character acting as a separator for each item")
    parser.add_argument("--key-separator", type=str, default=":",
                        help="Character acting as a separator for each key")
    args = parser.parse_args()

    for path_file in args.path_files:
        ppjson(
            path_file=path_file,
            sort_keys=args.sort_keys,
            indent=args.indent,
            item_separator=args.item_separator,
            key_separator=args.key_separator
        )


def ppjson(path_file: str, sort_keys: bool = False, indent: int = 4, item_separator: str = ",",
           key_separator: str = ":"):
    with open(path_file, "rb") as fp:
        obj = json.load(fp=fp, object_pairs_hook=collections.OrderedDict)
    with open(path_file, "w") as fp:
        json.dump(obj=obj, fp=fp, skipkeys=False, allow_nan=True, indent=indent,
                  separators=(item_separator, key_separator), sort_keys=sort_keys, cls=None)


if __name__ == '__main__':
    main()
