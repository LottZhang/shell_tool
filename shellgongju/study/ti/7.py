#!/usr/bin/python
# -*- coding: utf-8 -*- 
'''
用不同的格式进行输出（比如四舍五入到5位数字、截取前四位数字、用0填充左边或右边、左右对齐等）（输入输出操作）
'''
import math
import string
import biaozhunyichang
def initialize():
	#str 
	global str,fenge,zhu,flag,dict
	str=raw_input("please input your str to cal and method(e.g 555,a)\n四舍五入到5位数字a、截取前四位数字b、用0填充右边至10位c、用0中间对齐0d\n:")
	fenge=str.split(',')
	zhu=fenge[0]
	flag=fenge[1]
	#method
	dict={'a':'jinwei','b':'jiesiwei','c':'lbulin','d':'center'}
class jisuanprint:
	def __init__(self,zhu,flag):
		self.zhu = zhu
		self.flag = flag
	def jinwei(self):
		result=int(self.zhu)
		j=1
		for i in range(0,len(self.zhu))[::-1]:
			if self.zhu[i] < '5':
				break
			else:
				result=round(result,-j)
				self.zhu='%d' %result
				j+=1
				continue
			break		
		print int(result)
	def jiesiwei(self):
		result=biaozhunyichang.yichang(self.zhu,5)
		if result== None:
			pass
		else:
			if result.isdigit():
				print result[0:4]
	def lbulin(self):
		#result=int(self.zhu)
		print self.zhu.ljust(10,'0')
	def center(self):
		print self.zhu.center(10,'0')
def main():
	initialize()
	a=jisuanprint(zhu,flag)
	jisuan=eval('a.'+dict[flag])
	jisuan()
	#a.jinwei()
if __name__ == '__main__':
        main()
