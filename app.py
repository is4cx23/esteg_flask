from flask import Flask, render_template

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota cotificar
@app.route('/codificar')
def cotificar():
    return render_template('codificar.html')