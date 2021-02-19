from amazonpy import Amazon

amazon = Amazon()
product = amazon.get_product_by_url("https://www.amazon.co.jp/dp/B07T17NSJH/")

print(product.id)
print(product.title)
print(product.description)
print(product.price)
print(product.another_type)
