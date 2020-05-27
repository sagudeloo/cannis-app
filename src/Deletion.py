
import abc
from flask_mysqldb import MySQL
import CommonDBTools as dbTools

class Deleter(abc.ABCMeta):

    @abc.abstractclassmethod
    def delete():
        pass

class UserDeleter(Deleter):

    def __init__(self,document,mysql):
        self.document = document
        self.mysql = mysql
    
    def delete(self):

        success = 0
        if(dbTools.existInTable(self.document,'usuarios',self.mysql)):
            try:
                cursor = self.mysql.connection.cursor()
                cur.execute(f"DELETE FROM usuarios WHERE id={personDoc}")
                self.mysql.connection.commit()
                success = 1
            except Exception:
                success=0

        return success

class PersonDeleter(Deleter):

    def __init__(self,document,mysql):
        self.document = document
        self.mysql = mysql
    
    def delete(self):

        success = 0
        if(dbTools.existInTable(self.document,'personas',self.mysql)):
            try:
                cursor = self.mysql.connection.cursor()
                cur.execute(f"DELETE FROM usuarios WHERE id={personDoc}")
                self.mysql.connection.commit()
                success = 1
            except Exception:
                success=0
        return success

class DeletionFactory():

    @staticmethod
    def getDeleter():



