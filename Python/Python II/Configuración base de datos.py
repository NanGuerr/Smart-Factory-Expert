from google.oauth2 import service_account
from google.cloud import bigquery

# Configuración de credenciales
archivoCredenciales = "ingelearn-cloud-fc0b55d52874.json"
proyecto = "ingelearn-cloud"
base = "ingelearn_base"

credenciales = service_account.Credentials.from_service_account_file(archivoCredenciales)

# Creación del cliente
cliente = bigquery.Client(credentials=credenciales)

dataset_ref = cliente.dataset(base, proyecto)
dataset = cliente.get_dataset(dataset_ref)

# Listar tablas disponibles
tables = list(cliente.list_tables(dataset))
for tabla in tables:
    print(tabla.table_id)
