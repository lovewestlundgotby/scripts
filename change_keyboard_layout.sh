#!/bin/bash

# Usage: map a key to run this script, it will then switch between the layouts
# stated below.

current_layout=$(setxkbmap -query | awk '
    BEGIN{layout="";variant=""}
    /^layout/{layout=$2}
    /^variant/{variant=" ("$2")"}
END{printf("%s%s\n",layout,variant)}')

if [[ $current_layout == 'us' ]]; then
    setxkbmap se
    #echo "should set se"
elif [[ $current_layout == 'se' ]]; then
    setxkbmap us
    #echo "should set us"
fi

