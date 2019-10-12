#!/bin/bash

# This script takes screenshot. It depends on ImageMagick package.

DIR="${HOME}/Pictures/screenshots"
if [ ! -d $DIR ]; then
    mkdir -p $DIR
fi

DATE="$(date +%Y%m%d@%H%M%S)"
NAME="${DIR}/screenshot-${DATE}.png"
LOG="${DIR}/screenshots.log"

# Check if the dir to store the screenshots exists, else create it: 
if [ ! -d "${DIR}" ]; then mkdir -p "${DIR}"; fi 

# Screenshot a selected window
if [ "$1" = "win" ]; then import +repage "${NAME}"; fi

# Screenshot the entire screen
if [ "$1" = "scr" ]; then import -window root "${NAME}"; fi

# Screenshot a selected area
if [ "$1" = "area" ]; then import +repage "${NAME}"; fi

if [[ $# = 0 ]]; then import -window root "${NAME}"; fi

notify-send "Screenshot is stored at $NAME"
