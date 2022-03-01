from flask import Flask
from product.product_api import products
import configuration.configuration_loader as configuration_loader
from product.product_exceptions import ErrorResponse, InvalidRequestError, ProductNotFoundError

# Initialize flask application
app = Flask(__name__)
app.register_blueprint(products)
configuration_loader.app(app)


@app.errorhandler(ErrorResponse)
@app.errorhandler(InvalidRequestError)
@app.errorhandler(ProductNotFoundError)
def exception_handler(error):
    return error.convert_to_vnd()
