import requests
from product.product_exceptions import ProductNotFoundError


# Implementation to query external api and fetch the name of the product if product id is valid.
class ProductServiceManager(object):
    def __init__(self, endpoint, key):
        self.endpoint = endpoint
        self.key = key

    def fetch_name(self, product_id):
        params = {
            'key': str(self.key),
            'tcin': str(product_id)
        }
        result = requests.get(self.endpoint, params=params)
        if result.status_code != requests.codes["ok"]:
            raise ProductNotFoundError(
                "External api failed to fetch name for ProductID {}".format(product_id))
        data = result.json()
        try:
            name = data["data"]["product"]["item"]["product_description"]["title"]
        except KeyError:
            name = None
        return name
