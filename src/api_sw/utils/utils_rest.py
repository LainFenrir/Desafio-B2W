""" Coletania de funções utilizadas na api para a comunicação rest
"""

from flask_restful import reqparse
from api_sw.utils.swapi_access import SwapiConnection
from api_sw.persistence.mongodb_persistance import (get_last,
                                                    retrieve_planet_by_name,
                                                    return_planet_collection)


def post_parse():
    """Faz o parse no metodo post
    """
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument("nome_planeta",
                        type=str,
                        required=True,
                        help="campo obrigatorio")
    parser.add_argument("clima",
                        type=str,
                        required=True,
                        help="campo obrigatorio")
    parser.add_argument("terreno",
                        type=str,
                        required=True,
                        help="campo obrigatorio")
    return parser.parse_args()


def build_dict():
    """ Cria um dicionario adicionando um id e as apariçoes em filmes.
    """
    parse = post_parse()
    planeta_id = get_next_id()
    apparitions = add_apparitions(parse['nome_planeta'])

    planeta = {
        "id": planeta_id,
        "nome_planeta": parse["nome_planeta"],
        "clima": parse["clima"],
        "terreno": parse["terreno"],
        "quantidade_aparicoes": apparitions
    }
    return planeta


def add_apparitions(planeta_name):
    """Faz a conexão entre a api e o SWAPI retornando o numero de apariçoes
    """
    sc = SwapiConnection()
    count = sc.count_apparitions(planeta_name)
    return count


def create_deleted_message(planeta_name, planeta_id):
    """Cria um dicionario que será enviado quando um planeta é deletado
    """
    deleted_message = {
        "id": planeta_id,
        "nome_planeta": planeta_name,
        "status": "deleted"
    }
    return deleted_message


def get_next_id():
    """Cria um id simples para ser facilmente utilizado na api.
        É baseado no ultimo id do arquivo mais novo no mongodb.
    """
    if return_planet_collection().count_documents({}) == 0:
        id_planeta = 1
    else:
        last = get_last()
        id_planeta = last[0]["id"] + 1
    return id_planeta


def is_duplicate():
    """Checa se o planeta já existe no banco para evitar duplicatas
    """
    parse = post_parse()
    planeta = retrieve_planet_by_name(parse["nome_planeta"])
    if planeta is None:
        return False
    else:
        return True
