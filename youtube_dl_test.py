from youtube_dl import YoutubeDL
from sys import argv


def main(argv: int) -> int:
    if len(argv) != 2:
        print(
            "You need to pass at least one argument.\n" +
            "Usage : download_youtube_music_from_a_file.py [file]")
        return 1

    with open(argv[1], 'r') as file:
        options = {}
        with YoutubeDL(options) as ydl:
            for youtube_url in file:

                ydl.download()
                # Delete music from file IF THE DL IS A SUCCESS


if __name__ == '__main__':
    main(argv)
