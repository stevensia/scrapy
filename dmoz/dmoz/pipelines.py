# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from lxml import etree

class DmozPipeline(object):
    def process_item(self, item, spider):
        print "Dmoz"*50
        return item


class SammyPipeline(object):
	def process_item(self, item, spider):
		#line=json.dumps(dict(item),sort_keys=True,indent=4)+"\n"
		#with open('/tmp/sammy.data','a+') as SAMMY:
		#print item['title'][0]
		print "Starting SammyPipeline..."
		print item['title'][0]
		#content=''
		with  open('/tmp/b','a+') as SAMMY:
		#for post in item['content']:
		#for i in post.xpath("./p/text()|./u/text()|.//li/text()|./h1/text()|./h2/text()|./h3/text()|./h1/text()|./img/@src").extract():
		#for i in post.xpath("./li/descendant-or-self::*/text()|./p/descendant-or-self::*/text()|./h1/descendant-or-self::*/text()|./h2/descendant-or-self::*/text()|./h3/descendant-or-self::*/text()|./h4/descendant-or-self::*/text()").extract():
		#	for i in post.xpathxpath('string(.)').extract():
		#		print i	
		#print text
		#with  open('/tmp/sammy.data','w') as SAMMY:
		#	SAMMY.write(text)
			#body=item['content'].xpath('./div[@id="cnblogs_post_body"]')
			SAMMY.write(item['title'][0]+"\n")
			SAMMY.write(item['post_date'][0]+"\n")
			SAMMY.write(item['link']+"\n")
		#	for i in body.xpath('string(.)').extract():
		#		content=content+i
		return item
