from sys import argv
from os import system as run_command


def create_a_correct_command(youtube_url):
    return "youtube-dl --extract-audio --audio-format m4a --audio-quality 0 --embed-thumbnail " + youtube_url + " -o C:/Users/Nicolas/Downloads///%(title)s.%(ext)s --prefer-ffmpeg --ffmpeg-location \"C:/Program Files (x86)/Youtube DL/ffmpeg-20160922-7d17d31-win64-static/bin\""

if __name__ == '__main__':
    if (len(argv) != 2):
        print(
            "You need to pass at least one argument.\nUsage : download_youtube_music_from_a_file.py [file]")
    else:
        with open(argv[1], 'r') as file:
            for youtube_url in file:
                command = create_a_correct_command(youtube_url)
                run_command(command)
                # Delete music from file IF THE DL IS A SUCCESS
