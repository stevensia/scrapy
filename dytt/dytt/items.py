# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DyttItem(scrapy.Item):
    # define the fields for your item here like:
    enname = scrapy.Field()
    cnname = scrapy.Field()
    year= scrapy.Field()
    date= scrapy.Field()
    contry= scrapy.Field()
    category= scrapy.Field()
    language= scrapy.Field()
    imdb= scrapy.Field()
    douban= scrapy.Field()
    vision= scrapy.Field()
    size= scrapy.Field()
    link= scrapy.Field()

    pass
