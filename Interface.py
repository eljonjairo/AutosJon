import tkinter as tk
from tkinter import ttk
import SQLModule as sql
import pandas as pd
import Autos
import Clientes
import Empleados
import Facturas
import Inventarios
import OrdenCompras
from IPython.display import display

class Interface(tk.Frame):
    def __init__(self, root = None):
        sql.writeDebug("    Interface Constructor IN")  
        super().__init__(root, width=2200, height=600)
        self.root = root
        self.pack() 
        self.option_add( "*font", "lucida 23 bold " )
        self.conexion = sql.DBConnect()
        print(" Interface started ")
        sql.writeDebug("    Interface Constructor OUT")  

    def LoginUser(self):

        sql.writeDebug("    Interface LoginUser IN")  

        self.labelNombre = tk.Label( self, text = " Nombre : " )
        self.labelNombre.grid( row=1,column=0, padx=10, pady = 10 )         
        self.entryNombre = tk.Entry( self,width=30, borderwidth=3 )
        self.entryNombre.grid( row=1,column=1, padx=20, pady = 20 )         
       
        self.labelCedula = tk.Label( self, text = " Cedula : " )
        self.labelCedula.grid( row=2,column=0, padx=10, pady = 10)         
        self.entryCedula = tk.Entry( self,width=30, borderwidth=3 )
        self.entryCedula.grid( row=2,column=1, padx=20, pady = 20 )         
       
        self.labelClave = tk.Label( self, text = " Clave : " )
        self.labelClave.grid( row=3,column=0, padx=10, pady = 10 )         
        self.entryClave = tk.Entry( self,width=30, borderwidth=3, show="*")
        self.entryClave.grid( row=3,column=1, padx=20, pady = 20 )         

        self.loginButton = tk.Button( self, text="Ingresar",command = lambda: self.login() )
        self.loginButton.grid( row=5, column=0, columnspan=2,pady=30, padx=10, ipadx=100 )

        sql.writeDebug("    Interface LoginUser OUT")  

    def login(self):
        sql.writeDebug("    Interface login IN")  

        
        empleado = Empleados.Empleado( self.entryNombre.get(), self.entryCedula.get(), 
                                       self.entryClave.get()," None ")
        
        sql.writeDebug("   " + str(empleado)) 
        sql.writeDebug("   " + str(self.conexion)) 
        empleado = Empleados.isEmpleado(empleado,self.conexion)     
        sql.writeDebug(f"    empleado es: {empleado.Tipo} ")  

        sql.writeDebug("    Interface login OUT")  

        MenuAdministrador(self)

def MenuAdministrador(self):
    sql.writeDebug("    MenuAdministrador IN") 
    self.labelNombre.destroy() 
    self.labelClave.destroy() 
    self.labelCedula.destroy() 
    self.entryCedula.destroy() 
    self.entryNombre.destroy() 
    self.entryClave.destroy() 
    self.loginButton.destroy()

    root = self.root
    root.geometry("1200x800")
    menubar = tk.Menu()
    root.config(menu=menubar)

    AutosMenu = tk.Menu(menubar, tearoff=0)
    AutosMenu.add_command(label="Listar", command=lambda:tablaAutos(self))
    AutosMenu.add_command(label="Insertar Auto", command=lambda:insertarAuto(self) )
        
    ClientesMenu = tk.Menu(menubar, tearoff=0)
    ClientesMenu.add_command(label="Listar", command=lambda:tablaClientes(self) )
    ClientesMenu.add_command(label="Insertar Cliente", command=lambda:insertarCliente(self) )

    EmpleadosMenu = tk.Menu(menubar, tearoff=0)
    EmpleadosMenu.add_command(label="Listar", command=lambda:tablaEmpleados(self))
    EmpleadosMenu.add_command(label="Insertar Empleado", command=lambda:insertarEmpleado(self) )

    FacturasMenu = tk.Menu(menubar, tearoff=0)
    FacturasMenu.add_command(label="Listar", command=lambda:tablaFacturas(self))
    FacturasMenu.add_command(label="Insertar Factura", command=lambda:insertarFactura(self) )

    InventariosMenu = tk.Menu(menubar, tearoff=0)
    InventariosMenu.add_command(label="Listar", command=lambda:tablaInventarios(self))
    InventariosMenu.add_command(label="Insertar Inventario", command=lambda:insertarInventario(self) )

    OrdenComprasMenu = tk.Menu(menubar, tearoff=0)
    OrdenComprasMenu.add_command(label="Listar",command=lambda:tablaOrdenCompras(self))
    OrdenComprasMenu.add_command(label="Insertar OrdenCompra", command=lambda:insertarOrdenCompra(self) )

    ConsultasMenu = tk.Menu(menubar, tearoff=0)
    ConsultasMenu.add_command(label="Listar")

    menubar.add_cascade(label="Autos", menu=AutosMenu)
    menubar.add_cascade(label="Clientes", menu=ClientesMenu)
    menubar.add_cascade(label="Empleados", menu=EmpleadosMenu)
    menubar.add_cascade(label="Facturas", menu=FacturasMenu)
    menubar.add_cascade(label="Inventarios", menu=InventariosMenu)
    menubar.add_cascade(label="OrdenCompras", menu=OrdenComprasMenu)
    menubar.add_cascade(label="Consultas", menu=ConsultasMenu)

    sql.writeDebug("    MenuAdministrador OUT") 

def tablaAutos(self):
    sql.writeDebug("    tablaAutos IN") 
    DF = Autos.ListarAutos(self.conexion)
    self.tabla = ttk.Treeview(self, column = DF.columns.values)
    self.tabla.grid(row=1, column=0, columnspan=4, sticky='nse')
    self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
    self.scroll.grid(row=1,column=4,sticky='nse')
    self.tabla.configure(yscrollcommand = self.scroll.set)
   
    self.tabla.heading('#0', text='ID')
    self.tabla.heading('#1', text='Marca')
    self.tabla.heading('#2', text='Linea')
    self.tabla.heading('#3', text='Modelo')
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("lucida 23 bold "))
    style.configure("Treeview", rowheight=40, font=("lucida 20 bold "))

    for idx in reversed(DF.index):
        row = DF.loc[idx]
        self.tabla.insert('',0,text=row['ID'],
        values = (row['Marca'],row['Linea'],row['Modelo']))
 
    sql.writeDebug("    tablaAutos OUT") 
    
def insertarAuto(self):
    sql.writeDebug("   insertarAuto IN") 

    self.labelMarca = tk.Label( self, text = " Marca : " )
    self.labelMarca.grid( row=1,column=0, padx=10, pady = 10 )         
    self.entryMarca = tk.Entry( self,width=30, borderwidth=3 )
    self.entryMarca.grid( row=1,column=1, padx=20, pady = 20 )         

    self.labelLinea = tk.Label( self, text = " Linea : " )
    self.labelLinea.grid( row=2,column=0, padx=10, pady = 10 )         
    self.entryLinea = tk.Entry( self,width=30, borderwidth=3 )
    self.entryLinea.grid( row=2,column=1, padx=20, pady = 20 )         

    self.labelModelo = tk.Label( self, text = " Modelo : " )
    self.labelModelo.grid( row=3,column=0, padx=10, pady = 10 )         
    self.entryModelo = tk.Entry( self,width=30, borderwidth=3 )
    self.entryModelo.grid( row=3,column=1, padx=20, pady = 20 )         

    self.insertButton = tk.Button( self, text="Insertar Auto",command = lambda: sendAuto(self) )
    self.insertButton.grid( row=5, column=0, columnspan=2,pady=30, padx=10, ipadx=100 )

    sql.writeDebug("   insertarAuto OUT") 

def sendAuto(self):

    auto = Autos.Auto(self.entryMarca.get(),self.entryLinea.get(),self.entryModelo.get())
    sql.writeDebug(f"    auto es: {auto} ")
    Autos.InsertarAuto(self.conexion,auto)
    self.labelMarca.destroy()
    self.labelLinea.destroy()
    self.labelModelo.destroy()
    self.entryMarca.destroy()
    self.entryLinea.destroy()
    self.entryModelo.destroy()
    self.insertButton.destroy()
    self.label = tk.Label( self, text = " Auto agregado !! " )
    self.label.grid( row=1,column=0, padx=10, pady = 10 )         

def tablaClientes(self):
    sql.writeDebug("    tablaClientes IN")

    DF = Clientes.ListarClientes(self.conexion)
    self.tabla = ttk.Treeview(self, column = DF.columns.values)
    self.tabla.grid(row=1, column=0, columnspan=4, sticky='nse')
    self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
    self.scroll.grid(row=1,column=3,sticky='nse')
    self.tabla.configure(yscrollcommand = self.scroll.set)
   
    self.tabla.heading('#0', text='ID')
    self.tabla.heading('#1', text='Nombre')
    self.tabla.heading('#2', text='Cedula')
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("lucida 23 bold "))
    style.configure("Treeview", rowheight=40, font=("lucida 20 bold "))

    for idx in reversed(DF.index):
        row = DF.loc[idx]
        self.tabla.insert('',0,text=row['ID'],
        values = (row['Nombre'],row['Cedula']))
 
    sql.writeDebug("   insertarAuto OUT") 
 
def insertarCliente(self):
    sql.writeDebug("   insertarCliente IN") 

    self.labelNombre = tk.Label( self, text = " Nombre : " )
    self.labelNombre.grid( row=1,column=0, padx=10, pady = 10 )         
    self.entryNombre = tk.Entry( self,width=30, borderwidth=3 )
    self.entryNombre.grid( row=1,column=1, padx=20, pady = 20 )         

    self.labelCedula = tk.Label( self, text = " Cedula : " )
    self.labelCedula.grid( row=2,column=0, padx=10, pady = 10 )         
    self.entryCedula = tk.Entry( self,width=30, borderwidth=3 )
    self.entryCedula.grid( row=2,column=1, padx=20, pady = 20 )         

    self.labelClave = tk.Label( self, text = " Clave : " )
    self.labelClave.grid( row=3,column=0, padx=10, pady = 10 )         
    self.entryClave = tk.Entry( self,width=30, borderwidth=3 )
    self.entryClave.grid( row=3,column=1, padx=20, pady = 20 )         

    self.insertButton = tk.Button( self, text="Insertar Cliente",command = lambda: sendCliente(self) )
    self.insertButton.grid( row=5, column=0, columnspan=2,pady=30, padx=10, ipadx=100 )

    sql.writeDebug("   insertarCliente OUT")
 
def sendCliente(self):

    cliente = Clientes.Cliente(self.entryNombre.get(),self.entryCedula.get(),self.entryClave.get())
    sql.writeDebug(f"    cliente es: {cliente} ")
    Clientes.InsertarCliente(self.conexion,cliente)
    self.labelNombre.destroy()
    self.labelCedula.destroy()
    self.labelClave.destroy()
    self.entryNombre.destroy()
    self.entryCedula.destroy()
    self.entryClave.destroy()
    self.insertButton.destroy()
    self.label = tk.Label( self, text = " Cliente agregado !! " )
    self.label.grid( row=1,column=0, padx=10, pady = 10 )
         
def tablaEmpleados(self):
    sql.writeDebug("    tablaEmpleados IN") 

    DF = Empleados.ListarEmpleados(self.conexion)
    self.tabla = ttk.Treeview(self, column = DF.columns.values)
    self.tabla.grid(row=1, column=0, columnspan=4, sticky='nse')
    self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
    self.scroll.grid(row=1,column=4,sticky='nse')
    self.tabla.configure(yscrollcommand = self.scroll.set)
   
    self.tabla.heading('#0', text='ID')
    self.tabla.heading('#1', text='Nombre')
    self.tabla.heading('#2', text='Cedula')
    self.tabla.heading('#3', text='Tipo')
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("lucida 23 bold "))
    style.configure("Treeview", rowheight=40, font=("lucida 20 bold "))

    for idx in reversed(DF.index):
        row = DF.loc[idx]
        self.tabla.insert('',0,text=row['ID'],
        values = (row['Nombre'],row['Cedula'],row['Tipo']))

    sql.writeDebug("    tablaEmpleados OUT") 

 
def insertarEmpleado(self):
    sql.writeDebug("   insertarEmpleado IN") 

    self.labelNombre = tk.Label( self, text = " Nombre : " )
    self.labelNombre.grid( row=1,column=0, padx=10, pady = 10 )         
    self.entryNombre = tk.Entry( self,width=30, borderwidth=3 )
    self.entryNombre.grid( row=1,column=1, padx=20, pady = 20 )         

    self.labelCedula = tk.Label( self, text = " Cedula : " )
    self.labelCedula.grid( row=2,column=0, padx=10, pady = 10 )         
    self.entryCedula = tk.Entry( self,width=30, borderwidth=3 )
    self.entryCedula.grid( row=2,column=1, padx=20, pady = 20 )         

    self.labelClave = tk.Label( self, text = " Clave : " )
    self.labelClave.grid( row=3,column=0, padx=10, pady = 10 )         
    self.entryClave = tk.Entry( self,width=30, borderwidth=3 )
    self.entryClave.grid( row=3,column=1, padx=20, pady = 20 )         

    self.labelTipo = tk.Label( self, text = " Tipo : " )
    self.labelTipo.grid( row=4,column=0, padx=10, pady = 10 )         
    self.entryTipo = tk.Entry( self,width=30, borderwidth=3 )
    self.entryTipo.grid( row=4,column=1, padx=20, pady = 20 )         

    self.insertButton = tk.Button( self, text="Insertar Empleado",command = lambda: sendEmpleado(self) )
    self.insertButton.grid( row=6, column=0, columnspan=2,pady=30, padx=10, ipadx=100 )

    sql.writeDebug("   insertarEmpleado OUT")

def sendEmpleado(self):

    empleado = Empleados.Empleado(self.entryNombre.get(),self.entryCedula.get(),self.entryClave.get())
    sql.writeDebug(f"    empleado es: {empleado} ")
    Empleados.InsertarEmpleado(self.conexion,empleado)
    self.labelNombre.destroy()
    self.labelCedula.destroy()
    self.labelClave.destroy()
    self.labelTipo.destroy()
    self.entryNombre.destroy()
    self.entryCedula.destroy()
    self.entryClave.destroy()
    self.entryTipo.destroy()
    self.insertButton.destroy()
    self.label = tk.Label( self, text = " Empleado agregado !! " )
    self.label.grid( row=1,column=0, padx=10, pady = 10 )

def tablaFacturas(self):
    sql.writeDebug("    tablaFacturas IN") 
    DF = Facturas.ListarFacturas(self.conexion)
    self.tabla = ttk.Treeview(self, column = DF.columns.values)
    self.tabla.grid(row=1, column=0, columnspan=8, sticky='nse')
    self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
    self.scroll.grid(row=1,column=9,sticky='nse')
    self.tabla.configure(yscrollcommand = self.scroll.set)
   
    self.tabla.heading('#0', text='ID')
    self.tabla.heading('#1', text='idEmpleado')
    self.tabla.heading('#2', text='idCliente')
    self.tabla.heading('#3', text='idAuto')
    self.tabla.heading('#4', text='precioUnitario')
    self.tabla.heading('#5', text='Cantidad')
    self.tabla.heading('#6', text='Fecha')
    self.tabla.heading('#7', text='valorTotal')
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("lucida 23 bold "))
    style.configure("Treeview", rowheight=40, font=("lucida 20 bold "))

    for idx in reversed(DF.index):
        row = DF.loc[idx]
        self.tabla.insert('',0,text=row['ID'],
        values = (row['idEmpleado'],row['idCliente'],row['idAuto'],row['precioUnitario'],row['Cantidad'],row['Fecha'],row['valorTotal']))
 
    sql.writeDebug("    tablaFacturas OUT") 

def insertarFactura(self):
    sql.writeDebug("   insertarFactura IN") 

    self.labelidEmpleado = tk.Label( self, text = " idEmpleado : " )
    self.labelidEmpleado.grid( row=1,column=0, padx=10, pady = 10 )         
    self.entryidEmpleado = tk.Entry( self,width=30, borderwidth=3 )
    self.entryidEmpleado.grid( row=1,column=1, padx=20, pady = 20 )         

    self.labelidCliente = tk.Label( self, text = " idCliente : " )
    self.labelidCliente.grid( row=2,column=0, padx=10, pady = 10 )         
    self.entryidCliente = tk.Entry( self,width=30, borderwidth=3 )
    self.entryidCliente.grid( row=2,column=1, padx=20, pady = 20 )         

    self.labelidAuto = tk.Label( self, text = " idAuto : " )
    self.labelidAuto.grid( row=3,column=0, padx=10, pady = 10 )         
    self.entryidAuto = tk.Entry( self,width=30, borderwidth=3 )
    self.entryidAuto.grid( row=3,column=1, padx=20, pady = 20 )         

    self.labelprecioUnitario = tk.Label( self, text = " precioUnitario : " )
    self.labelprecioUnitario.grid( row=4,column=0, padx=10, pady = 10 )         
    self.entryprecioUnitario = tk.Entry( self,width=30, borderwidth=3 )
    self.entryprecioUnitario.grid( row=4,column=1, padx=20, pady = 20 )         

    self.labelCantidad = tk.Label( self, text = " Cantidad : " )
    self.labelCantidad.grid( row=5,column=0, padx=10, pady = 10 )         
    self.entryCantidad = tk.Entry( self,width=30, borderwidth=3 )
    self.entryCantidad.grid( row=5,column=1, padx=20, pady = 20 )         

    self.labelFecha = tk.Label( self, text = " Fecha : " )
    self.labelFecha.grid( row=6,column=0, padx=10, pady = 10 )         
    self.entryFecha = tk.Entry( self,width=30, borderwidth=3 )
    self.entryFecha.grid( row=6,column=1, padx=20, pady = 20 )         

    self.labelvalorTotal = tk.Label( self, text = " valorTotal : " )
    self.labelvalorTotal.grid( row=7,column=0, padx=10, pady = 10 )         
    self.entryvalorTotal = tk.Entry( self,width=30, borderwidth=3 )
    self.entryvalorTotal.grid( row=7,column=1, padx=20, pady = 20 )         

    self.insertButton = tk.Button( self, text="Insert Factura",command = lambda: sendFactura(self) )
    self.insertButton.grid( row=9, column=0, columnspan=2,pady=30, padx=10, ipadx=100 )

    sql.writeDebug("   insertarFactura OUT")

def sendFactura(self):

    factura = Facturas.Factura(self.entryidEmpleado.get(), self.entryidCliente.get(), self.entryidAuto.get(), self.entryprecioUnitario.get(), self.entryCantidad.get(), self.entryFecha.get(), self.entryvalorTotal.get() )
    sql.writeDebug(f"    factura es: {factura} ")
    Facturas.InsertarFactura(self.conexion,factura)
    self.labelidEmpleado.destroy()
    self.labelidCliente.destroy()
    self.labelidAuto.destroy()
    self.labelprecioUnitario.destroy()
    self.labelCantidad.destroy()
    self.labelFecha.destroy()
    self.labelvalorTotal.destroy()
    self.entryidEmpleado.destroy()
    self.entryidCliente.destroy()
    self.entryidAuto.destroy()
    self.entryprecioUnitario.destroy()
    self.entryCantidad.destroy()
    self.entryFecha.destroy()
    self.entryvalorTotal.destroy()
    self.insertButton.destroy()
    self.label = tk.Label( self, text = " Factura agregada !! " )
    self.label.grid( row=1,column=0, padx=10, pady = 10 )

def tablaInventarios(self):
    sql.writeDebug("    tablaInventarios IN") 
    DF = Inventarios.ListarInventarios(self.conexion)
    self.tabla = ttk.Treeview(self, column = DF.columns.values)
    self.tabla.grid(row=1, column=0, columnspan=4, sticky='nse')
    self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
    self.scroll.grid(row=1,column=5,sticky='nse')
    self.tabla.configure(yscrollcommand = self.scroll.set)
   
    self.tabla.heading('#0', text='ID')
    self.tabla.heading('#1', text='idEmpleado')
    self.tabla.heading('#2', text='idAuto')
    self.tabla.heading('#3', text='Cantidad')
    self.tabla.heading('#4', text='Fecha')
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("lucida 23 bold "))
    style.configure("Treeview", rowheight=40, font=("lucida 20 bold "))

    for idx in reversed(DF.index):
        row = DF.loc[idx]
        self.tabla.insert('',0,text=row['ID'],
        values = (row['idEmpleado'],row['idAuto'],row['Cantidad'],row['Fecha']))
 
    sql.writeDebug("    tablaInventarios OUT") 

def insertarInventario(self):
    sql.writeDebug("   insertarInventario IN") 

    self.labelidEmpleado = tk.Label( self, text = " idEmpleado : " )
    self.labelidEmpleado.grid( row=1,column=0, padx=10, pady = 10 )         
    self.entryidEmpleado = tk.Entry( self,width=30, borderwidth=3 )
    self.entryidEmpleado.grid( row=1,column=1, padx=20, pady = 20 )         

    self.labelidAuto = tk.Label( self, text = " idAuto : " )
    self.labelidAuto.grid( row=2,column=0, padx=10, pady = 10 )         
    self.entryidAuto = tk.Entry( self,width=30, borderwidth=3 )
    self.entryidAuto.grid( row=2,column=1, padx=20, pady = 20 )         

    self.labelCantidad = tk.Label( self, text = " Cantidad : " )
    self.labelCantidad.grid( row=3,column=0, padx=10, pady = 10 )         
    self.entryCantidad = tk.Entry( self,width=30, borderwidth=3 )
    self.entryCantidad.grid( row=3,column=1, padx=20, pady = 20 )         

    self.labelFecha = tk.Label( self, text = " Fecha : " )
    self.labelFecha.grid( row=4,column=0, padx=10, pady = 10 )         
    self.entryFecha = tk.Entry( self,width=30, borderwidth=3 )
    self.entryFecha.grid( row=4,column=1, padx=20, pady = 20 )         

    self.insertButton = tk.Button( self, text="Insert Factura",command = lambda: sendFactura(self) )
    self.insertButton.grid( row=6, column=0, columnspan=2,pady=30, padx=10, ipadx=100 )

    sql.writeDebug("   insertarInventario OUT")

def sendInventario(self):

    inventario = Inventarios.Inventario(self.entryidEmpleado.get(), self.entryidCliente.get(), self.entryidAuto.get(), self.entryprecioUnitario.get(), self.entryCantidad.get(), self.entryFecha.get(), self.entryvalorTotal.get() )
    sql.writeDebug(f"    factura es: {factura} ")
    Inventarios.InsertarInventario(self.conexion,inventario)
    self.labelidEmpleado.destroy()
    self.labelidAuto.destroy()
    self.labelCantidad.destroy()
    self.labelFecha.destroy()
    self.entryidEmpleado.destroy()
    self.entryidAuto.destroy()
    self.entryCantidad.destroy()
    self.entryFecha.destroy()
    self.insertButton.destroy()
    self.label = tk.Label( self, text = " Inventario agregado !! " )
    self.label.grid( row=1,column=0, padx=10, pady = 10 )

def tablaOrdenCompras(self):
    sql.writeDebug("    tablaOrdenCompras IN") 
    DF = OrdenCompras.ListarOrdenCompras(self.conexion)
    self.tabla = ttk.Treeview(self, column = DF.columns.values)
    self.tabla.grid(row=1, column=0, columnspan=6, sticky='nse')
    self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
    self.scroll.grid(row=1,column=7,sticky='nse')
    self.tabla.configure(yscrollcommand = self.scroll.set)
   
    self.tabla.heading('#0', text='ID')
    self.tabla.heading('#1', text='idEmpleado')
    self.tabla.heading('#2', text='idAuto')
    self.tabla.heading('#3', text='Cantidad')
    self.tabla.heading('#4', text='precioCompra')
    self.tabla.heading('#5', text='FechaOrden')
    self.tabla.heading('#6', text='FechaEntrega')
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("lucida 23 bold "))
    style.configure("Treeview", rowheight=40, font=("lucida 20 bold "))

    for idx in reversed(DF.index):
        row = DF.loc[idx]
        self.tabla.insert('',0,text=row['ID'],
        values = (row['idEmpleado'],row['idAuto'],row['Cantidad'],row['precioCompra'],row['fechaOrden'],row['fechaEntrega']))

    sql.writeDebug("    tablaOrdenCompras OUT") 

def insertarOrdenCompra(self):
    sql.writeDebug("   insertarOrdenCompra IN") 

    self.labelidEmpleado = tk.Label( self, text = " idEmpleado : " )
    self.labelidEmpleado.grid( row=1,column=0, padx=10, pady = 10 )         
    self.entryidEmpleado = tk.Entry( self,width=30, borderwidth=3 )
    self.entryidEmpleado.grid( row=1,column=1, padx=20, pady = 20 )         

    self.labelidAuto = tk.Label( self, text = " idAuto : " )
    self.labelidAuto.grid( row=2,column=0, padx=10, pady = 10 )         
    self.entryidAuto = tk.Entry( self,width=30, borderwidth=3 )
    self.entryidAuto.grid( row=2,column=1, padx=20, pady = 20 )         

    self.labelCantidad = tk.Label( self, text = " Cantidad : " )
    self.labelCantidad.grid( row=3,column=0, padx=10, pady = 10 )         
    self.entryCantidad = tk.Entry( self,width=30, borderwidth=3 )
    self.entryCantidad.grid( row=3,column=1, padx=20, pady = 20 )         

    self.labelprecioCompra = tk.Label( self, text = " Fecha : " )
    self.labelprecioCompra.grid( row=4,column=0, padx=10, pady = 10 )         
    self.entryprecioCompra = tk.Entry( self,width=30, borderwidth=3 )
    self.entryprecioCompra.grid( row=4,column=1, padx=20, pady = 20 )         

    self.labelFechaOrden = tk.Label( self, text = " Fecha : " )
    self.labelFechaOrden.grid( row=5,column=0, padx=10, pady = 10 )         
    self.entryFechaOrden = tk.Entry( self,width=30, borderwidth=3 )
    self.entryFechaOrden.grid( row=5,column=1, padx=20, pady = 20 )         

    self.labelFechaEntrega = tk.Label( self, text = " Fecha : " )
    self.labelFechaEntrega.grid( row=6,column=0, padx=10, pady = 10 )         
    self.entryFechaEntrega = tk.Entry( self,width=30, borderwidth=3 )
    self.entryFechaEntrega.grid( row=6,column=1, padx=20, pady = 20 )         

    self.insertButton = tk.Button( self, text="Insert Factura",command = lambda: sendFactura(self) )
    self.insertButton.grid( row=8, column=0, columnspan=2,pady=30, padx=10, ipadx=100 )

    sql.writeDebug("   insertarOrdenCompra OUT")


