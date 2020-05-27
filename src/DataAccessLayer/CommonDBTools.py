
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
                command+=f"{nameColumn} LIKE \"{columnValue}%\""
            else:
                command+=f"{nameColumn}={columnValue}"

        elif(numVars>1 and i<numVars-1):
            if(isinstance(columnValue,str)):
                command+=f"{nameColumn} LIKE \"{columnValue}%\""
            else:
                command+=f"{nameColumn}={columnValue} and "
    
    return command

#def transformDBResponse(responseTuple):
if __name__ == "__main__":
    #print(getQueryCommand({'documento':1037,'nombre':'Pedro'},'personas'))
    print(getQueryCommand({'datetime':23},'personas'))
    pass


