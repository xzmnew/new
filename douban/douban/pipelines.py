# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DoubanPipeline(object):

    def open_spider(self, spider):
        if spider.name == 'movie':
            self.file = open('movie.jsonlines', 'w', encoding='utf8')

    def process_item(self, item, spider):
        if spider.name == 'movie':
            json.dump(dict(item), self.file, ensure_ascii=False)
            self.file.write('\n')
        return item

    def close_spider(self, spider):
        """当爬虫关闭的时候执行, 只执行一次"""
        if spider.name == 'movie':
            self.file.close()
