# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import os
from urllib.parse import urlparse
from pymongo import MongoClient

class LeroymerlinPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.leroymerlin

    def process_item(self, item, spider):
        try:
            item['price'] = float(item['price'])
        except Exception as e:
            pass
        features = []
        for i in range(len(item['features_names'])):
            features.append(
                {
                    'name' : item['features_names'][i],
                    'value' : item['features_values'][0].strip()
                }
            )
        item['features'] = features
        del item['features_names']
        del item['features_values']
        collection = self.mongobase[spider.name]
        collection.insert_one(item)
        return item

class LeroymerlinPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
            if item['photos']:
                for img in item['photos']:
                    try:
                        yield scrapy.Request(img)
                    except Exception as e:
                        print(e)

    def item_completed(self, results, item, info):
            item['photos'] = [itm[1]['path'] for itm in results if itm[0]]
            return item
    def file_path(self, request, response=None, info=None, *, item=None):
            return item['_id'] + '/' + os.path.basename(urlparse(request.url).path)
