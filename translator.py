""" Translate text to a target custom language. """

import random
import re
import argparse

from googletrans import Translator


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
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
    parser_uwu = subparsers.add_parser('uwu')
    parser_uwu.set_defaults(func=uwu)
    parser_uwu.add_argument('string', type=str)

    # Subcommand translate
    parser_translate = subparsers.add_parser('translate')
    parser_translate.set_defaults(func=translate)
    parser_translate.add_argument('string', type=str)
    parser_translate.add_argument('-s', "--lang-src", type=str, default=None,
                                  help="The 2-characters country code matching the source "
                                       "language to translate. If set to `None`, let Google "
                                       "Translate find the language.")
    parser_translate.add_argument('-d', "--lang-dest", type=str, default="en",
                                  help="The 2-characters country code matching the destination "
                                       "language.")
    parser_translate.add_argument('-n', "--iterations", type=int, default=3,
                                  help="Number of times to repeat the translation.")

    # Subcommand nato
    parser_nato = subparsers.add_parser('nato')
    parser_nato.set_defaults(func=nato)
    parser_nato.add_argument('string', type=str)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        print("No subcommand has been given. See `--help` for all possible "
              "subcommands.")
        exit(1)

    if args.func.__name__ == "spongify":
        translation = args.func(
            string=args.string,
            diversity_bias=args.diversity_bias,
            seed=args.seed
        )
    elif args.func.__name__ == "uwu":
        translation = args.func(string=args.string)
    elif args.func.__name__ == "translate":
        translation = args.func(
            string=args.string,
            lang_src=args.lang_src,
            lang_dest=args.lang_dest,
            iterations=args.iterations
        )
    elif args.func.__name__ == "nato":
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


def translate(string, lang_src, lang_dest, iterations: int = 3):
    if lang_src is None:
        lang_src = Translator().translate(string).src

    for _ in range(iterations):
        string = _translate(string, lang_src=lang_src, lang_dest=lang_dest)
        string = _translate(string, lang_src=lang_dest, lang_dest=lang_src)
    return string


def nato(string):
    charmap = {
        'a': "alpha",
        'b': "bravo",
        'c': "charlie",
        'd': "delta",
        'e': "echo",
        'f': "foxtrot",
        'g': "golf",
        'h': "hotel",
        'i': "india",
        'j': "juliett",
        'k': "kilo",
        'l': "lima",
        'm': "mike",
        'n': "november",
        'o': "oscar",
        'p': "papa",
        'q': "quebec",
        'r': "romeo",
        's': "sierra",
        't': "tango",
        'u': "uniform",
        'v': "victor",
        'w': "whisky",
        'x': "x-ray",
        'y': "yankee",
        'z': "zulu",
        '0': "zero",
        '1': "one",
        '2': "two",
        '3': "three",
        '4': "four",
        '5': "five",
        '6': "six",
        '7': "seven",
        '8': "eight",
        '9': "nine",
        ',': "comma",
        '.': "STOP",
    }

    string = list(map(lambda c: _char_to_nato_alphabet(c, charmap),
                      string))
    string = list(filter(lambda c: c != '', string))
    string = _capitalize_sentence(string)
    return " ".join(string)


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


def _translate(string: str, lang_src: str = None, lang_dest: str = 'en'):
    """ Translate a string from a source natural language into another
    destination natural language using Google Translate.
    :param lang_src: The 2-characters country code matching the source
    language to translate. If set to `None`, let Google Translate find the
    language.
    """
    return Translator().translate(string, src=lang_src, dest=lang_dest).text


def _char_to_nato_alphabet(char, charmap):
    if char in ('!', '?'):
        return charmap['.']
    if char in (' ',):
        return ''
    return charmap[char.lower()]


def _capitalize_sentence(sentence):
    # Capitalize first word
    sentence[0] = sentence[0].capitalize()

    for i in range(len(sentence) - 1):
        if sentence[i] == "STOP":
            sentence[i + 1] = sentence[i + 1].capitalize()
    return sentence


if __name__ == '__main__':
    main()
