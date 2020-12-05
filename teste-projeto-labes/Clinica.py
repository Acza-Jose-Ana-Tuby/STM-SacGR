from .main2 import db

class clinica(main2.db.Model):
    Cli_ID = main2.db.Column(main2.db.Integer, primary_key = True)
    Cli_AdmCli_ID = main2.db.Column(main2.db.Integer)
    Cli_CNPJ = main2.db.Column(main2.db.VARCHAR(14), unique=True, nullable=False)
    Cli_Nome = main2.db.Column(main2.db.VARCHAR(50), unique=False, nullable=False)
    Cli_Endereco = main2.db.Column(main2.db.Text, unique=False, nullable=False)
    Cli_Telefone = main2.db.Column(main2.db.VARCHAR(30), unique=False, nullable=False)
    Cli_Prazo_Cancelamento = main2.db.Column(main2.db.Integer, unique=False, nullable=False)
    Cli_Taxa_Deslocamento = main2.db.Column(main2.db.Float, unique=False, nullable=False)

    def __repr__(self):
        return ''

if __name__ == "__main__":
    db.create_all()
