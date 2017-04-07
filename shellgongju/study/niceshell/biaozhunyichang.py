#!/usr/bin/python  
# -*- coding: utf-8 -*-  
# Filename: usingException.py  
# 异常处理  
  
  
# 写一个自己定义的异常类  
class MyInputException(Exception):  
    def __init__(self, length, least):  
        Exception.__init__(self)  
        self.length = length  
        self.least = least  
          
  
try:  
    s = raw_input('输入一个字符串：')  
# 如果长度小于5，触发自定义的异常   
    if len(s) < 5:  
        raise MyInputException(len(s),5)  
except EOFError:  
    print '触发了EOF错误,按了Ctrl+d'  
except MyInputException, x:  
    print '输入的字符串只有%d，至少需要%d个字符' % (x.length, x.least)  
except Exception:  
    print '不知道什么错误！'  
else:  
    print s
