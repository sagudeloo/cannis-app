
from flask_mysqldb import MySQL

def existInTable(userDoc,tableName,database):
        cursor = database.connection.cursor()
        cursor.execute(f"SELECT IF(EXISTS(SELECT * FROM {tableName} WHERE documento={userDoc}),1,0)")
        #cur.execute(f"CALL userExists({userDoc})")
        database.connection.commit()
        data = cursor.fetchone()
        print(type(data))
        print(data)
        return data[0]

def getVar(tableName,varName,doc):

    cursor = database.connection.cursor()
    cursor.execute(f"SELECT {varName} FROM {tableName} WHERE documento={doc}")
    #cur.execute(f"CALL userExists({userDoc})")
    database.connection.commit()
    data = cursor.fetchone()
    print(type(data))
    print(data)
    return data[0]


def getUpdateCommand(table,updateVars,searchVar):
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

def getIdObject(database):
        cursor = database.connection.cursor()
        cursor.execute(f"SELECT MAX(idObjeto) FROM objetos;")
        #cur.execute(f"CALL userExists({userDoc})")
        database.connection.commit()
        data = cursor.fetchone()
        print(type(data))
        print(data)
        return data[0]

def getQueryCommand(selectionVars,tableName):

    command = f"SELECT * FROM {tableName} WHERE "
    varNames = list(selectionVars.keys())
    numVars = len(varNames)
    print(varNames,numVars)

    for i in range(numVars):
        nameColumn = varNames[i]
        columnValue = selectionVars[nameColumn]

        if(numVars==1 or i==numVars-1):
            if(isinstance(columnValue,str)):
                command+=f"{nameColumn} LIKE '{columnValue}%' "
            else:
                command+=f"{nameColumn}={columnValue} "

        elif(numVars>1 and i<numVars-1):
            if(isinstance(columnValue,str)):
                command+=f"{nameColumn} LIKE '{columnValue}%' and "
            else:
                command+=f"{nameColumn}={columnValue} and "
    
    print('THE COMMAND')
    print(command)
    return command

#def transformDBResponse(responseTuple):
if __name__ == "__main__":
    #print(getQueryCommand({'documento':1037,'nombre':'Pedro'},'personas'))
    print(getQueryCommand({'datetime':23},'personas'))
    pass


