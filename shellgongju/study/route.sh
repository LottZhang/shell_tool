dhclient -v eth0 > ~/dhlog 2>&1
gw=$(cat ~/dhlog|grep DHCPACK|cut -d ' ' -f 5)
net=${gw%.*}.0
route add -net $net gw $gw

