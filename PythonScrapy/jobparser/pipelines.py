# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from itemadapter import ItemAdapter


class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.vacancies


    def process_item(self, item, spider):
        if spider.name == 'hhru':
            item['salary_min'], item['salary_max'], item['salary_cur'] = self.process_salary_hh(item['salary'])
        else:
            item['salary_min'], item['salary_max'], item['salary_cur'] = self.process_salary_sjru(item['salary'])
        del item['salary']
        collection = self.mongobase[spider.name]
        if not collection.find_one(item):
            collection.insert_one(item)
        return item

    def process_salary_hh(self, salary):
        if salary[0] == 'от' and salary[2] == 'до':
            min_zp = float(salary[1].replace('\xa0', ''))
            max_zp = float(salary[3].replace('\xa0', ''))
            cur_zp = salary[5]
        elif salary[0] == 'до':
            min_zp = None
            max_zp = None
            cur_zp = None
        else:
            min_zp = float(salary[1].replace('\xa0', ''))
            max_zp = None
            cur_zp = salary[3]
        return min_zp, max_zp, cur_zp

    def process_salary_sjru(self, salary):
        if salary[0] == 'от':
            zp_list = salary[2].split('\xa0')
            min_zp = float(''.join(zp_list[:2]))
            max_zp = None
            cur_zp = zp_list[2]
        elif salary[0] == 'до':
            zp_list = salary[2].split('\xa0')
            min_zp = None
            max_zp = float(''.join(zp_list[:2]))
            cur_zp = zp_list[2]
        elif salary[0] == 'По договорённости':
            min_zp = None
            max_zp = None
            cur_zp = None
        else:
            min_zp = float(salary[0].replace('\xa0', ''))
            max_zp = float(salary[4].replace('\xa0', ''))
            cur_zp = salary[6]
        return min_zp, max_zp, cur_zp