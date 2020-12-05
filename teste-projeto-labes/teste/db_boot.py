from .db_intantiation import app, db

@app.route('/')
def index():
    db.create_all()
    return 'Tabela criada'

if __name__ == "__main__":
    app.run(debug=True)
