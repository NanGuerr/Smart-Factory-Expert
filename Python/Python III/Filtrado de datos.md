# 🛢️ Análisis de datos con Pandas y Seaborn

## 📝 Resumen Analítico
Este flujo de trabajo detalla un análisis completo (End-to-End) de un set de datos sobre la producción de petróleo en Argentina. Abarca desde la carga de un archivo CSV en bruto, pasando por el filtrado de columnas relevantes, la agregación matemática mediante agrupaciones (`groupby`), hasta llegar a una visualización profesional utilizando la librería Seaborn.

---

## 🛠️ Flujo de Trabajo (Pipeline de Datos)

### 1. Ingesta de Datos 📥
El primer paso es usar Pandas para leer un archivo separado por comas (CSV) que contiene los datos históricos de producción.

```python
import pandas as pd
df = pd.read_csv("PetroleoArg.csv")

```

### 2. Filtrado y Limpieza de Variables (Features) 🧹
Los datasets del mundo real suelen tener docenas de columnas innecesarias. Aquí se define una lista con las variables de interés y se recorta el DataFrame original para hacer el análisis más eficiente en memoria.

```python
columnas_interesantes = ["empresa", "anio", "mes", "provincia", "cantidad", "indice_tiempo", "areayacimiento",
                        "concepto", "cuenca"]
datos = df[columnas_interesantes]
datos.head() # Muestra las primeras 5 filas para verificar

```

### 3. Exploración Rápida (EDA) 🔍

Antes de avanzar, es vital entender la distribución de la base de datos. Usando `value_counts()` podemos generar un ranking automático de las empresas petroleras que más registros de producción tienen (la moda de los datos).

```python
datos.empresa.value_counts()

```

### 4. Consultas Específicas Avanzadas (`query` y `loc`) 🎯

Se muestran dos formas de filtrar datos bajo condiciones estrictas:

* **Uso de `.query()`:** Permite escribir filtros como si fuera una sentencia SQL, incluso inyectando variables externas de Python usando el símbolo `@` (ej. `@empresaTarget`).
```python
empresaTarget = "YPF S.A."
soloYPF = datos.query("empresa == @empresaTarget and provincia == 'Neuquén'")

```


* **Uso de `.loc[]`:** El método estándar y vectorizado para filtrar cronológicamente.

```python
df_filtrado = datos.loc[datos.anio >= 2021]

```

### 5. Agrupación y Agregación Estadística (`groupby`) 📊

Este es el motor de cálculo. Se agrupan los registros primero por Año y luego por Provincia. Finalmente, se calcula la media matemática (`.mean()`) de la columna `cantidad` (el volumen de petróleo) para cada subgrupo.

```python
promProvincia = df_filtrado.groupby(["anio", "provincia"]).cantidad.mean()
# reset_index "aplana" el resultado agrupado, convirtiendo el Multi-Índice en columnas normales de DataFrame,
#lo cual es obligatorio para Seaborn.

promProvincia = promProvincia.reset_index() 

```

### 6. Ordenamiento (`sort_values`) 🔀

Se ordenan los resultados de mayor a menor (`ascending=False`) basándose en el volumen promedio de producción. Esto asegura que, al graficar, las barras más altas se posicionen de forma lógica.

```python
promProvincia = promProvincia.sort_values(by="cantidad", ascending=False)

```

### 7. Visualización Científica con Seaborn 🎨

Seaborn es una librería de alto nivel que funciona sobre Matplotlib.

```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(15,6)) # Lienzo panorámico

# Se genera un gráfico de barras múltiples. 
# X = Año, Y = Volumen promedio. 
# El truco es 'hue="provincia"', que le dice a Seaborn que dibuje una barra separada (y con distinto color)
# para cada provincia dentro de cada año.

ax = sns.barplot(x="anio", y="cantidad", hue="provincia", data=promProvincia, lw=0)

plt.xlabel('Año')
plt.ylabel('Promedio de producción por provincia')

# plt.legend().remove() # (Opcional) Si la leyenda estorba, se comenta o descomenta.
# plt.savefig('PromedioEmpresas.png') # Exporta el gráfico como imagen.

plt.show() # Muestra el resultado final en pantalla

```

### 📝 Resumen del Caso Práctico

El material que proporcionaste ilustra un excelente ciclo de vida de **Ciencia de Datos** en miniatura, aplicado a un escenario real (producción petrolera en Argentina). 

Aquí están los conceptos y procedimientos clave que abarcan los códigos 🛢️:

* **Ingesta y Limpieza (ETL) 📥🧹:** Todo inicia leyendo un archivo externo `.csv`. Como suele ocurrir, este archivo contiene basura o datos que no nos sirven, así que el primer paso inteligente es recortarlo usando una lista de `columnas_interesantes`.
* **Sondeo Rápido 🔍:** Usando `value_counts()` echamos un vistazo para saber qué empresa es la jugadora principal en la base de datos antes de hacer cálculos profundos.
* **Filtrado Avanzado 🎯:** Nos enseña a usar `.query()`, que es una función fenomenal que nos permite filtrar datos usando una sintaxis que parece casi inglés puro, en contraste con el uso clásico de corchetes con `.loc` que usamos para recortar datos desde el año 2021 en adelante.
* **El Poder de `groupby` ⚙️:** El corazón matemático del ejercicio. Al decirle a Pandas "agrupa por Año y Provincia y calcula la media", el programa aplasta miles de filas en un resumen de unas cuantas líneas con el promedio de producción exacto por zona temporal y geográfica. El uso posterior de `reset_index()` es un truco vital de formato para evitar errores en las bibliotecas de gráficos.
* **Visualización de Alto Nivel 🎨:** Finalmente introduce `Seaborn`. Es mucho más potente que el `plot` clásico de Matplotlib para estos casos porque el atributo `hue="provincia"` se encarga mágicamente de agrupar, colorear y generar las barras por separado para cada provincia en el gráfico final. 

