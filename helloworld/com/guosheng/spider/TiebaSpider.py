import requests
import json
from lxml import etree


class TiebaSpider():
    def __init__(self, tiebaName):
        self.tiebaName = tiebaName
        self.start_url = "https://tieba.baidu.com/f?kw=" + tiebaName + "&pn=0&"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Mobile Safari/537.36"}
        pass

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode();

    def get_context_list(self, html_str):
        html = etree.HTML(html_str)
        liList = html.xpath("//li[@class='tl_shadow tl_shadow_new ']")
        contentList = []
        for li in liList:
            item = {}
            item["title"] = li.xpath("./a/div[@class='ti_title']/span/text()")[0] if len(
                li.xpath("./a/div[@class='ti_title']/span/text()")) > 0 else None
            item["href"] = li.xpath("./a/@href")[0] if len(li.xpath("./a/@href")) > 0 else None
           # item["img_list"] = self.get_img_list(item["href"])
            # 获取下一页的url地址
            contentList.append(item)
            #下一页的地址是js渲染，暂时无法获取 TODO
        next_url = html.xpath("//a[@class='j_pager_next bottom_pager_btn pager_next active']/@href")[0] if len(#此处的下一页标签是js动态生成的，无法获取到
            html.xpath("//a[@class='j_pager_next bottom_pager_btn pager_next active']/@href")) > 0 else None
        return contentList, next_url
    def get_img_list(self, detail_href):
        pass

    def save_html(self, content_list,tiebaName):
        for content in content_list:
            print(content,end="\n")
        # file_path = "C:\BaiduNetdiskDownload\code14\{}.html".format(self.tiebaName)
        # with open(file_path, "w", encoding="utf-8") as f:
        #     for content in content_list:
        #         f.write(json.dumps(content))
        #         f.write("\n")
    def run(self):
        next_url = self.start_url
        while next_url is not None:
            html_str = self.parse_url(next_url)
            content_list, next_url = self.get_context_list(html_str)
            self.save_html(content_list, self.tiebaName)
        pass


if __name__ == '__main__':
    tieba = TiebaSpider("李毅")
    tieba.run()
