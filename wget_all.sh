#!/bin/bash
#
# Use the `wget` command to retrieve all documents of a certain type located
# in a domain and its subdomains.
#
# This script ignore all files 'robots.txt'
#
# Error codes:
# 1: Wrong number of arguments


readonly USAGE='Usage: wget_all.sh <EXTENSION> <URL>'


if [ "$#" -ne 2 ]; then
  >&2 echo "Wrong number of arguments"
  >&2 echo "$USAGE"
  exit 1
fi

EXTENSION="$1"
URL="$2"
leaf="${url##*/}"
OUTPUT_DIR="${leaf%.*}"

mkdir "$OUTPUT_DIR"
wget -r --no-check-certificate -nd --no-parent -A."$EXTENSION" -e robots=off "$URL" -P "$OUTPUT_DIR"
