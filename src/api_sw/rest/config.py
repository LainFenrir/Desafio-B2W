"""
"""
from api_sw.persistence.mongodb_persistance import MONGO_URI_TEST


class Config():
    DEBUG = False
    TESTING = False
    MONGO_URI = MONGO_URI_TEST


class ProductionConfig(Config):
    FLASK_ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'
    ENV = 'development'


class TestingConfig(Config):
    TESTING = True
    ENV = 'test'


def return_config(config_name: str):
    """ Retorna uma das configurações
    """
    configs = {
        "production": ProductionConfig(),
        "development": DevelopmentConfig(),
        "test": TestingConfig()
    }
    return configs[config_name]
