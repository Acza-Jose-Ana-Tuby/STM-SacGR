from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sistema-agendamento01'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    #cursor.execute("INSERT INTO Paciente(pct_nome, pct_RG, pct_CPF, pct_endereço, pct_grupo_risco, pct_ID) VALUES ('Tuby', '7421806', '70194401260', 'Boaventura', 0, 1)")
    cursor.execute("SELECT * FROM Usuarios")
    result = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return str(result)


if __name__ == "__main__":
    app.run(debug=True)