from flask import Flask
from product.products import products
import configuration.configuration_loader as configuration_loader
from utils.exceptions import ErrorResponse, InvalidRequestError, ProductNotFoundError

app = Flask(__name__)
app.register_blueprint(products)
configuration_loader.app(app)


@app.errorhandler(ErrorResponse)
@app.errorhandler(InvalidRequestError)
@app.errorhandler(ProductNotFoundError)
def exception_handler(error):
    return error.convert_to_vnd()
