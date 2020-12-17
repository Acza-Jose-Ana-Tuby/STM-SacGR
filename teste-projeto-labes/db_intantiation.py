from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from .adm_clinica import adm_clinica

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/sistema-agendamento'
db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)
db.create_all()
manager.create_api(adm_clinica)
