import tkinter as tk
import SQLModule as sql
import pandas as pd
from IPython.display import display

class Interface(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=1800, height=600)
        self.root = root
        self.pack() 
        self.option_add( "*font", "lucida 23 bold " )
        self.LoginUser()
        conexion = sql.DBConnection() 
        self.connection = conexion.DBConnect()  

    def LoginUser(self):
        self.labelNombre = tk.Label(self, text = " Nombre : ")
        self.labelClave = tk.Label(self, text = " Clave : ")
        self.labelNombre.grid(row=1,column=0, padx=10, pady = 10)         
        self.labelClave.grid(row=2,column=0, padx=10, pady = 10)         
        self.entryNombre = tk.Entry(self,width=30, borderwidth=3)
        self.entryClave = tk.Entry(self,width=30, borderwidth=3,show="*")
        self.entryNombre.grid(row=1,column=1, padx=20, pady = 20)         
        self.entryClave.grid(row=2,column=1, padx=20, pady = 20)         
        self.loginButton = tk.Button( self, text="Ingresar",command = lambda: self.login() )
        self.loginButton.grid(row=3, column=0, columnspan=2,pady=30, padx=10, ipadx=100)

    def login(self):

        print(self.entryNombre.get())

        Empleado = sql.CheckEmpleado(self.entryNombre.get(),self.entryClave.get(),self.connection)     
    
        print(Empleado) 
#        n = Empleado["Nombre"].size
#    
#        if n == 1: 
#            output = " "
#            interface.destroy()
#            interface = InterfaceAdministrador(Empleado,connection)
#     
#        elif n > 1:
#            output = " Más de un empleado con este Nombre y Clave "
#
#        else:
#            output = " Nombre o Clave incorrectas "
#
#        loginLabel = tkinter.Label(interface, text = output )
#        loginLabel.grid(row=5, column=0, columnspan=2,pady=20, padx=10, ipadx=100 )
#        loginLabel.config(font=("Arial", 20))

def StartInterface(): 
    interface = tkinter.Tk()
    interface.title("JonAutos Interface")
    interface.geometry("800x600")

    return(interface)

def InterfaceAdministrador(Empleado,connection):

    interface = tkinter.Tk()
    interface.title("JonAutos Interface")
    interface.geometry("1800x600")

    interface.option_add( "*font", "lucida 20 bold " )

    nombre = Empleado["Nombre"][0]
    cedula = Empleado["Cedula"][0]
    cargo = Empleado["Tipo"][0]

    user = " Empleado:  %s  Identificacion:  %s  Cargo:  %s  " %(nombre,cedula,cargo)

    interface.title(user)

    #Menus implementation

    menubar = tkinter.Menu(interface)

    AutosMenu = tkinter.Menu(menubar, tearoff=0)
    AutosMenu.add_command(label="Crear Tabla", command=lambda:SQLModule.CreateAutos(connection))
    AutosMenu.add_command(label="Listar", command=lambda:Listar(connection,"Autos"))
    AutosMenu.add_command(label="Eliminar Tabla", command=lambda:SQLModule.DropAutos(connection))

    ClientesMenu = tkinter.Menu(menubar, tearoff=0)
    ClientesMenu.add_command(label="Listar", command=lambda:ListarClientes(connection))

    EmpleadosMenu = tkinter.Menu(menubar, tearoff=0)
    EmpleadosMenu.add_command(label="Listar", command=lambda:SQLModule.ListarEmpleados(connection))

    FacturasMenu = tkinter.Menu(menubar, tearoff=0)
    FacturasMenu.add_command(label="Listar", command=lambda:SQLModule.ListarFacturas(connection))

    InventariosMenu = tkinter.Menu(menubar, tearoff=0)
    InventariosMenu.add_command(label="Listar", command=lambda:SQLModule.ListarInventarios(connection))

    OrdenComprasMenu = tkinter.Menu(menubar, tearoff=0)
    OrdenComprasMenu.add_command(label="Listar", command=lambda:SQLModule.ListarOrdenCompras(connection))

    menubar.add_cascade(label="Autos", menu=AutosMenu)
    menubar.add_cascade(label="Clientes", menu=ClientesMenu)
    menubar.add_cascade(label="Empleados", menu=ClientesMenu)
    menubar.add_cascade(label="Facturas", menu=ClientesMenu)
    menubar.add_cascade(label="Inventarios", menu=ClientesMenu)
    menubar.add_cascade(label="OrdenCompras", menu=ClientesMenu)

    interface.config(menu=menubar)

    return interface

def ListarClientes(connection):

    ClientesDF = SQLModule.ListarClientes(connection)
    display(ClientesDF)
    print(ClientesDF.iloc[0].tolist())


