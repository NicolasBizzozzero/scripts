#!/bin/bash
#
# Delete a sensitive file from an entire repository.
# This will overwrite the whole history of the repository, thus changing any
# commit hash from the first time that the file appeared in the repo. You
# should commit any changes you currently have and delete all branches you
# currently have before using this script.
# This script needs to be run from the root of the repo.
#
# Source :
# https://help.github.com/articles/removing-sensitive-data-from-a-repository/
#
# Error codes:
# 1: Wrong number of arguments


readonly USAGE="Usage: git_nuke.sh <FILE> [-i --add-gitignore (default: true)]"

readonly DEFAULT_ADD_GITIGNORE=true


if [ "$#" -ne 1 ]; then
  >&2 echo "Wrong number of arguments"
  >&2 echo "$USAGE"
  exit 1
fi

git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch $1' --prune-empty --tag-name-filter cat -- --all
if [ -eq $DEFAULT_ADD_GITIGNORE true ]; then
  echo "$1" >> .gitignore
  git add .gitignore
fi
git commit -m "Purged sensitive data contained in the file $1 from the repo"
git push origin --force --all
