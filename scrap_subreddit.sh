#!/bin/bash

# By Nicola Malizia https://unnikked.ga under MIT License

USER_AGENT="User-Agent: cli:bash:v0.0.0 (by /u/codesharer)"

if [ $# -ne 1 ]; then
 echo "USE: $0 subreddit"
 exit 1
fi

# Get the first page
DATA="$(curl -s -H $USER_AGENT https://www.reddit.com/r/$1/.json)"
AFTER="$(echo "$DATA" | jq '.data.after')"

# Parallel download all the links
echo "$DATA" | jq '.data.children[].data.url' | xargs -P 0 -n 1 -I {} bash -c 'curl -s -O {}'

# Iterate over listing and get all links
while [[ $AFTER != "null" ]]; do
 DATA="$(curl -s -H $USER_AGENT https://www.reddit.com/r/$1/.json?after=${AFTER:1:-1})"
 # Parallel download all the links
 echo "$DATA" | jq '.data.children[].data.url' | xargs -P 0 -n 1 -I {} bash -c 'curl -s -O {}'
 AFTER="$(echo "$DATA" | jq '.data.after')"
done