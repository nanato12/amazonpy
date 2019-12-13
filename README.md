# amazonpy

[![PyPi](https://img.shields.io/pypi/v/amazonpy.svg)](https://pypi.org/project/amazonpy)
[![Supported python versions: 3.x](https://img.shields.io/badge/python-3.x-green.svg "Supported python versions: 3.x")](https://www.python.org/downloads/)
[![GitHub](https://img.shields.io/github/license/nanato12/amazonpy)](https://img.shields.io/github/license/nanato12/amazonpy)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg?logo=paypal&style=flat-square)](https://paypal.me/bluesquarejb/100)

Amazon scraping library
<br><br>
Amazonアソシエイトアカウントの申請が3回も落ちてムカついたので、スクレイピングライブラリを作成しました（）<br>
APIではないので、アクセスキーやトークンは必要ありません。
<br><br><br>
v1.0.2からアクセス禁止回避のため、fake_useragentを追加しました。<br>
このため、予期せぬUAを取得した場合、titleやpriceがNoneになってしまう場合があります。
<br><br>
## Installation

```bash
pip install amazonpy
```

## How to use

```python
from amazonpy import Amazon

amazon = Amazon('B07T17NSJH')

print(amazon.get_title()) # タイトルの取得
# [コーチ] COACH バッグ ショルダーバッグ 斜めがけ MAE CROSSBODY レザー F34823 アウトレット [並行輸入品]

print(amazon.get_description()) # 製品の説明を取得
#  ■品　番：F34823 SV/XR ■サイズ：約高さ27.5x幅30xマチ7cm　ショルダー約103-119cm(3cm間隔で7段階調節可)　 ■重　さ：約600g ■仕　様：開閉 ：ファスナー式　内側 ：ホックポケット1　外側 ：ファスナーポケット1 ■素　材：レザー ■カラー：Carnation 金具シルバー ■付　属：箱なし、保存袋なし ■画像のお財布はサンプルにつき、付属しておりません。

print(amazon.get_url()) # 製品のURLを取得
# https://www.amazon.co.jp/dp/B07T17NSJH/

print(amazon.get_product_image_urls()) # 製品の画像を取得
# ['https://images-na.ssl-images-amazon.com/images/I/41VXva6p65L._AC_AC_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/41eyyUG0IEL._AC_AC_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/41pavjZNA5L._AC_AC_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/31EM6kp5xrL._AC_AC_.jpg']

print(amazon.get_price()) # 販売価格の取得
# 17800

print(amazon.get_ref_price()) # 参考価格の取得、参考価格が無い場合、Noneが返る
# 68040

print(amazon.get_down_ratio()) # 参考価格に対しての値引き率を取得、参考価格が無い場合、0が返る
# 74

print(amazon.get_another_type())
# ['B07MDJ5KG3', 'B07T17NSJH', 'B07PZJYLM7', 'B07Y57C6QZ', 'B07ZYFV9ZW', 'B07PZKPS68', 'B07Y4ZGWC9']
```

## Update information

| version | information |
| :--- | :--- |
| 1.0.0 | **release.** |
| 1.0.1 | **Add 2 functions.** <br>・get_description()<br>・get_another_type() |
| 1.0.2 | **Add fake-useragent.** <br>For avoid access prohibition. |
