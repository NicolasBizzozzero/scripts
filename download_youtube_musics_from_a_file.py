from sys import argv
from os import system as run_command


def create_a_correct_command(youtube_url: str) -> str:
    return (r"youtube-dl "
            #            "--extract-audio "
            #            "--audio-format m4a "
            #            "--audio-quality 0 "
            "--embed-thumbnail "
            "-o C:/Users/Nicolas/Downloads///%(title)s.%(ext)s "
            #            "--prefer-ffmpeg "
            #            "--ffmpeg-location C:/Program Files (x86)/Youtube DL/ffmpeg-20160922-7d17d31-win64-static/bin"
            "--limit-rate 20K "
            "--ignore-errors "
            + youtube_url
            )


if __name__ == '__main__':
    if (len(argv) != 2):
        print(("You need to pass at least one argument.\n"
               "Usage : download_youtube_music_from_a_file.py [file]"))
    else:
        with open(argv[1]) as file:
            for youtube_url in file:
                command = create_a_correct_command(youtube_url)
                run_command(command)
                # Delete music from file IF THE DL IS A SUCCESS

# Commands to copy paste :
# "youtube-dl --extract-audio --audio-format m4a --audio-quality 0 --embed-thumbnail -o C:/Users/Nicolas/Downloads///%(title)s.%(ext)s --prefer-ffmpeg --ffmpeg-location C:/Program Files (x86)/Youtube DL/ffmpeg-20160922-7d17d31-win64-static/bin"
# Limit rate : --limit-rate 50K
# Playlist range : --playlist-items 1-16,18-62,64-13
# Ignorer les erreurs : --ignore-errors

# Exemples :
# Telecharger à 30 Kio/s toute une playlist au meilleur format disponible en numérotant le numéro de la playlist dans le titre et avec des indexs bien précis, et ne s'arrete pas si il rencontre une vidéo qui n'existe plus
# youtube-dl --embed-thumbnail -o
# "C:/Users/Nicolas/Downloads///%(playlist_index)s - %(title)s.%(ext)s"
# --limit-rate 30K --ignore-errors
# https://www.youtube.com/playlist?list=PL7XlqX4npddfrdpMCxBnNZXg2GFll7t5y
