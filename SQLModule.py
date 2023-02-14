
import mysql.connector
from mysql.connector import Error
import pandas as pd

def StartDBConnection():

   User    = 'Jon'
   UserKey = "$Yes1k1na$"
   DataB   = 'JonAutos'
   #connection = ServerConnection("localhost", User, UserKey)
   connection = DBConnection("localhost", User, UserKey, DataB)

   return connection


def ServerConnection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )   
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error in ServerConnectio: '{err}'")
        
    return connection


def CreateDB(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error in CreateDB: '{err}'")

def DBConnection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error in DBConnection: '{err}'")

    return connection

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
        return Results

    except Error as err:
        print()
        print(f"Error in ReadQuery: '{err}'")
        print()
        print(query)
        print()

#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Drop Tables               +
#  +++++++++++++++++++++++++++++++++++++++++++
def DropTables(connection):
    ExecuteQuery(connection, DropFactura)
    ExecuteQuery(connection, DropVendedores)
    ExecuteQuery(connection, DropOrdenBodegaSala)
    ExecuteQuery(connection, DropInventarioSala)
    ExecuteQuery(connection, DropSalaVentas)
    ExecuteQuery(connection, DropBodega)
    ExecuteQuery(connection, DropAutos)
    ExecuteQuery(connection, DropUsuarios)
    ExecuteQuery(connection, DropClientes)
    ExecuteQuery(connection, DropSucursal)
    


#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Create Tables               +
#  +++++++++++++++++++++++++++++++++++++++++++
  
def CreateTables(connection):
    ExecuteQuery(connection, CreateSucursal)
    ExecuteQuery(connection, CreateAutos)
    ExecuteQuery(connection, CreateUsuarios)
    ExecuteQuery(connection, CreateClientes)
    ExecuteQuery(connection, CreateVendedores)
    ExecuteQuery(connection, CreateBodega)
    ExecuteQuery(connection, CreateSalaVentas)
    ExecuteQuery(connection, CreateOrdenBodegaSala)
    ExecuteQuery(connection, CreateInventarioSala)
    ExecuteQuery(connection, CreateFactura)


#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Data Into Tables               +
#  +++++++++++++++++++++++++++++++++++++++++++

def InsertData(connection):
    ExecuteQuery(connection, InsertSucursal)
    ExecuteQuery(connection, InsertAutos)
    ExecuteQuery(connection, InsertUsuarios)



# SQL querys .

#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table Sucursal              +
#  +++++++++++++++++++++++++++++++++++++++++++

DropSucursal = ''' DROP TABLE Sucursal;  '''

CreateSucursal = ''' CREATE TABLE Sucursal ( IDSucursal INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(20) NOT NULL, Ciudad VARCHAR(20) NOT NULL,
    Presupuesto VARCHAR(5) CHECK (Presupuesto IN('Alto','Medio','Bajo')) );  '''

InsertSucursal = ''' INSERT INTO Sucursal ( Nombre, Ciudad, Presupuesto ) VALUES
                     ( 'Principal', 'Bogota', 'Alto' ),  
                     ( 'Cedritos', 'Bogota', 'Alto' ),
                     ( 'Dorado', 'Bogota', 'Medio' ),
                     ( 'Centro', 'Bogota', 'Bajo' ),
                     ( 'Poblado', 'Medellin', 'Alto' ),
                     ( 'Laureles', 'Medellin', 'Medio' ),
                     ( 'Santo Domingo', 'Medellin', 'Bajo' ); '''

          
#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table Usuarios              +
#  +++++++++++++++++++++++++++++++++++++++++++

DropUsuarios = ''' DROP TABLE Usuarios;  '''

CreateUsuarios = ''' CREATE TABLE Usuarios ( IDUsuario INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(20) NOT NULL, Cedula VARCHAR(6) NOT NULL,
    IDSucursal INT , Clave VARCHAR(10) NOT NULL, Tipo VARCHAR(20) NOT NULL,
    CHECK (Tipo IN('Administrador DB','Gerente General','Gerente Sucursal')),
    FOREIGN KEY (IDSucursal) REFERENCES Sucursal(IDSucursal) );  '''

InsertUsuarios = ''' INSERT INTO Usuarios ( Nombre, Cedula, IDSucursal, Clave, Tipo ) VALUES 
                     ( 'Jon',2306,1,'2300', 'Administrador DB'),
                     ( 'Jairo',2307,1,'2300', 'Gerente General'),
                     ( 'Alejandra',7584,3,'2303', 'Gerente Sucursal'),
                     ( 'Julian',2548,1,'2301', 'Gerente Sucursal'),
                     ( 'Tito',1254,2,'2302', 'Gerente Sucursal'),
                     ( 'Alicia',6589,4,'2304', 'Gerente Sucursal'),
                     ( 'Carlos',2215,5,'2305', 'Gerente Sucursal'),
                     ( 'Ana',7845,6,'2306', 'Gerente Sucursal'); '''

def CheckUsuario(nombre,clave,connection):
    
    query = f''' SELECT * from Usuarios 
                 WHERE Nombre=\'{nombre}\' AND Clave=\'{clave}\'; ''' 
    
    Results = ReadQuery(connection, query)
    columns = ['IDUsuario','Nombre','Cedula','IDSucursal', 'Clave', 'Tipo']
    ResultsDF = pd.DataFrame(Results,columns=columns)

    return ResultsDF
 
def AddUsuario(nombre,cedula,idsucursal,clave,tipo,connection):
    pass 




def UsuarioSucursal(cedula,connection):

    query = f''' SELECT Usuarios.Cedula, Sucursal.Nombre
                 FROM Usuarios 
                 JOIN Sucursal ON Usuarios.IDSucursal = Sucursal.IDSucursal
                 WHERE Usuarios.Cedula = {cedula} ;''' 

    Results = ReadQuery(connection, query)
    columns = ['Cedula','NombreSucursal']
    ResultsDF = pd.DataFrame(Results,columns=columns)

    return ResultsDF

#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table Clientes              +
#  +++++++++++++++++++++++++++++++++++++++++++

DropClientes = ''' DROP TABLE Clientes;  '''

CreateClientes = ''' CREATE TABLE Clientes ( IDCliente INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(20) NOT NULL, Cedula VARCHAR(6) NOT NULL,
    Ciudad VARCHAR(5) DEFAULT 'TODAS', Clave VARCHAR(10) NOT NULL );  '''

InsertClientes = ''' INSERT INTO Clientes ( Nombre, Cedula, Ciudad, Clave ) VALUES 
                     ( 'Andres',8951,'Bogota', '21s45'),
                     ( 'Miguel',1524,'Bogota', '52sd4'),
                     ( 'Jose',8745,'Medellin', 'dd547'),
                     ( 'Luisa',9651,'Medellin', 'sqw54'),
                     ( 'Alex',2015,'Bogota', 'ret74'),
                     ( 'Diego',3054,'Medellin', '25ty1'),
                     ( 'Rosa',7840,'Medellin', '5rte2'),
                     ( 'Julio',9201,'Bogota', '514sq'); '''



#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table Vendedores            +
#  +++++++++++++++++++++++++++++++++++++++++++

DropVendedores = ''' DROP TABLE Vendedores; '''





#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table Clientes              +
#  +++++++++++++++++++++++++++++++++++++++++++

DropClientes = ''' DROP TABLE Clientes;  '''

CreateClientes = ''' CREATE TABLE Clientes ( IDCliente INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(20) NOT NULL, Cedula VARCHAR(6) NOT NULL,
    Ciudad VARCHAR(5) DEFAULT 'TODAS', Clave VARCHAR(10) NOT NULL );  '''

InsertClientes = ''' INSERT INTO Clientes ( Nombre, Cedula, Ciudad, Clave ) VALUES 
                     ( 'Andres',8951,'Bogota', '21s45'),
                     ( 'Miguel',1524,'Bogota', '52sd4'),
                     ( 'Jose',8745,'Medellin', 'dd547'),
                     ( 'Luisa',9651,'Medellin', 'sqw54'),
                     ( 'Alex',2015,'Bogota', 'ret74'),
                     ( 'Diego',3054,'Medellin', '25ty1'),
                     ( 'Rosa',7840,'Medellin', '5rte2'),
                     ( 'Julio',9201,'Bogota', '514sq'); '''



#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table Vendedores            +
#  +++++++++++++++++++++++++++++++++++++++++++

DropVendedores = ''' DROP TABLE Vendedores; '''

CreateVendedores = ''' CREATE TABLE Vendedores ( IDVendedor INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(20) NOT NULL, Cedula VARCHAR(6) NOT NULL,
    IDSucursal INT , Clave VARCHAR(10) NOT NULL,
    FOREIGN KEY ( IDSucursal ) REFERENCES Sucursal(IDSucursal) );  '''

#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table Bodega                +
#  +++++++++++++++++++++++++++++++++++++++++++

DropBodega = ''' DROP TABLE Bodega;  '''

CreateBodega = ''' CREATE TABLE Bodega ( IDBodega INT AUTO_INCREMENT PRIMARY KEY,
    IDSucursal INT, Ciudad VARCHAR(10) NOT NULL, 
    Nombre VARCHAR(10) NOT NULL, Capacidad INT NOT NULL,
    FOREIGN KEY ( IDSucursal ) REFERENCES Sucursal(IDSucursal) );  '''

#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table SalaVentas            +
#  +++++++++++++++++++++++++++++++++++++++++++

DropSalaVentas = ''' DROP TABLE SalaVentas;  '''

CreateSalaVentas = ''' CREATE TABLE SalaVentas ( IDSalaVentas INT AUTO_INCREMENT PRIMARY KEY,
    IDSucursal INT, Ciudad VARCHAR(10) NOT NULL, 
    Nombre VARCHAR(10) NOT NULL, Capacidad INT NOT NULL,
    FOREIGN KEY ( IDSucursal ) REFERENCES Sucursal(IDSucursal) );  '''


#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table OrdenBodegaSala       +
#  +++++++++++++++++++++++++++++++++++++++++++

DropOrdenBodegaSala = ''' DROP TABLE OrdenBodegaSala;  '''

CreateOrdenBodegaSala = ''' CREATE TABLE OrdenBodegaSala ( IDOrden INT AUTO_INCREMENT PRIMARY KEY,
    IDBodega INT, IDSalaVentas INT,IDAuto INT, Precio DECIMAL(12,3),
    Cantidad INT NOT NULL, FechaOrden DATE NOT NULL, FechaEntrega DATE, 
    FOREIGN KEY ( IDBodega ) REFERENCES Bodega(IDBodega),
    FOREIGN KEY ( IDSalaventas ) REFERENCES SalaVentas(IDSalaVentas), 
    FOREIGN KEY ( IDAuto ) REFERENCES Autos(IDAuto) );  '''

#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table InventarioSala        +
#  +++++++++++++++++++++++++++++++++++++++++++

DropInventarioSala = ''' DROP TABLE InventarioSala;  '''

CreateInventarioSala = ''' CREATE TABLE InventarioSala ( IDInventario INT AUTO_INCREMENT PRIMARY KEY,
    IDSalaVentas INT, IDAuto INT,
    Cantidad INT NOT NULL, Fecha DATE NOT NULL,
    FOREIGN KEY ( IDSalaventas ) REFERENCES SalaVentas(IDSalaVentas), 
    FOREIGN KEY ( IDAuto ) REFERENCES Autos(IDAuto) );  '''

#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table Factura               +
#  +++++++++++++++++++++++++++++++++++++++++++

DropFactura = ''' DROP TABLE Factura;  '''

CreateFactura = ''' CREATE TABLE Factura ( IDFactura INT AUTO_INCREMENT PRIMARY KEY,
    IDSalaVentas INT, IDCliente INT, IDVendedor INT, IDAuto INT,
    Cantidad INT NOT NULL, Fecha DATE NOT NULL , Precio DECIMAL (12,3) NOT NULL, 
    FOREIGN KEY ( IDSalaventas ) REFERENCES SalaVentas(IDSalaVentas), 
    FOREIGN KEY ( IDAuto ) REFERENCES Autos(IDAuto),
    FOREIGN KEY ( IDCliente ) REFERENCES Clientes(IDCliente),
    FOREIGN KEY ( IDVendedor ) REFERENCES Vendedores(IDVendedor) ); '''


#  +++++++++++++++++++++++++++++++++++++++++++
#  +             Table Autos                 +
#  +++++++++++++++++++++++++++++++++++++++++++

DropAutos = ''' DROP TABLE Autos;  '''

CreateAutos = ''' CREATE TABLE Autos ( IDAuto INT AUTO_INCREMENT PRIMARY KEY,
    Marca VARCHAR(20) NOT NULL, Modelo VARCHAR(10) NOT NULL,
    anio VARCHAR(5), NumeroMotor VARCHAR(10) NOT NULL );  '''

InsertAutos = ''' INSERT INTO Autos ( Marca, Modelo, anio, NumeroMotor ) VALUES
                  ( 'Ford', 'Mustang',2020,'ksjs4120' ),
                  ( 'Ford', 'Mustang',2020,'ksjs4121' ),
                  ( 'Ford', 'Mustang',2020,'ksjs4122' ),
                  ( 'Ford', 'Mustang',2021,'jhsg1250' ),
                  ( 'Ford', 'Mustang',2021,'jhsg1251' ),
                  ( 'Ford', 'Mustang',2021,'jhsg1252' ),
                  ( 'Ford', 'Mustang',2022,'gsft1548' ),
                  ( 'Ford', 'Mustang',2022,'gsft1549' ),
                  ( 'Ford', 'Mustang',2022,'gsft1550' ),
                  ( 'Ford', 'Explorer',2020,'hgdy4586' ),
                  ( 'Ford', 'Explorer',2020,'hgdy4587' ),
                  ( 'Ford', 'Explorer',2020,'hgdy4588' ),
                  ( 'Ford', 'Explorer',2021,'lmsq8457' ),
                  ( 'Ford', 'Explorer',2021,'lmsq8458' ),
                  ( 'Ford', 'Explorer',2021,'lmsq8459' ),
                  ( 'Ford', 'Explorer',2022,'uqst8024' ),
                  ( 'Ford', 'Explorer',2022,'uqst8025' ),
                  ( 'Ford', 'Explorer',2022,'uqst8026' ),
                  ( 'Ford', 'Edge',2020,'thuj5214' ),
                  ( 'Ford', 'Edge',2020,'thuj5215' ),
                  ( 'Ford', 'Edge',2020,'thuj5216' ),
                  ( 'Ford', 'Edge',2021,'wsft8795' ),
                  ( 'Ford', 'Edge',2021,'wsft8796' ),
                  ( 'Ford', 'Edge',2021,'wsft8798' ),
                  ( 'Ford', 'Edge',2022,'qsed2304' ),
                  ( 'Ford', 'Edge',2022,'qsed2305' ),
                  ( 'Ford', 'Edge',2022,'qsed2306' ); '''


