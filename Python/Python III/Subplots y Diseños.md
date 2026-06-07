# 🎨 Subplots y Diseños Multi-Panel en Matplotlib

## 📝 Resumen y Análisis de la Transcripción de la Imagen
La imagen `subplots.png` ilustra el concepto fundamental de la arquitectura de Matplotlib basada en **múltiples paneles o subtramas (`subplots`)**. 

* **Estructura Jerárquica 🏛️:** Explica que una figura (`Figure`) actúa como el lienzo o contenedor global, mientras que los ejes (`Axes`) representan los gráficos o planos cartesianos individuales que viven dentro de ese lienzo.
* **Organización en Rejillas 🗺️:** Permite dividir un panel visual único en matrices organizadas por filas y columnas (por ejemplo, una cuadrícula de $2 \\times 1$, $2 \\times 2$, etc.). Esto es crucial en ingeniería y análisis de datos para comparar diferentes señales, variables o métricas simultáneamente sin mezclar líneas ni saturar un solo gráfico.
* **Independencia de Ejes 📏:** Cada ventana o subgráfico mantiene su propia identidad, lo que significa que puede tener sus propias escalas, títulos, etiquetas de eje y estilos de trazado independientes.

---

## ⚙️ Procedimientos Detallados y Análisis de Código

El script provisto implementa el enfoque **Orientado a Objetos (OO)** de Matplotlib, el cual es el método recomendado para manejar diseños complejos y profesionales.

### 1. Inicialización y Configuración del Estilo 🎨

```python

import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 1, 5, 2]
y2 = [5, 1, 3, 2, 4]

# Aplicación de estilo global
plt.style.use("ggplot")

```

* **Procedimiento:** Se definen los vectores numéricos para los ejes. La instrucción `plt.style.use("ggplot")` modifica de manera global el aspecto visual, añadiendo un fondo gris claro con cuadrícula blanca y tipografías estilizadas al estilo de la famosa biblioteca de R.

### 2. Creación de la Matriz de Subplots 🗂️

```python
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 5))

```

* **Procedimiento:** La función `plt.subplots()` se encarga de desempaquetar dos elementos vitales:
1. `fig`: La referencia al contenedor principal (la ventana completa).
2. `axes`: Un **arreglo (array) de objetos** que contiene cada uno de los subgráficos. Al pasarle `nrows=2` y `ncols=1`, el arreglo `axes` se vuelve unidimensional con una longitud de 2 elementos (`axes[0]` y `axes[1]`).


* El parámetro `figsize=(10, 5)` establece el ancho en 10 pulgadas y el alto en 5 pulgadas, ideal para proporciones panorámicas.



### 3. Trazado y Personalización por Subgráfico (Enfoque de Objetos) 🎯

Cuando se trabaja con subplots individuales, la sintaxis cambia ligeramente en comparación con las funciones directas de `plt`. Se deben usar los métodos del objeto `Axes` que lleven el prefijo `.set_`:

#### 🔹 Primer Subplot (`axes[0]` - Panel Superior)

```python
axes[0].plot(x, y1, color='blue')
axes[0].set_title('Subplot 1')
axes[0].set_xlabel('Eje X')
axes[0].set_ylabel('Eje Y')

```

* **Explicación:** Se accede al índice `0` del arreglo. Se dibuja la primera serie de datos en color azul. Para colocar texto, se usan específicamente los métodos `.set_title()`, `.set_xlabel()` y `.set_ylabel()`.

#### 🔸 Segundo Subplot (`axes[1]` - Panel Inferior)

```python
axes[1].plot(x, y2, color='red')
axes[1].set_title('Subplot 2')
axes[1].set_xlabel('Eje X')
axes[1].set_ylabel('Eje Y')

```

* **Explicación:** Se accede al índice `1`. Se dibuja la segunda serie de datos (curva roja) y se configuran de manera independiente sus respectivos textos y etiquetas de escala.

### 4. Optimización de Espacios y Renderizado 🚀

```python
# Ajustar automáticamente los espacios entre subplots
plt.tight_layout()

# Mostrar los subplots
plt.show()

```

* **Procedimiento Técnico Crítico:** Por defecto, al apilar gráficos verticalmente, los títulos del subgráfico inferior pueden superponerse o chocar con las etiquetas del eje X del gráfico superior. La función `plt.tight_layout()` calcula de forma automática los márgenes óptimos y distribuye el espacio limpio entre los paneles para evitar colisiones tipográficas. Finalmente, `plt.show()` renderiza la ventana final en pantalla.


### 📝 Resumen del Análisis de Imágenes y Código

El código y las imágenes compartidas abordan un concepto fundamental y ligeramente más avanzado dentro de la biblioteca: **El paradigma orientado a objetos (OO) y los `Subplots`** 🏗️.

* **La Ventana vs Los Planos 🖼️:** Nos enseña a diferenciar el lienzo principal (la figura entera representada en código como `fig`) y los cuadrantes individuales que viven dentro de ella (representados en el array `axes`). Esto permite crear "paneles de control" o tableros ("dashboards") organizados.
* **Manejo de Índices 🔢:** Al usar `fig, axes = plt.subplots(nrows=2, ncols=1)`, generamos dos ventanas de forma vertical. Para indicarle a Matplotlib sobre cuál ventana queremos dibujar, debemos "apuntar" utilizando los índices como en cualquier arreglo de Python: `axes[0]` para el gráfico de arriba y `axes[1]` para el de abajo.
* **Nueva Sintaxis (`.set_`) ⚙️:** Cuando trabajamos con `axes` individuales, los comandos globales como `plt.title()` y `plt.xlabel()` deben ser reemplazados por sus homólogos orientados a objetos, como `axes[0].set_title()` y `axes[0].set_xlabel()`.
* **Ajuste Espacial Automático 📐:** Es muy común que, al colocar varios gráficos juntos, las etiquetas de uno interfieran con las del otro. El código introduce un método crucial, `plt.tight_layout()`, que previene este desorden visual redimensionando dinámicamente los paneles para que los textos nunca choquen.

He documentado paso a paso el procedimiento de esta sintaxis orientada a objetos en el archivo adjunto para tener siempre a mano esta referencia al crear visualizaciones complejas de sistemas múltiples.

```python
import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 1, 5, 2]
y2 = [5, 1, 3, 2, 4]
plt.style.use("ggplot")

# Crear una figura y una cuadrícula de subplots (2 filas, 1 columna)
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 5))

# Plot en el primer subplot
axes[0].plot(x, y1, color='blue')
axes[0].set_title('Subplot 1')
axes[0].set_xlabel('Eje X')
axes[0].set_ylabel('Eje Y')

# Plot en el segundo subplot
axes[1].plot(x, y2, color='red')
axes[1].set_title('Subplot 2')
axes[1].set_xlabel('Eje X')
axes[1].set_ylabel('Eje Y')

# Ajustar automáticamente los espacios entre subplots
plt.tight_layout()

# Mostrar los subplots
plt.show() 


```
