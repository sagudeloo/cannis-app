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
            self.__getTablesColumns()
            print(self.tables)
        command = getQueryCommand(selectionVars,tableName)
        data = ()
        try:
            cursor = self.mysql.connection.cursor()
            cursor.execute(command)
            dbReturn = cursor.fetchall()
            data = self.__fillQueryResponse(dbReturn,tableName)
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
        names = {}
        try:
            cursor = self.mysql.connection.cursor()
            print(self.mysql.app.config['MYSQL_DB'])
            cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{self.mysql.app.config['MYSQL_DB']}';")
            self.mysql.connection.commit()
            for varName in cursor.fetchall():
                names[varName[0]] = 0
            print(names)
        except Exception as e:
            print(e)
            print('Aca')
        
        return names
    
    def __getTablesColumns(self):

        columnDict = {}
        try:
            for table in self.tables:
                cursor = self.mysql.connection.cursor()
                cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{table}' order by ORDINAL_POSITION ASC;")
                self.mysql.connection.commit()
                for colName in cursor.fetchall():
                    columnDict[colName[0]] = 0
                self.tables[table] = columnDict
                columnDict = {}
        except Exception:
            print('Columnas',e)

    def __fillQueryResponse(self,data,tableName):
        
        print('DATA HERE')
        print(data)
        respList = []
        regDict = self.tables[tableName]
        colNames = list(regDict.keys())
        for numRegisters in range(len(data)):
            for valuePos in range(len(data[0])):
                value = data[numRegisters][valuePos]
                regDict[colNames[valuePos]] = value
            respList.append(regDict)

        return respList
