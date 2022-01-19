import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from leroyparser.items import LeroymerlinItem

class LeroySpider(scrapy.Spider):
    name = 'leroy'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, search):
        super().__init__()
        self.start_urls = [f'https://leroymerlin.ru/search/?q={search}']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[contains(@aria-label, 'Следующая страница')]/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
            links = response.xpath("//a[@data-qa='product-name']")
            for link in links:
                yield response.follow(link, callback=self.parse_item)

    def parse_item(self, response: HtmlResponse):
        loader = ItemLoader(item=LeroymerlinItem(), response=response)
        loader.add_xpath('_id', "//span[@slot='article']/@content")
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('price', "//span[@slot='price']/text()")
        loader.add_xpath('photos', "//uc-pdp-media-carousel//source[@srcset and contains(@media, '1024')]/@srcset")
        loader.add_xpath('features_names', "//dt[@class='def-list__term']/text()")
        loader.add_xpath('features_values', "dd[@class='def-list__definition']/text()")
        loader.add_value('url', response.url)
        yield loader.load_item()
