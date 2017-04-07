__author__ = 'zhazhich'
import linecache
import os
import re
file=open("C:/Users/zhazhich/PycharmProjects/validate_field/responsefile.txt","r+")
str=file.read()
field='countryName\n'
def asd(field):
    reip = re.compile("\<"+field+"\>.*?\<\/"+field+"\>",re.S)
    str_2=reip.findall(str)
    global str_2

asd(field)
print (str_2)