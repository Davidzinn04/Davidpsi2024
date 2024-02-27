from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return "faixa da tolf por 8 reais"

@app.route('/compras')
def compras():
    return render_template('compras.html')

@app.route('/mercados')
def mercados():
    return render_template('mercados.html')