# amazonpy

[![PyPi](https://img.shields.io/pypi/v/amazonpy.svg)](https://pypi.org/project/amazonpy)
[![Supported python versions: 3.x](https://img.shields.io/badge/python-3.x-green.svg "Supported python versions: 3.x")](https://www.python.org/downloads/)
[![GitHub](https://img.shields.io/github/license/nanato12/amazonpy)](https://img.shields.io/github/license/nanato12/amazonpy)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg?logo=paypal&style=flat-square)](https://paypal.me/bluesquarejb/100)

Amazon scraping library

## Description
Amazon（JP）の商品情報を取得するためのスクレイピングライブラリ

## Installation
```bash
pip install amazonpy
```

## Upgrade
```bash
pip install --upgrade amazonpy
```

## How to use
```python
from amazonpy import Amazon

amazon = Amazon()

# URLから製品情報を取得する。
product = amazon.get_product_by_url("https://www.amazon.co.jp/dp/B07T17NSJH/")

print(product.id) # 商品IDを取得する。
# B07T17NSJH

print(product.title) # タイトルを取得する。
# [コーチ] COACH バッグ ショルダーバッグ 斜めがけ MAE CROSSBODY レザー F34823 アウトレット [並行輸入品]

print(product.description) # 説明を取得する。
# ■品　番：34823 IMTAU ■サイズ：約高さ23x幅25xマチ5cm　ショルダー約103-119cm（取り外し不可）　 ■重　さ：約400g ■仕　様：開閉 ：ファスナー式　内側 ：ポケット1　外側 ：ポケット1 ■素　材：レザー ■カラー：Taupe 金具ゴールド ■付　属：箱なし、保存袋なし ■バッグ内の商品はサンプル品につき、付属しておりません。

print(product.price) # 販売価格を取得する。
# 17570

print(product.another_type) # 色などの同じ製品の違うタイプの製品IDを取得する。
['B08TW5VZX3', 'B07PZJYLM7', 'B07ZYFV9ZW', 'B0854LBQG2']
```
## Donation
Please donate me.<br>
- [PayPal](https://paypal.me/bluesquarejb/100)
