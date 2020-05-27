
import abc
from flask_mysqldb import MySQL
from CommonDBTools import *

'''
Interface for the insertion classes.
'''
class Inserter(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def insert():
        pass


'''
Class which handles the object insertion into the database
'''
class ObjectInserter(Inserter):
    def __init__(self,objData,secularData,database):
        self.objectData = objData
        self.secularData = secularData
        self.registerData = secularData['registro']
        self.database = database

    def insert(self):

        variables = tuple(self.objectData.values())
        isUser = self.__existsUser(self.registerData['usuario'])
        if(len(isUser)):

            existsPerson = existInTable(self.registerData['persona'],'personas',self.database)
            print('Exists Person')
            print(existsPerson)
            print(self.registerData['persona'])

            if('persona' in self.secularData.keys() and  not existsPerson):
                personInserter = PersonInserter(self.secularData['persona'],self.database)
                print('About to create a person')
                personInserter.insert()

            try:
                cursor = self.database.connection.cursor()
                cursor.execute("INSERT INTO objetos (diaEncontrado,color,estado,localizacionEncontrado,foto,descripcion) VALUES (%s,%s,%s,%s,%s,%s)",variables)
                self.database.connection.commit()
                self.registerData['objeto'] = getIdObject(self.database)
                self.createRegister()
                return 1
            except Exception as e:
                print(e)
                return 0

    def __existsUser(self,userDoc):
        cursor = self.database.connection.cursor()
        cursor.execute(f"SELECT IF(EXISTS(SELECT * FROM usuarios WHERE documento={userDoc}),1,0)")
        #cur.execute(f"CALL userExists({userDoc})")
        self.database.connection.commit()
        data = cursor.fetchall()
        print(type(data))
        print(data)
        return data

    def createRegister(self):

        variables = tuple(self.registerData.values())
        print(variables)
        try:
            cursor = self.database.connection.cursor()
            cursor.execute("INSERT INTO registros (fecha,usuario,persona,accion,objeto) VALUES (%s,%s,%s,%s,%s);",variables)
            self.database.connection.commit()
            return 1
        except Exception as e:
            print(e,'fuck')
            return 0


'''
Class which handles the person insertion into the database
'''
class PersonInserter(Inserter):

    def __init__(self,personData,database):
        self.personData = personData
        self.database = database
    
    def insert(self):
        #variables = (data['documento'],data['nombre'],data['telefono'])
        variables = tuple(self.personData.values())
        cursor = self.database.connection.cursor()
        try:

            cursor.execute("INSERT INTO personas (documento,nombre,telefono) VALUES (%s,%s,%s)",variables)
            self.database.connection.commit()
            print('Person Inserted')
            return 1
        except Exception as e:
            print(e)
            return 0

'''
Class which handles the user insertion into the database
'''

class UserInserter(Inserter):

    def __init__(self,dataUser,database):
        self.dataUser = dataUser
        self.database = database
    
    def insert(self):
        variables = tuple(self.userData.values())
        cursor = self.database.connection.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (documento,email,clave) VALUES (%s,%s,%s)",variables)
            self.database.connection.commit()
            return 1
        except Exception as e:
            print(e)
            return 0

    def __existsPerson(self,personDoc):
        cur = self.database.connection.cursor()
        cur.execute(f"SELECT IF(EXISTS(SELECT * FROM personas WHERE documento={personDoc}),1,0)")
        #cur.execute(f"CALL userExists({userDoc})")
        self.database.connection.commit()
        data = cur.fetchall()
        print(type(data))
        print(data)
        return data


class InserterFactory():

    @staticmethod
    def getInserter(entityData = {},secularData = {}, database = ''):

        if(len(secularData) != 0):
            return ObjectInserter(entityData,secularData,database)
        elif('clave' in entityData.keys()):
            return UserInserter(entityData,database)
        else:
            return PersonInserter(entityData,database)

