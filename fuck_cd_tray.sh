#!/bin/bash
#
# Infinitely open and close the CD/DVD tray.


while [ 1 -eq 1 ]; do
	eject -T
done &> /dev/null
