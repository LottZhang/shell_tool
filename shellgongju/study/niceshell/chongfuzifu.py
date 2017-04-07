#!/usr/bin/python
# -*- coding: utf-8 -*- 
#搜索出字符串的重复字母
import string
str=raw_input("please input your string:")
count=str.count('!')
if count > 1:
	print "the duplicate letter: !"
str=str.replace('!','')
for i in range(0,len(str)-1):
	count=str.count(str[i])
	if count > 1:
		if str[i] != '!':
			print "the duplicate letter:",str[i]
			str=str.replace(str[i],'!')
		else:
			continue
