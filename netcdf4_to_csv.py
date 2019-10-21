""" Convert a file from the netCDF4 format into the CSV format.

\b
It assumes the data you are trying to convert is in the following format :
dim1, dim2, ..., dimn, timestamp, value

\b
Dependencies:
* netCDF4 >= 1.5.0
* pandas >= 0.24.1
"""

import os
import ntpath
import argparse

from functools import reduce
from collections import OrderedDict

import numpy as np
import pandas as pd

from netCDF4 import Dataset


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("netcdf4_files", type=str, nargs="*",
                        help='netcdf4 files to convert.')
    parser.add_argument("--dir-dest", type=str, default=".",
                        help="Save all CSV files into this directory.")
    parser.add_argument("--delimiter", type=str, default=",",
                        help="Separator between data for the CSV file.")
    parser.add_argument("--encoding", type=str, default=None,
                        help="Encoding used to load the netCDF4 files.")
    parser.add_argument("--ignore-header", action="store_true",
                        help="Do not save the original header into the CSV file.")
    args = parser.parse_args()

    netcdf4_to_csv(
        netcdf4_files=args.netcdf4_files,
        dir_dest=args.dir_dest,
        delimiter=args.delimiter,
        encoding=args.encoding,
        ignore_header=args.ignore_header
    )


def netcdf4_to_csv(netcdf4_files, dir_dest, delimiter, encoding, ignore_header):
    for file_path in netcdf4_files:
        file_name = os.path.splitext(ntpath.basename(file_path))[0]
        file_path_dest = os.path.join(dir_dest, file_name + ".csv")

        df = load_netcdf4_file(file_path, encoding=encoding)
        save_dataframe(df, destination=file_path_dest,
                       delimiter=delimiter, header=not ignore_header)


def load_netcdf4_file(file_path: str, encoding: str) -> pd.DataFrame:
    data = Dataset(file_path, "r", encoding=encoding)
    header = []
    dtypes = []
    features = []

    for variable in data.variables.values():
        name = variable.long_name + " (%s)" % variable.units
        header.append(name)
        dtypes.append(variable.dtype)
        features.append(variable[...])

    # Reorder data to match the following pattern :
    # timestamp, dim1, dim2, ..., dimn, value
    header = [header[-2]] + header[:-2] + [header[-1]]
    dtypes = [dtypes[-2]] + dtypes[:-2] + [dtypes[-1]]
    features = [features[-2]] + features[:-2] + [features[-1]]

    # Compute the "CUBE" OLAP command across whole dataset
    number_of_rows = reduce(lambda a, b: a * b, features[-1].shape)
    for i_feature in range(len(features) - 2):
        features[i_feature] = \
            np.repeat(features[i_feature], number_of_rows //
                      features[i_feature].shape[0])
    features[-2] = \
        np.tile(features[-2], number_of_rows //
                features[-2].shape[0])
    features[-1] = features[-1].flatten()

    # New convert the dataset into a pandas dataframe
    data = OrderedDict()
    for name, feature, dtype in zip(header, features, dtypes):
        data[name] = pd.Series(feature, dtype=dtype)
    return pd.DataFrame(data, columns=header)


def save_dataframe(df: pd.DataFrame, destination: str, delimiter: str,
                   header: bool) -> None:
    df.to_csv(destination, header=header, index=False, sep=delimiter)


if __name__ == '__main__':
    main()
