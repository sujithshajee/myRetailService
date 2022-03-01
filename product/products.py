import json
from flask import request, Blueprint, Response, make_response, jsonify
from flask import current_app
from product.product_manager import ProductManager

products = Blueprint("products", __name__)


@products.route("/product/<int:product_id>", methods=["GET"])
def get_product(product_id):
    print("[+] Generating response for product_id {}".format(product_id))
    product_manager = ProductManager(current_app.config)
    response = Response(content_type="application/json")
    response.set_data(json.dumps(product_manager.get_product(product_id)))
    response.status_code = 200
    return response


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


