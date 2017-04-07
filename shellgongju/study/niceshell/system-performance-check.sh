#!/usr/bin/expect

set timeout 20#expect success timeout time

# Login
spawn telnet 192.168.1.254
sleep 1
expect "Login:"
send "admin\r"
sleep 1
expect "Password:"
send "1\r"
sleep 1
expect ">"
#checking shared memory
send "meminfo\r"
sleep 1
expect ">"
send "sh\r"
sleep 1
expect "#"
#checking DUT time
send "date\r"
sleep 1
expect "#"
#checking system memory
send "cat /proc/meminfo\r"
sleep 1
expect "#"
#checking CPU loading
send "mpstat -P ALL 5 1\r"
sleep 1
expect "#"
send "exit\r"
sleep 1
expect ">"
send "exit\r"


#interact # this commond can manual control

exit
