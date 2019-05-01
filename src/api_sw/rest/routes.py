"""

"""
from api_sw.rest.planets_resource import (PlanetaResource, PlanetasResource)


def register_resources_planets(api):
    """Registra os recursos envolvendo planetas para cada rota
    """
    api.add_resource(PlanetasResource, '/api/planetas/', endpoint="planetas")
    api.add_resource(PlanetaResource,
                     '/api/planeta/<int:planeta_id>',
                     endpoint="get_planet_id")
    api.add_resource(PlanetaResource,
                     '/api/planeta/delete/<int:planeta_id>',
                     endpoint="delete_planet_id")
    api.add_resource(PlanetaResource,
                     '/api/planeta/delete/<string:planeta_name>',
                     endpoint="delete_planet_name")
    api.add_resource(PlanetaResource,
                     '/api/planeta/<string:planeta_name>',
                     endpoint="get_planeta_name")
