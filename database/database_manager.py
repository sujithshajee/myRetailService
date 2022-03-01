from pymongo import MongoClient
import urllib.parse


class DatabaseManager(object):
    def __init__(self, db_config={}):
        self.db_name = db_config.get("database_name")
        self.host = db_config.get("host")
        self.port = db_config.get("port")
        self.username = urllib.parse.quote_plus(db_config.get('username'))
        self.password = urllib.parse.quote_plus(db_config.get('password'))
        self.col = db_config.get("collection_name")
        try:
            self.client = MongoClient(username=self.username, password=self.password, host=self.host, port=self.port)
            print("[+] Database connected!")
        except Exception as e:
            print("[+] Database connection error!")
            raise e
        self.db = self.client[self.db_name]
        self.col = self.db[self.col]

    def get_product_by_id(self, product_id):
        print("[+] Querying product for provided product_id!")
        return self.col.find_one({"id": product_id})

    def upsert_product(self, document):
        print("[+] Upserting product for provided product_id!")
        result = self.col.update_one({"id": document["id"]}, {"$set": document}, upsert=True)
        return result
