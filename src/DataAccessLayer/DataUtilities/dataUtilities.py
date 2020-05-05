import abc
from flask_mysqldb import MySQL



class dbManager(abc.ABC):
    @abc.abstractmethod
    def insert_object(self,id,foundedDay,color,state,location,photo,descr):
        pass
    @abc.abstractmethod
    def insert_person(self,doc,name,phoneNum):
        pass
    @abc.abstractmethod
    def insert_user(self,doc,email,password):
        pass
    @abc.abstractmethod
    def delete_person(self,doc):
        pass
    @abc.abstractmethod
    def delete_user(self,doc):
        pass
    @abc.abstractmethod
    def query_object(self,id,varsToGet,varsToSearch):
        pass
    @abc.abstractmethod
    def query_person(self,varsToGet,varsToSearch):
        pass
    @abc.abstractmethod
    def query_register(self,varsToGet,varsToSearch):
        pass
    @abc.abstractmethod
    def update_object():
        pass

class mysqlDBManager(dbManager):
    def __init__(self,app):
        self.mysql = MySQL(app)
        print('done----------------------')


    def insert_object(self,ide,foundedDay,color,state,location,photo,descr):

        variables = (ide,foundedDay,color,state,location,photo,descr)
        cursor = self.mysql.connection.cursor()
        try:
            cursor.execute("INSERT INTO objetos (id,diaEncontrado,color,estado,localizacionEncontrado,foto,descripcion) VALUES (%s,%s,%s,%s,%s,%s,%s)",variables)
            self.mysql.connection.commit()
            return 1
        except Exception as e:
            print(e)
            return 0

    def insert_person(self,doc,name,phoneNum):
        variables = (doc,name,phoneNum)
        cursor = self.mysql.connection.cursor()
        try:

            cursor.execute("INSERT INTO personas (documento,nombre,telefono) VALUES (%s,%s,%s)",variables)
            self.mysql.connection.commit()
            return 1
        except Exception as e:
            print(e)
            return 0

    def insert_user(self,doc,email,password):
        variables = (doc,email,password)
        cursor = self.mysql.connection.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (documento,email,clave) VALUES (%s,%s,%s)",variables)
            self.mysql.connection.commit()
            return 1
        except Exception:
            return 0
    
    def insert_registro(self,idReg,date,user,person,action,objectId):
        variables = (idReg,date,user,person,action,objectId)
        cursor = self.mysql.connection.cursor()
        try:
            cursor.execute("INSERT INTO registro (idRegistro,fecha,usuario,persona,accion,objeto) VALUES (%s,%s,%s,%s,%s,%s)",variables)
            mysql.connection.commit()
            return 1
        except Exception:
            return 0
    
    
    def delete_person(self,doc):
        try:
            cursor = self.mysql.connection.cursor()
            cur.execute(f"DELETE FROM personas WHERE id={doc}")
            self.mysql.connection.commit()
        except Exception:
            return 0

        return 1

    def delete_user(self,doc):
        try:
            cursor = self.mysql.connection.cursor()
            cur.execute(f"DELETE FROM usuarios WHERE id={doc}")
            self.mysql.connection.commit()
        except Exception:
            return 0

        return 1

    def query_object(self,varsToGet,varsToSearch):
        cursor = self.mysql.connection.cursor()
        data = ()
        try:
            command = self.get_query_command('objetos',varsToGet,varsToSearch)
            cursor.execute(command)
            data = cursor.fetchall()
        except Exception as e:
            print(e)
        return data

    def query_person(self,varsToGet,varsToSearch):
        cursor = self.mysql.connection.cursor()
        data = ()
        try:
            command = self.get_query_command('personas',varsToGet,varsToSearch)
            cursor.execute(command)
            data = cursor.fetchall()
        except Exception as e:
            print(e)
        return data
    
    def query_register(self,varsToGet,varsToSearch):
        cursor = self.mysql.connection.cursor()
        data = ()
        try:
            command = self.get_query_command('registros',varsToGet,varsToSearch)
            cursor.execute(command)
            data = cursor.fetchall()
        except Exception as e:
            print(e)
        return data
    
    def update_object(self,objectId):
        print('Yes')

    def get_query_command(self,table,varsToGet,varsToSearch):
        command = ''
        commaCount = 0
        if(len(varsToGet)==0):
            command=f"SELECT * FROM {table}"
        else:
            command = 'SELECT '
            for i in varsToGet:
                if(commaCount<len(varsToGet)-1):
                    command+=f"{i}, "
                else:
                    command+=f"{i} "
                commaCount+=1
            command+=f"FROM {table} WHERE "
            for i in varsToSearch:
                command+=f"{i[0]}={i[1]} "
        print(command)
        return command


