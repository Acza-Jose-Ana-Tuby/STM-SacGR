from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/sistema-agendamento01' #tirar o 01 para integração
db = SQLAlchemy(app)

class Medico(db.Model):
    Med_id = db.Column(db.Integer, primary_key=True)
    Med_Nome = db.Column(db.VARCHAR(50), unique=False, nullable=False)
    Med_CRM = db.Column(db.VARCHAR(7), unique=True, nullable=False)
    Med_Especialidade = db.Column(db.VARCHAR(50), unique=False, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    db.create_all()
    

    return 'activate'

if __name__ == "__main__":
    app.run(debug=True)