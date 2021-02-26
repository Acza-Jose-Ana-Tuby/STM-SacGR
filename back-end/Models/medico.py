import os
import sys
sys.path.append(os.path.realpath('.'))
from database_configuration import db

class medico(db.Model):
    __tablename__ = "medico"
    Med_ID = db.Column(db.Integer, primary_key=True)
    Med_Nome = db.Column(db.VARCHAR(50), unique=False, nullable=False)
    Med_CRM = db.Column(db.VARCHAR(7), unique=True, nullable=False)
    Med_Email = db.Column(db.VARCHAR(255), unique=False, nullable=False)
    Med_Telefone = db.Column(db.VARCHAR(255), unique=False, nullable=False)
    Med_Especialidade = db.Column(db.VARCHAR(50), unique=False, nullable=False)

    consultas = db.relationship('consulta', backref='medico', lazy='dynamic')
    horarios = db.relationship('agenda_medica', backref='medico', lazy='dynamic')
