import scrapy


class TutouSpider(scrapy.Spider):
    name = 'tutou'
    allowed_domains = ['/tutou.site']
    start_urls = ['http:///tutou.site/']

    def parse(self, response):
        pass
