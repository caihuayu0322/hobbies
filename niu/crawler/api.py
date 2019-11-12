import json
from urllib import request

URL = 'http://www.kuais55.cn/cus?rows='


def fetch_data(num=1000):
    url = URL + str(num)
    with request.urlopen(url) as f:
        res = json.loads(f.read().decode('utf-8'))['data']
    data = list()
    for i in res:
        codes = i['opencode'].split(',')
        codes = (i['opentime'], list(map(lambda x: int(x), codes)))
        data.append(codes)
    return data


def get_data(num=1000):
    return fetch_data(num)
