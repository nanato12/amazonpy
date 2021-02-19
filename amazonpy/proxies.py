# MIT License

# Copyright (c) 2021 nanato12

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""" amazonpy.proxies module """

from typing import Any, List

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import Response

from .objects import Proxy


def get_proxies() -> List[Proxy]:
    proxies: List[Proxy] = []
    response: Response = requests.get("https://free-proxy-list.net/")
    soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")

    table: Tag = soup.find("table", id="proxylisttable")

    tr: Tag
    for tr in table.find_all("tr"):
        td: Tag
        td_list: List[Any] = [td.get_text() for td in tr.find_all("td")]
        if not td_list:
            continue
        else:
            # 5: google, 6: https
            for i in [5, 6]:
                td_list[i] = True if td_list[5] == "yes" else False
            proxies.append(Proxy(*td_list))
    return proxies
