path=/home/actiontec/studyinformation/RFC/chinaunix/
function zhuanhuan(){
	 ls $path$i
	 if [ $?==0 ]; then
	    iconv -f gbk -t utf8 $path$i  > /home/actiontec/studyinformation/rfclinux/$i
	 fi
}
while read i
do
 zhuanhuan
done < /home/actiontec/studyinformation//example/rfcchap
