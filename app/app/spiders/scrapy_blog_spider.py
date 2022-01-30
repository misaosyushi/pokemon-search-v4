import scrapy


class ScrapyBlogSpiderSpider(scrapy.Spider):
    name = 'scrapy_blog_spider'
    allowed_domains = ['pente.koro-pokemon.com']
    start_urls = ['http://pente.koro-pokemon.com/zukan/']

    def parse(self, response):
        print('===================================')
        # print(response.css('a[href*=zukan]::attr(href)').getall())
        # TODO: ulのzukan_imgを指定できたら良さそう
        # ul指定して取ってからforで回す？
        # print(response.xpath('//ul[@class="zukan_img"]/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        print(response.xpath('//ul[@class="ul2"]/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        pass
