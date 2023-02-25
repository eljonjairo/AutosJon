
import mysql.connector
from mysql.connector import Error
import pandas as pd

def startDebug():
    msg = ''' 
    *******************************************
    *          Starting Debug File            *
    ******************************************* 
    '''
    with open("Debug.out", "w") as f:
        f.write(msg)

def writeDebug(msg):
    with open("Debug.out", "a") as f:
        f.write("\n")    
        f.write(msg)
        f.write("\n")    

def DBConnect():
    print()
    print( " DataBase Connection " )
    print()
    writeDebug("    SQLModule DBConnect IN ")
    conexion = None
    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            user = "Jon",
            passwd = "$Yes1k1na$",
            database = "JonAutos"
        )
        writeDebug("    MySQL Database connection successful")
    except Error as err:
        msg = f"Error in DBConnection: '{err}'"
        writeDebug(msgf)
  
    writeDebug("    SQLModule DBConnect OUT ")
    print(f' Connected to DataBase' )
    print()

    return conexion

def CreateDB(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error in CreateDB: '{err}'")

def ExecuteQuery(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print()
        print(f"Error in ExecuteQuery: '{err}'")
        print()
        print(query)
        print()

def ReadQuery(connection, query):
    cursor = connection.cursor()
    # Create a list to save output results
    Results = []
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            result = list(result)
            Results.append(result)
        print("Read Query successful")
    #ClientesDF = pd.DataFrame(clientes,columns=columns)

    except Error as err:
        print()
        print(f"Error in ReadQuery: '{err}'")
        print()
        print(query)
        print()
    return Results

#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Drop Tables               +
#  +++++++++++++++++++++++++++++++++++++++++++
def DropTables(connection):
    ExecuteQuery(connection, DropFacturas)
    ExecuteQuery(connection, DropOrdenCompras)
    ExecuteQuery(connection, DropInventarios)
    ExecuteQuery(connection, DropClientes)
    ExecuteQuery(connection, DropEmpleados)
    ExecuteQuery(connection, DropAutos)
    


#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Create Tables               +
#  +++++++++++++++++++++++++++++++++++++++++++
  
def CreateTables(connection):
    ExecuteQuery(connection, CreateAutos)
    ExecuteQuery(connection, CreateEmpleados)
    ExecuteQuery(connection, CreateClientes)
    ExecuteQuery(connection, CreateInventarios)
    ExecuteQuery(connection, CreateOrdenCompras)
    ExecuteQuery(connection, CreateFacturas)


#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Data Into Tables               +
#  +++++++++++++++++++++++++++++++++++++++++++

def InsertData(connection):
    ExecuteQuery(connection, InsertAutos)
    ExecuteQuery(connection, InsertEmpleados)
    ExecuteQuery(connection, InsertClientes)
    ExecuteQuery(connection, InsertInventarios)
    ExecuteQuery(connection, InsertOrdenCompras)
    ExecuteQuery(connection, InsertFacturas)

# SQL Tables.

#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table Autos                 +
#  +++++++++++++++++++++++++++++++++++++++++++

DropAutos = ''' DROP TABLE Autos;  '''

CreateAutos = ''' CREATE TABLE Autos ( IDAuto INT AUTO_INCREMENT PRIMARY KEY,
                  Marca VARCHAR(15) NOT NULL, Linea VARCHAR(20) NOT NULL, 
                  Modelo INT NOT NULL );  '''

InsertAutos = ''' INSERT INTO Autos ( Marca, Linea, Modelo ) VALUES
                  ( 'Ford', 'Mustang', 2020 ),
                  ( 'Ford', 'Mustang', 2020 ),
                  ( 'Ford', 'Mustang', 2020 ),
                  ( 'Ford', 'Mustang', 2021 ),
                  ( 'Ford', 'Mustang', 2021 ),
                  ( 'Ford', 'Mustang', 2021 ),
                  ( 'Ford', 'Mustang', 2022 ),
                  ( 'Ford', 'Mustang', 2022 ),
                  ( 'Ford', 'Mustang', 2022 ),
                  ( 'Ford', 'Explorer', 2020 ),
                  ( 'Ford', 'Explorer', 2020 ),
                  ( 'Ford', 'Explorer', 2020 ),
                  ( 'Ford', 'Explorer', 2021 ),
                  ( 'Ford', 'Explorer', 2021 ),
                  ( 'Ford', 'Explorer', 2021 ),
                  ( 'Ford', 'Explorer', 2022 ),
                  ( 'Ford', 'Explorer', 2022 ),
                  ( 'Ford', 'Explorer', 2022 ),
                  ( 'Ford', 'Edge', 2020 ),
                  ( 'Ford', 'Edge', 2020 ),
                  ( 'Ford', 'Edge', 2020 ),
                  ( 'Ford', 'Edge', 2021 ),
                  ( 'Ford', 'Edge', 2021 ),
                  ( 'Ford', 'Edge', 2021 ),
                  ( 'Ford', 'Edge', 2022 ),
                  ( 'Ford', 'Edge', 2022 ),
                  ( 'Ford', 'Edge', 2022 ); '''

def ListarAutos(connection):
    query = f''' SELECT * from Autos; ''' 
    
    Results = ReadQuery(connection, query)
    columns = ['IDAuto','Marca','Linea','Modelo']
    ResultsDF = pd.DataFrame(Results,columns=columns)


    return ResultsDF

#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table Clientes              +
#  +++++++++++++++++++++++++++++++++++++++++++

DropClientes = ''' DROP TABLE Clientes;  '''

CreateClientes = ''' CREATE TABLE Clientes ( IDCliente INT AUTO_INCREMENT PRIMARY KEY,
                     Nombre VARCHAR(20) NOT NULL, Cedula VARCHAR(6) NOT NULL, 
                     Clave VARCHAR(10) NOT NULL );  '''

InsertClientes = ''' INSERT INTO Clientes ( Nombre, Cedula, Clave ) VALUES 
                     ( 'Andres', 8951, '21s45' ),
                     ( 'Miguel', 1524, '52sd4' ),
                     ( 'Jose', 8745, 'dd547' ),
                     ( 'Luisa', 9651, 'sqw54' ),
                     ( 'Alex', 2015, 'ret74' ),
                     ( 'Diego', 3054, '25ty1' ),
                     ( 'Rita', 7840, '5rte2' ),
                     ( 'Julio', 9201, '514sq' ); '''

def ListarClientes(connection):
    query = f''' SELECT * from Clientes; ''' 
    
    Results = ReadQuery(connection, query)

    clientes = []
    for result in Results:
        result = list(result)
        clientes.append(result)

    columns = ['IDCliente','Nombre','Cedula','Clave']
    ClientesDF = pd.DataFrame(clientes,columns=columns)

    return ClientesDF

#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table Empleados             +
#  +++++++++++++++++++++++++++++++++++++++++++

DropEmpleados= ''' DROP TABLE Empleados  '''

CreateEmpleados= ''' CREATE TABLE Empleados ( IDEmpleado INT AUTO_INCREMENT PRIMARY KEY,
                     Nombre VARCHAR(20) NOT NULL, Cedula VARCHAR(6) NOT NULL,
                     Clave VARCHAR(10) NOT NULL, Tipo VARCHAR(20) NOT NULL,
                     CHECK (Tipo IN('Administrador DB','Gerente','Vendedor')));  '''

InsertEmpleados= ''' INSERT INTO Empleados ( Nombre, Cedula, Clave, Tipo ) VALUES 
                     ( 'Jon',2306,'2300', 'Administrador DB'),
                     ( 'Jairo',2307,'2300', 'Gerente'),
                     ( 'Alejandra',7584,'2303', 'Gerente'),
                     ( 'Julian',2548,'2301', 'Gerente'),
                     ( 'Tito',1254,'2302', 'Gerente'),
                     ( 'Alicia',6589,'2304', 'Vendedor'),
                     ( 'Carlos',2215,'2305', 'Vendedor'),
                     ( 'Ana',7845,'2306', 'Vendedor'); '''

def AddEmpleado(nombre,cedula,idsucursal,clave,tipo,connection):
    pass 


def ListarEmpleados(connection):
    query = f''' SELECT * from Empleados; ''' 
    
    Results = ReadQuery(connection, query)
    columns = ['IDEmpleado','Nombre','Cedula', 'Clave', 'Tipo']
    ResultsDF = pd.DataFrame(Results,columns=columns)

    return ResultsDF

#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table Facturas               +
#  +++++++++++++++++++++++++++++++++++++++++++

DropFacturas = ''' DROP TABLE Facturas;  '''

CreateFacturas = ''' CREATE TABLE Facturas ( IDFactura INT AUTO_INCREMENT PRIMARY KEY,
                     IDEmpleado INT, IDCliente INT, IDAuto INT, 
                     PrecioUnitario DECIMAL(12.3) NOT NULL, Cantidad INT NOT NULL, 
                     Fecha DATETIME NOT NULL, ValorTotal DECIMAL (12,3) NOT NULL, 
                     FOREIGN KEY ( IDEmpleado ) REFERENCES Empleados(IDEmpleado), 
                     FOREIGN KEY ( IDAuto ) REFERENCES Autos(IDAuto),
                     FOREIGN KEY ( IDCliente ) REFERENCES Clientes(IDCliente) ); '''

InsertFacturas = ''' INSERT INTO Facturas ( IDEmpleado, IDCliente, IDAuto, PrecioUnitario,
                     Cantidad, Fecha, ValorTotal ) VALUES 
                     ( 2,5,3,520325.201,1,'2021-01-13 12:45:56',520325.201),
                     ( 1,1,6,652100.254,1,'2021-01-15 13:24:21',652100.254),
                     ( 2,2,2,784521.581,1,'2021-01-14 14:52:01',784521.581), 
                     ( 3,4,1,201544.854,1,'2021-01-16 11:12:00',201544.854),
                     ( 2,1,2,789652.784,1,'2021-01-20 16:18:54',789652.784);'''

def ListarFacturas(connection):
    query = f''' SELECT * from Factura; ''' 
    
    Results = ReadQuery(connection, query)
    columns = ['IDFactura','IDEmpleado','IDCliente','IDVendedor','IDAuto',
               'Cantidad','ValorTotal']
    ResultsDF = pd.DataFrame(Results,columns=columns)

    return ResultsDF

#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table Inventarios           +
#  +++++++++++++++++++++++++++++++++++++++++++

DropInventarios = ''' DROP TABLE Inventarios;  '''

CreateInventarios = ''' CREATE TABLE Inventarios ( IDInventario INT AUTO_INCREMENT PRIMARY KEY,
                        IDEmpleado INT, IDAuto INT, Cantidad INT NOT NULL, Fecha DATE NOT NULL,
                        FOREIGN KEY ( IDEmpleado ) REFERENCES Empleados(IDEmpleado), 
                        FOREIGN KEY ( IDAuto ) REFERENCES Autos(IDAuto) );  '''

InsertInventarios = ''' INSERT INTO Inventarios ( IDEmpleado, IDAuto, Cantidad, fecha ) VALUES   
                        ( 2,4,5,'2021-01-01'),
                        ( 2,3,7,'2021-01-01'),
                        ( 2,7,3,'2021-01-01'),
                        ( 2,9,1,'2021-01-01'),
                        ( 2,1,8,'2021-01-01');'''


def ListarInventarios(connection):
    query = f''' SELECT * from Inventarios; ''' 
    
    Results = ReadQuery(connection, query)
    columns = ['IDInventario','IDEmpleado','IDAuto','Cantidad','Fecha']
    ResultsDF = pd.DataFrame(Results,columns=columns)

    return ResultsDF

#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table OrdenCompras          +
#  +++++++++++++++++++++++++++++++++++++++++++

DropOrdenCompras = ''' DROP TABLE OrdenCompras;  '''

CreateOrdenCompras = ''' CREATE TABLE OrdenCompras ( IDOrden INT AUTO_INCREMENT PRIMARY KEY,
                         IDEmpleado INT, IDAuto INT, Cantidad INT NOT NULL, PrecioCompra DECIMAL(12,3),
                         FechaOrden DATE NOT NULL, FechaEntrega DATE, 
                         FOREIGN KEY ( IDEmpleado ) REFERENCES Empleados(IDEmpleado),
                         FOREIGN KEY ( IDAuto ) REFERENCES Autos(IDAuto) );  '''

InsertOrdenCompras = ''' INSERT INTO OrdenCompras ( IDEmpleado, IDAuto, Cantidad, PrecioCompra, 
                         FechaOrden, FechaEntrega ) VALUES   
                         ( 2,1,10,124875.204,'2021-01-01','2021-01-01'),
                         ( 2,2,10,749215.548,'2021-01-01','2021-01-01'),
                         ( 2,3,10,500201.245,'2021-01-01','2021-01-01'),
                         ( 2,4,10,195210.047,'2021-01-01','2021-01-01'),
                         ( 2,5,10,541982.451,'2021-01-01','2021-01-01'),
                         ( 2,6,10,648210.589,'2021-01-01','2021-01-01'),
                         ( 2,7,10,985425.214,'2021-01-01','2021-01-01'),
                         ( 2,8,10,348965.578,'2021-01-01','2021-01-01'),
                         ( 2,9,10,961254.854,'2021-01-01','2021-01-01');'''

def ListarOrdenCompras(connection):
    query = f''' SELECT * from OrdenCompras; ''' 
    
    Results = ReadQuery(connection, query)
    columns = ['IDOrden','IDEmpleado','IDAuto','Cantidad','PrecioCompra','FechaOrden','FechaEntrega' ]
    ResultsDF = pd.DataFrame(Results,columns=columns)

    return ResultsDF

