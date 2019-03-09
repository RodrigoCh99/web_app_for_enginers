# importando a biblioteca
from flask import Flask, render_template, request
from functions import *

# Instanciando a variavel app:
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/send_data', methods = ['POST'])
def send_data():

    # Inputs do formulario para serem transformados em variaveis python:

    rugosidade = converter_para_metro(float(request.form['rugosidade-absoluta']))
    diametro = converter_para_metro(float(request.form['diametro-interno']))
    numero = float(request.form['numero-reynolds'])

    # Output do formulario:
    fator = str(calcula_fator_friccao(rugosidade, diametro, numero))
    return render_template('home.html', fator=fator)


# rodando a plicação:
if __name__ == '__main__':
    app.run(debug=True)