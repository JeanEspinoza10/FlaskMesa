import os
from flask import jsonify
from app.helpers.data  import Data
import time
import requests

class TicketController:
    def __init__(self):
        self.key = os.getenv("KEY")
        self.data = Data()
    def asignar(self,data):
        try:
            time_asignacion = time.time()
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_asignacion))
            agentes_disponibles = []
            for key, value in data.items():
                agentes_disponibles.append(value)

            
            ticketsnew = self.data.new()
            if ticketsnew:
                asignaciones = {}

                for i, ticket in enumerate(ticketsnew):
                    agente = agentes_disponibles[i % len(agentes_disponibles)]
                    asignaciones[ticket['Id']] = agente
                
                for key, values in asignaciones.items():
                    result = self.data.asignar(key,values)

                return  {
                    "Respuesta":f"{formatted_time}: {result['resultado']}",
                    "codigo": 200
                }
            else:
                return{
                    "Respuesta": "No hay tickets en la bandeja",
                    "Codigo":200
                }
        except Exception as e:
            return {
                "error": f"Error en la asignación de tickets {e}",
                "Codigo":400
            },400

    def asignarAgentes(self,agente,totalTickets):
        try:
            
            grupo_id = os.getenv("GRUPO_MESA")
            user_asignado = os.getenv(agente.upper())
            
            url_base = os.getenv("URL_INCIDENTES")

           
            for key,values in totalTickets.items():

                ticket_id = self.data.id(values)

                respuesta = {}
                url = f'{url_base}/{ticket_id}/escale'
                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': self.key
                }
            
                data = {
                    "PawSvcAuthGroups_id": f"{grupo_id}",
                    "PawSvcAuthUsers_id": f"{user_asignado}",
                    "Signer_id": f"{user_asignado}"
                }

                
                response = requests.put(url, headers=headers, json=data)
                
                # Verificar el estado de la respuesta
                if response.status_code == 200:
                    # La solicitud se realizó con éxito
                    data = response.json()
                    respuesta[values] = "Correctamente asignado"
                    
                else:
                    # Ocurrió un error al realizar la solicitud
                    respuesta[values] = f"Error en la asignación: Código de respuesta del Servidor de PROACTIVANET:{response.status_code}"

            return {
                "Respuesta": respuesta,
                "Código":200
            },200
        except Exception as e:
            return {
                "Respuesta": f"Error en la solicitud de asignar: {e}",
                "Código": 400
            },400
        