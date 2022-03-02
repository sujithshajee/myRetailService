import os

from pymongo import MongoClient
import urllib.parse


class DatabaseManager(object):
    def __init__(self):
        self.db_name = os.environ.get('DATABASE_NAME')
        self.host = os.environ.get('DATABASE_SERVER_HOST')
        self.port = int(os.environ.get('DATABASE_SERVER_PORT'))
        self.username = os.environ.get('DATABASE_USERNAME')
        self.password = os.environ.get('DATABASE_PASSWORD')
        self.col = os.environ.get('DATABASE_COLLECTION_NAME')
        print(os.environ.get('DATABASE_USERNAME'))
        try:
            self.client = MongoClient(username=self.username, password=self.password, host=self.host, port=self.port)
        except Exception as e:
            print("[+] Database connection error!")
            raise e
        self.db = self.client[self.db_name]
        self.col = self.db[self.col]
        print("[+] Database connected!")

    # GET the details from database based on the product ID
    def get_product_by_id(self, product_id):
        print("[+] Querying product for provided product_id!")
        return self.col.find_one({"id": product_id})

    # Update the details in database based on the product ID
    def upsert_product(self, document):
        print("[+] Upserting product for provided product_id!")
        result = self.col.update_one({"id": document["id"]}, {"$set": document}, upsert=True)
        return result
