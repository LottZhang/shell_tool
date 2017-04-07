#!/usr/bin/env python
#-*-coding:utf-8-*-

from htmlentitydefs import entitydefs
from HTMLParser import HTMLParser

class TitleParser(HTMLParser):
    
    def __init__(self):
        #定义要搜寻的标签
        self.handledtags = ['title','p']  #提出标签，理论上可以提取所有标签的内容
        self.processing = None
        HTMLParser.__init__(self)  #继承父类的构造函数

    def handle_starttag(self,tag,attrs):
        #判断是否在要搜寻的标签内
        if tag in self.handledtags:
            self.data = ''
            self.processing = tag

    def handle_data(self,data):
        if self.processing:
            self.data += data

    def handle_endtag(self,tag):
        if tag == self.processing:
            print str(tag)+' : '+str(self.data)
            self.processing = None

    #下面两个函数都是对html实体做的转码，没有深究
    def handle_entityref(self,name): 
        if entitydefs.has_key(name): 
            self.handle_data(entitydefs[name]) 
        else: 
            self.handle_data('&'+name+';') 
            
    def handle_charref(self,name): 
        try: 
            charnum=int(name) 
        except ValueError: 
            return 
        if charnum<1 or charnum>255: 
            return 
        self.handle_data(chr(charnum)) 
    
parser = TitleParser()
html1 = """
<html> 
<head> 
<title> XHTML 与 HTML 4.01 标准没有太多的不同</title> 
</head> 
<body> 
<p>i love you</p> 
</body> 
</html> 
"""

html2 = """
<html> 
<head> 
<title> XHTML 与&quot; HTML 4.01 &quot;标准没有太多的不同</title> 
</head> 
<body> 
<p>i love&#247; you&times;</p> 
</body> 
</html> 
"""
parser.feed(html2)
