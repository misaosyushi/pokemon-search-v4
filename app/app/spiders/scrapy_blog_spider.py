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
        next_page = response.xpath('//*[@id="c01"]/parent::h2/following::ul/li/a[contains(@href, "zukan") and contains(@href, "shtml")]/@href').extract_first()
        # https://qiita.com/watame/items/f71a8ad93bce9b8d12ab
        request = scrapy.Request(response.urljoin(next_page), callback=self.get_detail)
        yield request

    def get_detail(self, response):
        # TODO: ポケモンリストに突っ込んでいく？
        item: PokemonItem = PokemonItem()
        item['types'] = {}
        # item = response.meta['item']
        item['name'] = response.xpath('//*[@id="main"]/h1/text()').extract_first()
        item['types'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/child::a/child::span/text()').getall()
        yield item
