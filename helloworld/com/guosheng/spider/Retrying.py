''''
重试模块
'''
from retrying import retry
import requests

@retry(stop_max_attempt_number=3)
def _parse_url(url):
    response = requests.get(url, timeout=3)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url):
    print("***")
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(parse_url(url))
