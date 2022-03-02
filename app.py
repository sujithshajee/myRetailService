from flask import Flask
from config import Config
from product.product_api import products
from product.product_exceptions import ErrorResponse, InvalidRequestError, ProductNotFoundError

# Initialize flask application
app = Flask(__name__)
app.register_blueprint(products)
app.config.from_object(Config)


@app.errorhandler(ErrorResponse)
@app.errorhandler(InvalidRequestError)
@app.errorhandler(ProductNotFoundError)
def exception_handler(error):
    return error.convert_to_vnd()
