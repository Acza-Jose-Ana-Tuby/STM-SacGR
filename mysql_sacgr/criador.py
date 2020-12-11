import mysql.connector

def con_servidor(servidor, usuario, senha):
    conexao = mysql.connector.connect(
        host = servidor,
        user = usuario,
        password = senha)
    return conexao

def con_basededados(servidor, usuario, senha, basededados):
    conexao = mysql.connector.connect(
        host = servidor,
        user = usuario,
        password = senha,
        database = basededados)
    return conexao

def basededados(conexao, basededados):
    meubd = conexao.cursor()
    meubd.execute("CREATE DATABASE " + basededados)
    return True
