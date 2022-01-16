import scrapy


class ScrapyBlogSpiderSpider(scrapy.Spider):
    name = 'scrapy_blog_spider'
    allowed_domains = ['pente.koro-pokemon.com']
    start_urls = ['http://pente.koro-pokemon.com/zukan']

    def parse(self, response):
        print(response.css('.ul2 .zukan_img'))
        pass
