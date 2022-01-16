import scrapy


class ScrapyBlogSpiderSpider(scrapy.Spider):
    name = 'scrapy_blog_spider'
    allowed_domains = ['pente.koro-pokemon.com']
    start_urls = ['http://pente.koro-pokemon.com/zukan/']

    def parse(self, response):
        print('===================================')
        # print(response.css('a[href*=zukan]::attr(href)').getall())
        print(response.xpath('//a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        pass
