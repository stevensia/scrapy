# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DyttPipeline(object):
    def process_item(self, item, spider):
        print item['cnname'][0]
        #print item['date'][0]
        #print item['link'][0]
        return item
