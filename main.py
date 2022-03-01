from app import app
from database.seed_data_loader import load_seed_data
from configuration.configuration_loader import app_config

if __name__ == "__main__":
    config = {}
    app_config(config)
    if config.get("load_seed_data"):
        print("[+] Starting to load seed data in Mongo Database!")
        try:
            load_seed_data(config)
        except Exception as e:
            print("[+] Exception loading seed data in Mongo Database! Exception: " + e)
    app.run(port=8080)
