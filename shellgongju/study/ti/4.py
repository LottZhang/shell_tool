#!/usr/bin/python
# -*- coding: utf-8 -*- 
#雷诺数的计算公式是(Dvrho)mu，其中D为直径，v为速度，rho为密度，mu为黏性。编写一个程序，接收一组数据并计算雷诺数。如果小于 2100，则显示“层流”；在2100至4000之间，则显示“暂态流”；大与4000则显示“湍流”（使用分支语句if else then）；
#雷诺数=管径*流速*流体密度/流体粘度
import string
str=raw_input("please input your data,(D,v,rho,mu)use ',' to split:")
a=str.split(',')
D=float(a[0])
v=float(a[1])
rho=float(a[2])
mu=float(a[3])
leinuo=D*v*rho/mu
if leinuo <= 2100:
	print "层流"
elif leinuo >= 4000:
	print "瑞流"
else:
	print "暂态"
