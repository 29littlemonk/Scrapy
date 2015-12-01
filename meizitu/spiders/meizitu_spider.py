# -*- coding: utf-8 -*-
from scrapy.selector import Selector
import scrapy
from scrapy.loader import ItemLoader, Identity
from meizitu.items import MeizituItem
 
 
class MeizituSpider(scrapy.Spider):
    name = "meizitu"
    allowed_domains = ["meizitu.com"]
    start_urls = (
        'http://www.meizitu.com/a/',
    )
 
    def parse(self, response):
        sel = Selector(response)
        for link in sel.xpath('//li[@class="wp-item"]/div/h3/a/@href').extract():
            request = scrapy.Request(link, callback=self.parse_item)
            yield request
 
        if response.xpath('//div[@class="navigation"]/div[@id="wp_page_numbers"]/ul/li[last()-1]/a/@href').extract():
            nextpage = sel.xpath('//div[@class="navigation"]/div[@id="wp_page_numbers"]/ul/li[last()-1]/a/@href').extract()[0]
            print 'nextpage:%s' % nextpage
            request = scrapy.Request('http://www.meizitu.com/a/%s' % nextpage, callback=self.parse)
            yield request
 
    def parse_item(self, response):
        l = ItemLoader(item=MeizituItem(), response=response)
        l.add_xpath('name', '//h2/a/text()')
        #l.add_xpath('tag', "//div[@id='maincontent']/div[@class='postmeta  clearfix']/div[@class='metaRight']/p")
        l.add_xpath('image_url', "//div[@id='picture']/p/img/@src", Identity())
 
        l.add_value('url', response.url)
        return l.load_item()