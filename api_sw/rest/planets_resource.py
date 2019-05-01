"""Resources utilizados pelo Flask-Restful
"""

from flask_restful import Resource, fields, marshal
from api_sw.persistence.mongodb_persistance import (
    return_planet_collection, save_planet, retrieve_planet_list,
    retrieve_planet_by_name, retrieve_planet_by_id, delete_planet_by_name,
    delete_planet_by_id)
from api_sw.utils.utils_rest import (build_dict, create_deleted_message,
                                     is_duplicate)

# Template para utilizar com o marshal
reusltados = {
    "id": fields.Integer,
    "nome_planeta": fields.String,
    "clima": fields.String,
    "terreno": fields.String,
    "quantidade_aparicoes": fields.Integer
}


class PlanetasResource(Resource):
    """Resource para rotas api/planetas/
    """

    def get(self):
        lista_planetas = retrieve_planet_list()
        if return_planet_collection().count_documents({}) == 0:
            return " ", 204
        else:
            return marshal(list(lista_planetas), reusltados), 200

    def post(self):
        if is_duplicate():
            return "Planeta já cadastrado", 403
        else:
            planeta = build_dict()
            save_planet(planeta)
            return marshal(planeta, reusltados), 201


class PlanetaResource(Resource):
    """Resource para rotas api/planeta/
    """

    def get(self, planeta_name: str = None, planeta_id: int = None):
        if planeta_name:
            data = retrieve_planet_by_name(planeta_name)
            if data is None:
                return "Planeta {} não encontrado".format(planeta_name), 404
            else:
                return marshal(data, reusltados), 200

        elif planeta_id:
            data = retrieve_planet_by_id(planeta_id)
            if data is None:
                return "Planeta id: {} não encontrado".format(planeta_id), 404
            else:
                return marshal(data, reusltados), 200

    def delete(self, planeta_name: str = None, planeta_id: int = None):
        if planeta_name:
            data = delete_planet_by_name(planeta_name)
            if data is None:
                return "Planeta {} não encontrado. Operação delete não concluida".format(
                    planeta_name), 404
            else:
                deleted_message = create_deleted_message(
                    data["nome_planeta"], data["id"])
                return deleted_message, 200

        elif planeta_id:
            data = delete_planet_by_id(planeta_id)
            if data is None:
                return "Planeta id: {} não encontrado. Operação delete não concluida".format(
                    planeta_id), 404
            else:
                deleted_message = create_deleted_message(
                    data["nome_planeta"], data["id"])
                return deleted_message, 200
