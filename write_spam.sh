#!/bin/bash
#
# Use the `write` command to spam a message infinitely at the same user.
#
# Error codes:
# 1: Wrong number of arguments


if [! $# -eq 2 ]; then
	echo "Usage : ./write_spam.sh <USER_NAME> <SENTENCE>"
	exit 1
fi

USER_NAME="$1"
SENTENCE="$2"

while [ 1 -eq 1 ]; do
	write $USER_NAME
	"$2"
done
