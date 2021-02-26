import os
import sys
sys.path.append(os.path.realpath('.'))
from database_configuration import db

class paciente(db.Model):
    __tablename__ = "paciente"
    Pct_ID = db.Column(db.Integer, primary_key=True)
    Pct_Nome = db.Column(db.VARCHAR(50), unique=False, nullable=False)
    Pct_Rg = db.Column(db.VARCHAR(20), unique=False, nullable=True)
    Pct_CPF = db.Column(db.VARCHAR(11), unique=True, nullable=False)
    Pct_Endereco = db.Column(db.VARCHAR(255), unique=False, nullable=True)
    Pct_Email = db.Column(db.VARCHAR(50), unique=True, nullable=False)
    Pct_Telefone = db.Column(db.VARCHAR(30), unique=False, nullable=False)
    Pct_Senha = db.Column(db.VARCHAR(15), unique=False, nullable=False)
    Pct_Grupo_Risco = db.Column(db.VARCHAR(50), unique=False, nullable=False)

    consultas = db.relationship('consulta', backref='paciente', lazy='dynamic')

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
