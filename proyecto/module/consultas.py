import sqlite3
import pandas as pd

def consulta_general():
    connection = sqlite3.connect("valores.db")
    cursor=connection.cursor()
    
    rows=cursor.execute(""" select * from valores""").fetchall()
    
    valores = pd.DataFrame.from_records(rows,columns=[x[0] for x in cursor.description])
    
    print(valores)
    
    connection.close()
    return valores
