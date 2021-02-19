from amazonpy import Amazon

amazon = Amazon()
product = amazon.get_product_by_url(
    "https://www.amazon.co.jp/Fire-TV-Stick-Alexa%E5%AF%BE%E5%BF%9C%E9%9F%B3%E5%A3%B0%E8%AA%8D%E8%AD%98%E3%83%AA%E3%83%A2%E3%82%B3%E3%83%B3%E4%BB%98%E5%B1%9E-%E3%82%B9%E3%83%88%E3%83%AA%E3%83%BC%E3%83%9F%E3%83%B3%E3%82%B0%E3%83%A1%E3%83%87%E3%82%A3%E3%82%A2%E3%83%97%E3%83%AC%E3%83%BC%E3%83%A4%E3%83%BC/dp/B07ZZY2DFW/ref=zg_bs_electronics_home_1?_encoding=UTF8&psc=1&refRID=421Y1241ZWPNJCPGNAPS"
)

print(product.description)
