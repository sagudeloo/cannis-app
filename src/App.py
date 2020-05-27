from flask import Flask,request,render_template,redirect,url_for
from flask_mysqldb import MySQL
from DBServices import MysqlDBManager
import datetime

app = Flask(__name__)
'''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'zeus123*'
app.config['MYSQL_DB'] = 'cannis-db'
'''

app.config['MYSQL_HOST'] = 'pi1-eafit-db-fperezm1.mysql.database.azure.com'
app.config['MYSQL_USER'] = 'fperezm1@pi1-eafit-db-fperezm1'
app.config['MYSQL_PASSWORD'] = 'wxtIQN54'
app.config['MYSQL_DB'] = 'cannis-db'
mysql = MysqlDBManager(app)
#db = data(app)

@app.route('/')
def Index():
    return  render_template('index.html')

@app.route('/add_object', methods = ['POST'])
def add():

    if(request.method == 'POST'):
        fullname =request.form['fullname']
        phone =request.form['phone']
        email =request.form['email']
        #data = mysql.insert_person(doc=email,name=fullname,phoneNum=phone)
        #data2 = mysql.insert_object('2020-04-04 22:03','blue',1,'casa','fvfgfbrb','lindo')
        dataPerson = {'documento':14593,'nombre':'James','telefono':75737271}
        dataRegister = {'fecha':f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",'usuario':1037,'persona':14593,'accion':'ingreso','objeto':1}
        secularData = {'persona':dataPerson,'registro':dataRegister}
        dataUser = {'documento':1037,'email':'Pedropapa','clave':'Yeahhh'}
        dataObject = {'diaEncontrado': f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}",'color':'Azul','estado':1,'localizacionEncontrado':'Bloque 19','foto':'sfd','descripcion':'Bonito'}
        #resp = mysql.add(dataObject=dataUser,secularData={})
        selectionVars = {'localizacionEncontrado':'andson','diaEncontrado':"2019"} 
        resp = mysql.query('objetos',selectionVars)
        print(type(resp))
        print(resp)
    return redirect(url_for('Index'))

if __name__=='__main__':
    print(type(app))
    app.run(port=3000, debug = True)


#@app.route('/delete_object')
#def delete_obj():
#    #