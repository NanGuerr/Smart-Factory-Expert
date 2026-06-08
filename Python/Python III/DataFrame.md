# ℹ️ DataFrame

```python

import pandas as pd
import numpy as np
​
# Datos simulados de sensores
data = {
    'Tiempo': ['2023-08-01 08:00', '2023-08-01 09:00', '2023-08-01 10:00', '2023-08-01 11:00',
    '2023-08-01 12:00', '2023-08-01 13:00'],
    'Sensor': ['FT-001', 'FT-002', 'FT-001', 'FT-002', 'FT-001', 'FT-002'],
    'Temperatura (C)': [35.2, 36.5, 34.8, 37.2, 33.6, 37.9],
    'Presión (bar)': [2.1, 2.0, 2.2, 1.9, 2.5, 1.8]
}
​
# Crear un DataFrame a partir de los datos

df = pd.DataFrame(data)

```

# Creando una Serie

```python

import pandas as pd
import numpy as np
​
miLista = ["A", "B", "C", "D", "E"]
indices = ["uno","dos","tres","cuatro", "cinco"]
​
serie = pd.Series(miLista, index=indices)
serie["cinco"]

```

# Importar datos

```python

import pandas as pd

df = pd.read_csv("PetroleoArg.csv")

# Vemos la cantidad de filas y columnas.
df.shape

# Si queremos leer una columna, simplemente la "seleccionamos" con el .
df.head()

# Si queremos leer una columna, simplemente la "seleccionamos" con el .
df.cantidad

# Algunos métodos útiles de los Dataframes:

#mean:

df.mean(axis=0)

# median: Calcula la mediana de cada columna o fila
df.median(axis=0)

# mode: Calcula la moda de cada columna
df.mode()

# std: Calcula la desviación estándar de cada columna o fila
df.std(axis=0)

# sum: Calcula la suma de los elementos de cada columna o fila
df.sum(axis=0)


# min: Encuentra el valor mínimo de cada columna o fila
df.min(axis=0)

# max: Encuentra el valor máximo de cada columna o fila
df.max(axis=0)

# count: Cuenta el número de elementos no nulos en cada columna
df.count(axis=0)

# Descripción: Genera estadísticas descriptivas sobre el DataFrame
df.describe()

# Filtramos las columnas que nos interesan, creando una lista con las etiquetas que queremos.
columnas_interesantes = ["empresa","anio","mes","provincia","cantidad","indice_tiempo","areayacimiento",
"concepto","cuenca"]


datos = df[columnas_interesantes]
datos.head()

# unique:  nos devuelve las etiquetas únicas presentes en una fila (ej.: ¿cuáles son las regiones que aparecen
en esta columna?)
df.provincia.unique()


# value_counts: nos da las etiquetas únicas, y la cantidad de repeticiones de cada uno
df.provincia.value_counts()

```
