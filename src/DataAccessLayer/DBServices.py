import abc
from flask_mysqldb import MySQL
import datetime
import time
from Insertion import *
from CommonDBTools import *


class dbManager(abc.ABC):
    @abc.abstractmethod
    def add(self,dataObject={},secularData={}):
        pass
    @abc.abstractmethod
    def delete_person(self,personDoc):
        pass
    @abc.abstractmethod
    def delete_user(self,userDoc):
        pass
    @abc.abstractmethod
    def query(self,tableName,selectionVars):
        pass
    @abc.abstractmethod
    def update():
        pass

class MysqlDBManager(dbManager):
    def __init__(self,app):
        self.mysql = MySQL(app)
        self.tables = {}



    def add(self,dataObject={},secularData={}):

        insertSuccess = 0
        if(len(dataObject)!=0):
            inserter = InserterFactory().getInserter(dataObject,secularData,self.mysql)
            if(isinstance(inserter,Inserter)):
                inserter.insert()
                insertSuccess = 1
        
        return insertSuccess
            
    
    
    def delete_person(self,personDoc):
        try:
            cursor = self.mysql.connection.cursor()
            cur.execute(f"DELETE FROM personas WHERE id={personDoc}")
            self.mysql.connection.commit()
        except Exception:
            return 0

        return 1

    def delete_user(self,userDoc):
        try:
            cursor = self.mysql.connection.cursor()
            cur.execute(f"DELETE FROM usuarios WHERE id={userDoc}")
            self.mysql.connection.commit()
        except Exception:
            return 0

        return 1

    def query(self,tableName,selectionVars):

        if(len(self.tables)==0):
            self.tables = self.__getTablesNames()
        command = getQueryCommand(selectionVars,tableName)
        data = ()
        try:
            cursor = self.mysql.connection.cursor()
            cursor.execute(command)
            data = cursor.fetchall()
        except Exception as e:
            print(e)
        return data
    
    def update(self,tabla,updVars,searchVar):
        respCode = 0
        cursor = self.mysql.connection.cursor()
        commad = self.__getUpdateCommand()
        try:
            cursor.execute(command)
            self.mysql.connection.commit()
            respCode=1
        except Exception as e:
            print(e)
        
        return respCode

    
    def __getUpdateCommand(self,table,updVars,searchVar):
        commaCounter = 0
        command = f"UPDATE {table} SET "
        for i in data:
            if(commaCounter<len(updVars)-1):
                command+=f"{data[0]}={data[1]}, "
            else:
                command+=f"{data[0]}={data[1]} "
        
        if(len(searchVar)!=0):
            command+=f"WHERE {searchVar[0]}={searchVar[1]}"
        
        return command
    
    def __getTablesNames(self):
        names = ()
        try:
            cursor = self.mysql.connection.cursor()
            print(self.mysql.app.config['MYSQL_DB'])
            cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{self.mysql.app.config['MYSQL_DB']}';")
            self.mysql.connection.commit()
            names = cursor.fetchall()
            print(names)
        except Exception as e:
            print(e)
            print('Aca')
        
        return names

