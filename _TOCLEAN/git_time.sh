#!/bin/bash
#
# Make a Git commit at a specific date.
#
# The script alter the variables GIT_AUTHOR_DATE and GIT_COMMITTER_DATE before
# performing a commit.
# The date must follows the format of the 'approxidate' algorithm described
# in this source file : https://github.com/git/git/blob/master/date.c
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
# git_time.sh 'Sun Nov 26 19:32:10 2017 +0100'
# git_time.sh 'Sun Nov 26 19:32:10 2017 +0100' -m "Committing in the past !"
#
# Sources :
# * https://stackoverflow.com/questions/3895453/how-do-i-make-a-git-commit-in-the-past/3896112#3896112
#
# Error codes:
# 1: Wrong number of arguments


readonly USAGE='Usage: git_time.sh <DATE> <PARENT_COMMIT> <COMMIT_MESSAGE> <BRANCH_NAME>'  #[-m --message <COMMIT_MESSAGE>]'


# Check parameters' validity
if [ "$#" -lt 2 ]; then
  >&2 echo "Wrong number of arguments"
  >&2 echo "$USAGE"
  exit 1
fi

# TODO: wtf is this not working
# Unpack parameters
param_date="$1"
param_parent_commit="$2"
param_message="$3"
param_branch_name="$4"

# optspec="m:-:"
# while getopts "$optspec" flag; do
#   case "${flag}" in
#     -)
# 	  case "${OPTARG}" in
# 	    message=*)
# 	      val=${OPTARG#*=}
# 	      opt=${OPTARG%=$val}
# 	      param_message="${val}"
# 	      ;;
# 	    *)
# 	      if [ "$OPTERR" = 1 ] && [ "${optspec:0:1}" != ":" ]; then
# 	        echo "Unknown option --${OPTARG}" >&2
# 	      fi
# 	      ;;
# 	  esac;;
#     m) param_message="${OPTARG}" ;;
#     *) error "Unexpected option ${flag}" ;;
#   esac
# done


previous_author_date="$GIT_AUTHOR_DATE"
previous_committer_date="$GIT_COMMITTER_DATE"
GIT_AUTHOR_DATE="$1"
GIT_COMMITTER_DATE="$1"

git checkout -b "$param_branch_name" "$param_parent_commit"
git add todelete.txt
if [ ! -z "$param_message" ]; then
  git commit -m "$param_message"
else
  git commit
fi
git checkout master
git rebase "$param_branch_name"
git branch -d "$param_branch_name"

GIT_AUTHOR_DATE="$previous_author_date"
GIT_COMMITTER_DATE="$previous_committer_date"
