import os
import os.path


def main(path_dir_root: str):
    for file in iter_through_dir(path_dir_root=path_dir_root):
        if os.path.isdir(file):
            try:
                os.removedirs(file)
            except OSError:
                pass


def iter_through_dir(path_dir_root: str) -> str:
    for subdir, dirs, files in os.walk(path_dir_root):
        for directory in dirs:
            yield os.path.join(subdir, directory)


if __name__ == '__main__':
    main(path_dir_root=".")
