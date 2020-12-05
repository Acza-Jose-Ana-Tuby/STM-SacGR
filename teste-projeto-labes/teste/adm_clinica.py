from .db_intantiation import db

class adm_clinica(db.Model):
    AdmCli_ID = db.Column(db.Integer, primary_key=True)
    AdmCli_Email = db.Column(db.VARCHAR(50), unique=True, nullable=False)
    AdmCli_Senha = db.Column(db.VARCHAR(15), unique=False, nullable=False)

    def __repr__(self):
        return ''
