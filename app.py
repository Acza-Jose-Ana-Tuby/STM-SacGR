from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/stm-sacgr'
db = SQLAlchemy(app)

class Consultas(db.Model):
    Cons_ID        = db.Column(db.Integer, primary_key = True)
    Cons_Pct_ID    = db.Column(db.Integer)
    Cons_Med_ID    = db.Column(db.Integer)
    Cons_Horario   = db.Column(db.Time(6))
    Cons_Data      = db.Column(db.Date)
    Cons_Descricao = db.Column(db.Text(255))
    Cons_Pagamento = db.Column(db.VARCHAR(10))
    Cons_Tipo      = db.Column(db.VARCHAR(6))

    def __repr__(self):
        return '<User %r>' % self.username

class Clinica_Possui_Medico(db.Model):
    Cli_id = db.Column(db.Integer, primary_key = True)
    Med_id = db.Column(db.Integer, primary_key = True)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    db.create_all()
    return "True"

if __name__ == "__main__":
    app.run(debug=True)
