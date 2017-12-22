#!/bin/bash
#
# Change the date of a previous commit, or make an empty one at a specific
# date.
#
# WARNING, This method will invalidate all current hashes. You WILL have to
# force push. Don't use this script if there are people working in your git
# repository..
#
# The date must follows the format of the 'approxidate' algorithm described
# in this source file :
# https://github.com/git/git/blob/master/date.c
# Or in this manual page :
# https://www.kernel.org/pub/software/scm/git/docs/git-commit.html
# Here are some values :
# Format   : WEEK_DAY MONTH DAY HH:MM:SS YYYY UTC
# Weekdays : Sun, Mon, Tue, Wed, Thu, Fri, Sat
# Months   : Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
# UTC :
# * Paris : +0100
# * Chicago : -0600
#
#
# Examples :
# git_time.sh 'Nov 26 19:32:10 2017 +0100'
# git_time.sh 'Nov 26 19:32:10 2017 +0100' 16cb996f1c2150d13dfc3f8a14ca2d8b9299fac7
#
# Sources :
# * https://stackoverflow.com/a/454750
#
# Error codes:
# 1: Wrong number of arguments


readonly USAGE='Usage: git_time.sh <DATE>\n       git_time.sh <DATE> <COMMIT_HASH>'


# Check parameters' validity
if [ "$#" -lt 1 ]; then
  >&2 echo "Wrong number of arguments"
  >&2 printf "$USAGE\n"
  exit 1
fi


# Unpack parameters
param_date="$1"
param_commit_hash="$2"


previous_author_date="$GIT_AUTHOR_DATE"
previous_committer_date="$GIT_COMMITTER_DATE"

if [ -z $param_commit_hash ]; then
  export GIT_AUTHOR_DATE=$param_date
  export GIT_COMMITTER_DATE=$param_date
  git commit --allow-empty -m "Empty commit"
else
  git filter-branch --env-filter \
    "if [ $GIT_COMMIT = $param_commit_hash ]
     then
       export GIT_AUTHOR_DATE=$param_date
       export GIT_COMMITTER_DATE=$param_date
     fi"
fi

GIT_AUTHOR_DATE="$previous_author_date"
GIT_COMMITTER_DATE="$previous_committer_date"
