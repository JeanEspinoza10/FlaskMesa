import requests
import os
import time
import random
class Data:
    def __init__(self):
        self.request =requests
        self.key = os.getenv("KEY")
        self.headers = {
                'Accept': 'application/json',
                'Authorization': self.key ,
                'Accept-Language': 'es',
            }
        
    def new(self):
        try :
            url = os.getenv("URL_INCIDENTES")
            params = {
                'Status': 'New',
                '$fields': 'Code'
            }

            # Time delay
            random_delay = random.uniform(3, 5)
            time.sleep(random_delay)
            response = self.request.get(url, headers=self.headers, params=params)

            if response.status_code == 200:
                data = response.json()
                return data
            else:
                return {
                    "error": f"En la consulta de tickets de la bandeja del proactivanet: {response.status_code}"
                }

        except Exception as e:
            return {
                "error": e,
            }
    
    def asignar(self,id,agente):
        try:
            url = f'{os.getenv("URL_INCIDENTES")}/{id}/escale'       
            data = {
                "PawSvcAuthGroups_id": f'{os.getenv("GRUPO_MESA")}',
                "PawSvcAuthUsers_id": f"{os.getenv(agente)}",
                "Signer_id": f"{os.getenv(agente)}"
            }

            # Time delay
            random_delay = random.uniform(4, 10)
            time.sleep(random_delay)
            response = requests.put(url, headers=self.headers, json=data)
            time.sleep(1)

            # Verificar el estado de la respuesta
            if response.status_code == 200:
                # La solicitud se realizó con éxito
                data = response.json()
                return {"resultado":"Se realizo la asginacion correctamente"}
            else:
                # Ocurrió un error al realizar la solicitud
                return {"Hubo un error": response.status_code}
        except Exception as e:
            return {"Hubo error": e}

    def id(self,incidente):
        try:
            url = os.getenv("URL_INCIDENTES")
            headers = self.headers

            params = {
                'Code': f"{incidente}"
            }

            response = requests.get(url, headers=headers, params=params)

            # Verificar el estado de la respuesta
            if response.status_code == 200:
                
                data = response.json()
                
                json = data[0]
                incide = json["Id"]
                return incide
            else:
                # Ocurrió un error al realizar la solicitud
                print('Error:', response.status_code)
                return "error"
        except Exception as e:
            return "Error en la solicitud del código de la incidencia"