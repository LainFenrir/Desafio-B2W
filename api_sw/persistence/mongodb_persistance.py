"""Coletania de metodos para a conexão com o mongodb
"""
from flask_pymongo import PyMongo
mongo = PyMongo()
MONGO_URI_TEST = "mongodb://localhost:27017/teste"


def return_planet_collection():
    return mongo.db.planetas


def save_planet(data):
    """Salva um planeta na db
    """
    planetas = mongo.db.planetas
    planetas.insert_one(data)


def retrieve_planet_list():
    """Retorna a lista de planetas cadastrados
    """
    planetas = mongo.db.planetas
    list_planetas = planetas.find()
    return list_planetas


def retrieve_planet_by_id(planeta_id):
    """Retorna um planeta com um id especifico
    """
    planetas = mongo.db.planetas
    planet = planetas.find_one({"id": planeta_id})
    return planet


def retrieve_planet_by_name(planeta_name):
    """Retorna um planeta com um nome especifico
    """
    planetas = mongo.db.planetas
    planet = planetas.find_one({"nome_planeta": planeta_name})
    return planet


def delete_planet_by_id(planeta_id):
    """Deleta um planeta com um id especifico
    """
    planetas = mongo.db.planetas
    planet = planetas.find_one_and_delete({"id": planeta_id})
    return planet


def delete_planet_by_name(planeta_name):
    """Deleta um planeta com um nome especifico
    """
    planetas = mongo.db.planetas
    planet = planetas.find_one_and_delete({"nome_planeta": planeta_name})
    return planet


def get_last():
    """Retorna o arquivo mais novo cadastrado
    """
    planetas = mongo.db.planetas
    list_planets = planetas.find().limit(1).sort([{'$natural', -1}])
    last = []
    for planeta in list_planets:
        last.append(planeta)
    return last
