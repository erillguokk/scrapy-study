# -*- coding: utf-8 -*-
import scrapy
import logging


# logger = logging.getLogger(__name__)
class CmicSpider(scrapy.Spider):
    name = 'cmic'
    allowed_domains = ['search.51job.com']  # 允许爬取的范围
    start_urls = ['https://search.51job.com/list/030200,000000,0000,00,9,99,java,2,1.html']  # 最开始的url地址

    # logging.basicConfig(level= Warning)

    def parse(self, response):
        # 处理start_url的响应
        div_list = response.xpath("//div[@class = 'el']")
        for div in div_list:
            item = {}
            item["jobName"] = div.xpath("./p/span/a/text()").extract_first()
            yield item
            # 找到下一页的url地址
        next_List = response.xpath("//li[@class = 'bk']")
        a = next_List[1].xpath(".//a");
        if len(a) >=1 :
            next_url = next_List[1].xpath(".//a/@href").extract_first()
            yield scrapy.Request(next_url, callback=self.parse1,meta={"item":item},dont_filter= False)#过滤相同的请求
        pass
    def parse1(self,response):
        response.meta["item"]#能获取到parse传递的参数
        pass