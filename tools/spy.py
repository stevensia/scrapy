#!/usr/bin/python
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from lxml import etree
from io import StringIO
#from scrapy.spiders import Spider  
#from scrapy.selector import Selector
#from dmoz.items import DmozItem

  
#class DmozSpider(Spider):  
#    name = "dmoz"  
#    allowed_domains = ["dmoz.org"]  
#    start_urls = [  
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",  
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"  
#    ]  
#  
#    def parse(self, response):  
#        sel = Selector(response)  
#        sites = sel.xpath('//ul[@class="directory-url"]/li')  
#        items=[]
#        #filename = response.url.split("/")[-2]  
#        #open(filename, 'wb').write(response.body)  
#        for site in sites:  
#            item = DmozItem()  
#            item['title'] = site.xpath('a/text()').extract()  
#            item['link'] = site.xpath('a/@href').extract()  
#            item['desc'] = site.xpath('text()').extract()  
#            items.append(item)  
#        return items  
#
#class DmozSpider(Spider):
#    name = "liao"
#    allowed_domains = ["liaoxuefeng.com"]
#    start_urls = [
#		"http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
#    ]
#
#    def parse(self, response):
#        sel = Selector(response)
#        sites = sel.xpath('//ul[@class="uk-nav uk-nav-side"]/li')
#        items=[]
#        #filename = response.url.split("/")[-2]
#        #open(filename, 'wb').write(response.body)
#        n=0
#        for site in sites:
#            item = DmozItem()
#            title=site.xpath('a/text()').extract()
#            link = site.xpath('a/@href').extract()
#            #item['desc'] = site.xpath('text()').extract()
#            #items.append(item)
#            if len(title)<1:
#              continue
#            for t,l in zip(title,link):
#                print "%s\nhttp://www.liaoxufeng.com%s" % (t,l)
#            #if n<10:
#            #    n=n+1
#            #    continue
#            #else:

with open('func.html','r') as FH:
	response=FH.read()
parser=etree.HTMLParser()
tree=etree.parse(response,parser)
sites = tree.xpath('//ul[@class="uk-nav uk-nav-side"]/li')
items=[]
for site in sites:
            title=site.xpath('a/text()').extract()
            link = site.xpath('a/@href').extract()
            #item['desc'] = site.xpath('text()').extract()
            #items.append(item)
            if len(title)<1:
              continue
            for t,l in zip(title,link):
                print "%s\nhttp://www.liaoxufeng.com%s" % (t,l)

