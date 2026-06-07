import pyodbc

# Configura la conexión a tu SQL Server local
server = ___
database = ___
username = ___
password = ___

connection_string = f'Driver={{SQL Server}};Server={server};Database={database};UID={username};PWD={password}'

# Conecta a la base de datos
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()
# Ejemplo de consulta SELECT
query = """
SELECT * FROM PLC_01  
"""
cursor.execute(query)
# Imprime los resultados
for row in cursor:
    print(row)

# Cierra la conexión
connection.close()
