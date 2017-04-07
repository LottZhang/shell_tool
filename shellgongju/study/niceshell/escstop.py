#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
'''用到了标志位中断：global，
多线程threading
监控键盘模块pyHook'''  
  
import pythoncom  
import pyHook  
import time  
import sys 
import threading
import os
flag=0
def onKeyboardEvent(event):   
    "处理键盘事件"

    if str(event.Key)=='Escape':  #按下F12后终止
            #exit()
            global flag
            flag=1
            os.system("pause")        
    return True  
  
def jiankong():
    #创建hook句柄  
    hm = pyHook.HookManager()  
    
  
    #监控键盘  
    hm.KeyDown = onKeyboardEvent  
    hm.HookKeyboard()  
    #循环获取消息  
    pythoncom.PumpMessages(10000)
def printshuzi():
    i=1
    while 1:
         if flag == 0:
             print i
             i+=1
         else:
             c=raw_input("")
threads = []
t1 = threading.Thread(target=printshuzi)
threads.append(t1)
t2 = threading.Thread(target=jiankong)
threads.append(t2) 
if __name__ == "__main__":   
    ''''' 
    Function:操作SQLITE3数据库函数 
    Input：NONE 
    Output: NONE 
    author: socrates 
    blog:http://blog.csdn.net/dyx1024 
    date:2012-03-1 
    '''          
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
 
    
   