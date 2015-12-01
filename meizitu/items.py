# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeizituItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    url = scrapy.Field()
    name = scrapy.Field()
    #tag = scrapy.Field()
    image_url = scrapy.Field()
