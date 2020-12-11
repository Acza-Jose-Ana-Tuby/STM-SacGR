from flask import Flask

from mysql_sacgr.criador import criar_conexao_servidor, criar_basededados
from mysql_sacgr.verificador import procurar_basededados

app = Flask(__name__)

@app.route('/')
def criar_base_de_dados():
    conexao = criar_conexao_servidor("127.0.0.1", "root", None)
    resultado = procurar_basededados(conexao, "sacgr")
    if resultado == False:
        resultado = criar_basededados(conexao, "sacgr")
    return "Feito\n"   

if __name__ == "__main__":
    app.run(debug=True)
