# scrap.sh
# Download all files recursively from the website on $1 and with the extensions passed
# by all the next arguments

### Change this variable if you want to change to download destination ###
destination=~/Téléchargements

## Number of parameters error
if [ $# -le 1 ]; then
	echo "You need at least 2 parameters."
	echo "Usage : ./scrap.sh website extension1 extension2 ..."
	exit 1
fi

## Get the website name before shift it
website=$1
shift

## Scrapping all the stuff on the website
for extension in "$@"; do
	wget -r --no-check-certificate -nv -A.$extension "$website" -P $destination
done
exit 0

