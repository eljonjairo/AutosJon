import pandas as pd
import SQLModule as sql

class Inventario():
    def __init__(self,idempleado,idauto,cantidad,fecha):
        self.Id = None
        self.idEmpleado = idempleado
        self.idAuto = idauto
        self.Cantidad = cantidad
        self.Fecha = fecha
       
    def __str__(self):
        return ' Inventario--> id: ' + str(self.Id) + ' idEmpleado: ' + self.idEmpleado + ' idAuto: ' + str(self.idAuto) + ' Cantidad: ' + self.Cantidad + ' Fecha: ' + self.Fecha

def ListarInventarios(connection):
    sql.writeDebug("    Inventarios ListarInventarios IN")
    query = f''' SELECT * from Inventarios; '''
    sql.writeDebug("    query:" + query)

    Results = sql.ReadQuery(connection, query)
    columns = ['ID','idEmpleado','idAuto', 'Cantidad', 'Fecha']
    ResultsDF = pd.DataFrame(Results,columns=columns)

    sql.writeDebug("    " + str(ResultsDF))
    sql.writeDebug("    Inventarios ListarInventarios OUT")

    return ResultsDF

def InsertarInventario(connection,inventario):
    sql.writeDebug("    Inventarios InsertarInventario IN")
    query = f''' INSERT INTO Inventarios ( 'idEmpleado', 'idAuto', 'Cantidad', 'Fecha' ) VALUE 
               ( {factura.idEmpleado}, {factura.idAuto}, {factura.Cantidad}, \'{factura.Fecha}\' );'''

    sql.writeDebug("    query:" + query)
    
    sql.ExecuteQuery(connection, query)
    sql.writeDebug("    Inventarios InsertarInventario OUT")

# Colocar otroas funciones para hacer más pequeño SQLModule 
