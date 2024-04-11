import json

from flask import jsonify
import requests

class ControladorInscripciones():
    def __init__(self):
        print("\t>>Creando ControladorInscripciones")
        self.dataConfig = self.__loadFileConfig()

    def index(self):
        print("\t>>Inscripciones-Index")
        _headers = {"Content-Type": "application/json; charset=utf-8"}
        url=self.dataConfig["url-backend-academic"]+'/inscripciones'
        response = requests.get(url, headers=_headers)
        print(response)
        if response.status_code == 200:
            json = response.json()
            print(json)
            return json
        else:
            return {"msg": "Error en el microservicio Académico"}, 500

    def getInscripcion(self, id):
        print("\t>>Inscripciones-Get: " + id)
        _headers = {"Content-Type": "application/json; charset=utf-8"}
        url=self.dataConfig["url-backend-academic"]+'/inscripciones/'+id
        response = requests.get(url, headers=_headers)
        print(response)
        if response.status_code == 200:
            json = response.json()
            print(json)
            return json
        else:
            return {"msg": "Error en el microservicio Académico"}, 500

    def modificarNota(self, id, data):
        print("\t>>Inscripciones-Patch-Nota: " + id)
        _headers = {"Content-Type": "application/json; charset=utf-8"}
        url=self.dataConfig["url-backend-academic"]+'/inscripciones/'+id
        response = requests.patch(url, headers=_headers, json=data)
        print(response)
        if response.status_code == 200:
            json = response.json()
            print(json)
            return json
        else:
            return {"msg": "Error en el microservicio Académico"}, 500
    
    def __loadFileConfig(self):
        with open('config.json') as f:
            data = json.load(f)
        return data


