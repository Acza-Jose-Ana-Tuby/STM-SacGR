from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/sistema-agendamento' #para quem ta usando docker, pode ser diferente o link da conexão
db = SQLAlchemy(app)

class Oieee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usernamee = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    db.create_all()
    #user1 = user.User(3, 'tubyneto', 'netotuby')

    return 'aaa'

if __name__ == "__main__":
    app.run(debug=True)
