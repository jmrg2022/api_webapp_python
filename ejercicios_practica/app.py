#!/usr/bin/env python
'''
API Personas
---------------------------
Autor: Inove Coding School
Version: 1.0
 
Descripcion:
Se utiliza Flask para crear un WebServer que levanta los datos de
las personas registradas.

Ejecución: Lanzar el programa y abrir en un navegador la siguiente dirección URL
NOTA: Si es la primera vez que se lanza este programa crear la base de datos
entrando a la siguiente URL
http://127.0.0.1:5000/reset

Ingresar a la siguiente URL para ver los endpoints disponibles
http://127.0.0.1:5000/
'''

__author__ = "Inove Coding School"
__email__ = "INFO@INOVE.COM.AR"
__version__ = "1.0"

import traceback
import io
import sys
import os
import base64
import json
import sqlite3
from datetime import datetime, timedelta

import numpy as np
from flask import Flask, request, jsonify, render_template, Response, redirect, url_for
import matplotlib
matplotlib.use('Agg')   # For multi thread, non-interactive backend (avoid run in main loop)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.image as mpimg

from persona_orm import db
import persona_orm as persona
#import persona as persona  # Puede elegir esta opcion sino quieren usar ORM

from config import config

app = Flask(__name__)

# Obtener la path de ejecución actual del script
script_path = os.path.dirname(os.path.realpath(__file__))

# Obtener los parámetros del archivo de configuración
config_path_name = os.path.join(script_path, 'config.ini')
db_config = config('db', config_path_name)
server_config = config('server', config_path_name)

# Indicamos al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_config['database']}"
# Asociamos nuestro controlador de la base de datos con la aplicacion
db.init_app(app)


# Ruta que se ingresa por la ULR 127.0.0.1:5000
@app.route("/")
def index():
    try:
        # En el futuro se podria realizar una página de bienvenida
        return redirect(url_for('personas'))
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/api")
def api():
    try:
        # Imprimir los distintos endopoints disponibles
        result = "<h1>Bienvenido!!</h1>"
        result += "<h2>Endpoints disponibles:</h2>"
        result += "<h3>[GET] /reset --> borrar y crear la base de datos</h3>"
        result += "<h3>[GET] /personas --> mostrar la tabla de personas (el HTML)</h3>"
        result += "<h3>[GET] /registro --> mostrar el HTML con el formulario de registro de persona</h3>"
        result += "<h3>[POST] /registro --> ingresar nuevo registro de pulsaciones por JSON</h3>"
        result += "<h3>[GET] /comparativa --> mostrar un gráfico que compare cuantas personas hay de cada nacionalidad"
        
        return(result)
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/reset")
def reset():
    try:
        # Borrar y crear la base de datos
        persona.create_schema()
        result = "<h3>Base de datos re-generada!</h3>"
        return (result)
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/personas")
def personas():
    try:
        # Alumno: Implemente el manejo
        # del limit y offset para pasarle
        # como parámetros a report
        data = persona.report()
        
        result = '''<h3>Alumno: Implementar la llamada
                    al HTML tabla.html
                    con render_template, recuerde pasar
                    data como parámetro</h3>'''
        # Sacar esta linea cuando haya implementado el return
        # con render template
        return result 
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/comparativa")
def comparativa():
    try:
        # Mostrar todos los registros en un gráfico
        result = '''<h3>Implementar una función en persona.py
                    que se llame "age_report"</h3>'''
        result += '''<h3>Esa funcion debe devolver los datos
                    de todas las edades ingresadas e realizar
                    un gráfico "plot" para mostrar en el HTMl</h3>'''
        result += '''<h3>El eje "X" del gráfico debe ser los IDs
                    de las personas y el eje "Y" deben ser sus
                     respectivas edades</h3>'''
        result += '''<h3>Bonus track: puede hacer que esta endpoint reciba
                    como parámetro estático o dinámico que indique la nacionalidad
                    que se desea estudiar sus edades ingresadas (filtrar las edades
                    por la nacionalidad ingresada)</h3>'''
        return (result)
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/registro", methods=['GET', 'POST'])
def registro():
    if request.method == 'GET':
        try:
            return render_template('registro.html')
        except:
            return jsonify({'trace': traceback.format_exc()})

    if request.method == 'POST':
        try:
            # Alumno: Implemente
            # Obtener del HTTP POST JSON el nombre y los pulsos
            # name = ...
            # age = ...
            # nationality = ...

            # persona.insert(name, int(age), nationality)

            # Como respuesta al POST devolvemos la tabla de valores
            return redirect(url_for('personas'))
        except:
            return jsonify({'trace': traceback.format_exc()})
    

if __name__ == '__main__':
    print('Servidor arriba!')

    app.run(host=server_config['host'],
            port=server_config['port'],
            debug=True)
