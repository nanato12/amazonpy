class Config:
    host = 'https://www.amazon.co.jp/'
    p_url = host + 'dp/{}/'

    price_classes = ['priceBlockBuyingPriceString', 'priceBlockSalePriceString']

    temp_dir = 'temp/{}/'

    header = {
        "Referer": "https://www.amazon.co.jp/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
