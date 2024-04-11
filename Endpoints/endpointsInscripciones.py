from flask import jsonify, request, Blueprint
from Controladores.controlInscripciones import ControladorInscripciones

controladorInscripciones = ControladorInscripciones()

endpointInscripciones=Blueprint('endpointsInscripciones',__name__)

@endpointInscripciones.route("/inscripciones", methods=['GET'])
def listar_inscripciones():
    response=controladorInscripciones.index()
    print(response)
    return jsonify(response) if not isinstance(response,tuple) else (jsonify(response[0]), response[1])

@endpointInscripciones.route("/inscripciones/<string:id>", methods=['GET'])
def get_inscripcion(id):
    response=controladorInscripciones.getInscripcion(id)
    print(response)
    return jsonify(response) if not isinstance(response,tuple) else (jsonify(response[0]), response[1])

@endpointInscripciones.route("/inscripciones/<string:id>", methods=['PATCH'])
def modificarNota(id):
    data = request.get_json()
    response=controladorInscripciones.modificarNota(id, data)
    print(response)
    return jsonify(response) if not isinstance(response,tuple) else (jsonify(response[0]), response[1])

