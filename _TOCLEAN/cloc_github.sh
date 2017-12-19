#!/usr/bin/env bash

TEMP_DIR=".temp-linecount-repo"
USER_NAME="$1"
REPO_NAME="$2"
YOUR_LOGIN="" # Get parameter --login or -l
REPO_URL="https://$YOUR_LOGIN@github.com/$USER_NAME/$REPO_NAME.git"

git clone --depth 1 "$REPO_URL" $TEMP_DIR &&
printf "'$TEMP_DIR' will be deleted automatically\n\n\n" &&

cloc $TEMP_DIR &&

printf "\n\nDeleting '$TEMP_DIR' ...\n\n\n" &&
rm -rf "$TEMP_DIR"
