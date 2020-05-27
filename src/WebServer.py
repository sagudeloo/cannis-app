from flask import Flask, render_template, request
import datetime
from DBServices import MysqlDBManager

#Instancia de flask
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'pi1-eafit-db-fperezm1.mysql.database.azure.com'
app.config['MYSQL_USER'] = 'fperezm1@pi1-eafit-db-fperezm1'
app.config['MYSQL_PASSWORD'] = 'wxtIQN54'
app.config['MYSQL_DB'] = 'cannis-db'
database = MysqlDBManager(app)

#Ruta inicial de la aplicacion
@app.route('/')
def index():
    return render_template('index.html')

#Ruta para annadir un nuevo objeto
@app.route('/anadirObjeto', methods=['POST', 'GET'])
def anadirObjeto():
    if request.method == 'POST':
        print(request.form, 'eureca')
        dataObject={
            'diaEncontrado': request.form['diaEncontrado'].replace('T',' '),
            'color': request.form['color'],
            'estado': 1,
            'localizacionEncontrado':  request.form['ubicacion'],
            'foto': request.form['foto'],
            'descripcion': request.form['descripcion']
        }
        secularData = {
            'persona':{
                'documento': request.form['documento'],
                'nombre': request.form['llevado'],
                'telefono': request.form['telefono'],
            }, 'registro':{
                'fecha': f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",
                'usuario': '127001',
                'persona': request.form['documento'],
                'accion' : 'ingreso'
            }
        }
        database.add(dataObject, secularData)
    return render_template('nuevoObjeto.html')

#Ruta para realizar la busqueda de objetos
@app.route('/buscarObjeto', methods=['POST', 'GET'])
def buscarObjetos():
    if request.method == 'POST':
        print(request.form)
        tableName='objetos'
        
    return render_template('buscarObjetos.html')

""" @app.route('/login')
def login():
    return 'login' """
