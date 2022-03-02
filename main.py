import os
from app import app
from product.product_seed_data_loader import load_seed_data

if __name__ == "__main__":
    # load seed data to mongo data base if enabled in configuration file
    if os.environ.get('LOAD_SEED_DATA'):
        print("[+] Starting to load seed data in Mongo Database!")
        try:
            load_seed_data()
        except Exception as e:
            print("[+] Exception loading seed data in Mongo Database! Exception: " + e)
    app.run(host='0.0.0.0', port=8080, debug=False)
