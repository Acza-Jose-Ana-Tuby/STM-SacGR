from Models.paciente import paciente
import os
import sys
sys.path.append(os.path.realpath('.'))
from database_configuration import app, jsonify
from database_configuration import db

@app.route('/api/login', methods=['GET'])
def login():
    pacientes = paciente.query.all()
    objeto = []
    for linha in pacientes:
        objeto.append(paciente.as_dict(linha))
    return jsonify(objeto)
