#!/bin/bash
#ip0
read -p "please input the main ip:" ip0
sed -i "s/ip0/$ip0/g" ifcfg-eth0
cp -rf ./ifcfg-eth0 /etc/sysconfig/network-scripts/ifcfg-eth0
#jiaru panduan shuangwangka
read -p "please input the heartbeat ip:(if not double eth,please input \"0\")" ip1
if [ $ip1 != "0" ];then
	echo 'doing eth1 work'
	sed -i "s/ip1/$ip1/g" ifcfg-eth1
	cp -rf ./ifcfg-eth1 /etc/sysconfig/network-scripts/ifcfg-eth1
else
	echo 'no eth2 ,exit'
fi
#echo 'replace ip ok,start cp'
#echo 'cp ok,restart service network'
service network restart
