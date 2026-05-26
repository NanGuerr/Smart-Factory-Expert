# Automatización en BigQuery con Python 🐍📊

Este documento resume el flujo de trabajo para interactuar con bases de datos de Google BigQuery utilizando Python, facilitando la gestión automatizada de datos desde aplicaciones o dispositivos (como PLCs).

## 1. Preparación del Entorno 🛠️
Antes de ejecutar el código, es fundamental instalar las dependencias necesarias para la autenticación y conexión con Google Cloud:

```python

pip install google-auth google-cloud google-cloud-bigquery google-api-core

```

## 2. Conexión y Autenticación 🔑
El proceso se inicia cargando las credenciales desde un archivo `.json` de cuenta de servicio, permitiendo al cliente de BigQuery establecer una sesión segura con el proyecto y el conjunto de datos (*dataset*) especificado.

## 3. Operaciones Principales 🔄
* **Exploración:** Listado de tablas existentes dentro del conjunto de datos y verificación del esquema (*schema*) de una tabla seleccionada (ej. tabla "PLC").
* **Escritura (Inserción de Datos):** Automatización de la inserción de registros (filas) utilizando `insert_rows_json`. Se capturan datos como fecha/hora actual, setpoints y temperaturas, validando la operación mediante la respuesta de error del sistema.
* **Lectura (Consultas):** Ejecución de sentencias SQL (`SELECT * FROM ...`) para extraer información histórica, transformando los resultados en diccionarios de Python para su posterior procesamiento o visualización.

---
*Resumen técnico del flujo de datos entre Python y BigQuery.*

```python
from google.oauth2 import service_account
from google.cloud import bigquery
from datetime import datetime

# 1. Configuración de credenciales y conexión
archivoCredenciales = "ruta/a/tu/archivo_de_servicio.json"
proyecto = "tu-id-de-proyecto"
base = "tu_dataset_id" # El nombre de tu conjunto de datos en BigQuery

# Crear el cliente de BigQuery
credenciales = service_account.Credentials.from_service_account_file(archivoCredenciales)
cliente = bigquery.Client(credentials=credenciales, project=proyecto)

dataset_ref = cliente.dataset(base)

# 2. Exploración de tablas (Opcional)
print("Tablas en el dataset:")
tables = list(cliente.list_tables(dataset_ref))
for tabla in tables:
    print(f"- {tabla.table_id}")

# 3. Inserción de datos
nombre_tabla = "PLC" # Nombre de la tabla destino
tabla_ref = dataset_ref.table(nombre_tabla)
tabla = cliente.get_table(tabla_ref)

# Preparar los datos
now = datetime.now().isoformat() # Formato ISO para BigQuery
rows_to_insert = [
    {
        "FechayHora": now,
        "Setpoint": 10.0,
        "Temperatura": 30.0,
        "Salida_H": 10.0,
        "Salida_L": 0.0,
    }
]

# Ejecutar inserción
errors = cliente.insert_rows_json(tabla, rows_to_insert)
if errors == []:
    print("\n✅ Filas añadidas exitosamente.")
else:
    print(f"\n❌ Errores al insertar la fila: {errors}")

# 4. Lectura de valores (Consulta SQL)
print("\n--- Lectura de datos ---")
query = f"SELECT * FROM `{proyecto}.{base}.{nombre_tabla}` LIMIT 10;"
query_job = cliente.query(query)

for fila in query_job.result():
    # Acceder a los datos por nombre de columna
    print(f"Fecha: {fila['FechayHora']} | Setpoint: {fila['Setpoint']} | Temp: {fila['Temperatura']}")
```

### Puntos clave para que no falle:

* Formato de Fecha: He añadido .isoformat() a la fecha. BigQuery prefiere el formato YYYY-MM-DDTHH:MM:SS, que es el estándar de Python.

* Ruta del archivo: Asegúrate de que el archivo .json de la cuenta de servicio esté en la misma carpeta que tu script o coloca la ruta absoluta completa.

* Permisos (IAM): La cuenta de servicio (el usuario del archivo JSON) debe tener al menos los roles de BigQuery Data Editor y BigQuery User en tu proyecto de Google Cloud.
