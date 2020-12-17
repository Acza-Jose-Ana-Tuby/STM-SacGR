from teste-projeto-

db = SQLAlchemy(app)
db.create_all()
manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(adm_clinica)
