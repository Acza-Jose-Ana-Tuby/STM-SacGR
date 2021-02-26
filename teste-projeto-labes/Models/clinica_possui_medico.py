import os
import sys
sys.path.append(os.path.realpath('.'))
from database_configuration import db

class clinica_possui_medico(db.Model):
    Cli_ID = db.Column(db.Integer, primary_key = True)
    Med_ID = db.Column(db.Integer, primary_key = True)
