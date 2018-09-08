# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class DoubanDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.


    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        # 当引擎把request对象交给下载器的时候, 都会经过该方法

        # Must either:
        # - return None: continue processing this request(重点)
        # - 返回None: 继续该请求处理, 经过后面下载器中间 -> 下载器: 实现随机User-Agent,代理IP
        # - or return a Response object
        # - 返回Response对象, 中断本次请求, 响应对象-> 经过前面下载器中间件 -> 引擎
        # - 使用场景: 有个别请求, 需要使用selenium来提取数据,封装为response再交给引擎.
        # - or return a Request object
        # - 返回Request对象, 中断本次请求 -> 把新的Request对象,交给引擎 -> 调度器
        # - 使用场景: 做请求的重定向
        # - or raise IgnoreRequest: process_exception() methods of
        # - 抛出IgnoreRequest异常. 如果有实现process_exception()这个,那么该异常会经过该方法
        # - 如果没有实现process_exception() 那么请求就取消了, 也不会记录日志.
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        # 当下载器返回response对象给引擎的时候调用.
        # Must either;
        # - return a Response object
        # - 返回Response对象, 继续本次请求: 经过前面下载器中间 -> 引擎
        # - return a Request object
        # - 返回新的Request对象, 中断本次请求, 把请求对象 -> 引擎 -> 调度器
        # - or raise IgnoreRequest
        # - 抛出IgnoreRequest, 就忽略本次请求. 也不会经过process_exception
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
