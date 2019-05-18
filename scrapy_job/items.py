# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    city = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
    text = scrapy.Field()
    url = scrapy.Field()
    degree = scrapy.Field()
