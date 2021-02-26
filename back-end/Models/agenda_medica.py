import os
import sys
sys.path.append(os.path.realpath('.'))
from database_configuration import db

class agenda_medica(db.Model):
    __tablename__ = "agenda_medica"
    AgdMed_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    AgdMed_Marcado = db.Column(db.Integer, unique=False, nullable=False)
    AgdMed_Dia = db.Column(db.VARCHAR(20), unique=False, nullable=False)
    AgdMed_Hora_Inicio = db.Column(db.VARCHAR(10), unique=False, nullable=False)
    AgdMed_Duracao = db.Column(db.VARCHAR(10), unique=False, nullable=False)
    AgdMed_Med_ID = db.Column(db.Integer, db.ForeignKey('medico.Med_ID'), primary_key = True)
