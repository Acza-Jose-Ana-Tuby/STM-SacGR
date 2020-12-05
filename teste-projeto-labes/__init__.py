from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/sistema-agendamento'
db = SQLAlchemy(app)

from .Clinica import clinica

@app.route('/')
def index():
     db.create_all()
     return 'Tabela criada'

if __name__ == "__main__":
    app.run(debug=True)
