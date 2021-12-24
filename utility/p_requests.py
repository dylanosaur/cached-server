import requests


url = 'http://localhost:4999/forum'

def simple_unkeyed_query_params(page='cat&utm_content=1;page=dog'):
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Origin': 'Bullshido origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'close',
        'X-Forwarded-Host': 'extra-bullshido',
        'Content-Type': 'canary'
    }

    # url = 'http://localhost:4999/forum'
    params = {'page': page}
    res = requests.get(url, params=params, headers=headers)
    print(res.content)
    print(res.headers)

def check_header_for_processing(header='host'):
    url = 'http://localhost:4999/forum'
    headers = {
        'Host': 'somewhere.safe.com'
    }
    res = requests.get(url, headers=headers)
    print(res.headers)
    headers = {
        'Host': 'somewhere.safe.com:1337'
    }
    res = requests.get(url, headers=headers)
    print(res.headers)


import time
if __name__ == '__main__':
    simple_unkeyed_query_params(page='cat&utm_content=1;page=dog')
    time.sleep(1)
    simple_unkeyed_query_params(page='cat')

    # check_header_for_processing()