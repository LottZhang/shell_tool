#!/usr/bin/python
#def changdu(long):(8-4-4-4-12)
#random from ascii 
arg1=8
arg2=4
arg3=4
arg4=4
arg5=12
import random
final=[]
def uuid():
    item=[]
    def zengjia(qi,zhi):
        for x in range(qi,zhi):
            item.append(x)
    zengjia(48,58)
    zengjia(65,71)
    zengjia(97,103)

    suiji=random.choice(range(len(item)))
    return chr(item[suiji])
def xijie(number):
    zhong=[]
    for i in range(number):
        zhong.append(uuid())
    content = "".join(zhong)
    final.append(content)
    if number != arg5:
        final.append('-')
xijie(arg1)
xijie(arg2)
xijie(arg3)
xijie(arg4)
xijie(arg5)
content = "".join(final)
print "%s" %(content)
