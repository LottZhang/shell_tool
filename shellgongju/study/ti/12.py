#!/usr/bin/python
#this py used to read Ut.html,and select the date,write to txtUt.txt 
import re
count=0
file=open("C:/Users/zhazhich/Documents/dailywork/shterm intern/dailytool/shellgongju/study/ti/Ut.html","r+",encoding= 'utf-8')
str=file.read()
####
#reip = re.search(r"(?:(\<tr\>.*?\<\/tr\>))",str,re.S)
#str_2=reip.group()
####
reip = re.compile(r"\<tr\>.*?\<\/tr\>",re.S)
str_2=reip.findall(str)
####
reip = re.compile(r"\>.*\<")
file_2=open("txtUt.txt","w+")
for i in range(0,len(str_2)):
	for date in reip.findall(str_2[i]):
        date=re.sub(r'\<','',date)
        ss=1
        date=re.sub(r'\>','',date)
        file_2.write(date)
        file_2.write("\t")
        count+=1
	file_2.write("\n")
	#print "ip>>>", date
####

