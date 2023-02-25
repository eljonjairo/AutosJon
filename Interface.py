import tkinter as tk
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
        self.LoginUser()
        conexion = sql.DBConnect() 
        self.connection = conexion
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

        self.labelTipo = tk.Label( self, text = " Tipo : " ) 
        self.labelTipo.grid( row=4,column=0, padx=10, pady = 10 )         
       
        self.entryNombre = tk.Entry( self,width=30, borderwidth=3 )
        self.entryNombre.grid( row=1,column=1, padx=20, pady = 20 )         

        self.entryCedula = tk.Entry( self,width=30, borderwidth=3 )
        self.entryCedula.grid( row=2,column=1, padx=20, pady = 20 )         

        self.entryClave = tk.Entry( self,width=30, borderwidth=3, show="*")
        self.entryClave.grid( row=3,column=1, padx=20, pady = 20 )         

        self.entryTipo = tk.Entry( self,width=30, borderwidth=3 )
        self.entryTipo.grid( row=4,column=1, padx=20, pady = 20 )         

        self.loginButton = tk.Button( self, text="Ingresar",command = lambda: self.login() )
        self.loginButton.grid( row=5, column=0, columnspan=2,pady=30, padx=10, ipadx=100 )

        sql.writeDebug("    Interface LoginUser OUT")  

    def login(self):
        sql.writeDebug("    Interface login IN")  

        empleado = Empleados.Empleado( self.entryNombre.get(), self.entryCedula.get(), 
                                       self.entryClave.get(),self.entryTipo.get() )
        
        sql.writeDebug("   " + str(empleado)) 
        print(empleado)
        #Empleado = sql.CheckEmpleado(self.entryNombre.get(),self.entryClave.get(),self.connection)     
        # Veirificar si es Empleado y sacar el Tipo 
        sql.writeDebug("    Interface login OUT")  




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


