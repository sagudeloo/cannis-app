from flask import Flask, render_template, request

#Instancia de flask
app = Flask(__name__)

#Ruta inicial de la aplicacion
@app.route('/')
def index():
    return render_template('index.html')

#Ruta para annadir un nuevo objeto
@app.route('/anadirObjeto', methods=['POST', 'GET'])
def anadirObjeto():
    if request.method == 'POST':
        print(request.form)
        """ data={
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
        print(data) """
    return render_template('nuevoObjeto.html')

#Ruta para realizar la busqueda de objetos
@app.route('/buscarObjetos', methods=['POST', 'GET'])
def buscarObjetos():
    if request.method == 'POST':
        print(request.form)
        print("Se va a buscar un objeto")
    return render_template('buscarObjetos.html')

""" @app.route('/login')
def login():
    return 'login' """
