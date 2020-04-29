import  requests
from lxml import etree
class Job:
    def __init__(self):
        self.start_url = "https://search.51job.com/list/030200,000000,0000,00,9,99,java,2,1.html"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}
        pass
    def parse_url(self,url):
        response =  requests.get(url,headers = self.headers)
        return response.content.decode()
    def get_data(self,html_str):
        response = etree.HTML(html_str)
        div_list = response.xpath("//div[@class = 'el']")
        for div in div_list:
            item = {}
            item["jobName"] = div.xpath("./p/span/a/text()").extract_first()
            yield item
            # 找到下一页的url地址
        next_str = response.xpath("//li[@class = 'bk']")[1].xpath("/a/@href").extract_first()
    def run(self):
        #1.start_url,构造url,获取不同页的数据
        #2.发送请求，获取响应
        html_str = self.parse_url(self.start_url)
        #3.提取数据
        print(self.get_data(html_str))
        pass

if __name__ == '__main__':
    neihan = Job()
    neihan.run()