#coding:utf-8
'''
时间和日期：获取系统当前时间并将其转换成不同的格式；
'''
import time
import calendar
a=time.localtime(time.time())
print 'the current time is:',time.asctime(a)
print 'the calendar of this month is :\n',calendar.month(a[0],a[1],2,1)
