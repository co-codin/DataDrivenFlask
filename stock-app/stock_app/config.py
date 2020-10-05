class BaseConfig:
    TESTING = False

class DevConfig(BaseConfig):
    pass

class TestConfig(BaseConfig):
    TESTING = True
    DEBUG = False

class ProdConfig(BaseConfig):
    DEBUG = False

configurations = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig,
}
