import json
from flask import request, Blueprint, Response
from flask import current_app
from product.product_api_manager import ProductManager

products = Blueprint("products", __name__)


# Default response for undefined routes
@products.route('/', defaults={'path': ''})
@products.route('/<path:path>')
def get_default(path):
    print("[+] Default response")
    response = Response(content_type="application/json")
    response.set_data("""{
                          "code": "Invalid_URI_Request",
                          "message": "Valid URIs are GET and PUT on /product/<int:product_id>"
                        }""")
    response.status_code = 404
    return response


# GET call implementation
@products.route("/product/<int:product_id>", methods=["GET"])
def get_product(product_id):
    print("[+] Generating response for product_id {}".format(product_id))
    product_manager = ProductManager(current_app.config)
    response = Response(content_type="application/json")
    response.set_data(json.dumps(product_manager.get_product(product_id)))
    response.status_code = 200
    return response


# PUT call implementation
@products.route("/product/<int:product_id>", methods=["PUT"])
def put_product(product_id):
    print("[+] Updating details for product_id {}".format(product_id))
    product_manager = ProductManager(current_app.config)
    response = Response(content_type="application/json")
    new_product = product_manager.persist_product(
        product_id, request.get_data())
    response.status_code = 201
    response.set_data(json.dumps(new_product))
    return response
