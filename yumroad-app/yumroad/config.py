import os

class BaseConfig:
    pass

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite://dev.db'
    SQLALCHEMY_ECHO = True

class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite://test.db'
    DEBUG = False
    TESTING = True

class ProdConfig(BaseConfig):
    DEBUG = False

configurations = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}