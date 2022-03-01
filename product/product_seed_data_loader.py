import yaml
import os
from pymongo import MongoClient
import urllib.parse


# Loads seed entries in the database.
def load_seed_data(config):
    db_config = config.get("database_server")
    db_name = db_config.get("database_name", "product")
    db_host = db_config.get("host", "localhost")
    db_port = db_config.get("port", 27017)
    db_username = urllib.parse.quote_plus(db_config.get('username'))
    db_password = urllib.parse.quote_plus(db_config.get('password'))
    try:
        client = MongoClient("mongodb://{0}:{1}@{2}:{3}".format(db_username, db_password, db_host, int(db_port)))
    except Exception as e:
        print("[+] Database connection error!")
        raise e
    productdb = client[db_name]
    productcol = productdb[db_name]
    print("[+] Database connected!")
    print("[+] Clear existing data in Database collection!")
    productcol.delete_many({})
    print("[+] Begin inserting data from seed data file into Database collection!")
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "product_seed_data.yml"), "r") as stream:
        try:
            seed_data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    result = productcol.insert_many(seed_data['data'])
    print("[+] Product seed data inserted in collection")
