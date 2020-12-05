from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://root:@127.0.0.1/labes'
db = SQLAlchemy(app)


class Adm_Sistema(db.Model):
    AdmSis_id = db.Column(db.Integer, primary_key=True)
    AdmSis_email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    AdmSis_Senha = db.Column(db.VARCHAR(15), unique=True, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    db.create_all()
    #user1 = user.User(1, 'root', 'password')

    return 'Done'

if __name__ == "__main__":
    app.run(debug=True)
