import requests
from lxml import etree
import json
import threading
from queue import Queue


class QiubaiSpiderThread:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/text/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36"}
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()
        pass

    def get_url_list(self):
        for i in range(1, 14):
            self.url_queue.put(self.url_temp.format(i))
            # return [self.url_temp.format(i)  for i in range(1,14)]

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            print("开始请求"+url)
            response = requests.get(url, headers=self.headers, timeout=3)
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done()
            print("结束请求" + url)

    def get_content_list(self):
        print("开始解析")
        while True:
            html_str = self.html_queue.get()
            print(html_str)
            html = etree.HTML(html_str);
            # 分组
            div_list = html.xpath("//div[@class = 'col1 old-style-col1']/div")
            item_list = []
            for div in div_list:
                item = {}
                item["content"] = div.xpath(".//div[@class = 'content']/span/text()")
                item["sex"] = div.xpath("./div[@class = 'author clearfix']/div/@class")[0].split(" ")[-1].replace(
                    "Icon", "") if len(div.xpath("./div[@class = 'author clearfix']/div/@class")) > 0 else None
                item["name"] = div.xpath("./div[@class = 'author clearfix']//img/@alt")[0] if len(
                    div.xpath("./div[@class = 'author clearfix']//img/@alt")) > 0 else None
                item["headImage"] = div.xpath("./div[@class = 'author clearfix']//img/@src")[0] if len(
                    div.xpath("./div[@class = 'author clearfix']//img/@src")) > 0 else None
                item_list.append(item)
            self.content_queue.put(item_list)
            self.html_queue.task_done()
            #之所以放在最后的原因是有一种场景，html_queue只有一条数据content_queue的数据为空，如果马上调用task_done，那么主线程此时就会立马执行
            #但是还有一条数据没有添加到content_queue当中，所以数据会缺失
        print("结束解析")

    def save_list(self):
        while True:
            content_list = self.content_queue.get()
            print(json.dumps(content_list))
            self.content_queue.task_done()

    def run(self):
        thread_list = []
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        for i in range(3):
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)
        t_html = threading.Thread(target=self.get_content_list)
        thread_list.append(t_html)
        t_save = threading.Thread(target=self.save_list)
        thread_list.append(t_save)
        for t in thread_list:
            t.setDaemon(True)#把子线程设置为守护线程，当主线程结束，子线程结束
            t.start()
        for q in [self.url_queue,self.html_queue,self.content_queue]:
            q.join()#让主线程等待阻塞，直到三个队列中的数据都为空

pass
if __name__ == '__main__':
    qiubai = QiubaiSpiderThread()
    qiubai.run()# 让主线程等待队列中的元素为空的时候在继续往下执行
    # put,和task_done分别对应push和pop
