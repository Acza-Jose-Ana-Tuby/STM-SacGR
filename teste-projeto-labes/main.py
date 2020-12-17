from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
#from teste import clinica, adm_clinica, consulta, clinica_possui_medico, medico, paciente, adm_sistema, atendente

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/sistema-agendamento'




@app.route('/')
def index():
    #adm2 = adm_clinica(2, 'netotubias', 'pass1234')
    #db.session.add(adm2)
    #db.session.commit()
    return 'Tabela criada'

if __name__ == "__main__":
    app.run(debug=True)
