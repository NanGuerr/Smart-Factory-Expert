# Controles Dashboard 🎛️

# 🎚️ Guía de Controles en Dashboards

## 1. ¿Qué son los controles?
Son componentes de la interfaz que actúan como "entradas" (inputs) para tu análisis de datos. Permiten filtrar, segmentar o ajustar la vista de los gráficos en tiempo real.

## 2. Tipos de Controles Comunes
* **Dropdown (Menú desplegable):** Ideal para seleccionar categorías (ej. elegir una provincia o empresa específica).
* **Slider (Deslizador):** Perfecto para rangos numéricos o selección de fechas.
* **RadioItems / Checklist:** Permiten selecciones binarias o múltiples para cambiar el modo de visualización.
* **DatePicker:** Específico para filtrar series temporales por rangos de fechas precisos.

## 3. Lógica de Funcionamiento (Callback Decorators)
La magia ocurre mediante **decoradores** (como `@app.callback` en Dash o los `@mi_decorador` en tu ejemplo). 
* **Input:** El componente que dispara la acción (ej. un Dropdown con id='ciudad-selector').
* **Output:** El gráfico o tabla que se actualiza automáticamente.
* **Proceso:** Cuando el `Input` cambia, la función asociada se ejecuta, procesa el DataFrame con el nuevo filtro y devuelve el `Output` actualizado.

## 4. Ejemplo de Implementación Estructural

```python
# Decorador que "escucha" el cambio en un control
@app.callback(
    Output('grafico-principal', 'figure'),
    Input('selector-anio', 'value')
)
def actualizar_grafico(anio_seleccionado):
    # Filtrar datos basado en el control
    df_filtrado = df[df['anio'] == anio_seleccionado]
    # Retornar nueva figura
    return px.line(df_filtrado, x='mes', y='produccion')

```

Los controles en un Dashboard son los elementos que permiten al usuario final interactuar con la información, transformando visualizaciones estáticas en herramientas dinámicas de análisis 🎛️.

### 📝 Resumen Analítico

La interactividad en un tablero de control (como los desarrollados con Dash o Streamlit) se basa en **callbacks** o funciones que se ejecutan automáticamente ante un evento del usuario. El código que compartiste sobre "decoradores" es precisamente la base técnica de cómo funcionan estos controles: cuando un usuario mueve un deslizador o elige un valor en un menú, el sistema "decora" o intercepta esa acción para actualizar el gráfico sin recargar toda la página.

---

### 💡 Nota técnica sobre tu código
El ejemplo que enviaste sobre `mi_decorador` ilustra perfectamente cómo los frameworks de Dashboards encapsulan la lógica: el decorador `@mi_decorador` "envuelve" a tu función `saludar` para ejecutar código extra (el filtrado de datos) antes y después de que la función principal (dibujar el gráfico) realice su trabajo. ¿Te gustaría ver cómo conectar un Dropdown real de un archivo CSV con un gráfico de Seaborn usando esta lógica?


```python

def saludar(nombre):
    print("¡Hola!", nombre)

saludar("Ignacio")

def mi_decorador(parametro):
    def decorador(func):
        def envoltura():
            print(f"Antes {parametro}")
            func()
            print(f"Después {parametro}")
        return envoltura
    return decorador

@mi_decorador(parametro="texto")
def saludar():
    print("¡Hola!")
saludar()

```

# ⚡ Callbacks en Dashboards

## 1. Estructura de un Callback
Un callback se define mediante el decorador `@callback`. Es obligatorio seguir el orden: **primero las salidas (Output) y luego las entradas (Input).**

```python
@callback(
    Output(component_id='grafico', component_property='figure'),
    Input(component_id='selectora', component_property='value')
)
def mi_funcion(valor_entrada):
    # Lógica de filtrado de datos
    fig = px.histogram(datos, x='columna', y=valor_entrada)
    return fig

```

## 2. Controles Más Utilizados (Core Components)

* **`dcc.RadioItems`**: Ideal para selecciones únicas y rápidas (ej. cambiar entre tipo de gráfico).
* **`dcc.Dropdown`**: Selección simple o múltiple, perfecto para listas largas de categorías.
* **`dcc.Slider`**: Manejo de rangos numéricos continuos.
* **`dcc.Checklist`**: Selección múltiple.
* **`dcc.DatePicker`**: Gestión de rangos temporales o fechas únicas.

## 3. Componentes Avanzados

* **`dcc.Interval`**: Dispara callbacks automáticamente en bucle (ideal para dashboards de monitoreo en tiempo real).
* **`dcc.Store`**: Permite guardar datos en el navegador del cliente para no tener que procesar la misma información repetidamente.
* **`dcc.Upload`**: Permite al usuario final cargar sus propios archivos (como CSVs) para visualizarlos en el momento.

## 4. Buenas Prácticas

* **IDs Únicos**: Cada componente (`dcc` o `html`) debe tener un `id` único.
* **Manejo de estados**: Utiliza `n_clicks` en botones o el estado de los componentes para controlar cuándo se deben ejecutar procesos pesados.
* **Eficiencia**: Si un gráfico tarda mucho, usa `dcc.Loading` para notificar al usuario que el callback está procesando la información.

### 💡 Nota técnica
El decorador `@callback` no es solo código; es un **puente de comunicación**. Cuando el usuario interactúa con un `Input`, Dash captura el nuevo valor, lo pasa como argumento a tu función, y el `Output` toma el valor de retorno de esa función para redibujar el componente en el navegador en milisegundos. ¿Te gustaría crear un ejemplo donde un `Slider` y un `Dropdown` controlen simultáneamente un solo gráfico?

Los **callbacks** son el motor de interactividad en cualquier aplicación de Dash. Permiten que los componentes de tu interfaz (como un menú desplegable) "se comuniquen" con los gráficos de forma dinámica. 🔄

### 📝 Resumen Analítico

La estructura de un callback es el corazón de la arquitectura de eventos en Dash. Consta de tres elementos indispensables:

1. **Entradas (`Input`):** El componente que observa el usuario (un botón, un slider, un radio button). Cuando este cambia, el callback se dispara automáticamente.
2. **Salidas (`Output`):** El componente que se actualiza tras la interacción (un gráfico, un texto, una tabla).
3. **Función Decorada:** La lógica matemática o de filtrado que conecta el *Input* con el *Output*.

---

# App con gráficos + controles 🎛️

```python

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
​
app = Dash(__name__)
app.layout = html.Div([
    html.Div(children='Mi app con datos, gráfico y controles'),
    html.Hr(),
    dcc.RadioItems(options=['weight', 'horsepower', 'displacement'], value='horsepower', id='selectora'),
    dash_table.DataTable(data=datos.to_dict('records'), page_size=6),
    dcc.Graph(figure={}, id='grafico')
])
​
# -------------------------------------------------------------
@callback(
    # PRIMERO las salidas
    Output(component_id='grafico', component_property='figure'),
    # DESPUES las entradas
    Input(component_id='selectora', component_property='value')
)
def crear_grafico(col_seleccionada):
    fig = px.histogram(datos, x='model_year', y=col_seleccionada, histfunc='avg')
    return fig
# -------------------------------------------------------------
​
if __name__ == '__main__':
    app.run(debug=True)

    ```
