from os import rename
from os import listdir
from os.path import basename

def main():
	list_of_files = get_all_files_of_current_directory()

	for file in list_of_files:
		rename_file(file, add_jpg_at_the_end_of_the_string(str))


def get_all_files_of_current_directory():
	return listdir(".")


def add_jpg_at_the_end_of_the_string(str):
	return str + ".jpeg"


def rename_file(oldFilename, newFilename):
	if (oldFilename != basename(__file__))
		rename(oldFilename, newFilename)


if __name__ == '__main__':
	main()