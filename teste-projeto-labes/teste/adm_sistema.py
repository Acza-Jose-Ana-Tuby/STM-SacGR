from .db_intantiation import db

class adm_sistema(db.Model):
    AdmSis_id = db.Column(db.Integer, primary_key=True)
    AdmSis_email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    AdmSis_Senha = db.Column(db.VARCHAR(15), unique=True, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username
