# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WorkSpiderItem(scrapy.Item):
    job_type = scrapy.Field() #工作种类
    job_name = scrapy.Field() #工作岗位
    company = scrapy.Field() #公司名称
    address = scrapy.Field() #工作地点
    salary_min = scrapy.Field() #最低薪资
    salary_max = scrapy.Field() #最高薪资
    education = scrapy.Field() #学历要求
    experience = scrapy.Field() #工作要求
    content = scrapy.Field() #职业技能
    url = scrapy.Field() #工作链接
    release_time = scrapy.Field() #发布时间

class KeyWordItem(scrapy.Item):
    job_category=scrapy.Field() # 行业
    job_words=scrapy.Field() # 工作关键词