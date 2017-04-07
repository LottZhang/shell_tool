#!/bin/bash
function setting()
{
	ntpdate 192.168.5.1
	read -p "please input the patch ip:" patchip
	wget --no-check-certificate $patchip
	if [ $? == 0 ];then	
		patch=$(echo $patchip|sed 's/.*\///g')
		mkdir shterminstall
	#yong tar mingling zhijie gai wenjianjiaming -C mingling
		tar -xvf $patch -C ./shterminstall/
		cd shterminstall/
		cd *
		cp ../../3setup.sh ./
	#patch use upgrade,shterm use makefile ,confirm that,then continue coding
	
		echo "after install,do not forget ###usermod -s /bin/bash root"
	else
		echo "ip is wrong,exit 1"
		exit 1
	fi
}
