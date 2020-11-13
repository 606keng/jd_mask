#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: url.py
@time: 2020/11/13 
"""
#!/usr/bin/python
#coding=utf-8

#urllib2是python自带的模块，在python3.x中被改为urllib.request
import urllib.request
import re
import requests

# https://item.jd.com/100012043978.html
# page = urllib.request.urlopen('http://item.jd.com/100012043978.html')
# html = page.read().decode('utf-8')
html = requests.get("http://www.baidu.com").text
print(html)
# Python3 findall数据类型用bytes类型
# or html=urllib.urlopen(url).read()

title=re.findall('<title>(.+)</title>',html)
print (title)