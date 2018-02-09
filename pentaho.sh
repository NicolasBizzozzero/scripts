#!/bin/bash
#
# Launch the Pentaho software from the PPTI plateform of Pierre and
# Marie Curie University (Jussieu).
#
# Error codes:
# 1: Wrong number of arguments


readonly USAGE='Usage: pentaho.sh'

readonly HOSTNAME_ADDRESS=ppti-14-307-*
readonly PENTAHO_PATH='/usr/local/data-integration/spoon.sh'


if [[ `hostname` != $HOSTNAME_ADDRESS ]]; then
  # SSH to the provided hostname because it's the only machine
  # where Pentaho is installed.
  echo "Pentaho is not installed here"
  echo "You should SSH to one machine where it's installed, like :"
  echo "ssh -X $HOSTNAME_ADDRESS"
else
  sh $PENTAHO_PATH
fi
