import  requests
import re
class Neihan:
    def __init__(self):
        self.start_url = "http://www.haoduanzi.com/wen/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36"}
        pass
    def parse_url(self,url):
        response =  requests.get(url,headers = self.headers )
        return response.content.decode()
    def get_data(self,html_str):
       return re.findall(r"<div class=\"content\"><a href.*?>(.*?)</a></div>",html_str,re.S)
    def run(self):
        #1.start_url,构造url,获取不同页的数据
        #2.发送请求，获取响应
        html_str = self.parse_url(self.start_url)
        #3.提取数据
        print(self.get_data(html_str))
        pass

if __name__ == '__main__':
    neihan = Neihan()
    neihan.run()