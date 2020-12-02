import mysql.connector

# Cria uma conexão com privilégios de administrador no servidor MySQL:

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)

mycursor = mydb.cursor()

# Verifica se uma base de dados já existe

def search_database(database_name):
    mycursor.execute("SHOW DATABASES")
    result = False
    for x in mycursor:
        if x == (database_name,):
            result = True
            break
    return result
    
# Cria uma nova base de dados

def create_database(database_name):
    result = False
    if search_database(database_name) == False:
        mycursor.execute("CREATE DATABASE " + database_name)
        result = True
    return result


