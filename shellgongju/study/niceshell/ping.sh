#!/bin/bash
pre=$1
for i in `seq 1 254`
do
  echo $i
  ping $pre.$i -c 1 > /dev/null
  if [ $? == 0 ] ;then
  	echo "$pre.$i"
  else 
  	echo "$pre.$i is available"
  fi
done
			 
