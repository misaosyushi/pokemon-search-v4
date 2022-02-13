import scrapy


from ..items import PokemonItem


class ScrapyBlogSpiderSpider(scrapy.Spider):
    name = 'zukan'
    allowed_domains = ['pente.koro-pokemon.com']
    start_urls = ['http://pente.koro-pokemon.com/zukan/']

    def parse(self, response):
        print('===================================')
        # print(response.xpath('//*[@id="c01"]/parent::h2/following::ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        # print(response.xpath('//*[@id="c02"]/parent::h2/following::ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        # print(response.xpath('//*[@id="c03"]/parent::h2/following::ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        # print(response.xpath('//*[@id="c04"]/parent::h2/following::ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        # print(response.xpath('//*[@id="c05"]/parent::h2/following::ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        # print(response.xpath('//*[@id="c06"]/parent::h2/following::ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        # print(response.xpath('//*[@id="c07"]/parent::h2/following::ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        # print(response.xpath('//*[@id="c08"]/parent::h2/following::ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').getall())
        next_page = response.xpath('//*[@id="c08"]/parent::h2/following::ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').extract_first()
        # TODO: 2回呼ばれる。forの中で呼ぶ。
        # https://qiita.com/watame/items/f71a8ad93bce9b8d12ab
        request = scrapy.Request(response.urljoin(next_page), callback=self.getDetail)
        yield request

    def getDetail(self, response):
        # TODO: ポケモンリストに突っ込んでいく？
        item = PokemonItem()
        # item = response.meta['item']
        item['name'] = response.xpath('//*[@id="main"]/h1/text()').extract_first()
        print(item)
        yield item
