#!/bin/bash
#排序文件内的数字从小到大
 cat order|awk ' {for(i=1;i<=NF;i++)print $i}'|sort -n -r

#-r 逆序