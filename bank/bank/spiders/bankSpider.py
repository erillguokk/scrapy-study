# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BankspiderSpider(CrawlSpider):
    name = 'bankSpider'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com//political/index/politicsNewest?id=1&page=1']
    count = 0
    rules = (
        # LinkExtractor，连接提取器，提取url地址
        # callback 提取出来的url地址的response会交给callback,翻页是不需要
        # follow 当前url地址的响应是否需要重新进入rules
        # 这不是按照页码顺序提取的，是并发提取url，所以获取的数据不是顺序的
        # Rule(LinkExtractor(allow=r'/political/politics/index\?id=\d+'), callback='parse_item'),#获取详情页，具体内容都从详情页获取，也就是每一条数据
        # Rule(LinkExtractor(allow=r'political/index/politicsNewest\?id=1&page=\d+'),follow=True),#分页，不需要callback来处理
        Rule(LinkExtractor(allow=r'political/index/politicsNewest\?id=1&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # title = response.xpath("//p[@class='focus-details']/text()").extract_first()
        # print(title)
        # print("进入了parse_item")
        # print(response.url)
        li_list = response.xpath("//ul[@class = 'title-state-ul']/li")
        list = []
        for li in li_list:
            item = {}
            item["status"] = li.xpath("./span[2]/text()").extract_first()
            item["title"] = li.xpath("./span[3]/a/text()").extract_first()
            item["url"] = li.xpath("./span[3]/a/@href").extract_first()
            list.append(item)
        print(list)
        print("************")
        # with open("a.html", "a+", encoding="utf-8") as file:
        #     file.write(str(list))
            # file.write("/r/n")
            # print("********" + str(self.count))
            # self.count = self.count + 1
