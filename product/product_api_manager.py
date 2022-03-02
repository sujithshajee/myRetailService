import json
import os

import jsonschema
from copy import deepcopy
from database.database_manager import DatabaseManager
from product.product_external_api_manager import ProductServiceManager
from product.product_exceptions import ProductNotFoundError, InvalidRequestError, ErrorResponse


class ProductManager(object):
    def __init__(self, config):
        self.db_manager = DatabaseManager()
        endpoint = os.environ.get('EXTERNAL_API_URL')
        key = os.environ.get('EXTERNAL_API_KEY')
        self.product_service_manager = ProductServiceManager(endpoint, key)

    # fetch details from database for the product ID in the incoming request
    def get_product(self, product_id):
        product = self.db_manager.get_product_by_id(product_id)
        if not product:
            raise ProductNotFoundError(
                'No Product matching product id {} found'.format(product_id))
        # MongoDB Object _id need not be sent in response
        product.pop('_id')
        name = self.product_service_manager.fetch_name(product_id)
        if name:
            product["name"] = name
        return product

    # Update the product ID details based on the received details
    def persist_product(self, product_id, product):
        try:
            loaded_product = self.validate_product(product)
        except jsonschema.ValidationError as err:
            raise InvalidRequestError(err.message)
        except Exception as e:
            # Unlikely case but in case the schema cannot be found or the schema is flawed.
            raise ErrorResponse('internal server error:' + str(e))
        if loaded_product["id"] != product_id:
            raise InvalidRequestError('provided document id "{}" did not match id in request URL "{}"'.format(
                loaded_product["id"], product_id))
        self.db_manager.upsert_product(deepcopy(loaded_product))
        name = self.product_service_manager.fetch_name(product_id)
        if name:
            loaded_product["name"] = name
        return loaded_product

    # validate if the incoming PUT request is valid per defined schema
    @staticmethod
    def validate_product(product):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"product-schema.json")
        print("[+] Loading json from path: {}".format(path))
        with open(path, "r") as f:
            data = f.read()
        loaded_product = json.loads(product)
        jsonschema.validate(loaded_product, json.loads(data))
        return loaded_product
