__author__ = 'zhazhich'
#coding:utf-8
'''
时间和日期：获取系统当前时间并将其转换成不同的格式；
创建一个文件名中含有时间日期的文件；
'''
import time
import calendar
filename=''
a=time.localtime(time.time())
print 'the current time is:',time.asctime(a)
print 'the calendar of this month is :\n',calendar.month(a[0],a[1],2,1)
for i in range(0,5):
    if i == 4:
        filename=filename+str(a[i])
    else:
        filename=filename+str(a[i])+'_'
file=open(filename,"w")
file.write( 'the current time is:')
file.write(time.asctime(a))
file.write('\n')
file.write('the calendar of this month is :\n')
file.write(calendar.month(a[0],a[1],2,1))
file.write('\n')
file.close()
