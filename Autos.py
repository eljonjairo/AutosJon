import pandas as pd
import SQLModule as sql

class Auto():
    def __init__(self,marca,linea,modelo):
        self.Id = None
        self.Marca = marca
        self.Linea = linea
        self.Modelo = modelo
       
    def __str__(self):
        return ' Auto--> id: ' + str(self.Id) + ' Marca: ' + self.Marca + ' Linea: ' + str(self.Linea) + ' Modelo: ' + self.Modelo

def ListarAutos(connection):
    sql.writeDebug("    Autos ListarAutos IN")
    query = f''' SELECT * from Autos; '''
    sql.writeDebug("    query:" + query)

    Results = sql.ReadQuery(connection, query)
    columns = ['ID','Marca','Linea', 'Modelo']
    ResultsDF = pd.DataFrame(Results,columns=columns)

    sql.writeDebug("    " + str(ResultsDF))
    sql.writeDebug("    Autos ListarAutos OUT")

    return ResultsDF

def InsertarAuto(connection,auto):
    sql.writeDebug("    Autos InsertarAuto IN")
    query = f''' INSERT INTO Autos ( Marca, Linea, Modelo ) VALUE 
                 ( \'{auto.Marca}\', \'{auto.Linea}\', \'{auto.Modelo}\' ); '''

    sql.writeDebug("    query:" + query)

    sql.ExecuteQuery(connection, query)
    sql.writeDebug("    Autos InsertarAuto OUT")

# Colocar otroas funciones para hacer más pequeño SQLModule 
