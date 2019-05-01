import unittest
from flask_testing import TestCase
from api_sw.rest.start_api import create_app
from api_sw.rest.config import TestingConfig


class BaseTest(TestCase):
    def create_app(self):
        app = create_app(TestingConfig)
        return app

    def test_empty_get_planets(self):
        response = self.client.get("/api/planetas/")
        self.assertStatus(response, 204, message="DB não está vazia")

    def test_post_planeta(self):
        post_data = [{
            "nome_planeta": "Tatooine",
            "clima": "arido",
            "terreno": "deserto"
        }, {
            "nome_planeta": "Alderaan",
            "clima": "temperado",
            "terreno": "campina, montanha"
        }, {
            "nome_planeta": "Hoth",
            "clima": "congelado",
            "terreno": "tundra,cavernas de gelo,montanhas"
        }, {
            "nome_planeta": "Yavin IV",
            "clima": "temperado,tropical",
            "terreno": "selva,floresta"
        }]
        for i in range(len(post_data)):
            response = self.client.post("/api/planetas/", data=post_data[i])
            self.assertStatus(response,
                              201,
                              message="Adicionar um planeta falhou")

    def test_get_planets(self):
        response = self.client.get("/api/planetas/")
        self.assertStatus(response, 200, message="DB está vazia")

    def test_post_planet_duplicate(self):
        post_data = {
            "nome_planeta": "Tatooine",
            "clima": "arido",
            "terreno": "deserto"
        }
        response = self.client.post("/api/planetas/", data=post_data)
        self.assertStatus(response, 403, message="Checar duplicata falhou")

    def test_post_planet_requirement(self):
        post_data = {
            "nome_planeta": "Tatooine",
        }
        response = self.client.post("/api/planetas/", data=post_data)
        self.assertStatus(response, 400, message="Checar requerimento falhou")

    def test_get_planet_id(self):
        response = self.client.get("/api/planeta/2")
        self.assertStatus(response,
                          200,
                          message="retornar planeta pela id falhou")

    def test_get_planet_name(self):
        response = self.client.get("/api/planeta/Hoth")
        self.assertStatus(response,
                          200,
                          message="retornar planeta pelo nome falhou")

    def test_get_planet_ivalid_id(self):
        response = self.client.get("/api/planeta/6")
        self.assertStatus(response,
                          404,
                          message="checar id não valida para planeta falhou")

    def test_get_planet_ivalid_name(self):
        response = self.client.get("/api/planeta/something")
        self.assertStatus(response,
                          404,
                          message="checar nome não valido para planeta falhou")

    def test_delete_planet_id(self):
        response = self.client.delete("/api/planeta/4")
        self.assertStatus(response,
                          200,
                          message="deletar planeta pela id falhou")

    def test_delete_planet_name(self):
        response = self.client.delete("/api/planeta/Hoth")
        self.assertStatus(response,
                          200,
                          message="deletar planeta pelo nome falhou")

    def test_delete_planet_invalid_id(self):
        response = self.client.delete("/api/planeta/6")
        self.assertStatus(response,
                          404,
                          message="checar id não valida para planeta falhou")

    def test_delete_planet_invalid_name(self):
        response = self.client.delete("/api/planeta/soemthing")
        self.assertStatus(response,
                          404,
                          message="checar nome não valido para planeta falhou")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(BaseTest('test_empty_get_planets'))
    suite.addTest(BaseTest('test_post_planeta'))
    suite.addTest(BaseTest('test_get_planets'))
    suite.addTest(BaseTest('test_post_planet_requirement'))
    suite.addTest(BaseTest('test_post_planet_duplicate'))
    suite.addTest(BaseTest('test_get_planet_id'))
    suite.addTest(BaseTest('test_get_planet_name'))
    suite.addTest(BaseTest('test_get_planet_ivalid_id'))
    suite.addTest(BaseTest('test_get_planet_ivalid_name'))
    suite.addTest(BaseTest('test_delete_planet_name'))
    suite.addTest(BaseTest('test_delete_planet_id'))
    suite.addTest(BaseTest('test_delete_planet_invalid_id'))
    suite.addTest(BaseTest('test_delete_planet_invalid_name'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
