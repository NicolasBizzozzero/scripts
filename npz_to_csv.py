""" Convert a file from the npz format into the CSV format.

\b
Newly created CSV files will have the following filename :
NPZFILENAME_ARRAYNAME.csv


\b
Dependencies:
* pandas >= 0.24.1
* numpy >= 1.16.2
"""

import os
import ntpath
import argparse

from typing import List, Optional

import pandas as pd
import numpy as np


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("npz_files", type=str, nargs="*",
                        help='npz files to convert.')
    parser.add_argument("--dir-dest", type=str, default=".",
                        help="Save all CSV files into this directory.")
    parser.add_argument("--delimiter", type=str, default=",",
                        help="Separator between data for the CSV file.")
    parser.add_argument("--extract-only", type=str, default=None,
                        help="Extract only array with this name.")
    args = parser.parse_args()

    npz_to_csv(
        npz_files=args.npz_files,
        dir_dest=args.dir_dest,
        delimiter=args.delimiter
    )


def npz_to_csv(npz_files, dir_dest, delimiter, extract_only):
    for file_path in npz_files:
        # Extract all arrays name from file
        array_names = extract_arrays_from_npz(file_path,
                                              extract_only=extract_only)
        for arr_name in array_names:
            file_name = "{file_name}_{array_name}".format(
                file_name=os.path.splitext(ntpath.basename(file_path))[0],
                array_name=arr_name
            )
            file_path_dest = os.path.join(dir_dest, file_name + ".csv")

            array = load_npz_file(file_path, arr_name)
            save_array_to_csv(array, path_dest=file_path_dest,
                              delimiter=delimiter)


def extract_arrays_from_npz(file_path: str,
                            extract_only: Optional[str] = None) -> List[str]:
    npz_file = np.load(file_path)
    if extract_only is None:
        return npz_file.files
    else:
        if extract_only in npz_file.files:
            return [extract_only]
        else:
            return []


def load_npz_file(file_path: str, array_name: str) -> np.ndarray:
    return np.load(file_path)[array_name]


def save_array_to_csv(array: np.ndarray, path_dest: str, delimiter: str):
    pd.DataFrame(array).to_csv(path_dest, header=False, index=False,
                               sep=delimiter)


if __name__ == '__main__':
    main()
