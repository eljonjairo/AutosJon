import tkinter as tk
from tkinter import ttk
import SQLModule as sql
import pandas as pd
import Empleados
from IPython.display import display

class Interface(tk.Frame):
    def __init__(self, root = None):
        sql.writeDebug("    Interface Constructor IN")  
        super().__init__(root, width=1800, height=600)
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
       
        self.labelCedula = tk.Label( self, text = " Cedula : " )
        self.labelCedula.grid( row=2,column=0, padx=10, pady = 10)         
       
        self.labelClave = tk.Label( self, text = " Clave : " )
        self.labelClave.grid( row=3,column=0, padx=10, pady = 10 )         

        self.entryNombre = tk.Entry( self,width=30, borderwidth=3 )
        self.entryNombre.grid( row=1,column=1, padx=20, pady = 20 )         

        self.entryCedula = tk.Entry( self,width=30, borderwidth=3 )
        self.entryCedula.grid( row=2,column=1, padx=20, pady = 20 )         

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
    AutosMenu.add_command(label="Crear Tabla", command=lambda:SQLModule.CreateAutos(connection))
    AutosMenu.add_command(label="Listar", command=lambda:Listar(self.conexion,"Autos"))
    AutosMenu.add_command(label="Eliminar Tabla", command=lambda:SQLModule.DropAutos(connection))
        
    ClientesMenu = tk.Menu(menubar, tearoff=0)
    ClientesMenu.add_command(label="Listar")

    EmpleadosMenu = tk.Menu(menubar, tearoff=0)
    EmpleadosMenu.add_command(label="Listar", command=lambda:tablaEmpleados(self))

    FacturasMenu = tk.Menu(menubar, tearoff=0)
    FacturasMenu.add_command(label="Listar")

    InventariosMenu = tk.Menu(menubar, tearoff=0)
    InventariosMenu.add_command(label="Listar")

    OrdenComprasMenu = tk.Menu(menubar, tearoff=0)
    OrdenComprasMenu.add_command(label="Listar")

    OrdenComprasMenu = tk.Menu(menubar, tearoff=0)
    OrdenComprasMenu.add_command(label="Listar")

    menubar.add_cascade(label="Autos", menu=AutosMenu)
    menubar.add_cascade(label="Clientes", menu=ClientesMenu)
    menubar.add_cascade(label="Empleados", menu=EmpleadosMenu)
    menubar.add_cascade(label="Facturas", menu=FacturasMenu)
    menubar.add_cascade(label="Inventarios", menu=InventariosMenu)
    menubar.add_cascade(label="OrdenCompras", menu=OrdenComprasMenu)

    sql.writeDebug("    MenuAdministrador OUT") 
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
    















