# 📚 NumPy: Arrays, Operaciones y Agregación

Esta guía detalla el uso fundamental de la librería **NumPy** en Python, la herramienta estándar para el cálculo numérico. Abarca desde la creación de estructuras de datos multidimensionales (arrays) hasta la aplicación de operaciones matemáticas vectorizadas y funciones estadísticas de agregación.

---

## 🏗️ 1. Creación de Arrays Básicos
Un array es la estructura central de NumPy. Puede tener múltiples dimensiones:
* **1D (Vector):** Una sola lista de elementos. `np.array([7, 2, 9, 10])`
* **2D (Matriz):** Listas anidadas formando filas y columnas.
* **3D (Tensor):** Matrices anidadas, creando bloques tridimensionales de datos.

---

## 🛠️ 2. Funciones de Inicialización Rápida
NumPy permite generar arrays pre-configurados de forma rápida y eficiente:

* **`np.zeros(shape)`**: Crea un array completamente lleno de ceros (útil para reservar memoria).
* **`np.ones(shape)`**: Crea un array lleno de unos.
* **`np.empty(shape)`**: Crea un array sin inicializar. Es rapidísimo, pero contendrá datos aleatorios o "basura" en memoria hasta que lo sobrescribas.
* **`np.full(shape, fill_value)`**: Rellena el array con el valor exacto que le indiques.
* **`np.arange(start, stop, step)`**: Funciona como el `range()` de Python clásico. Crea secuencias con saltos definidos (el valor `stop` no se incluye).
* **`np.linspace(start, stop, num)`**: Crea un array de tamaño `num` donde todos los valores están **equiespaciados** (el valor `stop` sí se incluye). Excelente para crear ejes de tiempo o coordenadas gráficas.

*Nota sobre `shape`: Es una tupla que define el tamaño. Ej: `(2, 4)` significa 2 filas y 4 columnas.*

---

## 🧮 3. Operaciones Matemáticas Simples
NumPy realiza operaciones "elemento por elemento" (vectorización), lo cual es mucho más rápido que usar bucles `for`:

* **Aritmética:** `add` (+), `subtract` (-), `multiply` (*), `divide` (/).
* **Potencias y Raíces:** `sqrt` (raíz cuadrada), `exp` (exponencial).
* **Trigonometría:** `sin` (seno), `cos` (coseno), `tan` (tangente).
* **Logaritmos y Vectores:** `log` (logaritmo natural), `dot` (producto punto o matricial entre dos arrays).

---

## 📊 4. Funciones de Agregación y el concepto de "Axis"
Las funciones de agregación toman muchos valores y devuelven un resumen de los mismos.
* **Básicas:** `sum` (suma total), `mean` (promedio), `median` (mediana).
* **Dispersión:** `std` (desviación estándar), `var` (varianza).
* **Extremos:** `min` (mínimo), `max` (máximo).
* **Búsqueda de Índices:** `argmin` y `argmax` (te dicen *en qué posición* está el valor más pequeño o más grande, no el valor en sí).
* **Acumulativas:** `cumsum` (suma acumulada), `cumprod` (producto acumulado).

### 🧭 El Parámetro `axis` (Ejes)
Si tienes una matriz (2D) y aplicas una función matemática, puedes decidir en qué dirección aplicarla:
* `axis=0`: Opera a lo largo de las **columnas** (de arriba hacia abajo).
* `axis=1`: Opera a lo largo de las **filas** (de izquierda a derecha).
* *Si omites `axis`, NumPy "aplastará" el array y operará sobre absolutamente todos los elementos.*

---

## 💻 5. Resolución de los Ejercicios Prácticos

A partir de los ejercicios planteados en la transcripción, aquí tienes el código para resolverlos y graficarlos:


```python

import numpy as np
import matplotlib.pyplot as plt

# 1. Creación de los arrays solicitados

Coseno = np.empty(1500) # Array vacío
Seno = np.ones(1500)    # Array de unos
T = np.linspace(0, 2*np.pi, 1500) # Tiempo de 0 a 2*pi equiespaciado
Resumen = np.empty((2, 4)) # Array de 2 filas y 4 columnas vacío

# 2. Rellenando los arrays con las funciones matemáticas

Seno = np.sin(T)
Coseno = np.cos(T)

# 3. Graficando ambos en un solo plot

plt.figure(figsize=(10, 5))
plt.plot(T, Seno, label="Seno(T)", color="blue")
plt.plot(T, Coseno, label="Coseno(T)", color="red", linestyle="--")

plt.title("Ondas Seno y Coseno")
plt.xlabel("Tiempo (T) en Radianes")
plt.ylabel("Amplitud")
plt.axhline(0, color='black', linewidth=0.5) # Línea central en el eje X
plt.legend()
plt.grid(True)
plt.show()

```
### 📝 Resumen Analítico 

El poder matemático de Python mediante el uso de **NumPy** 🧮.

A diferencia de las listas tradicionales de Python, las imágenes y la transcripción se enfocan en demostrar cómo construir **arrays** (vectores, matrices y tensores) y cómo manipularlos de manera rápida ("vectorizada").

El contenido se divide en tres pilares esenciales:

1. **Inicialización 🏗️:** No necesitas ingresar datos a mano siempre. Se muestran métodos automáticos para generar listas masivas de datos para simulaciones, como llenar listas de ceros (`np.zeros`), crear rangos con pasos específicos (`np.arange`), o generar puntos equidistantes ideales para crear gráficas (`np.linspace`).
2. **Matemática Directa 📐:** Enseña cómo cruzar arrays de datos pasándolos directamente por operaciones elementales (`add`, `multiply`) o funciones trigonométricas complejas (`sin`, `cos`, `exp`), operando sobre todos los elementos simultáneamente.
3. **Agregación y Estadísticas 📊:** Ofrece un catálogo de funciones para resumir datos masivos (promedios, mínimos, varianzas). Es crucial la mención del concepto de `axis`, que es la clave para entender si estás promediando los datos de una sola columna, de una fila entera o de todo el bloque a la vez.

## Array.agg()

Por último, tenemos las funciones de agregación, las cuales
nos da información adicional de un array:

```python

array. sum() = Sumatoria del array
array.min(axis=) = Minimo del array, o del eje seleccionado
array.max(axis=) = Maximo del array, o del eje seleccionado
array.mean() = Promedio del array
array.std() = Desviación estándar del array

```

¡Y también podemos hacer comparaciones para cada elemento!

```python

b=np.arange(5)
b>2

array([0, 1, 2, 3, 4])
array([False, False, False, True, True])

```

# 🔃 Crear Arrays

```python
import numpy as np
array_1D = np.array([7,2,9,10])
array_2D = np.array([
    [5.2, 3.0, 4.5],
    [9.1,0.1,0.3]
])
array_3D = np.array([
[
    [1,4,7],
    [2,9,7],
    [1,3,0],
    [9,6,9]
],
[
    [2,3,4],
    [1,4,5],
    [4,7,2],
    [3,5,8]
]
])

```

## 🔄 Array[Indexing]

```python

array_2D[0,1:]
> array([3.,4.5])

array_2D[:,1]
> array([[3. ],
        [0.1]])

#Algo muy interesante, es que podemos seleccionar todas las
#celdas que cumplan cierta condición.

array_2D[array_2D>2]

> array([5.2, 3.,4.5, 9.1])

# O seleccionar la inversa de un array

array_2D[e, : :- 1]

> array([4.5, 3., 5.2])

```
