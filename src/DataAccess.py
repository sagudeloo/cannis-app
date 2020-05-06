import DatabaseConnection

#Capa de acceso a datos
class DataAccess:

    def __init__(self, app):
        db = DatabaseConnection(app)
        self.mysql = db.mysql
    
    def addObjeto(self, data):

