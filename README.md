# Desafio B2W

## Tecnologias usadas

- [Flask-PyMongo — Flask-PyMongo 2.2.0.post3 documentation](https://flask-pymongo.readthedocs.io/en/latest/)
- [Welcome to Flask — Flask 1.0.2 documentation](http://flask.pocoo.org/docs/1.0/)
- [Flask-RESTful — Flask-RESTful 0.3.7 documentation](https://flask-restful.readthedocs.io/en/latest/)
- [insomnia](https://insomnia.rest)
- [Flask-Testing — Flask-Testing 0.3 documentation](https://pythonhosted.org/Flask-Testing/)
- MongoDB
- Python
- unittest

## Como usar

### Configurações
Para executar a api é só rodar o arquivo `run.py`. Ele está setado para o ambiente de testes. Para mudar o ambiente basta mudar 
```
 flask_app = create_app(TestingConfig)
```
por uma dessas opções:
DevelopmentConfig, ProductionConfig,TestingConfig


### Rodando testes
Para rodar os testes basta executar o arquivo `base_test.py`, todos os testes estão nele.
> Ao termino dos testes dois arquivos são deixados na coleção para ter certeza de que os testes foram realmente executados.

## Rotas
As rotas mostradas abaixo usam o servidor local default do Flask

### Rotas /api/planetas/
```
GET http://127.0.0.1:5000/api/planetas/
```
```
POST http://127.0.0.1:5000/api/planetas/
```

### Rotas /api/planeta/
```
GET http://127.0.0.1:5000/api/planeta/id
```
```
GET http://127.0.0.1:5000/api/planeta/nome
```
### Rotas /api/planetas/delete/
As rotas para deletar um planeta são diferentes para evitar acidentes
```
DELETE http://127.0.0.1:5000/api/planeta/delete/nome
```
```
DELETE http://127.0.0.1:5000/api/planeta/delete/id
```
