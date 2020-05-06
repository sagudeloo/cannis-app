from flask_mysqldb import MySQL

#Coneccion de la instancia de flask con la base de datos
class DatabaseConnection:

    def __init__(self, app):
        app.config['MYSQL_HOST'] = '127.0.0.1'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = 'password'
        app.config['MYSQL_DB'] = 'cannis-db'
        self.mysql = MySQL(app)