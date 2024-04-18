from datetime import datetime, timedelta, timezone
import json

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from waitress import serve

import Endpoints
from Controladores.controlMiddleware import ControladorMiddleware

app=Flask(__name__)
cors = CORS(app)

app.config["JWT_SECRET_KEY"]="super-secret" #Cambiar por el que sea conveniente
jwt = JWTManager(app)

# Registro los endpoints
app.register_blueprint(Endpoints.endpointInscripciones)
app.register_blueprint(Endpoints.endpointSeguridad)

middleware = ControladorMiddleware()

def __loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

@app.before_request
def before_request_f():
    middleware.before_request_func()

@app.after_request
def after_request_f(response):
    r=middleware.after_request_func(response)
    return r

@app.route("/",methods=['GET'])
def test():
    json = {}
    __uptime = datetime.now(timezone(-timedelta(hours=5))) - __init_time
    json["message"] = "Server running..."
    json["uptime"]  = f'{__uptime}'
    return jsonify(json)


__init_time = None
if __name__=='__main__':
    dataConfig = __loadFileConfig()
    print(f'Server running: http://{dataConfig["url-backend"]}:{str(dataConfig["port"])}')
    __init_time = datetime.now(timezone(-timedelta(hours=5)))
    print(f'Init time: {__init_time}')
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])