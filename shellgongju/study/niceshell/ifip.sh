eth=$1
ifconfig $eth|grep -v '127.0.0.1'|grep 'inet addr'|sed 's/^.*addr://g'|sed 's/B.*$//g'

