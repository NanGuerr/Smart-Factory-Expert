# 📊 Análisis Detallado y Procedimientos con Matplotlib

En este documento se detalla el funcionamiento y la aplicación de los diferentes tipos de gráficos mostrados en las imágenes y en los fragmentos de código, utilizando la biblioteca `matplotlib.pyplot`.

---

## 📈 1. Gráficos de Líneas y Múltiples Ecuaciones

A partir de las imágenes analizadas, se observa que Matplotlib permite graficar funciones matemáticas iterando sobre un rango de valores.

* **Gráfico por defecto:** Al utilizar `plt.plot(valores)`, Matplotlib asume por defecto un **gráfico de líneas**. Es ideal para mostrar la evolución de datos continuos.
* **Múltiples líneas:** Para visualizar más de una función (por ejemplo, una curva exponencial y una cuadrática) en el mismo lienzo, basta con invocar `plt.plot()` varias veces antes de llamar a `plt.show()`. Esto superpone las curvas en los mismos ejes, permitiendo comparar su crecimiento.

---

## 🔵 2. Gráficos de Dispersión (Scatter Plots)

El gráfico de dispersión (`plt.scatter`) es sumamente útil para representar distribuciones conjuntas y visualizar rápidamente relaciones o tendencias entre dos conjuntos de variables (ejes X e Y). 

### Código Analizado:

```

```text
Archivo generado exitosamente.

```python
import matplotlib.pyplot as plt

Temperaturas1 = [27.1, 22.3, 26.8, 23.5, 22.7, 15.3, 26.6, 16.9, 18.1, 24.7, 23.8, 18.4, 26.1, 27.5, 27.3, 21.9, 25.4, 25.1, 20.4, 16.2, 27.5]
Temperaturas2 = [25.4, 21.5, 27.3, 25.5, 20.2, 26.6, 16.1, 27.7, 26.4, 24.0, 22.6, 19.4, 27.0, 18.3, 25.0, 24.3, 25.6, 27.1, 15.6, 27.1, 26.6]

plt.scatter(Temperaturas1, Temperaturas2)
# plt.show() # Para visualizar el resultado final

```

### Procedimiento y Análisis:

1. **Datos:** Se definen dos listas numéricas (`Temperaturas1` y `Temperaturas2`) de la misma longitud. Cada índice corresponde a un punto en el plano cartesiano `(x, y)`.
2. **Invocación:** Se utiliza `plt.scatter(x, y)`.
3. **Interpretación visual:** En lugar de conectar los puntos con una línea, este gráfico dibuja un punto individual para cada par de coordenadas. Como indica la imagen de referencia, esto nos permite ver dónde se "agrupan" los puntos e identificar visualmente los conjuntos de valores más comunes o si existe alguna correlación lineal entre ambas mediciones de temperatura.

---

## 📊 3. Gráficos de Barras (Bar Charts)

El gráfico de barras (`plt.bar`) es la herramienta predilecta para representar cantidades o categorías discretas de forma rectangular. Permite una comparación visual muy rápida de magnitudes entre diferentes grupos.

### Código Analizado:

```python
import matplotlib.pyplot as plt

productos_stock = {'producto1': 15, 'producto2': 7, 'producto3': 11, 'producto4': 5}

# Extracción de categorías y valores
productos = productos_stock.keys()
cantidades = productos_stock.values()

plt.bar(productos, cantidades)
# plt.show() # Para visualizar el resultado final

```

### Procedimiento y Análisis:

1. **Estructura de Datos:** Se emplea un diccionario `productos_stock` donde la clave (`key`) es el nombre de la categoría (el producto) y el valor (`value`) es la magnitud a graficar (el stock disponible).
2. **Extracción de Ejes:** * Se asigna a la variable `productos` el resultado de `productos_stock.keys()`. Esto constituirá el eje X (las categorías).
* Se asigna a la variable `cantidades` el resultado de `productos_stock.values()`. Esto constituirá la altura de las barras en el eje Y.


3. **Invocación:** Se llama a la función `plt.bar(categorias, valores)`, que en este caso es `plt.bar(productos, cantidades)`.
4. **Interpretación visual:** El resultado es un gráfico con 4 barras verticales separadas. Visualmente es inmediato identificar que el `producto1` tiene el inventario más alto (15), seguido por el `producto3` (11), y que el `producto4` tiene el inventario más bajo (5).


### 📝 Análisis 

Guía secuencial sobre los distintos tipos de visualizaciones que ofrece `matplotlib.pyplot` en Python. Aquí tienes el resumen analítico:

* **Matemáticas y Gráficos de Líneas 📉 (Imágenes 4, 5 y 6):** Se muestra cómo definir funciones lógicas/matemáticas (exponenciales, cuadráticas, etc.) y cómo representarlas. Se destaca que `plt.plot()` genera gráficos de líneas por defecto. Además, enseña una característica clave: si llamas a `plt.plot()` múltiples veces con diferentes conjuntos de datos antes de mostrar el gráfico, Matplotlib superpondrá todas las curvas en el mismo plano, permitiendo contrastar la evolución de distintos valores en el tiempo.
* **Gráficos de Dispersión o Scatter Plots 🌌 (Imagen 7):** Introduce la función `plt.scatter(x, y)`. El análisis resalta que este gráfico no une los puntos con líneas, sino que es fundamental para identificar cómo se distribuyen los datos, ver dónde se "agrupan" y descubrir relaciones o tendencias entre dos ejes (por ejemplo, relacionando dos mediciones de temperatura).
* **Gráficos de Barras 📊 (Imagen 8):** Muestra el uso de diccionarios para estructurar datos categóricos. Utilizando los métodos `.keys()` y `.values()`, separa los nombres de los productos y sus cantidades respectivas de stock para alimentar la función `plt.bar(categorias, valores)`. Esto genera barras rectangulares que facilitan enormemente la comparación de magnitudes.

```
