#!/bin/bash
ntpdate 192.168.5.1
read -p "please input the patch ip:" patchip
wget --no-check-certificate $patchip
patch=$(echo $patchip|sed 's/.*\///g')
mkdir shterminstall
#yong tar mingling zhijie gai wenjianjiaming -C mingling
tar -xvf $patch -C ./shterminstall/
cd shterminstall/
cd *
cp /root/setup/3setup.sh ./
#patch use upgrade,shterm use makefile ,confirm that,then continue coding

echo "after install,do not forget ###usermod -s /bin/bash root"
