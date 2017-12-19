#!/bin/bash
# find_videos.sh
#
# Find all video files on a computer


readonly USAGE='Usage: test <problem_number>'
readonly EXTENSIONS=("3gp" "8svx" "aa" "aac" "aax" "act" "aiff" "amr" "ape" "au" "awb" "dct" "dss" "dvf" "flac" "iklax" "ivs" "m4a" "mmf" "mogg" "mp3" "mpc" "msv" "oga" "ogg" "opus" "ra" "raw" "rm" "sln" "tta" "vox" "wav" "webm" "wma" "wv")

for extension in ${EXTENSIONS[@]}; do
    locate "*.$extension"
done

exit(0)
