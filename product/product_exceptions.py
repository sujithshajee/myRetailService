from flask import Response
import json


class ErrorResponse(Exception):
    def __init__(self, message, error_code="Internal_Server_Error", status_code=500):
        super(ErrorResponse, self).__init__(message)
        self.error_code = error_code
        self.status_code = status_code
        self.message = message

    def convert_to_vnd(self):
        body = json.dumps({
            "code": self.error_code,
            "message": self.message
        })
        response = Response()
        response.status_code = self.status_code
        response.set_data(body)
        return response


class ProductNotFoundError(ErrorResponse):
    def __init__(self, message):
        super(ProductNotFoundError, self).__init__(message, "Product_Not_Found", 404)


class InvalidRequestError(ErrorResponse):
    def __init__(self, message):
        super(InvalidRequestError, self).__init__(message, "Bad_Request", 400)

