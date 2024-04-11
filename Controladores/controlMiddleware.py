import json, re

from flask import jsonify, request
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
import requests

class ControladorMiddleware():
    def __init__(self):
        print("\t>>Creando ControladorMiddleware")
        self.dataConfig = self.__loadFileConfig()

    def before_request_func(self):
        print("\t\t>>BEFORE")
        endPoint=self.__limpiarURL(request.path)
        print('endpoint: ' + endPoint)
        excludedRoutes=["/", "/login"]
        if excludedRoutes.__contains__(request.path):
            print("ruta excluida ",request.path)
            pass
        elif verify_jwt_in_request():
            usuario = get_jwt_identity()
            print("\t>>Usuario: " + str(usuario))
            if usuario["rol"]is not None:
                tienePersmiso=self.__validarPermiso(endPoint,request.method,usuario["rol"]["tipo"])
                if not tienePersmiso:
                    return jsonify({"message": "Permission denied"}), 401
            else:
                return jsonify({"message": "El usuario no tiene un Rol asociado -> Permiso denegado"}), 403

    
    def after_request_func(self, response):
        print("\t\t>>AFTER")
        return response
    
    def __limpiarURL(self, url):
        partes = request.path.split("/")
        for laParte in partes:
            if re.search('\\d', laParte):
                url = url.replace(laParte, "?")
        return url
    
    def __validarPermiso(self, endPoint, metodo, rol):
        url=self.dataConfig["url-backend-security"]+"/permisosrol/validar/"+str(rol)
        tienePermiso=False
        headers = {"Content-Type": "application/json; charset=utf-8"}
        body={"url":endPoint,"metodo":metodo}
        response = requests.get(url, json=body, headers=headers)
        try:
            data=response.json() # Cuerpo de la respuesta
            if("_id" in data):
                tienePermiso=True
        except:
            pass
        return tienePermiso

    def __loadFileConfig(self):
        with open('config.json') as f:
            data = json.load(f)
        return data


