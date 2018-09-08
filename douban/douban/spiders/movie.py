# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from douban.items import DoubanItem

# 3. 生成电影爬虫
# 4. 完善爬虫 1. 完善提取URL的规则 2. 完善提取数据

class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    # 4.1 完善提取URL规则
    rules = (
        # LinkExtractor: 用于提取列表页分页URL
        # callback: 通过规则提取出来的URL对应响应交给给parse_item进行处理
        # follow=True:  通过规则提取出来的URL对应响应继续给rules来提取新的URL
        Rule(LinkExtractor(allow=r'\?start=\d+&filter='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 3.2 提取我们需要的数据
        # 先分组: 获取包含电影信息的li标签列表
        lis = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        # 遍历li标签列表, 提取需要的数据
        for li in lis:
            """提取数据"""
            item = DoubanItem()
            item['name'] = li.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract_first()
            item['score'] = li.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract_first()
            item['info'] = ''.join([i.strip().replace('\xa0', ' ') for i in li.xpath('./div/div[2]/div[2]/p[1]/text()').extract()])
            item['intro'] = li.xpath('./div/div[2]/div[2]/p[2]/span/text()').extract_first()
            print(item)
            #  Spider must return Request, BaseItem, dict or None, got 'list' i
            # yield ['hehe']