# -*- coding: utf-8 -*-

# Scrapy settings for meizitu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'meizitu'

SPIDER_MODULES = ['meizitu.spiders']
NEWSPIDER_MODULE = 'meizitu.spiders'
ITEM_PIPELINES = {'meizitu.pipelines.MeizituPipeline': 2,'scrapy.pipelines.images.ImagesPipeline': 1,'meizitu.pipelines.MeizituImagesPipeline':1}
IMAGES_STORE = 'E:/Eclipse/workspace/Jinbag/src/meizitu'
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meizitu (+http://www.yourdomain.com)'
