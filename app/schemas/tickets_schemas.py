from flask_restx import fields

class TicketsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    # Asignar a los agentes los tickets nuevos
    def update(self):
        return self.namespace.model("Agente Create",
        {
            "agente_1": fields.String(max_length=120),
            "agente_2": fields.String( max_length=120),
            "agente_3": fields.String(max_length=120),
            "agente_4": fields.String(max_length=120),
            "agente_5": fields.String(max_length=120)
        })

    def tickets(self):
        return self.namespace.model("Tickets",{
            
            "ticket_1": fields.String(max_length=120),
            "ticket_2": fields.String( max_length=120),
            "ticket_3": fields.String(max_length=120),
            "ticket_4": fields.String(max_length=120),
            "ticket_5": fields.String(max_length=120)

        })
    