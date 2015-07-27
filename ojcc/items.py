# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AccountItem(scrapy.Item):

    origin_oj = scrapy.Field()
    username = scrapy.Field()
    nickname = scrapy.Field()
    accept = scrapy.Field()
    submit = scrapy.Field()
    rank = scrapy.Field()
    status = scrapy.Field()
    solved = scrapy.Field()
