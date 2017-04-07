#!/usr/bin/python
# -*- coding: utf-8 -*- 
#让用户输入一些数字或字符串，以升序或降序进行排列；
import string
str=raw_input("please input your str,use ',' to split:")
a=str.split(',')
a.sort()
print a
