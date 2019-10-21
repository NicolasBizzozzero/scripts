#!/usr/bin/python3
""" Process a gridsearch over a command parameters read from a JSON file. """

import itertools
import json
import subprocess
import argparse

from collections import OrderedDict


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("command", type=str,
                        help='Command to execute.')
    parser.add_argument("json_files", type=str, nargs="*",
                        help="JSON files containing parameters combinations of the command.")
    args = parser.parse_args()

    gridrun(
        command=args.command,
        json_files=args.json_files
    )


def gridrun(command, json_files):
    for json_file in json_files:
        with open(json_file) as file:
            parameters = json.load(file, object_pairs_hook=OrderedDict)

        param_keys = list(parameters.keys())

        # Convert unique parameters to a list with a single elements.
        # Make them iterable.
        param_values = list(map(lambda v: v if isinstance(v, list) else [v],
                                parameters.values()))

        # Compute the grid of parameters, all possibles and uniques
        # combinations
        grid = list(itertools.product(*param_values))

        for values in grid:
            command_parameters = dict_to_command_parameters(param_keys,
                                                            values)
            execute(command, *command_parameters)


def execute(command: str, *parameters: str, stdin=None, stdout=None,
            stderr=None) -> int:
    """ Execute `command` in a subprocess and return the result code of the
    command.
    """
    result = subprocess.run([command, *parameters], stdin=stdin, input=None,
                            stdout=stdout, stderr=stderr, shell=False,
                            timeout=None, check=False)
    return_code = result.returncode
    return return_code


def dict_to_command_parameters(param_keys, param_value):
    command_parameters = list(zip(param_keys, param_value))
    formated_command = []
    for param in command_parameters:
        if param[0][0] != '-':
            # Remove the key for arguments. Thus arguments needs to be passed
            # in order.
            formated_command.append(param[1])
        elif isinstance(param[1], bool):
            # Convert booleans to flag
            formated_command.append(param[0])
        else:
            # Convert to string
            if ((len(param[0]) >= 2) and (param[0][0] == param[0][1] == "-")):
                formated_command.append("%s=%s" % (param[0], param[1]))
            else:
                formated_command.append("%s %s" % (param[0], param[1]))
    return formated_command


if __name__ == '__main__':
    main()
