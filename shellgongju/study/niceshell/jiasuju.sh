#!/bin/bash
find ./ -type f|while read name
do
        if [ -s "$name" ]
                then echo -e "###\n$name\n###"
        else
                dd if=/home/lott/wenjian of="$name"
#               cat /home/lott/wenjian >> "$name"
        fi
done
