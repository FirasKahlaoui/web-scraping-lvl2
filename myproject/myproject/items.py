# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

import scrapy

class CarItem(scrapy.Item):
    image = scrapy.Field()
    name = scrapy.Field()
    start_price = scrapy.Field()
    type = scrapy.Field()
