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

""" amazonpy.main module """

from typing import Dict, Optional

import requests
from fake_useragent import UserAgent
from requests import Response

from .consts import Config
from .objects import Product, Proxy
from .scrap import Scrap
from .utils import parse


class Amazon:
    proxy: Optional[Dict[str, str]] = None

    def __init__(self, proxy: Proxy = None):
        if proxy:
            self.proxy = {proxy.protcol: proxy.url}

    def get_product_by_url(self, url: str) -> Product:
        headers: Dict[str, str] = Config.HEADERS
        headers.update({"User-Agent": UserAgent().safari})
        res: Response = requests.get(url, headers=headers, proxies=self.proxy)
        return parse(Scrap(url, res))
