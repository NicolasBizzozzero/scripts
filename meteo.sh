#!/bin/bash
#
# Print the current meteo of a location.
#
# This script use the `curl` command to retrieve the formated response given
# by the site 'http://wttr.in' for a specific location.
# The site handle itself all errors regarding the name of the location or its
# inexistence.
#
# Error codes:
# 1: Wrong number of arguments


readonly HOST_URL="http://wttr.in/"
readonly USAGE="Usage: meteo.sh <LOCATION>"

if [ "$#" -ne 1 ]; then
  >&2 echo "Wrong number of arguments"
  >&2 echo "$USAGE"
  exit 1
fi

LOCATION="$1"

curl -4 "${HOST_URL}$1"
