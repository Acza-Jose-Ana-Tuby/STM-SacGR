from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/labes'
db = SQLAlchemy(app)


class Atendente(db.Model):
    Atd_ID = db.Column(db.Integer, primary_key=True)
    Atd_Email = db.Column(db.varchar(255), unique=True, nullable=False)
    Atd_Senha = db.Column(db.varchar(15), unique=True, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    db.create_all()
    #user1 = user.User(1, 'root', 'password')

    return 'sucess'

if __name__ == "__main__":
    app.run(debug=True)
