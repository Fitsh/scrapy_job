# -*- coding: utf-8 -*-
import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['www.zhiping.com']
    start_urls = ['http://www.zhiping.com/']

    def parse(self, response):
        pass
