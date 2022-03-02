import json
import os
import unittest
import requests_mock
from urllib.parse import urljoin

from dotenv import load_dotenv

from app import app
from product.product_seed_data_loader import load_seed_data


class TestProductRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        load_dotenv()
        load_seed_data()
        external_api = os.environ.get('EXTERNAL_API_URL')
        query_string = "?key=" + os.environ.get('EXTERNAL_API_KEY') + "&tcin="
        self.product_url = urljoin(external_api, query_string +
                                   (str(read_json("get_product_id_and_product_name_valid.json")["id"])))

    def test_product_id_and_product_name_valid(self):
        with requests_mock.mock() as m:
            m.get(self.product_url, text=json.dumps(read_json("external_api_response_product_id_valid.json")))
            r = self.app.get("/product/{}".format(str(read_json("get_product_id_and_product_name_valid.json")["id"])))
        self.assertEqual(json.loads(r.get_data()), read_json("get_product_id_and_product_name_valid.json"))

    def test_get_product_id_invalid(self):
        with requests_mock.mock() as m:
            m.get(self.product_url, text=json.dumps(read_json("external_api_response_product_id_invalid.json")))
            r = self.app.get("/product/{}".format(str(13860429)))
        self.assertEqual(json.loads(r.get_data()), read_json("get_product_id_invalid.json"))

    def test_get_request_uri_incorrect(self):
        with requests_mock.mock() as m:
            m.get(self.product_url, text=json.dumps(read_json("external_api_response_product_id_valid.json")))
            r = self.app.get("/products/{}".format(str(read_json("get_product_id_and_product_name_valid.json")["id"])))
        self.assertEqual(json.loads(r.get_data()), read_json("get_product_request_uri_invalid.json"))

    def test_put_product_id_and_product_name_valid(self):
        data = read_json("put_product_id_and_product_name_valid.json")
        expected_response = read_json("get_product_id_and_product_name_valid.json")["current_price"]["value"] = 100.00
        with requests_mock.mock() as m:
            m.get(self.product_url, text=json.dumps(read_json("external_api_response_product_id_valid.json")))
            r = self.app.put("/product/{}".format(str(read_json("get_product_id_and_product_name_valid.json")["id"])), data=json.dumps(data))
        self.assertEqual(json.loads(r.get_data())["current_price"]["value"], expected_response)

    def test_put_product_id_and_product_name_invalid(self):
        data = read_json("put_product_id_and_product_name_invalid.json")
        r = self.app.put("/product/{}".format(data["id"]), data=json.dumps(data))
        self.assertEqual(r.status_code, 400)


def read_json(name):
    f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "sample_response", str(name)))
    return json.load(f)
