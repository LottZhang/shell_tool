#!/bin/bash
#you pwd path should be patch path,then running this sh
function fileinstall(){
	file=$(ls|grep Makefile)
	checkinstall=0
	if [ -z $file ];then
        	echo "there is no makefile"
		checkinstall=$(($checkinstall+1))
	else
        	make install
	fi
}
function upgradeinstall(){
upgrade=$(ls|grep upgrade)
if [ -z $upgrade ];then
        echo "there is no upgrde file"
	checkinstall=$(($checkinstall+1))
else
        . $upgrade
fi
}
function checkinstall(){
if [ $checkinstall = "2" ];then
	echo "setup all fail"
	exit 0
fi
}
function changerootmode(){
	cat /etc/passwd|grep root
	read -p "do you need to change root usermod?(Y or N)" option
	case $option in
  		"y"|"Y")
		  usermod -s /bin/bash root
		  ;;
  		"n"|"N")
    		  echo "do noting"
    		  ;;	
  		 *)
    		  echo "usage y or n"
    		  ;;
	esac
	cat /etc/passwd|grep root
}
##########main
fileinstall
upgradeinstall
checkinstall
changerootmode
