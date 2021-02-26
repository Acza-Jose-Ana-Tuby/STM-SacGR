import os
import sys
sys.path.append(os.path.realpath('.'))
from database_configuration import db

class politica_agendamento(db.Model):
    __tablename__ = "politica_agendamento"
    PltAgd_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PltAgd_Turno_Regular = db.Column(db.VARCHAR(50), unique=False, nullable=False)
    PltAgd_Turno_Grupo_Risco = db.Column(db.VARCHAR(50), unique=False, nullable=False)
    PltAgd_Capacidade_Regular = db.Column(db.Integer, unique=False, nullable=False)
    PltAgd_Capacidade_Grupo_Risco = db.Column(db.Integer, unique=False, nullable=False)
    PltAgd_Protocolos_Regular = db.Column(db.Text, unique=False, nullable=False)
    PltAgd_Protocolos_Grupo_Risco = db.Column(db.Text, unique=False, nullable=False)
