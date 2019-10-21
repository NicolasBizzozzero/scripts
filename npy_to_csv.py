""" Convert a file from the npy format into the CSV format.

\b
Dependencies:
* pandas >= 0.24.1
* numpy >= 1.16.2
"""

import os
import ntpath
import argparse

import pandas as pd
import numpy as np


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("npy_files", type=str, nargs="*",
                        help='npy files to convert.')
    parser.add_argument("--dir-dest", type=str, default=".",
                        help="Save all CSV files into this directory.")
    parser.add_argument("--delimiter", type=str, default=",",
                        help="Separator between data for the CSV file.")
    args = parser.parse_args()

    npy_to_csv(
        npy_files=args.npy_files,
        dir_dest=args.dir_dest,
        delimiter=args.delimiter
    )


def npy_to_csv(npy_files, dir_dest, delimiter):
    for file_path in npy_files:
        file_name = os.path.splitext(ntpath.basename(file_path))[0]
        file_path_dest = os.path.join(dir_dest, file_name + ".csv")

        array = load_npy_file(file_path)
        save_array_to_csv(array, path_dest=file_path_dest,
                          delimiter=delimiter)


def load_npy_file(path_file: str) -> np.ndarray:
    return np.load(path_file)


def save_array_to_csv(array: np.ndarray, path_dest: str, delimiter: str):
    pd.DataFrame(array).to_csv(path_dest, header=False, index=False,
                               sep=delimiter)


if __name__ == '__main__':
    main()
