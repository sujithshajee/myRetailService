import json
import jsonschema
from copy import deepcopy
from database.database_manager import DatabaseManager
from product.product_service_manager import ProductServiceManager
from utils.exceptions import ProductNotFoundError, InvalidRequestError, ErrorResponse
from utils.utils import load_json


class ProductManager(object):
    def __init__(self, config):
        self.config = config
        db_config = self.config.get("database_server")
        self.db_manager = DatabaseManager(db_config)
        endpoint = self.config.get('external_api').get("url")
        key = self.config.get('external_api').get("key")
        self.product_service_manager = ProductServiceManager(endpoint, key)

    def get_product(self, product_id):
        product = self.db_manager.get_product_by_id(product_id)
        if not product:
            raise ProductNotFoundError(
                'No Product matching product id {} found'.format(product_id))
        # Mongo Object _id need not be sent to client so pop from response
        product.pop('_id')
        name = self.product_service_manager.fetch_name(product_id)
        if name:
            product["name"] = name
        return product

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

    @staticmethod
    def validate_product(product):
        schema = load_json("schemas/product.json")
        loaded_product = json.loads(product)
        jsonschema.validate(loaded_product, schema)
        return loaded_product
