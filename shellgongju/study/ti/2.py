#!/usr/bin/python
# -*- coding: utf-8 -*- 
#斐波那契数列、交换两个变量的值、从一组数据中找出最大最小值等；
#count 控制数列行数
i=1
j=1
count=0
k=[]
k.append(i)
k.append(j)
while count < 100:
	 k.append(k[len(k)-1]+k[len(k)-2])
	 count+=1
print k
