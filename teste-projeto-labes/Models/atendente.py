import os
import sys
sys.path.append(os.path.realpath('.'))
from database_configuration import db

class atendente(db.Model):
    Atd_ID = db.Column(db.Integer, primary_key=True)
    Atd_Email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    Atd_Senha = db.Column(db.VARCHAR(15), unique=True, nullable=False)
