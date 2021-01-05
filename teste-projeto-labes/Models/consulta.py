import os
import sys
sys.path.append(os.path.realpath('.'))
from database_configuration import db

class consulta(db.Model):
    __tablename__ = "consulta"
    Cons_ID        = db.Column(db.Integer, primary_key = True, autoincrement=True)
    Cons_Pct_ID    = db.Column(db.Integer)
    Cons_Med_ID    = db.Column(db.Integer)
    Cons_Horario   = db.Column(db.Time(6))
    Cons_Data      = db.Column(db.Date)
    Cons_Descricao = db.Column(db.Text(255))
    Cons_Pagamento = db.Column(db.VARCHAR(10))
    Cons_Tipo      = db.Column(db.VARCHAR(6))
    Cons_Pct_ID    = db.Column(db.Integer, db.ForeignKey('paciente.Pct_ID'), primary_key = True)
    Cons_Med_ID    = db.Column(db.Integer, db.ForeignKey('medico.Med_ID'), primary_key = True)
