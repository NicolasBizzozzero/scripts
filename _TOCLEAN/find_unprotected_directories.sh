
file=~/Documents/unprotected_directories.txt
echo > $file

i=0
while [ ! $i -eq 10 ]; do
	echo "Etu$i" >> $file
	ls -l /users/nfs/Etu$i | grep drwxrwxrwx >> $file
	i=$((i+1))
done

gedit $file &
