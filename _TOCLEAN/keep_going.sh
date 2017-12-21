#!/bin/bash
#
# Prompt the user to continue the execution.
# If its response is positive, return 0.
# If its response is negative, return a non-zero value.
# Otherwise, keep repeating the question until he answer correctly.
#
# Error codes:
# 1: Wrong number of arguments
# 2: User want to exit


readonly USAGE='Usage: keep_going.sh'

readonly POSITIVE_RESPONSES=("y" "ye" "yes")
readonly NEGATIVE_RESPONSES=("n" "no")
readonly QUESTION="Do you want to continue ?\n> "

readonly CODE_EXIT_YES=0
readonly CODE_EXIT_NO=2


if [ "$#" -ne 0 ]; then
  >&2 echo "Wrong number of arguments"
  >&2 echo "$USAGE"
  exit 1
fi

while [ 1 -eq 1 ]; do
    printf $QUESTION
    # answer=PROMPT
    if $answer in $POSITIVE_RESPONSES; do
        exit $CODE_EXIT_YES
    elif $answer in $NEGATIVE_RESPONSES; do
        exit $CODE_EXIT_NO
done
