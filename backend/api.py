from flask import Flask, jsonify, request  
import pandas as pd
import numpy as np
import socket
from contextlib import closing
from funciones import eleccion_presidencial_con_votos_por_region, eleccion_senadores_con_votos_por_region, hay_segunda_instancia, resultados_presidenciales_por_region_provincia, resultados_presidenciales_por_region_especifica
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Rutas de la API
@app.route('/eleccion/presidencial/<int:anio>', methods=['GET'])
def get_eleccion_presidencial(anio):
    try:
        resultado = eleccion_presidencial_con_votos_por_region(anio)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/eleccion/presidencial/region/<int:anio>/<region>', methods=['GET'])
def get_resultados_region(anio, region):
    instancia_votacion = request.args.get('instancia', None)

    try:
        resultado = resultados_presidenciales_por_region_especifica(anio, region, instancia_votacion)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/eleccion/presidencial/detalle/<int:anio>', methods=['GET'])
def get_resultados_presidenciales(anio):
    # Opcionalmente, obtener la instancia de votación desde los parámetros de la consulta
    instancia_votacion = request.args.get('instancia', None)

    try:
        resultado = resultados_presidenciales_por_region_provincia(anio)
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

@app.route('/eleccion/presidencial/segunda_instancia/<int:anio>', methods=['GET'])
def get_segunda_instancia(anio):
    try:
        resultado = hay_segunda_instancia(anio)
        return jsonify({'segunda_instancia': resultado}), 200
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
        port = 52379
        app.run(host='127.0.0.1', port=port, debug=True)
    except OSError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_server(app)
