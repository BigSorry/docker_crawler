import scrapy

class Coin(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()