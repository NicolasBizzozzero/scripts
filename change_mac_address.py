""" Spoof your current MAC address with a custom MAC address. """

import subprocess
import argparse
import re
import random


RE_MAC_ADDRESS = r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})"


# TOOD: check validity provided MAC address


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('interface', type=str,
                        help='Interface form which to change the MAC address')
    parser.add_argument("-m", '--new-mac', type=str, default=None,
                        help='New MAC address to use for the provided interface')
    args = parser.parse_args()

    current_mac = get_current_mac_address(args.interface)
    if current_mac is None:
        print("Could not find a MAC address for interface", args.interface)
        exit(2)

    change_mac_address(interface=args.interface,
                       new_mac_address=args.new_mac)


def change_mac_address(interface: str, new_mac_address: str = None):
    if new_mac_address is None:
        new_mac_address = generate_mac_address()

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac_address(interface: str):
    global RE_MAC_ADDRESS

    cmd_output = subprocess.check_output(["ifconfig", interface])
    re_search = re.search(RE_MAC_ADDRESS, cmd_output)

    if re_search:
        return re_search.group(0)
    else:
        return None


def generate_mac_address(separator: str = ":") -> str:
    return "02%s00%s00%s%02x%s%02x%s%02x" % (separator,
                                             separator,
                                             separator,
                                             random.randint(0, 255),
                                             separator,
                                             random.randint(0, 255),
                                             separator,
                                             random.randint(0, 255))


if __name__ == '__main__':
    main()
