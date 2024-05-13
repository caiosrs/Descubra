from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Número aleatório para adivinhar
numero_secreto = random.randint(1, 100)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adivinhar', methods=['POST'])
def adivinhar():
    palpite = int(request.form['palpite'])
    if palpite == numero_secreto:
        resultado = 'Parabéns! Você acertou o número secreto.'
    elif palpite < numero_secreto:
        resultado = 'O número é maior. Tente novamente.'
    else:
        resultado = 'O número é menor. Tente novamente.'
    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
