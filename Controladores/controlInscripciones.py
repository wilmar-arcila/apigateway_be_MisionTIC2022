import json

from flask import jsonify
import requests

class ControladorInscripciones():
    def __init__(self):
        print("\t>>Creando ControladorInscripciones")
        self.dataConfig = self.__loadFileConfig()

    def index(self):
        print("\t>>Inscripciones-Index")
        headers = {"Content-Type": "application/json; charset=utf-8"}
        url=self.dataConfig["url-backend-academic"]+'/inscripciones'
        response = requests.get(url, headers=headers)
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return {"msg": "Error en el servidor del sistema Académico"}, 500
    
    def __loadFileConfig(self):
        with open('config.json') as f:
            data = json.load(f)
        return data


