"""
"""
from flask import Flask
from flask_restful import Api
from api_sw.rest.routes import register_resources_planets
from api_sw.persistence.mongodb_persistance import mongo, MONGO_URI_TEST


def create_app(config):
    app = Flask("Star Wars API")
    api = Api(app)
    app.config.from_object(config)
    mongo.init_app(app, MONGO_URI_TEST)
    register_resources_planets(api)
    return app
