from bs4 import BeautifulSoup

import requests

def get_proxies():
    proxies = []
    response = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(response.text, "html.parser")

    for tr in soup.find_all('tr'):
        td_list = tr.find_all('td')
        proxy_dict = {}
        if not td_list is None and len(td_list) == 8:
            for n, key in enumerate(['IP', 'Port', 'code', 'country',
                                     'anonymity', 'google', 'https', 'refresh']):
                text = td_list[n].get_text()
                if text == 'yes': text = True
                elif text == 'no': text = False
                proxy_dict[key] = text
            proxies.append(proxy_dict)
    return proxies
