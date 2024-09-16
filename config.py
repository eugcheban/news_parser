import os
from dotenv import load_dotenv

class Config:
    load_dotenv()
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_TESTING', 'postgresql://username:password@localhost/dbname')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TESTING = True
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 0

class DevelopmentConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    TESTING = True