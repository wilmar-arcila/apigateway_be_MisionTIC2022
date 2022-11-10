from flask import jsonify, request, Blueprint
from Controladores.controlSeguridad import ControladorSeguridad

controladorSeguridad = ControladorSeguridad()

endpointSeguridad=Blueprint('endpointsSeguridad',__name__)

@endpointSeguridad.route("/login",methods=['POST'])
def login():
    data = request.get_json()
    response=controladorSeguridad.login(data)
    print(response)
    return jsonify(response) if not isinstance(response,tuple) else (jsonify(response[0]), response[1])

# @endpointSeguridad.route("/estudiantes/<string:id>",methods=['GET'])
# def retrieve(id):
#     json=controladorEstudiante.retrieve(id)
#     return jsonify(json)
