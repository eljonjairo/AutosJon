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

    return ResultsDF['Tipo'][0]

# Colocar otroas funciones para hacer más pequeño SQLModule 
