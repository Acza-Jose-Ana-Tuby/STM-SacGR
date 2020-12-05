from .db_intantiation import db

class clinica(db.Model):
    Cli_ID = db.Column(db.Integer, primary_key = True)
    Cli_AdmCli_ID = db.Column(db.Integer)
    Cli_CNPJ = db.Column(db.VARCHAR(14), unique=True, nullable=False)
    Cli_Nome = db.Column(db.VARCHAR(50), unique=False, nullable=False)
    Cli_Endereco = db.Column(db.Text, unique=False, nullable=False)
    Cli_Telefone = db.Column(db.VARCHAR(30), unique=False, nullable=False)
    Cli_Prazo_Cancelamento = db.Column(db.Integer, unique=False, nullable=False)
    Cli_Taxa_Deslocamento = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return ''
