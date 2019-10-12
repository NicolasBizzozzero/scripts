""" zip-pw dictionary cracker.
This script will crack a pw- protected zip file with a dictionary list. It will
create a pseudo-Thread for each dictionary_file line to speed up the process.
"""

import zipfile
import argparse

from threading import Thread


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zip_file", type=str,
                        help="Zip file to bruteforce")
    parser.add_argument("dictionary", type=str,
                        help="Dictionary to use for bruteforcing")
    args = parser.parse_args()

    bruteforce_zipfile(path_zipfile=args.zip_file,
                       path_dictionary=args.dictionary)


def bruteforce_zipfile(path_zipfile, path_dictionary, encoding='utf8'):
    zip_file = zipfile.ZipFile(path_zipfile)
    with open(path_dictionary) as dictionary:
        for password in dictionary:
            password = password.rstrip("\n")
            password = str.encode(password, encoding)
            Thread(target=try_extract_zip,
                   args=(zip_file, password, encoding)).start()


def try_extract_zip(zip_file, password, encoding):
    try:
        zip_file.extractall(pwd=password)
        print("[+]", '"' + zip_file.filename + '" password:',
              password.decode(encoding))
    except RuntimeError:
        pass


if __name__ == '__main__':
    main()
