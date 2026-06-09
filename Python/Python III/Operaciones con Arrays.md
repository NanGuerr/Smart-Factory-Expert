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
# 🛠️ Manipulación Avanzada de Arrays en NumPy


---

## 🔄 1. Transposición de Matrices (`matriz transpuesta`)
La transposición es una operación fundamental de álgebra lineal que intercambia las filas por columnas (y viceversa).
* **El atributo `.T`:** Es el método más directo. Si tienes una matriz `A`, escribir `A.T` invierte sus ejes instantáneamente.
* **La función `np.transpose(arr)`:** Hace exactamente lo mismo, pero es preferida cuando se trabaja con tensores (arrays de 3 o más dimensiones), ya que te permite especificar exactamente cómo permutar los ejes.

---

## ➕➖ 2. Modificación Estructural (`append`, `insert`, `delete`)
NumPy prioriza la eficiencia, por lo que los arrays tienen tamaños fijos. Cuando modificas uno, NumPy suele devolver una copia nueva reestructurada:
* **`np.append(arr, values, axis=None)`:** Añade nuevos valores al final. Ojo: si no defines un `axis` (eje), el array se aplanará (se volverá 1D) antes de pegar los valores.
* **`np.insert(arr, obj, values, axis)`:** Mucho más preciso. Te permite inyectar datos (como una nueva columna de sensores) en un índice específico (`obj`) sin borrar lo anterior.
* **`np.delete(arr, obj, axis)`:** El proceso inverso. Puedes purgar filas o columnas enteras especificando su posición.

---

## 🧱 3. Unión y Concatenación (`hstack` y `vstack`)
Es muy común tener datos divididos en varios archivos o variables y necesitar unirlos en una sola gran tabla.
* **`np.vstack((a, b))` (Vertical Stack):** Apila los arrays uno debajo del otro, como si agregaras más filas a una tabla. *Condición:* Ambos arrays deben tener exactamente el mismo número de columnas.
* **`np.hstack((a, b))` (Horizontal Stack):** Pega los arrays de lado a lado, añadiendo columnas. *Condición:* Deben tener el mismo número de filas.

---

## 🔀 4. Ordenamiento de Datos (`sort`)
Organizar los datos de menor a mayor es crítico para encontrar patrones, medianas o límites.
* **`np.sort(a, axis=-1)`:** Devuelve una copia ordenada del array. En matrices bidimensionales, si no indicas lo contrario, ordenará los elementos de cada fila de forma independiente. Si quieres ordenar por columnas, debes especificar `axis=0`.
* **Bonus - `np.argsort(a)`:** A veces no quieres mover los datos reales, sino saber *en qué orden* deberían ir. `argsort` te devuelve los índices ordenados, lo que es invaluable cuando sincronizas dos arrays distintos.

---

## ✂️ 5. Indexación y Atributos Básicos (`array1` a `array5`)
El manejo básico de cualquier matriz implica saber acceder a sus entrañas y conocer sus propiedades físicas:
* **Atributos:** `.shape` te dice el tamaño (ej. `(3, 4)`), `.ndim` te dice cuántas dimensiones tiene (ej. `2`), y `.size` el número total de elementos.
* **Slicing (Rebanadas):** Extraer cuadrantes usando la sintaxis `arr[inicio:fin]`. Por ejemplo, `arr[:, 1:3]` significa "dame todas las filas (:`), pero solo las columnas 1 y 2`.
* **Máscaras Booleanas:** Filtrar datos mediante condiciones matemáticas directamente en los corchetes, por ejemplo: `arr[arr > 5]` te devolverá solo los elementos mayores a 5.

### 📝 Resumen del Análisis 

El conjunto aborda la **manipulación estructural y arquitectónica de datos** dentro de NumPy 🏗️. Ya no se trata solo de hacer cálculos, sino de darle la forma correcta a la información:

* **Pivotar Datos 🔄:** La imagen de `matriz transpuesta` muestra cómo rotar matrices usando `.T`, esencial en álgebra lineal o al cruzar datos para machine learning.
* **Ensamble de Bloques 🧱:** Con `hstack` y `vstack`, aprendes a tomar arrays individuales y pegarlos de lado a lado (horizontal) o apilarlos (vertical) para construir bases de datos más complejas a partir de fragmentos.
* **Edición Quirúrgica ✂️:** Operaciones como `append`, `insert` y `delete` ilustran cómo inyectar nuevas mediciones o purgar variables defectuosas de tus matrices.
* **Orden y Selección 🔀:** Se detallan comandos como `sort` para organizar secuencias de menor a mayor, acompañado de los conceptos básicos de "slicing" para extraer únicamente los rangos (filas o columnas) que realmente necesitas analizar.
