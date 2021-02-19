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

""" amazonpy.scrap module """

import re
from typing import List, Optional

from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import Response

from .consts import ClassName, Config


class Scrap:
    def __init__(self, url: str, res: Response) -> None:
        self.url = url
        self.soup = BeautifulSoup(res.text, "html.parser")

    @property
    def id(self) -> Optional[str]:
        result = re.search(r"/(?<=\/dp\/).*?(?=\/)/", self.url)
        if result:
            return result.group()[1:-1]
        return None

    @property
    def title(self) -> Optional[str]:
        element: Tag = self.soup.find("span", id="productTitle")
        if element:
            return element.get_text().strip()
        return None

    @property
    def description(self) -> Optional[str]:
        element: Tag = self.soup.find("div", id="feature-bullets")
        if element:
            return element.get_text().strip()
        return None

    @property
    def images_urls(self) -> List[str]:
        url_list: List[str] = []
        element: Tag
        for element in self.soup.find_all("img"):
            image_url: str = element.get("src")
            for part in Config.IMAGE_PARTS:
                if part in image_url:
                    image_id = image_url.split("/")[-1].split(".")[0]
                    url_list.append(Config.IMAGE_URL.format(image_id))
        return url_list

    @property
    def price(self) -> Optional[int]:
        for price_class in ClassName.PRICE_CLASSES:
            element: Tag = self.soup.find("span", class_=price_class)
            if element:
                return int(element.get_text().replace("￥", "").replace(",", ""))
        return None

    @property
    def ref_price(self) -> Optional[int]:
        element: Tag = self.soup.find("span", class_="priceBlockStrikePriceString")
        if element:
            return int(element.get_text().replace("￥", "").replace(",", ""))
        return None

    @property
    def down_ratio(self) -> Optional[int]:
        element: Tag = self.soup.find("td", class_="priceBlockSavingsString")
        if element:
            pattern = r"￥(.*)\((.*)\%\)"
            string = element.get_text().replace(" ", "").replace("\n", "")
            result = re.match(pattern, string)
            if result:
                return int(result.group(2))
        return None

    @property
    def another_type(self) -> Optional[List[str]]:
        element: Tag = self.soup.find("ul", class_="imageSwatches")
        if element:
            return [li.get("data-defaultasin") for li in element.find_all("li")]
        return None
