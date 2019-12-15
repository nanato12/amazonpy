from amazonpy import Amazon

pid = 'B07T17NSJH'
amazon = Amazon(pid, proxy=True)

print(amazon.get_title())
print(amazon.get_description())
print(amazon.get_url())
print(amazon.get_product_image_urls())
print(amazon.get_price())
print(amazon.get_ref_price())
print(amazon.get_down_ratio())
print(amazon.get_another_type())
