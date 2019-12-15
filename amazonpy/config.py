class Config:
    host = 'https://www.amazon.co.jp/'
    p_url = host + 'dp/{}/'

    price_classes = ['priceBlockBuyingPriceString', 'priceBlockSalePriceString']

    temp_dir = 'temp/{}/'

    header = {
        "Referer": "https://www.amazon.co.jp/",
        "User-Agent": ""
    }
