# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TimeworkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Id = scrapy.Field()
    company_name = scrapy.Field()
    base = scrapy.Field()
    department_name = scrapy.Field()
    start_time = scrapy.Field()
    end_time = scrapy.Field()
    create_time = scrapy.Field()
    # 详情
    source = scrapy.Field()
    open_id = scrapy.Field()
    industry_name = scrapy.Field()
    job_category = scrapy.Field()
    occupation = scrapy.Field()
    lunch_time = scrapy.Field()
    dinner_time = scrapy.Field()
    working_days = scrapy.Field()
    remark = scrapy.Field()
    work_id = scrapy.Field()
    pass
