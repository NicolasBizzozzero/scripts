for f in *; do
	if [ -d "$f" ]; then
		# We are in a directory, we must call recursively our function in this directory
		#./$0
	fi

	else if [ -f "$f"]; then
		# We are in a file, we must look for "TODO" comments.

	fi
done