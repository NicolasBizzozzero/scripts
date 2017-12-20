""" Convert all adresses in the hexadecimal format passed by command-line to
their respective IPv4 or IPv6 format.

Known issues;
* The IPv6 simplification does not work as espected as for now.

Error codes:
0 - Success
1 - Wrong number of arguments
2 - Not an hexadecimal value
3 - The hex string doesn't have the right size to be an IPv4 address
4 - The hex string doesn't have the right size to be an IPv6 address
"""
import sys
import string


_STR_USAGE = ("Usage: python hextoip.py <HEX> ... "
              "[--ipv6]")
_STR_WRONG_NUMBER_ARGUMENTS = "Error: Wrong number of arguments"
_STR_NOT_HEXADECIMAL_VALUE = ("The string \"{string}\" does not represents an"
                              " hexadecimal value")
_STR_WRONG_SIZE_IPV4 = ("The hex string \"{string}\"doesn't have the right "
                        "size to be an IPv4 address")
_STR_WRONG_SIZE_IPV6 = ("The hex string \"{string}\"doesn't have the right "
                        "size to be an IPv6 address")

_CODE_SUCCESS = 0
_CODE_WRONG_NUMBER_ARGUMENT = 1
_CODE_NOT_HEXADECIMAL_VALUE = 2
_CODE_WRONG_SIZE_IPV4 = 3
_CODE_WRONG_SIZE_IPV6 = 4


def main():
    if len(sys.argv) <= 1:
        print(_STR_WRONG_NUMBER_ARGUMENTS)
        print(_STR_USAGE)
        exit(_CODE_WRONG_NUMBER_ARGUMENT)

    # Unpack parameters
    hex_numbers, ipv6 = _parse_args(sys.argv)

    for hex_number in hex_numbers:
        if _is_hexadecimal(hex_number):
            if ipv6:
                ip = hex_to_ipv6(hex_number=hex_number)
            else:
                ip = hex_to_ipv4(hex_number=hex_number)
            print(ip)
        else:
            print(_STR_NOT_HEXADECIMAL_VALUE.format(string=hex_number))
            exit(_CODE_NOT_HEXADECIMAL_VALUE)


def _parse_args(argv):
    hex_numbers = []
    ipv6 = False

    parse_ipv6 = False
    for param in argv[1:]:
        if parse_ipv6:
            ipv6 = True
            break
        if param in ("--ipv6"):
            parse_ipv6 = True
            continue
        else:
            hex_numbers.append(param)
    return hex_numbers, ipv6


def _is_hexadecimal(string):
    """ Return `True` if `string` represents an hexadecimal number, `False`
    otherwise.
    """
    try:
        int(string, 16)
        return True
    except ValueError:
        return False


def hex_to_ipv4(*, hex_number):
    """ Convert an hexadecimal number into an IPv4 address.

        Example :
            >>> hex_to_ipv4(hex_number="C02C4112")
            "192.44.65.18"
    """
    if len(hex_number) != 8:
        print(_STR_WRONG_SIZE_IPV4.format(string=hex_number))
        exit(_CODE_WRONG_SIZE_IPV4)

    ip_address = ""
    for digit in range(0, len(hex_number), 2):
        ip_address = "{}.{}".format(ip_address, _hex_to_dec(
            hex_number[digit:digit + 2]))
    return ip_address[1:]  # Ignore initial '.' created during formating


def _hex_to_dec(hex_number):
    """ Convert an hexadecimal number into a decimal integer. """
    return int(hex_number, 16)


def hex_to_ipv6(*, hex_number, simplify=False):
    """ Convert an hexadecimal number into an IPv6 address.

        Example :
        >>> hex_to_ipv6(hex_number="20010DB8100000000000000000000001")
        "2001:0DB8:1000:0000:0000:0000:0000:0001"
        >>> hex_to_ipv6(hex_number="20010DB8100000000000000000000001",
                        simplify=True)
        "2001:DB8:1000::1"
    """
    if len(hex_number) != 32:
        print(_STR_WRONG_SIZE_IPV6.format(string=hex_number))
        exit(_CODE_WRONG_SIZE_IPV6)

    ip_address = ""
    for digit in range(0, len(hex_number), 4):
        ip_address = "{}:{}".format(ip_address, hex_number[digit:digit + 4])
    ip_address = ip_address[1:]  # Ignore initial ':' created during formating

    if simplify:
        # Remove useless 0
        groups = ip_address.split(":")
        for i in range(len(groups)):
            if any(string.hexdigits[1:] in groups[i]):
                while groups[i][0] == "0":
                    groups[i] = groups[i][1:]
        ip_address = ":".join(groups)

        # Remove consecutives 0
        pass
    return ip_address


if __name__ == '__main__':
    main()
