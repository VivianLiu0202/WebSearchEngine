# -*- coding: utf-8 -*-
import scrapy
from work_spider.items import KeyWordItem
from work_spider.settings import COOKIE,USER_AGENT

class KeyWordSpider(scrapy.Spider):
    name = 'keywords_spider'
    allowed_domains = ['https://www.zhaopin.com/']
    start_urls = ['https://www.zhaopin.com/']

    headers = {
        "HOST": "www.zhaopin.com/",
        "Referer": "http://www.zhaopin.com/",
        'User-Agent': USER_AGENT,
        'cookie': COOKIE,
    }

    def parse(self, response):
        for job_category in response.xpath('//*[@id="root"]/main/div[1]/div[1]/ol/li'):
            item = KeyWordItem()
            # 提取 'job_category'，即每个类别的名称
            item['job_category'] = job_category.xpath('./nav/a/text()').extract_first()
            # 提取 'job_words'，即类别下的所有工作关键词
            item['job_words'] = job_category.xpath('./nav/div/div/a/text()').extract()
            yield item