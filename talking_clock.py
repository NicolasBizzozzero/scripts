import argparse
import time


_INT_TO_WORD = {
    0: 'oh',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'fourty',
    50: 'fifty',
}


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-t", "--time", type=str, default=None,
                        help='Time to enumerate. If not provided, default to current time.')
    parser.add_argument("-s", "--separator", type=str, default=":",
                        help='Separator character used in a given time')
    parser.add_argument("-o", "--oh", type=str, default="oh",
                        help='How to pronunce the substring separating hours and minutes.')
    args = parser.parse_args()

    if args.time is None:
        args.time = get_current_time(separator=args.separator)

    res = talking_clock(
        time=args.time,
        separator=args.separator,
        oh=args.oh
    )
    print(res)


def talking_clock(time: str, separator: str = ":", oh: str = "oh") -> str:
    """ Takes a 24-hour time and translates it into words.

    Examples:
    >>> talking_clock("00:00")
    "twelve am"
    >>> talking_clock("01:30")
    "one thirty am"
    >>> talking_clock("12:05")
    "twelve oh five pm"
    >>> talking_clock("14:01")
    "two oh one pm"
    >>> talking_clock("20:29")
    "eight twenty nine pm"
    >>> talking_clock("21:00")
    "nine pm"
    """
    # Parsing input
    hours, minutes = time.split(separator)
    hours, minutes = int(hours), int(minutes)

    # Processing result
    suffix = "pm" if (hours > 12) or ((hours == 12) and minutes != 0) else "am"
    hours = hours - 12 if suffix == "pm" else hours
    hours_str, minutes_str = _int_to_time(hours), _int_to_time(minutes)
    if 0 < minutes < 10:
        minutes_str = "{oh} {minutes}".format(oh=oh, minutes=minutes_str)

    # Building result
    if minutes != 0:
        return "{hours} {minutes} {suffix}".format(hours=hours_str,
                                                   minutes=minutes_str,
                                                   suffix=suffix)
    else:
        return "{hours} {suffix}".format(hours=hours_str,
                                         suffix=suffix)


def get_current_time(separator: str) -> str:
    return time.strftime('%H{}%M'.format(separator))


def _int_to_word(integer: int) -> str:
    """ Translate an integer into its english word representation. """
    global _INT_TO_WORD

    try:
        return _INT_TO_WORD[integer]
    except KeyError:
        div, mod = divmod(integer, 10)
        return "{} {}".format(_int_to_word(div * 10), _int_to_word(mod))


def _int_to_time(integer: int) -> str:
    """ Translate an integer into its english word representation for a
    time.
    """
    if integer == 0:
        return _int_to_word(12)
    else:
        return _int_to_word(integer)


if __name__ == '__main__':
    main()
