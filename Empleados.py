import pandas as pd

class Empleado():
    def __init__(self,nombre,cedula,clave,tipo):
        self.Id = None
        self.Nombre = nombre
        self.Cedula = cedula
        self.Clave = clave
        self.Tipo = tipo
       
    def __str__(self):
        return ' Empleado: ' + str(self.Id) + ' ' + self.Nombre + ' ' + str(self.Cedula) + ' ' + self.Clave + ' ' + self.Tipo


# Colocar otroas funciones para hacer más pequeño SQLModule 
