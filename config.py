import os


class Config:
    DEBUG = False
    DATABASE_SERVER_HOST = os.environ.get('DATABASE_SERVER_HOST')
    DATABASE_SERVER_PORT = os.environ.get('DATABASE_SERVER_PORT')
    DATABASE_NAME = os.environ.get('DATABASE_NAME')
    DATABASE_COLLECTION_NAME = os.environ.get('DATABASE_COLLECTION_NAME')
    DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME')
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
    EXTERNAL_API_URL = os.environ.get('EXTERNAL_API_URL')
    EXTERNAL_API_KEY = os.environ.get('EXTERNAL_API_KEY')
    LOAD_SEED_DATA = os.environ.get('LOAD_SEED_DATA')
