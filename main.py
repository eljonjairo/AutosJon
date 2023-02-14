#! /usr/bin/DataB/python3
# SQL Implementation
# 
# John Diaz january 2023 
# TO DO list:

# sql commands from all tables
import SQLModule  
import Interface

if __name__ == '__main__':

    connection = SQLModule.StartDBConnection()

    interface = Interface.StartInterface()

    login = Interface.UserLogin(interface,connection)
    #interface.mainloop()

    #SQLModule.DropTables(connection)
    #SQLModule.CreateTables(connection)
    #SQLModule.InsertData(connection)
    
