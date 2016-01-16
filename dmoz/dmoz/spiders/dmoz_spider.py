import sys
reload(sys)
sys.setdefaultencoding('utf8')

from scrapy.spiders import Spider  
from scrapy.selector import Selector
from dmoz.items import WebsiteItem
from dmoz.items import DmozItem

  
class DmozSpider(Spider):  
    name = "dmoz"  
    allowed_domains = ["dmoz.org"]  
    start_urls = [  
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",  
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"  
    ]  
  
    def parse(self, response):  
        sel = Selector(response)  
        sites = sel.xpath('//ul[@class="directory-url"]/li')  
        items=[]
        #filename = response.url.split("/")[-2]  
        #open(filename, 'wb').write(response.body)  
        for site in sites:  
            item = DmozItem()  
            item['title'] = site.xpath('a/text()').extract()  
            item['link'] = site.xpath('a/@href').extract()  
            item['desc'] = site.xpath('text()').extract()  
            items.append(item)  
        return items  

class liaoSpider(Spider):
    name = "liao"
    allowed_domains = ["liaoxuefeng.com"]
    start_urls = [
		"http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="uk-nav uk-nav-side"]/li')
        items=[]
        #filename = response.url.split("/")[-2]
        #open(filename, 'wb').write(response.body)
        n=0
        for site in sites:
            item = DmozItem()
            title=site.xpath('a/text()').extract()
            link = site.xpath('a/@href').extract()
            #item['desc'] = site.xpath('text()').extract()
            #items.append(item)
            if len(title)<1:
              continue
            for t,l in zip(title,link):
                print "%s\nhttp://www.liaoxufeng.com%s" % (t,l)
            #if n<10:
            #    n=n+1
            #    continue
            #else:
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
add=0
class sammy(CrawlSpider):
    name = 'sammy'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com/sammyliu/default.html?page=1']

    rules = (
        Rule(LinkExtractor(allow=('sammyliu/default.html\?page\=',),)), #([\w]+)',),)),
        Rule(LinkExtractor(allow=('sammyliu/p', )), callback='parse_item'),
    )

    def parse_item(self, response):
        global add
        add+=1

        print
        print ('=='*50)
        self.log('Hi, this is an item page! %s' % add)

        sel = Selector(response)
        items = []
        item = WebsiteItem()

        item['title'] = sel.xpath('/html/head/title/text()').extract()
        item['link'] = response.url
        item['post_date']=sel.xpath('//span[@id="post-date"]/text()').extract()
        #item['content']=sel.xpath("//div[@id='post_detail']/descendant::*")

        #item['content']=sel.xpath("//div[@id='post_detail']/descendant::*")

        #print type(post_detail)
        #print dir(post_detail)
        #for post in post_detail.xpath(".//p").extract():
        #     print type (post)
        #     #if post.tag=='p' or post.tag=='pre':
        #     print post
        #     #    print (post.xpath('string(.)'))
        #     #if post.tag=='img':
        #     #    print (post.xpath("@src"))

        #if add=='3':
        #   exit
        #with open('/tmp/sammy.data','a+') as SAMMY:
        #    for i in item:
        #      SAMMY.write(i) 
        #  
        #items.append(item)
        #for i in title:
        #    print i
        #for post in item['post_date']:
        #    print post
        #print title
        return item
        #item = scrapy.Item()
        #item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        #item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        #item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        #return item
