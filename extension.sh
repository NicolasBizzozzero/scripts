#!/bin/bash
#
# Print the extension of the file passed as argument.
# By default, print everything after the last occurence of the character `.`. 
#
# Examples:
# $ extension.sh file.txt
# txt
# $ extension.sh file
#
# $ extension.sh file.tar.gz
# gz
#
# Source:
# * https://unix.stackexchange.com/a/1572
#
# Error codes:
# 1: Wrong number of arguments


readonly USAGE='Usage: extension.sh <FILE_NAME>'

if [ "$#" -ne 1 ]; then
  >&2 echo "Wrong number of arguments"
  >&2 echo "$USAGE"
  exit 1
fi


extension=`echo "$1" | awk -F . '{print $NF}'`

# Case where the file does not have any extension
if [  "$1" == "$extension" ]; then
  echo ""
else
  echo "$extension"
fi

