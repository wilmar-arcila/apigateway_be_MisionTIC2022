import json
from datetime import timedelta

from flask import jsonify
from flask_jwt_extended import create_access_token, verify_jwt_in_request
import requests

class ControladorSeguridad():
    def __init__(self):
        print("\t>>Creando ControladorSeguridad")
        self.dataConfig = self.__loadFileConfig()

    def login(self, data):
        print("\t>>Login: " + str(data))
        # lógica de verificación de Usuario
        # 1. Consumir el servicio de validación de usuarios de ms_seguridad
        headers = {"Content-Type": "application/json; charset=utf-8"}
        url=self.dataConfig["url-backend-security"]+'/usuarios/validar'
        response = requests.post(url, json=data, headers=headers)
        print(response)
        if response.status_code == 200:
            user = response.json()
            print(user)
            expires = timedelta(seconds=60 * 60*24)
            access_token = create_access_token(identity=user, expires_delta=expires)
            print(access_token)
            return {"token": access_token, "user_id": user["_id"]}
        else:
            return {"msg": "Bad username or password"}, 401
    
    def __loadFileConfig(self):
        with open('config.json') as f:
            data = json.load(f)
        return data


