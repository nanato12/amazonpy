from .scrap import Scrap

class Amazon:
    """
    initialize Amazon(product_id)
    """
    def __init__(self, product_id):
        self.sc = Scrap(product_id)

    def get_title(self):
        """
        This function gets the product title.

        If it could not be obtained, return None

        return
            string or None
        """
        return self.sc.title

    def get_description(self):
        """
        This function gets the product description.

        If it could not be obtained, return None

        return
            string or None
        """
        return self.sc.desc

    def get_url(self):
        """
        This function gets the product url.

        return
            string
        """
        return self.sc.product_url

    def get_product_image_urls(self):
        """
        This function gets the product image urls.

        return
            list
        """
        return self.sc.img_list

    def get_price(self):
        """
        This function gets the product buying price.

        return
            int
        """
        return self.sc.price

    def get_ref_price(self):
        """
        This function gets the product reference price.

        If it could not be obtained, return None

        return
            int or None
        """
        return self.sc.ref_price

    def get_down_ratio(self):
        """
        This function gets the product discount ratio to reference price.

        If there is no reference price, return 0

        return
            int
        """
        return self.sc.down_ratio

    def get_another_type(self):
        """
        This function gets the product another type product ids.

        return
            list
        """
        return self.sc.another_type
