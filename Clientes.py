import pandas as pd
import SQLModule as sql

class Cliente():
    def __init__(self,nombre,cedula,clave):
        self.Id = None
        self.Nombre = nombre
        self.Cedula = cedula
        self.Clave = clave
       
    def __str__(self):
        return ' Cliente--> id: ' + str(self.Id) + ' Nombre: ' + self.Nombre + ' Cedula: ' + str(self.Cedula) + ' Clave: ' + self.Clave 

def ListarClientes(connection):
    sql.writeDebug("    Clientes ListarClientes IN")
    query = f''' SELECT * from Clientes; '''
    sql.writeDebug("    query:" + query)

    Results = sql.ReadQuery(connection, query)
    columns = ['ID','Nombre','Cedula', 'Clave']
    ResultsDF = pd.DataFrame(Results,columns=columns)

    sql.writeDebug("    " + str(ResultsDF))
    sql.writeDebug("    Clientes ListarClientes OUT")

    return ResultsDF

def InsertarCliente(connection,cliente):
    sql.writeDebug("    Clientes InsertarCliente IN")
    query = f''' INSERT INTO Clientes ( 'Nombre','Cedula', 'Clave' ) VALUE 
                 ( \'{cliente.Nombre}\', {cliente.Cedula}, \'{cliente.Clave}\' ); '''

    sql.writeDebug("    query:" + query)

    sql.ExecuteQuery(connection, query)
    sql.writeDebug("    Clientes InsertarCliente OUT")




# Colocar otroas funciones para hacer más pequeño SQLModule 
