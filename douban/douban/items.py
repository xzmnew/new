# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 需求: 爬取豆瓣电影Top250所有电影信息(电影名称,评分,描述信息,简介)
class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影名称
    name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 描述信息: 导演,主演
    info = scrapy.Field()
    # 简介: 对电影内容简短概况
    intro = scrapy.Field()


