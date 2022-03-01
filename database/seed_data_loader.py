import logging
from pymongo import MongoClient
import urllib.parse

def load_seed_data(config):
    # Loads seed entires in the databse. See ../data/test-data.json
    logging.basicConfig(level=config.get("log_level"))
    db_config = config.get("database_server")
    db_name = db_config.get("database_name", "product")
    db_host = db_config.get("host", "localhost")
    db_port = db_config.get("port", 27017)
    db_username = urllib.parse.quote_plus(db_config.get('username'))
    db_password = urllib.parse.quote_plus(db_config.get('password'))
    try:
        productclient = MongoClient("mongodb://{0}:{1}@{2}:{3}".format(db_username,db_password,db_host,int(db_port)))
        print("[+] Database connected!")
    except Exception as e:
        print("[+] Database connection error!")
        raise e
    productdb = productclient[db_name]
    productcol = productdb["product"]
    productcol.delete_many({})
    data = [
        {"id": 13860428, "current_price": { "currency_code": "USD", "value": 13.49 }},
        {"id": 13860429, "current_price": { "currency_code": "USD", "value": 11.98 }},
        {"id": 16696650, "current_price": { "currency_code": "USD", "value": 25.00 }},
        {"id": 16696651, "current_price": { "currency_code": "USD", "value": 30.49 }},
        {"id": 16696652, "current_price": { "currency_code": "USD", "value": 35.99 }}
    ]
    result = productcol.insert_many(data)
    print("[+] Product seed data inserted in collection")


