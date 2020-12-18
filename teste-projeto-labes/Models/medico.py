import os
import sys
sys.path.append(os.path.realpath('.'))
from database_configuration import db

class medico(db.Model):
    Med_id = db.Column(db.Integer, primary_key=True)
    Med_Nome = db.Column(db.VARCHAR(50), unique=False, nullable=False)
    Med_CRM = db.Column(db.VARCHAR(7), unique=True, nullable=False)
    Med_Especialidade = db.Column(db.VARCHAR(50), unique=False, nullable=False)
