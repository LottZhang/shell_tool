#!/usr/bin/python
# -*- coding: utf-8 -*- 
#雷诺数=管径*流速*流体密度/流体粘度
''' 雷诺数的计算公式是(Dvrho)mu，其中D为直径，v为速度，rho为密度，mu为黏性。编写一个程序，接收一组数据并计算雷诺数。如果小于 2100，则显示“层流”；在2100至4000之间，则显示“暂态流”；大与4000则显示“湍流”（使用分支语句if else then）；
5、 修改上面的程序，显示“开始新的计算？（是否）”，如果选“是”，则重新输入一组数据；如果选“否”，则退出程序（使用循环语句）。如果mu 的值为0，程序是否会提示“除数为0”的错误？或是给出“程序崩溃”的提示？怎样处理这种情况呢？该程序语言里是否提供了这样的机制？（异常处理）
'''
import string
def jisuan():
	str=raw_input("please input your data,(D,v,rho,mu)use ',' to split:")
	a=str.split(',')
	D=float(a[0])
	v=float(a[1])
	rho=float(a[2])
	mu=float(a[3])
	#determine mu is 0 or not
	if mu == 0:
		raise ValueError,"除数为%d错误" %mu
	leinuo=D*v*rho/mu
	#determine the result of leinuo
	if leinuo <= 2100:
		print "层流"
	elif leinuo >= 4000:
		print "瑞流"
	else:
		print "暂态"

def main():
	flag='yes'
	while flag == 'yes':
		jisuan()
		flag=raw_input("开始新的计算？（yes|no）:")

if __name__ == '__main__':
        main()

