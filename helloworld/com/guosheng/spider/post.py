import requests
import json
import sys
# query_string = sys.argv[1]#获取终端输入的参数
# print(query_string)
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

data = {"from": "AUTO",
"to": "AUTO",
"i": "人生苦短"}

post_url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
r = requests.post(post_url,data=data,headers=headers)
print(r.content.decode())
res = json.loads(r.content.decode())
print(res["from"])

##代理，让服务器以为不是同一个客户端在请求，防止我们的真实地址被泄露，防止被泄露
proxes = {"http":""}#代理ip地址
requests.get("http://www.baidu.com",proxes=proxes,headers=headers)
'''
使用代理ip：
准备ip地址池，在爬取数据的时候随机选择ip，或者使用算法，是所有ip被选择的概率均等
检查代理ip可用性：requests添加重试机制
'''

###处理session,模拟登陆
requests.session()#保持客户端与服务端之间的会话
#使用session发送请求，保存cookie到session中
#使用能够自动的携带登陆成功的时候保存在其中的cookie,进行请求


 ####定位想要的js

 #1.选中带有触发js事件的按钮，点击之后观察eventlistener,就可以定位到js
 #2.根据请求url，在search中查找具体js的位置


 #####抓包

# 勾选perserve log ,保留请求日志，跳转页面的时候勾选上，可以看到跳转前的请求，防止页面跳转找不到url地址

