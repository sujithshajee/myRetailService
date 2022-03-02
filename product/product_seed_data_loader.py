import yaml
import os
from pymongo import MongoClient
import urllib.parse


# Loads seed entries in the database.
def load_seed_data():
    db_name = os.environ.get('DATABASE_NAME')
    db_host = os.environ.get('DATABASE_SERVER_HOST')
    db_port = int(os.environ.get('DATABASE_SERVER_PORT'))
    db_username = os.environ.get('DATABASE_USERNAME')
    db_password = os.environ.get('DATABASE_PASSWORD')
    db_collection = os.environ.get('DATABASE_COLLECTION_NAME')
    try:
        client = MongoClient("mongodb://{0}:{1}@{2}:{3}".format(db_username, db_password, db_host, int(db_port)))
    except Exception as e:
        print("[+] Database connection error!")
        raise e
    productdb = client[db_name]
    productcol = productdb[db_collection]
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
