import requests
import json
'''
'''
class BaiduFanyi:
    def __init__(self,tran_str):
        self.tran_str = tran_str
        self.lang_dect_url = "https://fanyi.baidu.com/langdetect"
        self.tran_url = "https://fanyi.baidu.com/basetrans"
        self.headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
    def parse_url(self,url,data):#发送post请求
        response = requests.post(url,data=data,headers = self.headers,timeout = 10)
        dict = {"aa":"bb","cc":"dd"}
        print(json.dumps(dict))#将python对象转换成对象
        return json.loads(response.content.decode())
    def run(self):
        #发送语言检测请求
        lang_dec_data = {"query": self.tran_str}
        lang = self.parse_url(self.lang_dect_url,lang_dec_data)["lan"]
        #请求翻译接口
        print(lang)
        trans_data = {"query":self.tran_str,"from":"zh","to":"en"} if lang =="zh" else \
            {"query": self.tran_str, "from": "en", "to": "zh"}
        dict_response = self.parse_url(self.tran_url,trans_data)
        print(dict_response)

b = BaiduFanyi("人生苦短");
b.run()