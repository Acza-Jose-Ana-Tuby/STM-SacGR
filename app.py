import mysql.connector

# Cria uma conexão com o servidor ou o banco de dados:

def create_connection(server, userid, passwd, databs=None):
    if databs == None:
        connection = mysql.connector.connect(
            host = server, user = userid, password = passwd)
    else:
        connection = mysql.connector.connect(
            host = server, user = userid, password = passwd, database = databs)
    return connection

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

mydb = create_connection("localhost", "root", "password")
mycursor = mydb.cursor()
create_database("mydatabase")

mydb = create_connection("localhost", "root", "password", "mydatabase")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
