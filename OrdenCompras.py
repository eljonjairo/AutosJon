import pandas as pd
import SQLModule as sql

class OrdenCompra():
    def __init__(self,idempleado,idauto,cantidad,preciocompra,fechaorden,fechaentrega):
        self.Id = None
        self.idEmpleado = idempleado
        self.idAuto = idauto
        self.Cantidad = cantidad
        self.precioCompra = preciocompra
        self.fechaOrden = fechaorden
        self.fechaEntrega = fechaentrega
       
    def __str__(self):
        return ' OrdenCompra--> id: ' + str(self.Id) + ' idEmpleado: ' + self.idEmpleado 
        + ' idAuto: ' + str(self.idAuto) + ' Cantidad: ' + self.Cantidad + ' precioCompra: ' 
        + self.precioCompra + ' fechaOrden: ' + self.fechaOrden + ' fechaEntrega: ' + self.fechaEntrega 
    
def ListarOrdenCompras(connection):
    sql.writeDebug("    OrdenCompras ListarOrdenCompras IN")
    query = f''' SELECT * from OrdenCompras; '''
    sql.writeDebug("    query:" + query)

    Results = sql.ReadQuery(connection, query)
    columns = ['ID','idEmpleado','idAuto','Cantidad','precioCompra','fechaOrden','fechaEntrega']
    ResultsDF = pd.DataFrame(Results,columns=columns)

    sql.writeDebug("    " + str(ResultsDF))
    sql.writeDebug("    OrdenCompras ListarOrdenCompras OUT")

    return ResultsDF

def InsertarOrdenCompras(connection,orden):
    sql.writeDebug("    OrdenCompras InsertarOrdenCompras IN")
    query = f''' INSERT INTO OrdenCompras ( IDEmpleado, IDAuto, Cantidad, PrecioCompra, 
                 FechaOrden, FechaEntrega ) VALUES 
                 ( {orden.idEmpleado}, {orden.idAuto}, {orden.Cantidad}, {orden.precioCompra},
                   {orden.fechaOrden},{orden.fechaEntrega} );    '''

    sql.writeDebug("    query:" + query)

    sql.ExecuteReadQuery(connection, query)

    sql.writeDebug("    OrdenCompras InsertarOrdenCompras OUT")

def InsertarOrdenCompra(connection,ordencompra):
    sql.writeDebug("    OrdenCompras InsertarOrdenCompra IN")
    query = f''' INSERT INTO OrdenCompras ( 'idEmpleado', 'idAuto', 'Cantidad', 'FechaOrden',
                                             'FechaEntrega' ) VALUE 
                 ( {ordencompra.idEmpleado}, {ordencompra.idAuto}, {ordencompra.Cantidad}, 
                    \'{ordencompra.FechaOrden}\',\'{ordencompra.FechaEntrega}\'  ); '''

    sql.writeDebug("    query:" + query)
    
    sql.ExecuteQuery(connection, query)
    sql.writeDebug("    OrdenCompras InsertarOrdenCompra OUT")




# Colocar otroas funciones para hacer más pequeño SQLModule 
