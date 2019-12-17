class Config:
    host = 'https://www.amazon.co.jp/'
    p_url = host + 'dp/{}/'

    price_classes = ['priceBlockBuyingPriceString', 'priceBlockSalePriceString']

    temp_dir = 'temp/{}/'

    header = {
        "Referer": "https://www.amazon.co.jp/",
        "User-Agent": ""
    }

    image_parts = ['US40', 'SR38']

    image_url = 'https://images-na.ssl-images-amazon.com/images/I/{}._AC_.jpg'
