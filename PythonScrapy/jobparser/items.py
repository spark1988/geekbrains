# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobparserItem(scrapy.Item):
    name = scrapy.Field()
    salary = scrapy.Field()
    url = scrapy.Field()
    salary_min = scrapy.Field()
    salary_max = scrapy.Field()
    salary_cur = scrapy.Field()
    _id = scrapy.Field()