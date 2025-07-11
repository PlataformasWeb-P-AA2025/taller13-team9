from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from config import token  # Importar el token desde config.py

app = Flask(__name__)
app.secret_key = '1939d7316d374f28705e04a107a0bba446609534'

API_BASE = 'http://127.0.0.1:8000/api'
HEADERS = {'Authorization': f'Token {token}'}


@app.route('/')
def index():
    try:
        edificios_resp = requests.get(f'{API_BASE}/edificios/', headers=HEADERS)
        departamentos_resp = requests.get(f'{API_BASE}/departamentos/', headers=HEADERS)

        edificios = edificios_resp.json().get('results', [])
        departamentos = departamentos_resp.json().get('results', [])

    except Exception as e:
        flash(f"❌ Error de conexión: {e}")
        edificios = []
        departamentos = []

    print("DEPARTAMENTOS:", departamentos_resp.json())


    return render_template('index.html', edificios=edificios, departamentos=departamentos)


@app.route('/crear_edificio', methods=['GET', 'POST'])
def crear_edificio():
    if request.method == 'POST':
        data = {
            'nombre': request.form['nombre'],
            'direccion': request.form['direccion'],
            'ciudad': request.form['ciudad'],
            'tipo': request.form['tipo']
        }

        response = requests.post(f'{API_BASE}/edificios/', json=data, headers=HEADERS)
        if response.status_code == 201:
            flash('✅ Edificio creado correctamente.')
            return redirect(url_for('index'))
        else:
            flash(f'❌ Error al crear edificio: {response.text}')
    return render_template('crear_edificio.html')


@app.route('/crear_departamento', methods=['GET', 'POST'])
def crear_departamento():
    edificios_resp = requests.get(f'{API_BASE}/edificios/', headers=HEADERS)
    edificios = edificios_resp.json().get('results', [])

    if request.method == 'POST':
        data = {
            'nombre_propietario': request.form['nombre_propietario'],
            'costo': request.form['costo'],
            'num_cuartos': request.form['num_cuartos'],
            'edificio': request.form['edificio_id']  # ya viene como URL
        }

        print("📦 Enviando:", data)

        response = requests.post(f'{API_BASE}/departamentos/', json=data, headers=HEADERS)
        print("❌ Error:", response.status_code, response.text)

        if response.status_code == 201:
            flash('✅ Departamento creado correctamente.')
            return redirect(url_for('index'))
        else:
            flash(f'❌ Error al crear departamento: {response.text}')

    return render_template('crear_departamento.html', edificios=edificios)


if __name__ == '__main__':
    app.run(debug=True)
