import time
import argparse

from typing import Union, List

import vlc


PLAYING_STATES = set([1, 2, 3, 4])
SLEEPING_TIME = 2


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('music_files', type=str, nargs="*",
                        help='Music files to play.')
    parser.add_argument('-r', '--repeat', type=int, default=0,
                        help="Number of time to repeat a song. Set to -1 for infinite loop.")
    args = parser.parse_args()

    player(
        music_files=args.music_files,
        repeat=args.repeat
    )


def player(music_files, repeat):
    instance = vlc.Instance("--input-repeat={repeat}".format(repeat=repeat),
                            "--fullscreen")
    media_player = instance.media_player_new()

    for music_file in _iter_args_files(music_files):
        media = instance.media_new(music_file)
        media_player.set_media(media)
        media_player.play()
        while media_player.get_state() in PLAYING_STATES:
            time.sleep(SLEEPING_TIME)


def _iter_args_files(files: Union[str, List[str]]) -> iter:
    if len(files) == 1:
        yield files[0]
    else:
        for file in files:
            yield file


if __name__ == "__main__":
    main()
