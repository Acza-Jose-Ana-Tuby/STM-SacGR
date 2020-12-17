import os
import sys
sys.path.append(os.path.realpath('.'))
from database_configuration import db


class clinica(db.Model):
    Cli_ID = db.Column(db.Integer, primary_key = True)
    Cli_AdmCli_ID = db.Column(db.Integer, db.ForeignKey('adm_clinica.AdmCli_ID'))
    Cli_CNPJ = db.Column(db.VARCHAR(14), unique=True, nullable=False)
    Cli_Nome = db.Column(db.VARCHAR(50), unique=False, nullable=False)
    Cli_Endereco = db.Column(db.Text, unique=False, nullable=False)
    Cli_Telefone = db.Column(db.VARCHAR(30), unique=False, nullable=False)
    Cli_Prazo_Cancelamento = db.Column(db.Integer, unique=False, nullable=False)
    Cli_Taxa_Deslocamento = db.Column(db.Float, unique=False, nullable=False)

    adm_clinica = db.relationship('adm_clinica', backref=db.backref('clinica', lazy=True))

    def __repr__(self):
        return ''
