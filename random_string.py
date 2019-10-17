""" Generate a random string. """
import string
import random
import argparse


# TODO: Accents support. Maybe generate a blob with only ascii bytes


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--size", type=int, default=32,
                        help='Number of characters to generate')
    parser.add_argument("-f", "--forbidden-chars", type=str, default="",
                        help='Chars which will not appear in the generated string')
    parser.add_argument("--no-digits", action='store_true',
                        help='Generated string will not includes digits')
    parser.add_argument("--no-uppercase", action='store_true',
                        help='Generated string will not includes uppercase characters')
    parser.add_argument("--no-lowercase", action='store_true',
                        help='Generated string will not includes lowercase characters')
    parser.add_argument("--no-punctuation", action='store_true',
                        help='Generated string will not includes punctuation characters')
    args = parser.parse_args()

    string = random_string(
        size=args.size,
        forbidden_chars=args.forbidden_chars,
        digits=not args.no_digits,
        uppercase=not args.no_uppercase,
        lowercase=not args.no_lowercase,
        punctuation=not args.no_punctuation
    )
    print(string)


def random_string(size: int, forbidden_chars: str = "", digits: bool = True,
                  uppercase: bool = True, lowercase: bool = True,
                  punctuation: bool = True) -> str:
    choices = ""
    if digits:
        choices += string.digits
    if uppercase:
        choices += string.ascii_uppercase
    if lowercase:
        choices += string.ascii_lowercase
    if punctuation:
        choices += string.punctuation
    for char in forbidden_chars:
        if char in choices:
            choices = choices.replace(char, '')

    return "".join(random.choice(choices) for _ in range(size))


if __name__ == '__main__':
    main()
