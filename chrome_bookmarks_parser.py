""" Takes the path of chrome bookmarks export file (in HTML format) parse it,
then create a corresponding JSON file with all the links (name, url, and
attributes like add date or icon) and folders (name, add and last modified
date) following the nested folder structure.

Usage: chrome_bookmarks_parser.py <bookmarks_files>
Original Author: P1tr0w
Source: https://gist.github.com/P1tr0w/a505ad6c851f2b7f1c7d82799d2a5df0
"""

import re
import json
import operator
import os
import argparse

from functools import reduce


class BookmarkParser():
    def __init__(self, outdir=".", output_indent=4, ensure_ascii=False,
                 encoding_input='utf8', encoding_output='utf8'):
        self.encoding_input = encoding_input
        self.encoding_output = encoding_output
        self.output_indent = output_indent
        self.ensure_ascii = ensure_ascii
        self.outdir = outdir

    def parse(self, infile):
        # Read input file, lines to list, strip each line.
        self._file_lines = []

        with open(infile, encoding=self.encoding_input) as f:
            self._file_lines = f.read().splitlines()
            for i in range(len(self._file_lines)):
                self._file_lines[i] = self._file_lines[i].strip()

        # self.tree: dict with the whole structure
        # root: key that holds all the structure in its value, it's used
        # to have a root directory that is not the tree itself
        self._tree = {'root': {}}

        # list to store the path of the current directory through the
        # iteration, used by _change_folder
        self._path = ['root']

        # reference to the tree used by _change_folder
        self._folder = self._tree

        self._change_folder()
        self._iterate()
        self._save_json(outfile=change_file_extension(infile, "json"))
        self._save_to_clickable_link(outdir=self.outdir)

    def _change_folder(self):
        """ Change the folder reference to the last folder in path. """
        self._folder = get_by_path(self._tree, self._path)

    def _iterate(self):
        """ Iterate HTML lines to parse structure from <DT H3 and </DL, and
        data from <DT H3 and <DT A
        """
        for line in self._file_lines:
            # If the first tag is DT
            if line[1:3] == 'DT':
                # And if the second tag is A
                if line[5] == 'A':
                    # Its a link: get its parameters and append to current
                    # folder
                    self._handle_link(line)
                # If the second tag is H3
                elif line[5:7] == 'H3':
                    # Its a folder: get its parameters, append to current
                    # folder, create this folder with meta subfolder, and set
                    # current folder to this
                    self._handle_folder(line)
            # If tag is /DL we closed current folder: pop it from the path and
            # change folder
            elif line[1:4] == '/DL':
                self._path.pop()
                self._change_folder()

    def _handle_link(self, line):
        name = re.findall(r"<A.*?>(.*?)</A>", line)[-1]
        href = re.search(r'(?<=HREF=").*?(?=")', line).group()
        add_date = re.search(r'(?<=ADD_DATE=").*?(?=")', line).group()

        # Check if the link has an icon
        icon = ''
        has_icon = re.search(r'(?<=ICON=").*?(?=")', line)
        if has_icon:
            icon = has_icon.group()

        info = {
            'url': href,
            'add_date': add_date,
            'icon': icon
        }
        self._folder.update({name: info})

    def _handle_folder(self, line):
        name = re.findall(r'(?<=>)[\w\s]*?(?=<)', line)[-1]
        last_modified = re.search(
            r'(?<=LAST_MODIFIED=").*?(?=")', line).group()
        add_date = re.search(r'(?<=ADD_DATE=").*?(?=")', line).group()
        info = {
            'add_date': add_date,
            'last_modified': last_modified
        }
        self._folder.update({name: {'meta': info}})
        self._path.append(name)
        self._change_folder()

    def _save_json(self, outfile):
        """ Save the tree dict to a json file. """
        with open(outfile, 'w', encoding=self.encoding_output) as outfile:
            json.dump(self._tree, outfile, indent=self.output_indent,
                      ensure_ascii=self.ensure_ascii)

    def _save_to_clickable_link(self, outdir):
        """ Outpu the JSON nested lists to the disk by creating directories and
        clickable links.
        TODO: The directories are not nested. But I gave up.
        TODO: This function is a mess, but it seems to work.
        """
        toclean = [self._tree["root"]]
        toclean_names = ["root"]
        os.makedirs(os.path.join(outdir, "root"), exist_ok=True)
        while toclean:
            current_dict = toclean.pop()
            current_dict_name = toclean_names.pop()
            for k, v in current_dict.items():
                if k == "meta":
                    continue

                if isinstance(v, dict):
                    # Check if this dict is a leaf
                    if "url" in v.keys():
                        # Preprocess filename to be compatible with a Windows
                        # filesystem, then create the bookmark
                        create_chrome_windows_bookmark(
                            filepath=os.path.join(outdir, current_dict_name,
                                                  get_valid_filename(k)),
                            url=v["url"]
                        )
                    else:
                        os.makedirs(os.path.join(outdir, k), exist_ok=True)
                        toclean.append(v)
                        toclean_names.append(k)


def change_file_extension(filename, new_extension):
    """ Swap the extension of a file for a provided `new_extension`.

    Example:
    >>> change_file_extension("file.txt", "md")
    "file.md"
    """
    return os.path.splitext(filename)[0] + "." + new_extension


def get_by_path(dictionary, map_list):
    """ Access a nested object in a dictionary by item sequence.
    Source:
    * https://stackoverflow.com/a/14692747/4406340
    """
    return reduce(operator.getitem, map_list, dictionary)


def set_by_path(dictionary, map_list, value):
    """ Set a value in a nested object in a dictionary by item sequence.
    Source:
    * https://stackoverflow.com/a/14692747/4406340
    """
    get_by_path(dictionary, map_list[:-1])[map_list[-1]] = value


def get_valid_filename(s):
    """ Return the given string converted to a string that can be used for a
    clean filename. Remove leading and trailing spaces; convert other spaces to
    underscores; and remove anything that is not an alphanumeric, dash,
    underscore, or dot.
    >>> get_valid_filename("john's portrait in 2004.jpg")
    'johns_portrait_in_2004.jpg'

    Source:
    https://github.com/django/django/blob/master/django/utils/text.py#L219
    """
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)


def create_chrome_windows_bookmark(filepath, url, extension=".url"):
    with open(filepath + extension, 'w') as file:
        file.write("[InternetShortcut]\nURL=" + url)


def main(*, bookmarks_files, encoding_input, encoding_output, ensure_ascii,
         output_indent, outdir):
    parser = BookmarkParser(encoding_input=encoding_input,
                            encoding_output=encoding_output,
                            ensure_ascii=ensure_ascii,
                            output_indent=output_indent,
                            outdir=outdir)

    for bookmarks_file in bookmarks_files:
        parser.parse(bookmarks_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('bookmarks_files', default='utf8', type=str, nargs="+",
                        help='Chrome HTML bookmarks files')
    parser.add_argument('--encoding-input', default='utf8', type=str,
                        help='Input files encoding')
    parser.add_argument('--encoding-output', default='utf8', type=str,
                        help='Output files encoding')
    parser.add_argument('--output-indent', default=4, type=int, metavar='N',
                        help='Output indentation')
    parser.add_argument('--outdir', default='chrome_bookmarks', type=str,
                        help='Output dir for clickable links')
    parser.add_argument('--ensure-ascii', dest='ensure_ascii',
                        action='store_true',
                        help='Escape non-ASCII characters in output files')

    args = parser.parse_args()
    main(bookmarks_files=args.bookmarks_files,
         encoding_input=args.encoding_input,
         encoding_output=args.encoding_output,
         ensure_ascii=args.ensure_ascii,
         output_indent=args.output_indent,
         outdir=args.outdir)
