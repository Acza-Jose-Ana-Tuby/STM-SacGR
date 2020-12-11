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

def procurar_tabelas(conexao, listadetabelas):
    meubd = conexao.cursor()
    meubd.execute("SHOW DATABASES")
    resultado = False

    for x in listadetabelas:
        for y in meubd:
            if y == (x,):
                resultado = True
                break
        break
    return resultado
