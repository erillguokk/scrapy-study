import requests
# session = requests.session()
# post_url = "http://www.renren.com/"
# post_data = {}
# headers = {}
# #使用session发送请求，cookie保存在其中
# session.post(post_url,data=post_data,headers=headers)
# #使用session请求登陆之后才能访问的地址
# r = session.get("",headers=headers)
# print(r.content.decode())

#####字典推导式
v ={i:i+10 for i in range(10)}
print(v)
s = "a=b;c=d;e=f;g=y"
v = {i.split("=")[0]:i.split("=")[1] for i in s.split(";")}
print(v)
