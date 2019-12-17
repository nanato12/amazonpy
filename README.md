# amazonpy

[![PyPi](https://img.shields.io/pypi/v/amazonpy.svg)](https://pypi.org/project/amazonpy)
[![Supported python versions: 3.x](https://img.shields.io/badge/python-3.x-green.svg "Supported python versions: 3.x")](https://www.python.org/downloads/)
[![GitHub](https://img.shields.io/github/license/nanato12/amazonpy)](https://img.shields.io/github/license/nanato12/amazonpy)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg?logo=paypal&style=flat-square)](https://paypal.me/bluesquarejb/100)

Amazon scraping library

## Description
Amazonアソシエイトアカウントの申請が3回も落ちてムカついたので、スクレイピングライブラリを作成しました（）<br>
APIではないので、アクセスキーやトークンは必要ありません。

## Latest information
**v1.0.5 Release**  
使用したプロキシを表示するコードを削除。  
また、imgタグの`US40`で製品の画像を絞り込んでいましたが、`SR38,50`などの製品もあり、画像取得ができなかったため、`config.py`に新しく`image_parts`というリストを追加しました。  
このリストの中にある文字列とマッチしたものが製品画像に絞り込まれます。  
他にも製品画像が`[]`になった場合の絞り込み要素を見つけ次第アップデートします。  
気づき次第、プルクエストください。

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

amazon = Amazon('B07T17NSJH', proxy=True)

print(amazon.get_title()) # タイトルを取得する。
# [コーチ] COACH バッグ ショルダーバッグ 斜めがけ MAE CROSSBODY レザー F34823 アウトレット [並行輸入品]

print(amazon.get_description()) # 製品の説明を取得する。
#  ■品　番：F34823 SV/XR ■サイズ：約高さ27.5x幅30xマチ7cm　ショルダー約103-119cm(3cm間隔で7段階調節可)　 ■重　さ：約600g ■仕　様：開閉 ：ファスナー式　内側 ：ホックポケット1　外側 ：ファスナーポケット1 ■素　材：レザー ■カラー：Carnation 金具シルバー ■付　属：箱なし、保存袋なし ■画像のお財布はサンプルにつき、付属しておりません。

print(amazon.get_url()) # 製品のURLを取得する。
# https://www.amazon.co.jp/dp/B07T17NSJH/

print(amazon.get_product_image_urls()) # 製品の画像を取得する。
# ['https://images-na.ssl-images-amazon.com/images/I/41VXva6p65L._AC_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/41eyyUG0IEL._AC_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/41pavjZNA5L._AC_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/31EM6kp5xrL._AC_.jpg']

print(amazon.get_price()) # 販売価格を取得する。
# 17800

print(amazon.get_ref_price()) # 参考価格の取得、参考価格が無い場合、0が返る。
# 68040

print(amazon.get_down_ratio()) # 参考価格に対しての値引き率を取得、参考価格が無い場合、0が返る。
# 74

print(amazon.get_another_type()) # 色などの同じ製品の違うタイプの製品IDを取得する。
# ['B07MDJ5KG3', 'B07T17NSJH', 'B07PZJYLM7', 'B07Y57C6QZ', 'B07ZYFV9ZW', 'B07PZKPS68', 'B07Y4ZGWC9']
```

## Caution
v1.0.2からアクセス禁止回避のため、fake_useragentを追加しました。<br>
このため、予期せぬUAを取得した場合、titleやdescriptionがNoneになってしまう場合があります。<br>
今の所、safariのUAはNoneになっていません。<br>
<br><br>
v1.0.4からアクセス禁止回避のため、proxy設定を追加しました。<br>
デフォルトで`False`になっていますが、無料プロキシ総当たりなので、稼働しているプロキシに接続できるまで時間がかかってしまう場合があります。<br>
`False`で`time.sleep()`などを挟み、低速で使う事をオススメします。

## Update information

| version | information |
| :--- | :--- |
| 1.0.0 | **release.** |
| 1.0.1 | **Add 2 functions.** <br>・get_description()<br>・get_another_type() |
| 1.0.2 | **Add fake-useragent.** <br>For avoid access prohibition. |
| 1.0.3 | **Change default values.** <br>`price`, `ref_price` default value is `0`. |
| 1.0.4 | **Add proxy setting.** <br>For avoid access prohibition. |
| 1.0.5 | **Add config img part.** <br>Add `img_parts` in `config.py`. |

## Donation
Please donate me.<br>
- [PayPal](https://paypal.me/bluesquarejb/100)
