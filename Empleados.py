import pandas as pd

class Empleado():
    def __init__(self,Id,nombre,cedula,clave,tipo):
        self.Id = None
        self.Nombre = nombre
        self.Cedula = cedula
        self.Clave = clave
        self.Tipo = tipo
       
    def __str__(self):
        return f " Empleado: [{self.id}.{self.Nombre},{self.Cedula},{self.Clave},{self.Tipo}] 




