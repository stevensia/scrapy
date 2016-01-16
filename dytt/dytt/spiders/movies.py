# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from dytt.items import DyttItem


class MoviesSpider(CrawlSpider):
    name = 'movies'
    allowed_domains = ['www.dy2018.com']
    start_urls = ['http://www.dy2018.com/html/gndy/dyzz/index.html']

    rules = (# Rule(LinkExtractor(allow=r'dyzz/index'), callback='parse_item', follow=True)),
        Rule(LinkExtractor(allow=r'dyzz/index.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = DyttItem()
        item['cnname'] = response.xpath('//b/a[@class="ulink"]/text()').extract()
        item['link'] = response.xpath('//b/a[@class="ulink"]/@href').extract()
        item['date'] = response.xpath('//font[@color="#8F8C89"]/text()').extract()
        print item['cnname'][0]
        print item['date'][0]
        print item['link'][0]
        return item
