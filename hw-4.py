# Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru, yandex-новости.
# Для парсинга использовать XPath.
# Структура данных должна содержать:
# название источника;
# наименование новости;
# ссылку на новость;
# дата публикации.
# Сложить собранные новости в БД
# Минимум один сайт, максимум - все три

from lxml import html
import requests
from pprint import pprint
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['parser_db']


series_collection = db['hh_ru']
url = 'https://lenta.ru/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

response = requests.get(url, headers=header)
dom = html.fromstring(response.text)

news = dom.xpath("//div[@class='topnews__column']//span[@class='card-mini__title']")


def insert_document(collection, data):
    if not collection.find_one({'link': good['link']}):
        return collection.insert_one(data).inserted_id

goods = []
counter = 1
for new in news:
    good = {}

    name = new.xpath("./text()")[0]
    link = new.xpath("../../@href")[0]
    time = new.xpath(".//..//time[@class='card-mini__date']/text()")[0]

    good['counter'] = counter
    good['name'] = name
    good['link'] = link
    good['time'] = time

    goods.append(good)
    counter += 1
    insert_document(series_collection, good)

pprint(goods)