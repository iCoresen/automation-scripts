# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubantop250Item(scrapy.Item):
    serial_number = scrapy.Field()
    movie_name = scrapy.Field()
    introduction = scrapy.Field()
    rating_num = scrapy.Field()
    comment_num = scrapy.Field()
    quote = scrapy.Field()