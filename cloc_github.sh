#!/bin/bash
#
# Use the `cloc` command in a repository hosted at Github.
#
# Error codes:
# 1: Wrong number of arguments


readonly TEMP_DIR="~temp-cloc"

readonly USAGE='Usage: cloc_github.sh <USER_NAME> <REPO_NAME>'

if [ "$#" -ne 2 ]; then
  >&2 echo "Wrong number of arguments"
  >&2 echo "$USAGE"
  exit 1
fi

USER_NAME="$1"
REPO_NAME="$2"
REPO_URL="https://github.com/$USER_NAME/$REPO_NAME.git"

git clone --depth 1 "$REPO_URL" $TEMP_DIR &&
cloc "$TEMP_DIR" &&
rm -rf "$TEMP_DIR"
