from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://root:@localhost/labes'
db = SQLAlchemy(app)


class Adm_Sistema(db.Model):
    AdmSis_id = db.Column(db.Integer, primary_key=True)
    AdmSis_email = db.Column(db.varchar(255), unique=True, nullable=False)
    AdmSis_Senha = db.Column(db.varchar(15), unique=True, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    db.create_all()
    #user1 = user.User(1, 'root', 'password')

    return 'sucess'

if __name__ == "__main__":
    app.run(debug=True)
