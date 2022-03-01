from app import app
from product.product_seed_data_loader import load_seed_data
from configuration.configuration_loader import app_config

if __name__ == "__main__":
    # load seed data to mongo data base if enabled in configuration file
    config = {}
    app_config(config)
    if config.get("load_seed_data"):
        print("[+] Starting to load seed data in Mongo Database!")
        try:
            load_seed_data(config)
        except Exception as e:
            print("[+] Exception loading seed data in Mongo Database! Exception: " + e)
    app.run(host='0.0.0.0', port=8080, debug=False)
