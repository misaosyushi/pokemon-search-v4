import scrapy


from ..items import PokemonItem, AbilityItem, BaseStatsItem


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
        # item = response.meta['item']
        pokemon: PokemonItem = PokemonItem()
        pokemon['type'] = {}
        pokemon['name'] = response.xpath('//*[@id="main"]/h1/text()').extract_first()
        pokemon['species'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/text()[1]').get().split(': ')[1]
        pokemon['type'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/child::a/child::span/text()').getall()
        pokemon['height'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/text()[3]').get().split(': ')[1]
        pokemon['weight'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/text()[4]').get().split(': ')[1]

        ability: AbilityItem = AbilityItem()
        # TODO: 複数とれるようにする、親のtrを指定して取ってくる
        ability['name'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[10]/td[1]/text()').get()
        ability['description'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[10]/td[2]/text()').get()
        pokemon['ability'] = [dict(ability)]

        hidden_ability: AbilityItem = AbilityItem()
        # TODO: 複数とれるようにする、親のtrを指定して取ってくる
        hidden_ability['name'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[12]/td[1]/text()').get()
        hidden_ability['description'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[12]/td[2]/text()').get()
        pokemon['hidden_ability'] = [dict(hidden_ability)]

        base_stats: BaseStatsItem = BaseStatsItem()
        base_stats['hp'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[4]/td[1]/table/tbody/tr[1]/td[2]/text()').get()
        base_stats['attack'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[4]/td[1]/table/tbody/tr[2]/td[2]/text()').get()
        base_stats['defense'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[4]/td[1]/table/tbody/tr[3]/td[2]/text()').get()
        base_stats['sp_attack'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[4]/td[1]/table/tbody/tr[4]/td[2]/text()').get()
        base_stats['sp_defense'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[4]/td[1]/table/tbody/tr[5]/td[2]/text()').get()
        base_stats['speed'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[4]/td[1]/table/tbody/tr[6]/td[2]/text()').get()
        base_stats['total'] = response.xpath('//*[@id="col1"]/table[1]/tbody/tr[4]/td[1]/table/tbody/tr[7]/td[2]/text()').get()
        pokemon['base_stats'] = [dict(base_stats)]

        yield pokemon
