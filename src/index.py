from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/anadirObjeto', methods=['POST', 'GET'])
def anadirObjeto():
    if request.method == 'POST':
        print(request.form.keys)
    return render_template('nuevoObjeto.html')

@app.route('/buscarObjetos', methods=['POST', 'GET'])
def buscarObjetos():
    if request.method == 'POST':
        print(request.form.keys)
    return render_template('buscarObjetos.html')

@app.route('/login')
def login():
    return 'login'


if __name__ == "__main__":
    app.run(port = 3000, debug=True)