from retrying import retry
import requests
import re
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
    url = 'https://36kr.com/'
    html_str = parse_url(url)
    ret = re.findall("<script>window.initialState=(.*?)</script>",html_str)[0]
    print(ret)


