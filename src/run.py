"""Starta o serviço as configuraçoes são:
DevelopmentConfig = ambiente de desenvolvimento
ProductionConfig = ambiente de produção
TestingConfig = ambiente de testes
"""
from api_sw.rest.start_api import create_app
from api_sw.rest.config import (DevelopmentConfig, ProductionConfig,
                                TestingConfig)

if __name__ == '__main__':
    flask_app = create_app(TestingConfig)
    flask_app.run()
