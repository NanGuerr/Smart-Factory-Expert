# 🐼 Pandas y Análisis de Datos

## 📝 Resumen Analítico
La librería **Pandas** es la herramienta estándar en Python para la limpieza, manipulación y análisis de datos. Se fundamenta sobre la arquitectura de **NumPy**, aprovechando su velocidad computacional pero añadiendo una capa de usabilidad crucial: la capacidad de trabajar con datos tabulares etiquetados (texto, fechas y números mezclados).

---

## 🏗️ 1. Estructuras de Datos Principales
Pandas divide la información en dos estructuras fundamentales, dependiendo de sus dimensiones:

* **Series (1D):** 📏 Es un arreglo unidimensional. Puedes imaginarlo como una sola columna de Excel o una simple lista de Python, pero con un "índice" explícito (una etiqueta para cada fila).
* **DataFrames (2D):** 📊 Es una estructura bidimensional compuesta por múltiples Series. Es el equivalente exacto a una hoja de cálculo completa o a una tabla de base de datos SQL. Tiene filas (índices), columnas (cabeceras) y los datos en sí.

---

## ⚙️ 2. Procedimiento: Creación y Manejo de DataFrames
Para trabajar con DataFrames, el flujo de trabajo estándar consiste en estructurar primero la información en bruto y luego convertirla al formato tabular.

### Paso 1: Importar la librería
Por convención universal, Pandas se importa con el alias `pd`.

```python
import pandas as pd

```

### Paso 2: Estructurar los datos base
La forma más común de crear un DataFrame desde cero es utilizando un diccionario de Python (`dict`), donde las **claves** (`keys`) serán los nombres de las columnas y los **valores** (`values`) serán listas con los datos correspondientes.

```python
dic = {
    'Nombres': ['Ana', 'Juan', 'Luis', 'María', 'Pedro'],
    'Edades': [22, 25, 20, 23, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao']
}


```

### Paso 3: Instanciar el DataFrame

Se utiliza la función `pd.DataFrame()` pasando el diccionario como argumento.

```python
df = pd.DataFrame(dic)
print(df)

```

*Resultado esperado:* Una tabla perfectamente formateada con índices numéricos automáticos a la izquierda.

### Paso 4: Extracción de Columnas 🔍

Para aislar una variable específica y analizarla por separado (lo cual devuelve una estructura tipo **Series**), se llama al DataFrame usando corchetes y el nombre exacto de la columna como string.

```python
edades = df['Edades']
print(edades)

```

### 📝 Resumen del Contenido de las Imágenes

El material subido introduce la transición del cálculo numérico puro hacia la manipulación de datos estructurados utilizando la librería **Pandas** 🐼.

* **El Puente entre NumPy y Pandas 🤝:** Las imágenes resaltan que Pandas no reemplaza a NumPy, sino que se construye *sobre* él. Mientras NumPy es excelente para hacer matemáticas rápidas con matrices invisibles, Pandas envuelve esas matrices y les pone nombres de columnas e índices. Esto permite limpiar y preparar datos del mundo real (que a menudo mezclan texto, números y fechas).

* **La Anatomía de los Datos 🏗️:** Se definen los dos bloques de construcción principales:
    * **Series:** Un arreglo de una sola dimensión (1D). Básicamente, una sola columna de datos.
    * **DataFrames:** Un arreglo de dos dimensiones (2D). Es la estructura estrella de Pandas, comportándose exactamente como una tabla relacional o una hoja de Excel, compuesta por índices (filas), columnas y celdas de datos.

* **Sintaxis Práctica 💻:** Se demuestra el procedimiento estándar para inyectar datos en un DataFrame. Consiste en declarar un diccionario en Python (`{}`) donde la clave es el título de la columna y el valor es una lista con los registros. Luego, al pasar este diccionario por `pd.DataFrame()`, se genera automáticamente la tabla. Finalmente, muestra cómo extraer una columna individual escribiendo su nombre entre corchetes, por ejemplo: `df['Edades']`.

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
