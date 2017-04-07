#!/bin/bash
s=0
i=0
read -p "please input the final number for 1+2+.....+top (e.g 100 555): " top
while [ "$i" != "$top" ]
      #123123123123
do
	i=$(($i+1))
	s=$(($i+$s))
done
echo $s

