from flask import Flask
from flask_restx import Api
# La siguiente linea es para decirle a flask que solamente en esta parte 
# del codigo se ejecutara la instancia flask
app = Flask(__name__)


# Api:
# La clase Api se utiliza para crear una instancia de una API en una aplicación Flask, 
# lo que te permite agregar recursos (también conocidos como endpoints) 
# y definir las operaciones que pueden realizarse en esos recursos, 
# como GET, POST, PUT y DELETE. También facilita la generación de la documentación de la API automáticamente.

api = Api(
    app,
    title="Mesa de servicios",
    version="1.1",
    description="Endpoints"
)
