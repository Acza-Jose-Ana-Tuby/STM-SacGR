from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/sistema-agendamento01' #tirar o 01 para integração
db = SQLAlchemy(app)

class Paciente(db.Model):
    Pct_id = db.Column(db.Integer, primary_key=True)
    Pct_Nome = db.Column(db.VARCHAR(50), unique=False, nullable=False)
    Pct_Rg = db.Column(db.VARCHAR(20), unique=False, nullable=False)
    Pct_CPF = db.Column(db.VARCHAR(11), unique=True, nullable=False)
    Pct_Endereco = db.Column(db.VARCHAR(255), unique=False, nullable=False)
    Pct_Email = db.Column(db.VARCHAR(50), unique=True, nullable=False)
    Pct_Telefone = db.Column(db.VARCHAR(30), unique=False, nullable=False)
    Pct_Senha = db.Column(db.VARCHAR(15), unique=False, nullable=False)
    Pct_Grupo_Risco = db.Column(db.VARCHAR(50), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    db.create_all()


    return 'activate'

if __name__ == "__main__":
    app.run(debug=True)