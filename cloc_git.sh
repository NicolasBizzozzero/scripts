#!/usr/bin/env bash

TEMP_DIR=".temp-linecount-repo"

git clone --depth 1 "$1" $TEMP_DIR &&
printf "'$TEMP_DIR' will be deleted automatically\n\n\n" &&

cloc $TEMP_DIR &&

printf "\n\nDeleting '$TEMP_DIR' ...\n\n\n" &&
rm -rf "$TEMP_DIR"
