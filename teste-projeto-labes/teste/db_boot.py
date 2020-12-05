from .db_intantiation import app, db
from .adm_clinica import adm_clinica

@app.route('/')
def index():
    db.create_all()
    adm1 = adm_clinica(1, 'netotuby', 'pass1234')
    db.session.add(adm1)
    db.session.commit()
    return 'Tabela criada'

if __name__ == "__main__":
    app.run(debug=True)
