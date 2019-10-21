""" Translate text to a target custom language. """

import random
import re
import argparse


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    subparsers = parser.add_subparsers()

    # Subcommand add
    parser_spongiy = subparsers.add_parser('spongify')
    parser_spongiy.set_defaults(func=spongify)
    parser_spongiy.add_argument('string', type=str)
    parser_spongiy.add_argument('-d', "--diversity-bias", type=float, default=0.5,
                                help="Probability of flipping the capitalization of a character")
    parser_spongiy.add_argument('-s', "--seed", type=int, default=None,
                                help="Set a fixed random seed")

    # Subcommand del
    parqer_uwu = subparsers.add_parser('uwu')
    parqer_uwu.set_defaults(func=uwu)
    parqer_uwu.add_argument('string', type=str)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        print("No subcommand has been given. See `--help` for all possible subcommands.")
        exit(1)

    if args.func.__name__ == "spongify":
        translation = args.func(
            string=args.string,
            diversity_bias=args.diversity_bias,
            seed=args.seed
        )
    elif args.func.__name__ == "uwu":
        translation = args.func(string=args.string)

    print(translation)


def spongify(string, diversity_bias=0.5, seed=None):
    """ Randomly flip capitalization of characters in a string.

    Source:
    * https://github.com/nkrim/spongemock
    """
    if seed is not None:
        random.seed(seed)

    out = ''
    last_was_upper = True
    swap_chance = 0.5
    for c in string:
        if c.isalpha():
            if random.random() < swap_chance:
                last_was_upper = not last_was_upper
                swap_chance = 0.5
            c = c.upper() if last_was_upper else c.lower()
            swap_chance += (1 - swap_chance) * diversity_bias
        out += c
    return out


def uwu(string):
    dictionary = {
        "r": "w",
        "R": "w",
        "l": "w",
        "L": "w",
        "th": "d",
        "tH": "d",
        "Th": "d",
        "TH": "d",
    }
    return _replace_substrings(string, dictionary) + " uwu"


def _replace_substrings(string, map_substrings):
    # Iterate through keys by length, in reverse order
    for item in sorted(map_substrings.keys(), key=len, reverse=True):
        string = re.sub(item, map_substrings[item], string)
    return string


def _reverse_capitalization(string):
    """ Reverse the capitalization of a string.

    Examples:
    >>> _reverse_capitalization("a")
    "A"
    >>> _reverse_capitalization("A")
    "a"
    >>> _reverse_capitalization(";")
    ";"
    >>> _reverse_capitalization("Hello, World!")
    "hELLO, wORLD!"
    """
    res = ""
    for c in string:
        if c.islower():
            res += c.upper()
        elif c.isupper():
            res += c.lower()
        else:
            res += c
    return res


if __name__ == '__main__':
    main()
