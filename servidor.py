from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from mysql_sacgr.criador import con_servidor, con_basededados, basededados
from mysql_sacgr.verificador import procurar_basededados, procurar_tabelas

listadetabelas = [
    "Adm_Clinica",
    "Adm_Sistema",
    "Atendente",
    "Clinica",
    "Clinica_Possui_Medico",
    "Consulta",
    "Medico",
    "Paciente"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/sacgr'
bd = SQLAlchemy(app)

class adm_clinica(bd.Model):
    AdmCli_ID = bd.Column(bd.Integer, primary_key=True)
    AdmCli_Email = bd.Column(bd.VARCHAR(50), unique=True, nullable=False)
    AdmCli_Senha = bd.Column(bd.VARCHAR(15), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class adm_sistema(bd.Model):
    AdmSis_id = bd.Column(bd.Integer, primary_key=True)
    AdmSis_email = bd.Column(bd.VARCHAR(255), unique=True, nullable=False)
    AdmSis_Senha = bd.Column(bd.VARCHAR(15), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class atendente(bd.Model):
    Atd_ID = bd.Column(bd.Integer, primary_key=True)
    Atd_Email = bd.Column(bd.VARCHAR(255), unique=True, nullable=False)
    Atd_Senha = bd.Column(bd.VARCHAR(15), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class clinica(bd.Model):
    Cli_ID = bd.Column(bd.Integer, primary_key = True)
    Cli_AdmCli_ID = bd.Column(bd.Integer)
    Cli_CNPJ = bd.Column(bd.VARCHAR(14), unique=True, nullable=False)
    Cli_Nome = bd.Column(bd.VARCHAR(50), unique=False, nullable=False)
    Cli_Endereco = bd.Column(bd.Text, unique=False, nullable=False)
    Cli_Telefone = bd.Column(bd.VARCHAR(30), unique=False, nullable=False)
    Cli_Prazo_Cancelamento = bd.Column(bd.Integer, unique=False, nullable=False)
    Cli_Taxa_Deslocamento = bd.Column(bd.Float, unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class clinica_possui_medico(bd.Model):
    Cli_id = bd.Column(bd.Integer, primary_key = True)
    Med_id = bd.Column(bd.Integer, primary_key = True)

    def __repr__(self):
        return ''

class consulta(bd.Model):
    Cons_ID        = bd.Column(bd.Integer, primary_key = True)
    Cons_Pct_ID    = bd.Column(bd.Integer)
    Cons_Med_ID    = bd.Column(bd.Integer)
    Cons_Horario   = bd.Column(bd.Time(6))
    Cons_Data      = bd.Column(bd.Date)
    Cons_Descricao = bd.Column(bd.Text(255))
    Cons_Pagamento = bd.Column(bd.VARCHAR(10))
    Cons_Tipo      = bd.Column(bd.VARCHAR(6))

    def __repr__(self):
        return '<User %r>' % self.username

class medico(bd.Model):
    Med_id = bd.Column(bd.Integer, primary_key=True)
    Med_Nome = bd.Column(bd.VARCHAR(50), unique=False, nullable=False)
    Med_CRM = bd.Column(bd.VARCHAR(7), unique=True, nullable=False)
    Med_Especialidade = bd.Column(bd.VARCHAR(50), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class paciente(bd.Model):
    Pct_id = bd.Column(bd.Integer, primary_key=True)
    Pct_Nome = bd.Column(bd.VARCHAR(50), unique=False, nullable=False)
    Pct_Rg = bd.Column(bd.VARCHAR(20), unique=False, nullable=False)
    Pct_CPF = bd.Column(bd.VARCHAR(11), unique=True, nullable=False)
    Pct_Endereco = bd.Column(bd.VARCHAR(255), unique=False, nullable=False)
    Pct_Email = bd.Column(bd.VARCHAR(50), unique=True, nullable=False)
    Pct_Telefone = bd.Column(bd.VARCHAR(30), unique=False, nullable=False)
    Pct_Senha = bd.Column(bd.VARCHAR(15), unique=False, nullable=False)
    Pct_Grupo_Risco = bd.Column(bd.VARCHAR(50), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/basededados') # Cria a base de dados no servidor
def criar_base_de_dados():
    conexao = con_servidor("127.0.0.1", "root", None)
    if procurar_basededados(conexao, "sacgr") == False:
        basededados(conexao, "sacgr")
    return "Feito\n"

@app.route('/tabelas') # Cria as tabelas no servidor
def criar_tabelas():
    conexao = con_basededados("127.0.0.1", "root", None, "sacgr")
    if procurar_tabelas(conexao, listadetabelas) == False:
        bd.create_all()
    return "Feito\n"

if __name__ == "__main__":
    app.run(debug=True)
