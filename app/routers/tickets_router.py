from app import api
from flask_restx import Resource
from flask import request
from app.schemas.tickets_schemas import TicketsRequestSchema
from app.controllers.tickets_controller import TicketController


# Documentacion para el swagger

tickets_ns = api.namespace(
    name = "Tickets",
    description = "Rutas para asignar tickets",
    path = "/tickets"
)

request_schema = TicketsRequestSchema(tickets_ns)

# Creando rutas

# Ruta: Obtener todos los tickets nuevos y asginar
@tickets_ns.route("/asignar")
class Tickets(Resource):
    @tickets_ns.expect(request_schema.update())
    def put(self):
        '''Asignar tickets de la bandeja a los agentes'''
        controller = TicketController()
        return controller.asignar(request.json)
   

# Ruta: Asignar ciertos tickets a los agentes

@tickets_ns.route("/asignar/<string:agente>")
class Agentes(Resource):
    @tickets_ns.expect(request_schema.tickets())
    def put(self,agente):
        ''' Asignar ciertos tickets a los agentes'''
        data = request.json
        controller = TicketController()
        resultado = controller.asignarAgentes(agente,data)
        return resultado