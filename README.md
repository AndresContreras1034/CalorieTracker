# 📊 Calorie Tracker

Aplicación web desarrollada con **Flask**, **SQLite**, **Chart.js** y **HTML/CSS** para registrar el peso corporal diario y las calorías consumidas mediante una interfaz moderna y visual.

## 🧠 Características principales

* 📥 Registro de peso diario (fecha y valor).
* 🍽️ Registro de alimentos con nombre, fecha y calorías.
* 📈 Visualización de datos mediante gráficos interactivos con Chart.js.
* 🌐 Interfaz responsiva, minimalista y moderna.

## 🛠 Tecnologías utilizadas

* **Backend:** Python 3, Flask, Flask-SQLAlchemy
* **Frontend:** HTML5, CSS3, JavaScript (Chart.js)
* **Base de datos:** SQLite

## 📂 Estructura del proyecto

```
calorie-tracker/
├── app.py
├── database.db (ignorado en git)
├── templates/
│   ├── index.html
│   ├── add_food.html
│   └── add_weight.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── chart-handler.js
│   └── img/
│       └── favicon.ico
├── requirements.txt
├── README.md
└── .gitignore
```

## ▶️ Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/calorie-tracker.git
cd calorie-tracker
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación

```bash
python app.py
```

Abre en tu navegador: `http://localhost:5000`

## 📸 Capturas de pantalla

> Puedes incluir aquí capturas del dashboard mostrando los gráficos de peso y calorías.

## 📦 Requisitos

Contenido del archivo `requirements.txt`:

```txt
Flask==2.3.2
Flask-SQLAlchemy==3.0.5
```

## 📄 .gitignore sugerido

```gitignore
__pycache__/
*.pyc
instance/
database.db
.env
venv/
```

## 🧩 Ideas de mejora

* 🔐 Agregar autenticación de usuarios.
* 🧮 Cálculo automático de calorías objetivo.
* ⏳ Historial por semana/mes con filtros.
* 📥 Exportar datos a CSV/Excel.
* 📲 Implementación como PWA para acceso móvil.

## 👨‍💻 Autor

**Andrés Felipe Contreras Méndez**
Desarrollador Backend | Estudiante de Ingeniería de Sistemas
Colombia 🇨🇴

---

> Proyecto desarrollado con fines educativos, personales y de seguimiento de salud.
