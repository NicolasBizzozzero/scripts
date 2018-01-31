#!/usr/bin/perl
# Click the living hell out of whatever's under the mouse cursor
#
# Source :
# https://www.reddit.com/r/incremental_games/comments/4pygkl/autoclicker_for_ubuntu_linux/d7ftapf/


use Time::HiRes qw (usleep nanosleep);


# Sleep a little bit after starting the script 
# Gives time to get into the game window
sleep 3;

# Endless loop - press and hold the mouse button to stop registering click events,
# then mouse back over to the terminal and Ctrl-C to stop
while (1) {
    # 10,000 microseconds == 10 milliseconds == 1/100 of a second.
    # 2 of these per loop means ~~ 50 clicks per second.

    print `/usr/bin/xdotool mousedown 1`;
    usleep(10000);
    print `/usr/bin/xdotool mouseup 1`;
    usleep(10000);
}
