#!/bin/bash
#
# Find all commits where there message match a grep query.
#
# Source:
# * https://stackoverflow.com/a/7124949
#
# Error codes:
# 1: Wrong number of arguments


readonly USAGE='Usage: git_grep.sh <FILE_NAME>'

if [ "$#" -ne 1 ]; then
  >&2 echo "Wrong number of arguments"
  >&2 echo "$USAGE"
  exit 1
fi

git log --all --grep="$1"
