#!/bin/bash
#
# Retrieve the location of an IP address by curling the website "ip-api.com".
# If no argument is passed, retrieve the current location / IP address of the
# computer.
#
# Error codes:
# 1: Wrong number of arguments


readonly USAGE='Usage: ip_to_location.sh <IP_ADDRESS>'

readonly WEBSITE='http://ip-api.com'


if [ "$#" -ge 2 ]; then
  >&2 echo "Wrong number of arguments"
  >&2 echo "$USAGE"
  exit 1
fi

curl "${WEBSITE}/$1"
