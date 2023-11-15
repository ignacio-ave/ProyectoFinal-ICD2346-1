from flask import Flask, jsonify
import pandas as pd
import socket
from contextlib import closing
from funciones import eleccion_presidencial_con_votos_por_region, eleccion_senadores_con_votos_por_region

app = Flask(__name__)

# Rutas de la API
@app.route('/eleccion/presidencial/<int:anio>', methods=['GET'])
def get_eleccion_presidencial(anio):
    try:
        resultado = eleccion_presidencial_con_votos_por_region(anio)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/eleccion/senadores/<int:anio>', methods=['GET'])
def get_eleccion_senadores(anio):
    try:
        resultado = eleccion_senadores_con_votos_por_region(anio)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def run_server(app):
    ports = [5000, 5001, 5002, 5003]  # Lista de puertos para intentar
    for port in ports:
        try:
            app.run(host='127.0.0.1', port=port, debug=True)
            break  # Si el servidor se inicia correctamente, sal del bucle
        except OSError as e:
            if e.errno == 98:  # Error de puerto en uso
                print(f"El puerto {port} está en uso, intentando con otro puerto.")
            else:
                raise  # Si es otro tipo de OSError, lánzalo


def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]

def run_server(app):
    try:
        port = find_free_port()
        app.run(host='127.0.0.1', port=port, debug=True)
    except OSError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_server(app)