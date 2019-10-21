""" Blur pictures with a gaussian filter.

Dependencies :
* Pillow

Error codes :
0 - Success
1 - Wrong number of arguments
2 - The file does not exists
3 - The file is not an image or its format is currently not supported
"""

from os import listdir, remove
from os.path import isfile
from sys import argv

from PIL import ImageFilter, ImageFile, Image


_STR_USAGE = "Usage: python blur.py <FILES> ... [-i --intensity <INTENSITY>]"
_STR_WRONG_NUMBER_ARGUMENTS = "Error: Wrong number of arguments"
_STR_FILE_DOES_NOT_EXISTS = "Error: Not such file \"{file}\""
_STR_FILE_NOT_AN_IMAGE = "Error: The file \"{file}\" is not an image"

_CODE_SUCCESS = 0
_CODE_WRONG_NUMBER_ARGUMENT = 1
_CODE_FILE_DOES_NOT_EXISTS = 2
_CODE_FILE_NOT_AN_IMAGE = 3

_SUPPORTED_EXTENSIONS = ("jpg", "png", "jpeg")
_DEFAULT_INTENSITY = 2


def main():
    if len(argv) <= 1:
        print(_STR_WRONG_NUMBER_ARGUMENTS)
        print(_STR_USAGE)
        exit(_CODE_WRONG_NUMBER_ARGUMENT)

    # Unpack arguments
    files, intensity = _parse_args(argv)

    for path in files:
        blur(path=path, intensity=intensity)

    exit(_CODE_SUCCESS)


def blur(*, path, intensity):
    if not isfile(path):
        print(_STR_FILE_DOES_NOT_EXISTS.format(file=path))
        exit(_CODE_FILE_DOES_NOT_EXISTS)

    if not _is_image(path):
        print(_STR_FILE_NOT_AN_IMAGE.format(file=path))
        exit(_CODE_FILE_NOT_AN_IMAGE)

    blurred_image = _get_blurred_image(path, intensity)
    blurred_image.save(path)


def _parse_args(argv):
    global _DEFAULT_INTENSITY

    intensity = _DEFAULT_INTENSITY
    files = []

    parse_default_intensity = False
    for param in argv[1:]:
        if parse_default_intensity:
            parse_default_intensity = False
            intensity = float(param)
            continue
        if param in ("-i", "--intensity"):
            parse_default_intensity = True
            continue
        else:
            files.append(param)
    return files, intensity


def _is_image(file):
    """ Check whether or not the file located at `file` is a picture.
    This is done by comparing the extension of the file
    """
    global _SUPPORTED_EXTENSIONS

    file = file.lower()  # Ignore the case of the extension 
    for supported_extension in _SUPPORTED_EXTENSIONS:
        if file.endswith(supported_extension):
            return True
    return False


def _get_blurred_image(path, intensity):
    """ Return an object containing a blurred image, computed from the image
    located at `path`.
    """
    return Image.open(path).filter(ImageFilter.GaussianBlur(radius=intensity))


if __name__ == '__main__':
    main()
