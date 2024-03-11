import pyodbc

def conectar():
    server = 'LAPTOP-JG6RLSQO'
    database = 'TiendaAxM'
    
    # Establece la conexión a la base de datos
    conn = pyodbc.connect(f'Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes;')
    
    return conn
