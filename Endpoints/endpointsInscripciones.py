from flask import jsonify, request, Blueprint
from Controladores.controlInscripciones import ControladorInscripciones

controladorInscripciones = ControladorInscripciones()

endpointInscripciones=Blueprint('endpointsInscripciones',__name__)

@endpointInscripciones.route("/inscripciones",methods=['GET'])
def get_inscripciones():
    response=controladorInscripciones.index()
    print(response)
    return jsonify(response) if not isinstance(response,tuple) else (jsonify(response[0]), response[1])
