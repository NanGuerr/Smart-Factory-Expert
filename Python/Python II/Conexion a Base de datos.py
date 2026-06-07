import pyodbc # El nombre correcto es pyodbc, no pyhodbc

# 1. Configuración de parámetros
server = r'localhost\SQLEXPRESS' # Usa 'r' al principio por la barra invertida
database = "Main"
username = "admin"
password = "12345"

# 2. Construcción de la cadena de conexión
# Corregimos los corchetes del Driver y el nombre de la variable de base de datos
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # 3. Establecer la conexión
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    print("Conexión exitosa")

    # 4. Definición de la consulta (Corregimos el formato de la cadena)
    query = """
    SELECT Alarma, COUNT(Alarma) AS Cantidad 
    FROM PLC_02
    GROUP BY Alarma
    """

    cursor.execute(query)

    # 5. Iterar resultados (Corregimos el f-string y las variables)
    for nombre, cantidad in cursor:
        print(f"Tenemos {cantidad} sensores con estado {nombre}")

except Exception as e:
    print(f"Error al conectar o consultar: {e}")

finally:
    # 6. Siempre cerrar la conexión
    if 'connection' in locals():
        connection.close()
        print("Conexión cerrada.")
