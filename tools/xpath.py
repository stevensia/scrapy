#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import lxml
from lxml import etree
import re
#import requests
tag=0
headers = {
   'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
   #'Referer': followee_url
   }

with open('func.html','r') as FH:
	javahtml=FH.read()
	htmlElement=etree.HTML(javahtml)
linkhtml=htmlElement.xpath(u'//div[@class="x-sidebar-left-content"]/li')
for i in linkhtml:
	link = i.xpath('a/@href')
	print link
	#linkaf=i.attrib["href"]
	#link="http://www.liaoxuefeng.com"+linkaf
	#if re.match(r'map',name):
	#	name='set-map'
	#print name,
	##r=requests.get(link,headers=headers)
	#continue
	#with open(name,'w') as NAME:
	#	NAME.write(r.content)
