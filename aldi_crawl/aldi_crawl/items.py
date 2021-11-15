# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AldiCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_title = scrapy.Field()
    product_image = scrapy.Field()
    pack_size = scrapy.Field()
    price_per_unit = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()
    pass
