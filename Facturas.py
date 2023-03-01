import pandas as pd
import SQLModule as sql

class Factura():
    def __init__(self,idempleado,idcliente,idauto,preciounitario,cantidad,fecha,valortotal):
        self.Id = None
        self.idEmpleado = idempleado
        self.idCliente = idcliente
        self.idAuto = idauto
        self.precioUnitario = preciounitario
        self.Cantidad = cantidad
        self.Fecha = fecha
        self.valorTotal = valortotal
       
    def __str__(self):
        return ' Factura--> id: ' + str(self.Id) + ' idEmpleado: ' + self.idEmpleado + ' idCliente: ' + str(self.idCliente) + ' idAuto: ' + self.idAuto + ' precioUnitario: ' + self.precioUnitario +  ' Cantidad: ' + self.Cantidad + ' Fecha: ' + self.Fecha + ' valorTotal: ' + self.valorTotal

def ListarFacturas(connection):
    sql.writeDebug("    Facturas ListarFacturas IN")
    query = f''' SELECT * from Facturas; '''
    sql.writeDebug("    query:" + query)

    Results = sql.ReadQuery(connection, query)
    columns = ['ID','idEmpleado','idCliente', 'idAuto', 'precioUnitario', 'Cantidad', 'Fecha', 'valorTotal' ]
    ResultsDF = pd.DataFrame(Results,columns=columns)

    sql.writeDebug("    " + str(ResultsDF))
    sql.writeDebug("    Facturas ListarFacturas OUT")

    return ResultsDF

def InsertarFactura(connection,factura):
    sql.writeDebug("    Facturas InsertarFactura IN")
    query = f''' INSERT INTO Facturas ( 'idEmpleado','idCliente', 'idAuto', 'precioUnitario', 
                'Cantidad', 'Fecha', 'valorTotal' ) VALUE 
                 ( {factura.idEmpleado}, {factura.idCliente}, {factura.idAuto}, 
                   {factura.precioUnitario}, {factura.Cantidad}, \'{factura.Fecha}\',
                   {factura.valorTotal}  ); '''

    sql.writeDebug("    query:" + query)

    sql.ExecuteQuery(connection, query)
    sql.writeDebug("    Facturas InsertarFactura OUT")

# Colocar otroas funciones para hacer más pequeño SQLModule 
