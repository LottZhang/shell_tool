#!/bin/bash
while read i
do
 echo $i|awk '{for(x=1;x<=NF;x++)print $x}'
done < /home/actiontec/studyinformation/example/order
