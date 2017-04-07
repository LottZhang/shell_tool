#for i in 'seq 5 474'
path=/home/actiontec/studyinformation/RFC/chinaunix/
while read i
do
 ls $path$i
 if [ $?==0 ]; then
    iconv -f gbk -t utf8 $path$i  > /home/actiontec/studyinformation/rfclinux/$i
 fi
done < /home/actiontec/studyinformation/example/rfcchap

