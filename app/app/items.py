# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class PokemonItem(Item):
    name = Field()
    species = Field()
    type = Field()
    height = Field()
    weight = Field()
    ability = Field()
    hidden_ability = Field()
    base_stats = Field()


class BaseStatsItem(Item):
    hp = Field()
    attack = Field()
    defense = Field()
    sp_attack = Field()
    sp_defense = Field()
    speed = Field()
    total = Field()
