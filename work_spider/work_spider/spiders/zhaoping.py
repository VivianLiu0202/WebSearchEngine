from typing import Iterable
import scrapy
from scrapy.http import Request
import json
import re
from bs4 import BeautifulSoup
from work_spider.items import WorkSpiderItem
from work_spider.items import KeyWordItem
from work_spider.settings import COOKIE,USER_AGENT
import random

# 城市代码
city_dict = {
    "上海": 538,
    "北京": 530,
    "天津": 531,
    "广州": 763,
    "深圳" :765,
    "武汉" :736,
    "西安" :854,
    "成都" :801,
    "重庆" :551,
    "郑州" :719,
    "南京" :635,
    "杭州" :653,
    "苏州" :639,
    "长沙" :749,
    "沈阳" :600
}

class ZhaopingSpider(scrapy.Spider):
    name = "zhaoping"
    allowed_domains = ["sou.zhaoping.com"]
    base_urls = 'https://sou.zhaopin.com/?jl={0}&kw={1}&p=1'

    num = random.randint(0, len(USER_AGENT) - 1)
    headers = {
        "HOST": "www.zhaopin.com/",
        "Referer": "http://www.zhaopin.com/",
        'User-Agent': USER_AGENT[num],
        'cookie': COOKIE,
    }

    def start_requests(self):
        '''
        初始换爬取地址，取关键词组成爬取初始地址
        :return: url
        '''
        with open('keywords.json', 'r', encoding='utf-8') as f:
            keywords = json.load(f)
        
        start_urls = []
        for city_key in city_dict.keys():
            for item in keywords:
                for job_key in item['job_words']:
                    start_urls.append(self.base_urls.format(city_dict[city_key],job_key))

        if start_urls is not None:
            for url in start_urls:
                print("start_urls is ",url)
                yield scrapy.Request(url=url,callback=self.parse_item,meta={'start_url':url})


    @staticmethod
    def salary_transform(salary_str):
        """
        薪资格式转化
        :param salary_str:薪资字符串比如1.5万
        :return: 返回数字，例如15000
        """
        if salary_str.endswith("万"):
            salary = float(salary_str[:-1]) * 10000
        elif salary_str.endswith("千"):
            salary = float(salary_str[:-1]) * 1000
        else:
            salary = float(salary_str[:-1]) * 1
        return salary



    def parse_item(self, response):
        job_list = response.xpath('//div[@class="positionlist"]/div[contains(@class, "joblist-box__item")]')
        for job in job_list:
            item = WorkSpiderItem()
            item['url'] = job.xpath('.//a[contains(@class, "joblist-box__iteminfo")]/@href').extract_first()

            item['job_name'] = job.xpath('.//span[@class="iteminfo__line1__jobname__name"]/text()').extract_first()
            item['company'] = job.xpath('.//span[@class="iteminfo__line1__compname__name"]/text()').extract_first()
            item['address'] = job.xpath('.//li[@class="iteminfo__line2__jobdesc__demand__item"][1]/text()').extract_first()

            # 提取薪资字符串
            salary_text = job.xpath('.//p[@class="iteminfo__line2__jobdesc__salary"]/text()').extract_first()

            # 检查薪资字符串是否存在并且包含预期的分隔符
            if salary_text and '-' in salary_text:
                salary_parts = salary_text.split('-')
                item['salary_min'] = self.salary_transform(salary_parts[0].strip())
                item['salary_max'] = self.salary_transform(salary_parts[1].strip())
            else:
                # 如果没有薪资信息或格式不匹配，可以设为默认值或不设置
                item['salary_min'] = salary_text
                item['salary_max'] = salary_text

            
            item['education'] = job.xpath('.//li[@class="iteminfo__line2__jobdesc__demand__item"][3]/text()').extract_first()
            item['experience'] = job.xpath('.//li[@class="iteminfo__line2__jobdesc__demand__item"][2]/text()').extract_first()
            # 技能列表可能包含多个元素，因此我们使用 extract() 而不是 extract_first()
            item['content'] = job.xpath('.//div[@class="iteminfo__line3__welfare__item"]/text()').extract()
            yield item
