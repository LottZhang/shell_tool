#!/usr/bin/python
#this py used to read filelog,and select the ip which is real to print,then print count of ip's
import re
count=0
file=open("log","r+")
str=file.read()
reip = re.compile(r"(?:(?:2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(?:2[0-4]\d|25[0-5]|[01]?\d\d?)")
for ip in reip.findall(str):
	count+=1
	print "ip>>>", ip
print "the real ip count:",count
