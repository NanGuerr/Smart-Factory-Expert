# 🧮 Operaciones Básicas y Estructura en NumPy

## 🔲 Estructura de un Array 2D
Un array bidimensional (matriz) se organiza mediante ejes (**axis**) y tiene una forma o dimensión definida (**shape**).

* **`axis 0`**: ↕️ Representa el eje vertical (opera a través de las filas, por columna).
* **`axis 1`**: ↔️ Representa el eje horizontal (opera a través de las columnas, por fila).
* **`shape`**: 📐 Define las dimensiones de la matriz (filas, columnas). Ejemplo: `(2, 3)`.

**Ejemplo de Matriz con shape `(2, 3)`:**

| | Columna 1 | Columna 2 | Columna 3 |
| :--- | :---: | :---: | :---: |
| **Fila 1** | 5.2 | 3.0 | 4.5 |
| **Fila 2** | 9.1 | 0.1 | 0.3 |

---

## ➕ Operaciones Elemento a Elemento (`array[] + array[]`)
NumPy permite realizar operaciones aritméticas directas entre arrays, calculando posición por posición de manera súper eficiente:

| Operación | Operador Python | Función NumPy |
| :--- | :---: | :--- |
| **Suma** | `+` | `np.add` |
| **Resta** | `-` | `np.subtract` |
| **Multiplicación** | `*` | `np.multiply` |
| **División** | `/` | `np.divide` |

---

## 📐 Funciones Matemáticas Universales
Estas funciones se aplican a un solo array, transformando cada uno de sus elementos individualmente:

* **`np.sqrt(x)`**: 🔲 Calcula la raíz cuadrada de cada elemento.
* **`np.exp(x)`**: 📈 Calcula el valor exponencial ($e^x$).
* **`np.sin(x)`**: 🌊 Calcula el seno de cada elemento (los valores de entrada deben estar en radianes).
* **`np.cos(x)`**: 🎢 Calcula el coseno de cada elemento (los valores de entrada deben estar en radianes).
* **`np.log(x)`**: 📉 Calcula el logaritmo natural de cada elemento.

---

## ✖️ Producto Matricial y Operaciones de Vectores
* **`arr1.dot(arr2)`**: 🎯 Realiza el producto punto (producto escalar o matricial) entre dos arrays. Es importante destacar que esto es matemática matricial real, diferente a la simple multiplicación elemento a elemento (`*`).

### 📝 Resumen del Contenido

He estructurado la información que me pasaste en un documento claro y visual 🗂️. El archivo cubre:

* **Morfología de un Array 2D 🧊:** Explica de forma gráfica la matriz de valores `[5.2, 3.0, 4.5]` y `[9.1, 0.1, 0.3]`, aclarando que un `shape: (2, 3)` significa 2 filas y 3 columnas. También detalla hacia dónde apuntan el `axis 0` (vertical) y el `axis 1` (horizontal).
* **Operaciones Aritméticas ➕:** Organiza en una tabla las cuatro operaciones básicas, mostrando su operador tradicional (`+`, `-`, `*`, `/`) y su función equivalente vectorizada en NumPy (`np.add`, `np.subtract`, etc.).
* **Matemática Avanzada 📐:** Enumera las funciones universales que se aplican a un solo array (raíz cuadrada, exponente, logaritmo, seno y coseno).
* **Álgebra Lineal ✖️:** Cierra con el método `.dot()`, crucial para realizar el producto punto entre matrices.
