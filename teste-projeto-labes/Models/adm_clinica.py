import os
import sys
sys.path.append(os.path.realpath('.'))
from database_configuration import db


class adm_clinica(db.Model):
    AdmCli_ID = db.Column(db.Integer, primary_key=True)
    AdmCli_Senha = db.Column(db.VARCHAR(15), unique=False, nullable=False)
    AdmCli_Email = db.Column(db.VARCHAR(50), unique=True, nullable=False)
