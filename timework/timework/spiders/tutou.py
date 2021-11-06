import scrapy
from scrapy import Request

from timework.items import TimeworkItem
from timework.sqlhelper import DBHelper


class TutouSpider(scrapy.Spider):
    name = 'tutou'
    allowed_domains = ['tutou.site']
    # start_urls = ['http://tutou.site/']
    start_urls = ["https://tutou.site:8080/?method=multi_search&company_department=公司&sorted=0&page_index=1&limit=10"]

    def parse(self, response):
        # print(response.json())
        _data_json = response.json()

        _next_data = _data_json['data']
        print(f"len(_next_data)", len(_next_data))

        if len(_next_data) != 0:
            index = 1
            for i in range(0, len(_next_data)):
                print(f"i的值", i)
                index += 1
                item = TimeworkItem()
                item['Id'] = _next_data[i]['id']
                item['company_name'] = _next_data[i]['company_name']
                item['base'] = _next_data[i]['base']
                item['department_name'] = _next_data[i]['department_name']
                item['start_time'] = _next_data[i]['start_time']
                item['end_time'] = _next_data[i]['end_time']
                item['create_time'] = _next_data[i]['create_time']
                # 详情页
                detail_url = "https://tutou.site:8080/?method=detail_page&id={}".format(item['Id'])
                yield Request(detail_url, callback=self.parse_detail, meta={"item": item})
                for index in range(2, 150):
                    _next = "https://tutou.site:8080/?method=multi_search&company_department=%E5%85%AC%E5%8F%B8&sorted=0&page_index={}&limit=10".format(
                        index)
                    # print(f"_next", _next)
                    yield Request(_next, callback=self.parse)
                # yield item

    # 详情页面
    # yield Request()

    # 下一页
    # i = 0

    def parse_detail(self, response):
        # "https://tutou.site:8080/?method=detail_page&id=2819"
        _data = response.json()
        _data = _data["data"]
        item = response.meta['item']
        item['source'] = _data['source']
        item['open_id'] = _data['open_id']
        item['industry_name'] = _data['industry_name']
        item['job_category'] = _data['job_category']
        item['occupation'] = _data['occupation']
        item['lunch_time'] = _data['lunch_time']
        item['dinner_time'] = _data['dinner_time']
        item['working_days'] = _data['working_days']
        item['remark'] = _data['remark']
        # item['Id'] = _data['id']
        yield item
