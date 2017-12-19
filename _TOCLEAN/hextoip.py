from sys import argv
from traceback import print_exc as print_exception_message
from traceback import print_stack


def hexa_to_decimal(hexa: str) -> int:
    """ Convert an hexadecimal number into a
        decimal integer.
    """
    return int(hexa, 16)


def hexa_to_ipv4address(hexa: str) -> str:
    """ Convert an hexadecimal number into an
        IPv4 address.
        Example :
        >>> hexa_to_ipaddress("C02C4112")
        "192.44.65.18"
    """
    # Bad format exceptions
    if len(hexa) != 8:
        print_stack()
        print("ValueError: Your number's size must be 8.")
        return None
    try:
        int(hexa, 16)
    except ValueError:
        print_exception_message()
        return None

    ip_address = ""
    for digit in range(0, len(hexa), 2):
        ip_address = "{}.{}".format(ip_address, hexa_to_decimal(hexa[digit:digit+2]))
    return ip_address[1:]


def main():
    for hexa in argv[1:]:
        print(hexa_to_ipv4address(hexa))


if __name__ == '__main__':
    main()
