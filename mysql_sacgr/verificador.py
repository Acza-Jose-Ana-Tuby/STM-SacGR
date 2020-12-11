import mysql.connector

def procurar_basededados(conexao, basededados):
    meubd = conexao.cursor()
    meubd.execute("SHOW DATABASES")
    resultado = False

    for x in meubd:
        if x == (basededados,):
            resultado = True
            break
    return resultado
