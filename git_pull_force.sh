#!/bin/bash
#
# Overwrite all the non-saved data in a repository and force pull the latest
# commit from its master branch.


readonly USAGE='Usage: git_pull_force.sh'


git fetch --all
git reset --hard origin/master
git pull origin master
