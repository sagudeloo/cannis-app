
import abc
from flask_mysqldb import MySQL
from CommonDBTools import *


class Searcher(abc.ABCMeta):
    @abc.abstractclassmethod
    def search():
        pass

class UserSeacher(Searcher):
    def __init__(self,selectionVars,database):
        self.database = database
        self.selectionVars = selectionVars

    def search():
        command = getQueryCommand(self.selectionVars,'usuarios')
        userData = ()
        try:
            cursor = self.mysql.connection.cursor()
            cursor.execute(command)
            userData = cursor.fetchall()
        except Exception as e:
            print(e)
        return userData
