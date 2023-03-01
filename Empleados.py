import pandas as pd
import SQLModule as sql

class Empleado():
    def __init__(self,nombre,cedula,clave,tipo):
        self.Id = None
        self.Nombre = nombre
        self.Cedula = cedula
        self.Clave = clave
        self.Tipo = tipo
       
    def __str__(self):
        return ' Empleado--> id: ' + str(self.Id) + ' Nombre: ' + self.Nombre + ' Cedula: ' + str(self.Cedula) + ' Clave: ' + self.Clave + ' Tipo: ' + self.Tipo

def isEmpleado(empleado,connection):
    sql.writeDebug("    Empleados isEmpleado IN")

    query = f''' SELECT * from Empleados 
                 WHERE Nombre = \'{empleado.Nombre}\' AND Cedula = {empleado.Cedula} AND Clave = \'{empleado.Clave}\' ; '''
    sql.writeDebug("    query:" + query)

    Results = sql.ReadQuery(connection, query)
    columns = ['id','Nombre','Cedula','Clave','Tipo']
    ResultsDF = pd.DataFrame(Results,columns=columns)    

    sql.writeDebug("    " + str(ResultsDF))
    sql.writeDebug("    Empleados isEmpleado OUT")

    empleado.Tipo = ResultsDF['Tipo'][0]

    return empleado

def ListarEmpleados(connection):
    sql.writeDebug("    Empleados ListarEmpleados IN")
    query = f''' SELECT * from Empleados; '''
    sql.writeDebug("    query:" + query)

    Results = sql.ReadQuery(connection, query)
    columns = ['ID','Nombre','Cedula', 'Clave', 'Tipo']
    ResultsDF = pd.DataFrame(Results,columns=columns)

    sql.writeDebug("    " + str(ResultsDF))
    sql.writeDebug("    Empleados ListarEmpleados OUT")

    return ResultsDF

def InsertarEmpleado(connection,empleado):
    sql.writeDebug("    Empleados InsertarEmpleado IN")
    query = f''' INSERT INTO Empleados ( 'Nombre','Cedula','Clave','Tipo' ) VALUE 
                 ( \'{empleado.Nombre}\', {empleado.Cedula}, \'{empleado.Clave}\', \'{empleado.Tipo}\' ); '''


    sql.writeDebug("    query:" + query)

    sql.ExecuteQuery(connection, query)
    sql.writeDebug("    Empleados InsertarEmpleado OUT")




# Colocar otroas funciones para hacer más pequeño SQLModule 
