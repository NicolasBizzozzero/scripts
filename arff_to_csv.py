""" Sequentially load one or multiple files in the ARFF format and save them in the CSV format.

All files are saved in the `dir_dest` directory with the same name as their respective arff file, but with the '.csv'
extension.
"""

import os
import ntpath
import argparse

import pandas as pd

from scipy.io import arff


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('arff_files', type=str, nargs="*",
                        help='Target host')
    parser.add_argument("--dir-dest", type=str, default=".",
                        help="Save all CSV files into this directory")
    parser.add_argument("--delimiter", type=str, default=",",
                        help="Separator between data for the CSV file")
    parser.add_argument("--ignore-header", action="store_true",
                        help="Do not save the original header into the CSV file")
    args = parser.parse_args()

    arff_to_csv(
        arff_files=args.arff_files,
        dir_dest=args.dir_dest,
        delimiter=args.delimiter,
        ignore_header=args.ignore_header
    )


def arff_to_csv(arff_files, dir_dest, delimiter, ignore_header):
    for file_path in arff_files:
        file_name = os.path.splitext(ntpath.basename(file_path))[0]
        file_path_dest = os.path.join(dir_dest, file_name + ".csv")

        df = load_arff_file(file_path)
        save_dataframe(df, destination=file_path_dest, delimiter=delimiter, header=not ignore_header)


def load_arff_file(file_path: str) -> pd.DataFrame:
    data, meta = arff.loadarff(file_path)
    return pd.DataFrame(data, columns=meta.names())


def save_dataframe(df: pd.DataFrame, destination: str, delimiter: str, header: bool) -> None:
    df.to_csv(destination, header=header, index=False, sep=delimiter)


if __name__ == '__main__':
    main()
