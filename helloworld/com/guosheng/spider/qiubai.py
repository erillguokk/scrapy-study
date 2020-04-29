import  requests
from lxml import  etree
import  json
class QiubaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/text/page/{}/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36"}
        pass
    def get_url_list(self):
        return [self.url_temp.format(i)  for i in range(1,14)]
    def parse_url(self,url):
        response = requests.get(url,headers = self.headers,timeout = 3)
        return response.content.decode()
    def get_content_list(self,html_str):
        html = etree.HTML(html_str);
        #分组
        div_list = html.xpath("//div[@class = 'col1 old-style-col1']/div")
        item_list = []
        for div in div_list:
            item = {}
            item["content"] = div.xpath(".//div[@class = 'content']/span/text()")
            item["sex"] = div.xpath("./div[@class = 'author clearfix']/div/@class")[0].split(" ")[-1].replace("Icon","") if len(div.xpath("./div[@class = 'author clearfix']/div/@class")) >0 else None
            item["name"] = div.xpath("./div[@class = 'author clearfix']//img/@alt")[0] if len(div.xpath("./div[@class = 'author clearfix']//img/@alt")) >0 else None
            item["headImage"] = div.xpath("./div[@class = 'author clearfix']//img/@src")[0] if len(div.xpath("./div[@class = 'author clearfix']//img/@src")) >0 else None
            item_list.append(item)
        return item_list
    def run(self):
        #1.url_list
        url_list = self.get_url_list()
        #2.遍历发送请求，获取数据
        for url in url_list:
            print("开始了，url:{}".format(url))
            html_str = self.parse_url(url)
            # 3.提取数据
            cont_list = self.get_content_list(html_str)
            # 4.存储数据
            print(cont_list)
            print("结束了")



        pass
if __name__ == '__main__':
    qiubai = QiubaiSpider();
    qiubai.run()
