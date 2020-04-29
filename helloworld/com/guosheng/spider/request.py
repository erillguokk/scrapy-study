import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
kw = {'wd':'中移'}
response = requests.get("http://www.baidu.com/s",headers = headers,params=kw)
print(response.status_code)
print(response.request.url)
print(response.request.headers)
print(response.url)
print(response.headers)
print(response.content.decode())
