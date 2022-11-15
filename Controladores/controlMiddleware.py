import json, re

from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

import requests

class ControladorMiddleware():
    def __init__(self):
        print("\t>>Creando ControladorMiddleware")
        self.dataConfig = self.__loadFileConfig()

    def limpiarURL(self, url):
        partes = request.path.split("/")
        for laParte in partes:
            if re.search('\\d', laParte):
                url = url.replace(laParte, "?")
        return url

    def validarPermiso(self, endPoint, metodo, rol):
        print("\t\t>Validando permiso: ", endPoint, metodo, rol)
        url=self.dataConfig["url-backend-security"]+"/permisosrol/validar/"+str(rol)
        print("\t\t  >",url)
        tienePermiso=False
        headers = {"Content-Type": "application/json; charset=utf-8"}
        body={"url":endPoint, "metodo":metodo}
        response = requests.get(url,json=body, headers=headers)
        print("\t\t  >", response)
        try:
            data=response.json()
            print("\t\t  >", data)
            if("_id" in data):
                tienePermiso=True
                print("\t\t  >", tienePermiso)
        except:
            pass
        return tienePermiso

    def before_request_func(self):
        print("\t>>BEFORE request -> " + request.path)
        excludedRoutes=["/", "/login"]
        endpoint = self.limpiarURL(request.path)
        if excludedRoutes.__contains__(request.path):
            print("\t  >ruta excluida ", request.path)
            pass
        elif verify_jwt_in_request():
            usuario = get_jwt_identity()
            print("\t  >usuario: " + str(usuario))
            if usuario["email"]is not None:
                tienePermiso=self.validarPermiso(endpoint, request.method, usuario["rol"]["tipo"])
                print("\t  >tienePermiso:", tienePermiso)
                if not tienePermiso:
                    return jsonify({"message": "Permission denied"}), 401
            else:
                return jsonify({"message": "Permission denied"}), 401
    
    def after_request_func(self, response):
        print("\t>>AFTER request -> " + str(response))
        return response

    def __loadFileConfig(self):
        with open('config.json') as f:
            data = json.load(f)
        return data