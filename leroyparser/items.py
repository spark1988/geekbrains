# Define here the models for your scraped items
#
# See documentation in:

import scrapy

from itemloaders.processors import TakeFirst, MapCompose

class LeroymerlinItem(scrapy.Item):
    _id = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
    price = scrapy.Field(output_processor=TakeFirst())
    features_names = scrapy.Field()
    features_values = scrapy.Field()
    features = scrapy.Field()
    url = scrapy.Field(output_processor=TakeFirst())
