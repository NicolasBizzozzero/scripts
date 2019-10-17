""" Take one or more JSON files of sorted dates paired with a value. Keys act as dates. Then plot the evolution of this
value with respects to time in a figure.
"""
import json
import collections
import argparse

import matplotlib.pyplot as plt


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("json_files", type=str, nargs="*",
                        help='Flat JSON files of sorted dates paired with a value. Keys act as dates.')
    args = parser.parse_args()

    for file in args.json_files:
        with open(file) as f:
            content = json.load(f, object_pairs_hook=collections.OrderedDict)

        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.title("Evolution of value wrt time for \"{file}\"".format(file=file))
        plt.xticks(rotation=45)

        plt.plot_date(content.keys(), content.values(), "-", tz=None, xdate=True)
    plt.show()


if __name__ == '__main__':
    main()
