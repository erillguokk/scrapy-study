# -*- coding: utf-8 -*-
import scrapy
from  copy import  deepcopy
import re

class SuningspiderSpider(scrapy.Spider):
    name = 'suningSpider'
    allowed_domains = ['www.suning.com','list.suning.com','product.suning.com','book.suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        # print("进入了parse")
        div_list = response.xpath("//div[@class = 'left-menu-container']/div[@class='menu-list']/div")
        for div in div_list:
            item = {}
            item["classification"] = div.xpath(".//h3/a/text()").extract_first()
            item["class_url"] = div.xpath(".//h3/a/@href").extract_first()
            if item["class_url"] is not None:
                # print(item["class_url"])
                url = item["class_url"]
                yield scrapy.Request(url, callback=self.parse_book_list, meta={"item": item})
    def parse_book_list(self, response):
        # print("进入了parse_book_list")
        item = response.meta["item"]
        li_list = response.xpath("//ul[@class='clearfix']/li")
        page_count = int(re.findall("param.currentPage = \"(.*?)\";", response.body.decode())[0])
        page_num = int(re.findall("param.pageNumbers = \"(.*?)\";", response.body.decode())[0])
        item["currentPage"] = page_count
        for li in li_list:
            item["bookContent"] = li.xpath(".//div[@class='img-block']/a/img/@alt").extract_first()
            item["book_imag"] = li.xpath(".//div[@class='img-block']/a/img/@src2").extract_first()
            item["book_url"] = li.xpath(".//div[@class='img-block']/a/@href").extract_first()
            # print(item["book_url"])
            if item["book_url"] is not None:
                yield scrapy.Request(url="https:"+item["book_url"], callback=self.parse_book_detail, meta={"item": deepcopy(item)});
                #深拷贝，避免产生数据覆盖
        class_urls = item["class_url"].split("0.html")
        if(len(class_urls)>=1):
            if page_count < page_num:
                next_url = class_urls[0]+"{}".format(page_count + 1)+".html"
                print(item["classification"]+"第{}页--next_url:{}".format(page_count,next_url))
                yield scrapy.Request(next_url, callback=self.parse_book_list, meta={"item": item})
    def parse_book_detail(self, response):
        item = response.meta["item"]
        item["author"] = "".join(response.xpath("//ul[contains(@class,'bk-publish clearfix')]/li[1]/text()").extract_first().split())
        print(item)
