#! /usr/bin/DataB/python3
# SQL Implementation
# 
# John Diaz january 2023 
# TO DO list:

# sql commands from all tables
import tkinter as tk
import Interface as inter
import SQLModule as sql

def startInterface():
    root = tk.Tk()
    root.title(" JonAutos ")
    root.resizable(0,0)

    interface = inter.Interface(root = root)
    interface.mainloop()

if __name__ == '__main__':

    #connexion = sql.DBConnection()
    #connexion.DBConnect()    

    #SQLModule.DropTables(connection)
    #SQLModule.CreateTables(connection)
    #SQLModule.InsertData(connection)
    
    startInterface()

