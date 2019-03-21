#!/bin/bash

# Usage: bind key to run the script. It will open a rofi prompt that will search
# through the chosen directory dir.

dir="/home/love"

xdg-open "$(locate $dir | rofi -threads 0 -width 1920 -padding 300 -dmenu -i -p "locate")"
