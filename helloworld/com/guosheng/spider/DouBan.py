import requests
import json


class DoubanSpider:
    def __init__(self):
        self.start_url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7" \
                         "&sort=recommend&page_limit=20&page_start={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36X-Requested-With: XMLHttpRequest"}
        pass

    def run(self):
        # 1.start_url
        # 发送请求
        # 提取数据并处理
        # 构造下一页url地址
        i = 0
        while True:
            num = i * 20
            i = i + 1
            htmlstr = self.parse_url(num)
            lens = self.get_content(htmlstr)
            if (len(lens) < 20):
                break
            # lens["contry"] = "ZN"
            lens.append("ZN")
            print(lens, end="\t")

    pass

    def _parse_url(self, url):
        response = requests.get(url, headers=self.headers, timeout=3)
        assert response.status_code == 200
        return response.content.decode()

    def get_content(self, json_str):
        dict_ret = json.loads(json_str)
        return dict_ret["subjects"]

    def parse_url(self, num):
        print("***")
        try:
            html_str = self._parse_url(self.start_url.format(num))
        except:
            html_str = None
        return html_str


if __name__ == '__main__':
    douban = DoubanSpider()
    douban.run()
