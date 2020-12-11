import mysql.connector

def criar_conexao_servidor(servidor, usuario, senha):
    conexao = mysql.connector.connect(
        host = servidor,
        user = usuario,
        password = senha)
    return conexao

def criar_basededados(conexao, basededados):
    meubd = conexao.cursor()
    meubd.execute("CREATE DATABASE " + basededados)
    return True
