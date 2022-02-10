import scrapy


class ScrapyBlogSpiderSpider(scrapy.Spider):
    name = 'scrapy_blog_spider'
    allowed_domains = ['pente.koro-pokemon.com']
    start_urls = ['http://pente.koro-pokemon.com/zukan/']

    def parse(self, response):
        print('===================================')
        # これだといらんやつもとれちゃう
        # print(response.xpath('//ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        print(response.xpath('//*[@id="content_in"]/div[3]/ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        print(response.xpath('//*[@id="content_in"]/div[5]/ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        print(response.xpath('//*[@id="content_in"]/div[7]/ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        print(response.xpath('//*[@id="content_in"]/div[9]/ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        # TODO: 2桁から取れない
        print(response.xpath('//*[@id="content_in"]/div[11]/ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        print(response.xpath('//*[@id="content_in"]/div[13]/ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        print(response.xpath('//*[@id="content_in"]/div[15]/ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        print(response.xpath('//*[@id="content_in"]/div[17]/ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        pass
