from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# ===========================
# Configuración de la base de datos
# ===========================
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ===========================
# Modelos de la base de datos
# ===========================

class Peso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    peso = db.Column(db.Float, nullable=False)

class Alimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    calorias = db.Column(db.Integer, nullable=False)

# ===========================
# Rutas principales
# ===========================

@app.route('/')
def index():
    pesos = Peso.query.order_by(Peso.fecha).all()
    alimentos = Alimento.query.order_by(Alimento.fecha).all()

    # Convertir a formato JSON serializable
    pesos_json = [
        {"fecha": p.fecha.strftime('%Y-%m-%d'), "peso": p.peso}
        for p in pesos
    ]
    alimentos_json = [
        {"fecha": a.fecha.strftime('%Y-%m-%d'), "nombre": a.nombre, "calorias": a.calorias}
        for a in alimentos
    ]

    return render_template('index.html', pesos=pesos_json, alimentos=alimentos_json)

@app.route('/add_weight', methods=['GET', 'POST'])
def add_weight():
    if request.method == 'POST':
        fecha = request.form['fecha']
        peso = request.form['peso']
        print(f"[DEBUG] Fecha ingresada: {fecha}, Peso ingresado: {peso}")
        nuevo_peso = Peso(
            fecha=datetime.strptime(fecha, '%Y-%m-%d'),
            peso=float(peso)
        )
        db.session.add(nuevo_peso)
        db.session.commit()
        return redirect('/')
    return render_template('add_weight.html')

@app.route('/add_food', methods=['GET', 'POST'])
def add_food():
    if request.method == 'POST':
        fecha = request.form['fecha']
        nombre = request.form['nombre']
        calorias = request.form['calorias']
        nuevo_alimento = Alimento(
            fecha=datetime.strptime(fecha, '%Y-%m-%d'),
            nombre=nombre,
            calorias=int(calorias)
        )
        db.session.add(nuevo_alimento)
        db.session.commit()
        return redirect('/')
    return render_template('add_food.html')

# ===========================
# Inicialización de la app
# ===========================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


