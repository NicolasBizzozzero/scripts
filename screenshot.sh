#!/bin/bash
#
# Use the `scrot` command to take a screenshot of the screen and save it under
# the file passed by argument (or in the current directory with a timestamp as
# a name if no argument).
#
# Usage:
# screenshot.sh <DEST_DIR>
#
# Dependencies:
# - The Scrot command-line utility: https://en.wikipedia.org/wiki/Scrot
#
# Error codes:
# 1: Wrong number of arguments


readonly USAGE='Usage: screenshot.sh <DEST_DIR>'


case "$#" in
  0) scrot;;
  1) mkdir ~screenshot_tmp_dir
     scrot -e 'mv -f $f ~screenshot_tmp_dir/$f'
     cp -r ~screenshot_tmp_dir "$1"
     rm -rf ~screenshot_tmp_dir;;
  *) >&2 echo "Wrong number of arguments"
     >&2 echo "$USAGE"
esac
