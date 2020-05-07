# -*- coding: utf-8 -*-
import scrapy
from sunProject.items import  SunprojectItem


class SunspiderSpider(scrapy.Spider):
    name = 'sunSpider'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']

    def parse(self, response):
       # self.settings.get("","")#获取配置文件settings中的配置
        li_list = response.xpath("//ul[@class = 'title-state-ul']/li")
        for li in li_list:
            item = SunprojectItem()
            item["status"] = li.xpath("./span[2]/text()").extract_first()
            item["title"] = li.xpath("./span[3]/a/text()").extract_first()
            item["url"] = li.xpath("./span[3]/a/@href").extract_first()
            yield item
        next_url = "http://wz.sun0769.com/"+response.xpath("//a[contains(@class,'arrow-page prov_rota')]/@href").extract_first()
        print("********"+next_url)
        yield scrapy.Request(next_url,callback= self.parse)
        pass
