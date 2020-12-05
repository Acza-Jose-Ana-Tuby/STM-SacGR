from .db_intantiation import db

class atendente(db.Model):
    Atd_ID = db.Column(db.Integer, primary_key=True)
    Atd_Email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    Atd_Senha = db.Column(db.VARCHAR(15), unique=True, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username
