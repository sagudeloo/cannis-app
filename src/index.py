from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/anadirObjeto', methods=['POST', 'GET'])
def anadirObjeto():
    if request.method == 'POST':
        print("Se va a annadir un objeto")
        informacion={
            'object':{
                'descripcion': request.form['descripcion'],
                'color': request.form['color'],
                'estado': 1,
                'localizacionEncontrado':  request.form['localizacionEncontrado'],
                'foto': request.form[foto]
            },
            'persona':{
                'documento': request.form['documentoPersona'],
                'nombre': request.form['nombrePersona'],
                'telefono': request.form['telefonoPersona'],
            },
            'registro':{
                'fecha': request.form['fecha'],
                'usuario': request.form['usuario'],
                'accion' : 'ingreso'
            }
        }
    return render_template('nuevoObjeto.html')

@app.route('/buscarObjetos', methods=['POST', 'GET'])
def buscarObjetos():
    if request.method == 'POST':
        print("Se va a buscar un objeto")
    return render_template('buscarObjetos.html')

@app.route('/login')
def login():
    return 'login'


if __name__ == "__main__":
    app.run(port = 3000, debug=True)