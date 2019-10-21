""" I'm sorry.

Source:
https://www.reddit.com/r/pcmasterrace/comments/7oimam/a_productive_day_at_work_nsfw/ds9wtjc/
"""
import os
import time
import argparse


s1 = """
3
33
333
3333                /---\\
3333================|   |===================MM------
33333               |___|                   ||       \\
33333               \\___/                   ||        )
33333                                       ||        -)
33333                  /--\\ /--\\ /--\\ /--\\  ||        )
33333                  |==| |==| |==| |==|  ||       /
3333===================|  |=|  |=|  |=|  |==WW------
3333                   \\__/ \\__/ \\__/ \\__/
333
33
3
"""

s2 = """
3
33
333
3333              /---\\
3333==============|   |=====================MM------
33333             |___|                     ||       \\
33333             \\___/                     ||        )
33333                                       ||        -)
33333                /--\\ /--\\ /--\\ /--\\    ||        )
33333                |==| |==| |==| |==|    ||       /
3333=================|  |=|  |=|  |=|  |====WW------
3333                 \\__/ \\__/ \\__/ \\__/
333
33
3
"""

s3 = """
3
33
333
3333            /---\\
3333============|   |=======================MM------
33333           |___|                       ||       \\
33333           \\___/                       ||        )
33333                                       ||        -)
33333              /--\\ /--\\ /--\\ /--\\      ||        )
33333              |==| |==| |==| |==|      ||       /
3333===============|  |=|  |=|  |=|  |======WW------
3333               \\__/ \\__/ \\__/ \\__/
333
33
3
"""

s4 = """
3
33
333
3333          /---\\
3333==========|   |=========================MM------
33333         |___|                         ||       \\
33333         \\___/                         ||        )
33333                                       ||        -)
33333            /--\\ /--\\ /--\\ /--\\        ||        )
33333            |==| |==| |==| |==|        ||       /
3333=============|  |=|  |=|  |=|  |========WW------
3333             \\__/ \\__/ \\__/ \\__/
333
33
3
"""

s5 = """
3
33
333
3333        /---\\
3333========|   |===========================MM------
33333       |___|                           ||       \\
33333       \\___/                           ||        )
33333                                       ||        -)
33333          /--\\ /--\\ /--\\ /--\\          ||        )
33333          |==| |==| |==| |==|          ||       /
3333===========|  |=|  |=|  |=|  |==========WW------
3333           \\__/ \\__/ \\__/ \\__/
333
33
3
"""

s6 = """
3
33
333
3333      /---\\
3333======|   |=============================MM------
33333     |___|                             ||       \\
33333     \\___/                             ||        )
33333                                       ||        -)
33333        /--\\ /--\\ /--\\ /--\\            ||        )
33333        |==| |==| |==| |==|            ||       /
3333=========|  |=|  |=|  |=|  |============WW------
3333         \\__/ \\__/ \\__/ \\__/
333
33
3
"""

s7 = """
3
33
333
3333    /---\\
3333====|   |===============================MM------
33333   |___|                               ||       \\
33333   \\___/                               ||        )
33333                                       ||        -)
33333      /--\\ /--\\ /--\\ /--\\              ||        )
33333      |==| |==| |==| |==|              ||       /
3333=======|  |=|  |=|  |=|  |==============WW------
3333       \\__/ \\__/ \\__/ \\__/
333
33
3
"""

s8 = """
3
33
333
3333  /---\\
3333==|   |=================================MM------
33333 |___|                                 ||       \\
33333 \\___/                                 ||        )
33333                                       ||        -)
33333    /--\\ /--\\ /--\\ /--\\                ||        )
33333    |==| |==| |==| |==|                ||       /
3333=====|  |=|  |=|  |=|  |================WW------
3333     \\__/ \\__/ \\__/ \\__/
333
33
3
"""

j1 = """
3
33
333
3333                /---\\
3333================|   |===================MM------
33333               |___|                   ||       \\
33333               \\___/                   ||        )
33333                                       ||        -) -
33333                  /--\\ /--\\ /--\\ /--\\  ||        )
33333                  |==| |==| |==| |==|  ||       /
3333===================|  |=|  |=|  |=|  |==WW------
3333                   \\__/ \\__/ \\__/ \\__/
333
33
3
"""

j2 = """
3
33
333
3333                /---\\
3333================|   |===================MM------
33333               |___|               ||       \\
33333               \\___/                  ||        )
33333                               ||        -) -=
33333                  /--\\ /--\\ /--\\ /--\\  ||        )
33333                  |==| |==| |==| |==|  ||       /
3333===================|  |=|  |=|  |=|  |==WW------
3333                   \\__/ \\__/ \\__/ \\__/
333
33
3
"""

j3 = """
3
33
333
3333                /---\\
3333================|   |===================MM------
33333               |___|               ||       \\
33333               \\___/                  ||        )
33333                               ||        -) -==
33333                  /--\\ /--\\ /--\\ /--\\  ||        )
33333                  |==| |==| |==| |==|  ||       /
3333===================|  |=|  |=|  |=|  |==WW------
3333                   \\__/ \\__/ \\__/ \\__/
333
33
3
"""

j4 = """
3
33
333
3333                /---\\
3333================|   |===================MM------
33333               |___|               ||       \\
33333               \\___/                  ||        )
33333                               ||        -) -==<
33333                  /--\\ /--\\ /--\\ /--\\  ||        )
33333                  |==| |==| |==| |==|  ||       /
3333===================|  |=|  |=|  |=|  |==WW------
3333                   \\__/ \\__/ \\__/ \\__/
333
33
3
"""

j5 = """
3
33
333
3333                /---\\
3333================|   |===================MM------
33333               |___|               ||       \\
33333               \\___/                  ||        )      /
33333                               ||        -) -==< -
33333                  /--\\ /--\\ /--\\ /--\\  ||        )      \\
33333                  |==| |==| |==| |==|  ||       /
3333===================|  |=|  |=|  |=|  |==WW------
3333                   \\__/ \\__/ \\__/ \\__/
333
33
3
"""

j6 = """
3
33
333
3333                /---\\
3333================|   |===================MM------
33333               |___|               ||       \\
33333               \\___/                  ||        )      / -
33333                               ||        -) -==< --
33333                  /--\\ /--\\ /--\\ /--\\  ||        )      \\ -
33333                  |==| |==| |==| |==|  ||       /
3333===================|  |=|  |=|  |=|  |==WW------
3333                   \\__/ \\__/ \\__/ \\__/
333
33
3
"""

j7 = """
3
33
333
3333                /---\\
3333================|   |===================MM------
33333               |___|               ||       \\
33333               \\___/                  ||        )      / - - \\
33333                               ||        -)   =< -- -
33333                  /--\\ /--\\ /--\\ /--\\  ||        )      \\ - - /
33333                  |==| |==| |==| |==|  ||       /
3333===================|  |=|  |=|  |=|  |==WW------
3333                   \\__/ \\__/ \\__/ \\__/
333
33
3
"""

j8 = """
3
33
333
3333                /---\\
3333================|   |===================MM------
33333               |___|               ||       \\
33333               \\___/                  ||        )      / - - \\
33333                               ||        -)    < -- -- >
33333                  /--\\ /--\\ /--\\ /--\\  ||        )      \\ - - /
33333                  |==| |==| |==| |==|  ||       /
3333===================|  |=|  |=|  |=|  |==WW------
3333                   \\__/ \\__/ \\__/ \\__/
333
33
3
"""

stroke_list = [s1, s2, s3, s4, s5, s6, s7, s8]
jizz_list = [j1, j2, j3, j4, j5, j6, j7, j8]


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-w", "--wank-speed", type=float, default=0.075,
                        help="Animation speed of wanks in ms")
    parser.add_argument("-s", "--jerks", type=int, default=3,
                        help="Number of jerks")
    parser.add_argument("-j", "--jizz-speed", type=float, default=0.05,
                        help="Animation speed of jizz in ms")
    args = parser.parse_args()

    wank(
        jerks=args.jerks,
        wank_speed=args.wank_speed,
        jizz_speed=args.jizz_speed
    )


def wank(jerks: int = 3, wank_speed: float = 0.075, jizz_speed: float = 0.05):
    # Wank
    for jerk in range(jerks):
        for stroke in range(len(stroke_list)):
            _clear_screen()
            print(stroke_list[stroke])
            time.sleep(wank_speed)
        for putz in range(len(stroke_list) - 2, 0, -1):
            _clear_screen()
            print(stroke_list[putz])
            time.sleep(wank_speed)

    # Finale
    for _ in range(3):
        for spurt in range(len(jizz_list)):
            _clear_screen()
            print(jizz_list[spurt])
            time.sleep(jizz_speed)
    time.sleep(1)
    _clear_screen()


def _clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == '__main__':
    main()