import tkinter
import SQLModule
import pandas as pd


def StartInterface(): 
    interface = tkinter.Tk()
    interface.title("JonAutos Interface")
    interface.geometry("800x600")

    return(interface)

def InterfaceUsuario(Usuario,connection):

    interface = tkinter.Tk()
    interface.title("JonAutos Interface")
    interface.geometry("1800x600")

    # Font Size
    FSize = 15
    WSize = 15

    nombre = Usuario["Nombre"][0]
    cedula = Usuario["Cedula"][0]
    cargo = Usuario["Tipo"][0]

    Sucursal = SQLModule.UsuarioSucursal(cedula,connection)
    SucName = Sucursal["NombreSucursal"][0]

    user = " Usuario:  %s  Identificacion:  %s  Cargo:  %s  Sucursal:  %s " %(nombre,cedula,cargo,SucName)

    UserLabel = tkinter.Label(interface, text = user )
    UserLabel.grid(row=0, column=0, columnspan=5, pady=20, padx=10, ipadx=100 )
    UserLabel.config(font=("Arial", 20))

    # Optionmenu for each table modifications
    strAutos = tkinter.StringVar()
    strAutos.set(" Auto ") 
    menuAutos = tkinter.OptionMenu(interface,strAutos," Agregar Auto "," Borrar Auto ", " Listar Auto ")
    menuAutos.grid(row=1,column=0)
    menuAutos.config(font=("Arial", FSize),width=WSize)
 
    strBodega = tkinter.StringVar()
    strBodega.set(" Bodega") 
    menuBodega = tkinter.OptionMenu(interface,strBodega," Agregar Bodega"," Borrar Bodega", " Listar Bodega")
    menuBodega.grid(row=1,column=1)
    menuBodega.config(font=("Arial", FSize),width=WSize)

    strCliente = tkinter.StringVar()
    strCliente.set(" Cliente") 
    menuCliente = tkinter.OptionMenu(interface,strCliente," Agregar Cliente"," Borrar Cliente", " Listar Cliente")
    menuCliente.grid(row=1,column=2)
    menuCliente.config(font=("Arial", FSize),width=WSize)

    strFactura = tkinter.StringVar()
    strFactura.set(" Factura") 
    menuFactura = tkinter.OptionMenu(interface,strFactura," Agregar Factura"," Borrar Factura", " Listar Factura")
    menuFactura.grid(row=1,column=3)
    menuFactura.config(font=("Arial", FSize),width=WSize)
 
    strInvSala = tkinter.StringVar()
    strInvSala.set(" Cliente") 
    menuInvSala = tkinter.OptionMenu(interface,strInvSala," Agregar Inverntario Sala"," Borrar Inverntario Sala", " Listar Inverntario Sala")
    menuInvSala.grid(row=1,column=4)
    menuInvSala.config(font=("Arial", FSize),width=WSize)

    strOrdBodSala = tkinter.StringVar()
    strOrdBodSala.set(" OrdenBodegaSala") 
    menuOrdBodSala = tkinter.OptionMenu(interface,strOrdBodSala," Agregar OrdenBodegaSala"," Borrar OrdenBodegaSala", " Listar OrdenBodegaSala")
    menuOrdBodSala.grid(row=1,column=5)
    menuOrdBodSala.config(font=("Arial", FSize),width=WSize)

    strSalaVentas = tkinter.StringVar()
    strSalaVentas.set(" SalaVentas") 
    menuSalaVentas = tkinter.OptionMenu(interface,strSalaVentas," Agregar SalaVentas"," Borrar SalaVentas", " Listar SalaVentas")
    menuSalaVentas.grid(row=1,column=6)
    menuSalaVentas.config(font=("Arial", FSize),width=WSize)

    strSucursal = tkinter.StringVar()
    strSucursal.set(" Sucursal") 
    menuSucursal = tkinter.OptionMenu(interface,strSucursal," Agregar Sucursal"," Borrar Sucursal", " Listar Sucursal")
    menuSucursal.grid(row=1,column=7)
    menuSucursal.config(font=("Arial", FSize),width=WSize)

    strUsuario = tkinter.StringVar()
    strUsuario.set(" Usuario") 
    menuUsuario = tkinter.OptionMenu(interface,strUsuario," Agregar Usuario"," Borrar Usuario", " Listar Usuario")
    menuUsuario.grid(row=1,column=8)
    menuUsuario.config(font=("Arial", FSize),width=WSize)

    strVendedor = tkinter.StringVar()
    strVendedor.set(" Vendedor") 
    menuVendedor = tkinter.OptionMenu(interface,strVendedor," Agregar Vendedor"," Borrar Vendedor", " Listar Vendedor")
    menuVendedor.grid(row=1,column=9)
    menuVendedor.config(font=("Arial", FSize),width=WSize)

    return(interface)



def UserMenu(interface):
    click = tkinter.StringVar()
    click.set( " Usuario " )
    menu = tkinter.OptionMenu( interface, click, "Gerente General", "Gerente Sucursal" )
    menu.grid( row=0, column=0, padx=30, pady = 20 )   
 
    return menu

def login(interface, Name, Key, connection):

    Usuario = SQLModule.CheckUsuario(Name.get(),Key.get(),connection)     
  
    n = Usuario["Nombre"].size

    if n == 1: 
        output = " "
        interface.destroy()
        interface = InterfaceUsuario(Usuario,connection)
 
    elif n > 1:
        output = " Más de un usuario con este Nombre y Clave "

    else:
        output = " Nombre o Clave incorrectas "

    loginLabel = tkinter.Label(interface, text = output )
    loginLabel.grid(row=5, column=0, columnspan=2,pady=20, padx=10, ipadx=100 )
    loginLabel.config(font=("Arial", 20))

def UserLogin(interface,connection):
    Name = tkinter.Entry( interface, width=30, borderwidth=3, font=("Arial", 20) )
    Name.grid(row=1, column=1, pady=30)
    Key = tkinter.Entry( interface, width=30, borderwidth=3, show="*", font=("Arial", 20) )
    Key.grid(row=2, column=1, pady=30)

    NameLabel = tkinter.Label( interface, text=" Nombre Usuario ", font=("Arial", 20) )
    NameLabel.grid(row=1,column=0)
    KeyLabel = tkinter.Label( interface, text=" Clave Usuario ", font=("Arial", 20) )
    KeyLabel.grid(row=2,column=0)

    loginButton = tkinter.Button( interface, text="Ingresar", font=("Arial", 20),
    command = lambda: login( interface,Name,Key,connection ) )
    loginButton.grid(row=3, column=0, columnspan=2,pady=30, padx=10, ipadx=100)

    interface.mainloop()

