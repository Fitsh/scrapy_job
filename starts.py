from scrapy.crawler import CrawlerProcess
from scrapy_job.spiders.boss import BossSpider
from scrapy.utils.project import get_project_settings

setting = get_project_settings()
process = CrawlerProcess(settings=setting)
process.crawl(BossSpider)
process.start()
