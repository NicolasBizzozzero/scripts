#from os import listdir
import os


def is_ASCII(string):
    """
            Return True if string contain only ASCII characters.
            Extended-ASCII characters are not considered as ASCII
            characters.
    """
    try:
        string.encode("ascii")
    except UnicodeEncodeError:
        return False
    else:
        return True


def convert_to_ascii(string):

    return string


def get_all_files_from_current_directory():
    """
            Get all the files from the current directory. Ignore
            all the subdirectories.
            This function can cause issues with Windows.
    """
    return [file for file in os.listdir(".") if os.path.isfile(os.path.join(".", file))]


def rename_file(oldName, newName):
    """
            Rename the file located on the current directory as
            the name "oldName" with the name "newName".
    """
    os.rename(oldName, newName)


def convert_name_of_all_files_to_ascii():
    array_of_files = get_all_files_from_current_directory()
    for file in array_of_files:
        if (is_ASCII(file)):
            rename_file(file, convert_to_ascii(files))

if __name__ == '__main__':
    convert_name_of_all_files_to_ascii()
