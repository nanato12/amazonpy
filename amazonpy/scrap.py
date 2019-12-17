from .config import Config
from .proxies import *
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

import re
import requests

class Scrap(Config):

    title = None
    desc = None
    price = 0
    ref_price = 0
    another_type = []
    down_ratio = 0

    def __init__(self, product_id, proxy=False):
        self.product_id = product_id
        self.product_url = self.p_url.format(product_id)
        self.header['User-Agent'] = UserAgent().safari
        if proxy:
            for proxy in get_proxies():
                if proxy.get('https'):
                    ip = proxy.get('IP')
                    port = proxy.get('Port')
                    try:
                        self.html = requests.get(url=self.product_url, headers=self.header,
                                                 proxies={"https": f"https://{ip}:{port}"}).text
                        break
                    except:
                        pass
        else:
            self.html = requests.get(url=self.product_url, headers=self.header).text
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.__get_title()
        self.__get_description()
        self.__get_images_urls()
        self.__get_price()
        self.__get_ref_price()
        self.__get_down_ratio()
        self.__get_another_type()

    def __get_title(self):
        element = self.soup.find('span', id='productTitle')
        if element:
            self.title = element.get_text().replace('\n', '').replace('  ', '')

    def __get_description(self):
        element = self.soup.find('div', id='feature-bullets')
        if element:
            self.desc = element.get_text().replace('\n', '').replace('  ', '').replace('\t', '')

    def __get_images_urls(self):
        url_list = []
        for element in self.soup.find_all("img"):
            image_url = element.get('src')
            for part in self.image_parts:
                if part in image_url:
                    image_id = image_url.split('/')[-1].split('.')[0]
                    url_list.append(self.image_url.format(image_id))
        self.img_list = url_list

    def __get_price(self):
        for price_class in self.price_classes:
            element = self.soup.find('span', class_=price_class)
            if element:
                self.price = int(element.get_text().replace('￥', '').replace(',', ''))

    def __get_ref_price(self):
        element = self.soup.find('span', class_='priceBlockStrikePriceString')
        if element:
            self.ref_price = int(element.get_text().replace('￥', '').replace(',', ''))

    def __get_down_ratio(self):
        element = self.soup.find('td', class_='priceBlockSavingsString')
        if element:
            pattern = r'￥(.*)\((.*)\%\)'
            string = element.get_text().replace(' ', '').replace('\n', '')
            self.down_ratio = int(re.match(pattern, string).group(2))

    def __get_another_type(self):
        element = self.soup.find('ul', class_='imageSwatches')
        if element:
            self.another_type = [li.get('data-defaultasin') for li in element.find_all('li')]
