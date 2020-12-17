from database_configuration import app, db
from flask_restless import APIManager

manager = APIManager(app, flask_sqlalchemy_db=db)

from APIs import adm_clinica, adm_sistema, atendente, clinica_possui_medico, clinica, consulta, medico, paciente
