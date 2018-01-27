#!/bin/bash
#
# Extract audio flux from multiple video files.
#
# Dependencies:
# - ffmpeg
# - extension.sh 
#
# Error codes:
# 1: Wrong number of arguments


readonly USAGE="Usage: extract_audio.sh <VIDEO_FILE> [-e --extension EXTENSION (default: mp3)]" 

readonly DEFAULT_AUDIO_EXTENSION="mp3"

for arg in "$@"; do
	# Choose the proper extension for the output audio file
	extension=`extension.sh "$arg"`
	case "$extension" in
	  mkv) audio_extension="m4a";;
	  *) audio_extension=$DEFAULT_AUDIO_EXTENSION
	esac

	# Extract the audio from the source video file
	video_basename=`basename "$arg"`
	ffmpeg -i "$arg" -vn -c:a copy "$video_basename.$audio_extension"
done
