#!/bin/bash
#
# List all unprotected home directories from the PPTI plateform of Pierre and
# Marie Curie University (Jussieu).
#
# Error codes:
# 1: Wrong number of arguments


readonly DIR_NUMBER=10

readonly USAGE='Usage: ppti_open_homes.sh'


if [ "$#" -ne 0 ]; then
  >&2 echo "Wrong number of arguments"
  >&2 echo "$USAGE"
  exit 1
fi

i=0
while [ ! $i -eq $DIR_NUMBER ]; do
    ls -l /users/nfs/Etu$i | grep drwxrwxrwx
    i=$((i+1))
done

