# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ContactcarsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    links = scrapy.Field()
    make = scrapy.Field()
    model = scrapy.Field()
    year = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    