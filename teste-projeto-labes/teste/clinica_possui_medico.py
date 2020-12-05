from .db_intantiation import db

class Clinica_Possui_Medico(db.Model):
    Cli_id = db.Column(db.Integer, primary_key = True)
    Med_id = db.Column(db.Integer, primary_key = True)

    def __repr__(self):
        return ''
