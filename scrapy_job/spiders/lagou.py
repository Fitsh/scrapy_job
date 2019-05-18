# -*- coding: utf-8 -*-
import scrapy
from scrapy_job.items import BossJobItem


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['www.zhiping.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=python&page=1&ka=page-9']

    def parse(self, response):
        print(response.url)
        divlist = response.xpath("//div[@class=\"job-primary\"]")
        for div in divlist:
            item = BossJobItem()
            item["name"] = div.xpath(".//div[@class=\"job-title\"]/text()").extract()[0]
            item["url"] = div.xpath(".//div[@class=\"info-primary\"]/h3[@class=\"name\"]/a/@href").extract()[0]
            item["url"] = "https://www.zhipin.com"+item["url"]
            item["salary"] = div.xpath(".//div[@class=\"info-primary\"]/h3[@class=\"name\"]/a/span/text()").extract()[0]
            item["company"] = div.xpath(".//div[@class=\"info-company\"]//h3[@class=\"name\"]/a/text()").extract()[0]
            item["city"] = div.xpath(".//div[@class=\"info-primary\"]/p/text()").extract()[0].split()[0]
            item["degree"] = div.xpath(".//div[@class=\"info-primary\"]/p/text()").extract()[2]
            yield item
        next = response.xpath("//a[@class=\"next\"]/@href").extract()
        if len(next)>0:
            yield scrapy.Request("https://www.zhipin.com"+next[0],callback=self.parse,dont_filter=True)
        pass
