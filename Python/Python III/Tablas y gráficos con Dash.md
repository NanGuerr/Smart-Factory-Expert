# 🗄️ Tablas Interactivas (DataTable)

## 1. Estructura de Datos
* **`data`**: Entrada principal. Debe ser una lista de diccionarios (usualmente `df.to_dict('records')`).
* **`columns`**: Define el esquema. Lista de diccionarios con `name` (etiqueta visible) y `id` (referencia al dato).

## 2. Estilos (CSS Dinámico)
El diseño se controla mediante diccionarios CSS aplicados a diferentes niveles:
* **`style_table`**: Estilo del contenedor (ej. `{'overflowX': 'auto'}` para permitir scroll horizontal).
* **`style_cell`**: Estilo global de la celda (ej. alineación, padding).
* **`style_header`**: Diseño del encabezado (ej. color de fondo, negritas).
* **`style_data`**: Diseño específico de las filas de datos.

## 3. Controles de Interactividad
* **Filtrado (`filter_action`)**: Permite que el usuario escriba criterios de búsqueda. 
    * `native`: El filtro ocurre automáticamente sin recargar la página.
* **Ordenamiento (`sort_action`)**: 
    * `sort_mode='single'` (una columna) o `'multi'` (varias columnas).
* **Selección y Edición**:
    * **`row_selectable`**: Activa checkboxes (`'multi'`) o selección única (`'single'`).
    * **`editable`**: Si es `True`, permite que el usuario modifique celdas directamente en la interfaz.
    * **`row_deletable`**: Permite eliminar filas al vuelo.

## 4. Gestión de Visualización
* **`page_size`**: Define la cantidad de registros por página para mantener el rendimiento alto en datasets extensos.

Los componentes de tablas interactivas (comúnmente asociados a librerías como *Dash DataTable*) son fundamentales para que los usuarios finales no solo visualicen datos, sino que también interactúen con ellos. A continuación, presento el resumen estructurado y el archivo `.md` con la guía de configuración.

### 📝 Resumen Analítico

La configuración de tablas interactivas se divide en tres pilares:

1. **Datos y Estructura:** `data` y `columns` definen el contenido base, transformando DataFrames de Pandas en objetos JSON que el frontend entiende.
2. **Estilo (CSS):** Mediante diccionarios (`style_header`, `style_data`, `style_cell`), puedes aplicar diseño profesional (colores, alineación, negritas) de forma modular.
3. **Interactividad:** Parámetros como `filter_action`, `sort_action` y `editable` transforman una tabla estática en una herramienta de análisis dinámico donde el usuario puede buscar, ordenar, modificar y seleccionar registros en tiempo real.

Plotly Express es una herramienta de visualización de alto nivel diseñada para que el análisis de datos sea rápido, interactivo y estéticamente profesional. A diferencia de bibliotecas más estáticas, Plotly permite que el usuario final pueda hacer zoom, filtrar y consultar valores directamente sobre el gráfico 📈.

### 📝 Resumen Analítico

La librería se organiza mediante métodos (`px.metodo`) que esperan como entrada principal un DataFrame de Pandas. Los parámetros clave suelen ser siempre los mismos, lo que reduce la curva de aprendizaje:

* **`x`, `y**`: Los ejes cartesianos.
* **`color`**: Permite segmentar visualmente los datos por categorías.
* **`size` / `values**`: Define la magnitud de los elementos.
* **`title`**: Etiquetado del gráfico.

---

# 📊 Gráficos Comunes en Plotly Express

## 1. Gráficos de Evolución y Tendencia
* **Línea (`px.line`)**: Ideal para series temporales. Muestra cómo cambia una variable respecto al tiempo.
* **Área (`px.area`)**: Similar a la línea, pero rellena el espacio inferior, útil para enfatizar la magnitud total.

## 2. Gráficos de Comparación
* **Barras (`px.bar`)**: La forma estándar de comparar cantidades entre categorías. Se puede usar `barmode="group"` para comparar grupos lado a lado.

## 3. Gráficos de Distribución Estadística
* **Dispersión (`px.scatter`)**: Revela correlaciones entre dos variables continuas. Soporta dimensiones adicionales con `size` (tamaño) y `color`.
* **Histograma (`px.histogram`)**: Muestra la frecuencia de datos en rangos (bins).
* **Caja (`px.box`)**: Esencial para detectar valores atípicos (outliers) y ver la mediana y cuartiles de un set de datos.

## 4. Gráficos de Composición y Jerarquía
* **Pastel (`px.pie`)**: Visualiza la proporción de una variable frente a un total.
* **Treemap (`px.treemap`)**: Representa estructuras jerárquicas (ej. Países > Ciudades) mediante rectángulos anidados.

## 5. Visualización Especializada
* **Mapa de calor (`px.density_heatmap`)**: Cruza dos variables categóricas o numéricas y usa la intensidad de color para representar la magnitud de una tercera variable.
* **Mapa Geoespacial (`px.scatter_geo`)**: Proyecta puntos sobre un mapa mundial utilizando coordenadas de latitud y longitud.

# Tablas 📊

```python

import seaborn as sns
import pandas as pd
datos = sns.load_dataset("mpg")

from dash import Dash, html, dash_table

app = Dash(__name__)
columnas = [{"name": i, 'id'} for i in datos.columns]
app.layout = html.Div([
    html.H1(children='Mi primer app con datos'),
    dash_table.DataTable(data=datos.to_dict('records'), page_size=15, sort_action="native",filter_action="native"),
])

if __name__ == '__main__':
    app.run(debug=True)

```

# Gráficos 📉

```python

import seaborn as sns
import pandas as pd
datos = sns.load_dataset("mpg")

from dash import Dash, html, dash_table, dcc
import plotly.express as px
app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Mi primer app con datos'),
    dash_table.DataTable(data=datos.to_dict('records'), page_size=15),
    dcc.Graph(figure=px.histogram(datos, x="model_year",y="horsepower",histfunc="avg"))
])

if __name__ == '__main__':
    app.run(debug=True)

```
