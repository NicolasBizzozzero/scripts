import os
import time
from typing import Union, List

import vlc
import click


PLAYING_STATES = set([1, 2, 3, 4])
SLEEPING_TIME = 2


def _iter_args_files(files: Union[str, List[str]]) -> iter:
	if len(files) == 1:
		yield files[0]
	else:
		for file in files:
			yield file


@click.command()
@click.argument("music_files", nargs=-1)
@click.option("--repeat", default=0, help=("Number of time to repeat a song. "
	                                       "Set to -1 for infinite loop."))
def player(music_files: Union[str, List[str]], repeat: int):
    instance = vlc.Instance("--input-repeat={repeat}".format(repeat=repeat),
    	                    "--fullscreen")
    player = instance.media_player_new()

    for music_file in _iter_args_files(music_files):
	    media = instance.media_new(music_file)
	    player.set_media(media)
	    player.play()
	    while player.get_state() in PLAYING_STATES:
	    	time.sleep(SLEEPING_TIME)


if __name__ == "__main__":
    player()
