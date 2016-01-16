#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from lxml import etree

with open('fangfa','r') as FH:
	html=FH.read()
	htmlElement=etree.HTML(html)
htcontent=htmlElement.xpath("//div[@class='x-wiki-content']/descendant::*")
for i in htcontent:
    if i.tag=='p' or i.tag=='pre':
       print (i.xpath('string(.)'))
#
