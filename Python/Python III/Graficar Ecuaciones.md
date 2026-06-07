# 📊 Matplotlib: Graficas de Ecuaciones

## 🖼️ Conceptos
Los conceptos básicos para iniciar con **Matplotlib**, la biblioteca estándar de visualización en Python:

1. **Versatilidad de Datos 📈**: Matplotlib es capaz de ingerir y graficar múltiples estructuras de datos:
   * **Listas y Arrays de NumPy**: Para datos uni, bi o multidimensionales (como mapas de calor o gráficos 3D).
   * **DataFrames de Pandas**: Excelente integración para graficar directamente desde estructuras tabulares sin mucho procesamiento.
   * **Diccionarios Anidados**: Extracción de datos estructurados para su visualización.
2. **Módulo Pyplot 🛠️**: Se explica la importancia de importar el submódulo `pyplot` usando el alias convencional `plt` (`import matplotlib.pyplot as plt`) para evitar escribir código excesivo.
3. **Visualización (`plt.plot` y `plt.show`) 💻**: 
   * Se utiliza `plt.plot(datos)` para generar el trazado matemático en memoria (las imágenes muestran el ejemplo básico de una línea recta usando `range(10)`).
   * La función `plt.show()` es crucial en entornos de scripting tradicionales para invocar la ventana interactiva de la figura (como se ve en la imagen con la interfaz de "Figure 1"). En entornos interactivos como Jupyter Notebooks, la figura suele renderizarse automáticamente en la salida de la celda, como se aprecia en otra de las capturas.

---

## 🧮 Procedimientos: Ecuaciones y Gráficos de Líneas

A continuación, se detalla el procedimiento lógico y descriptivo de las funciones matemáticas planteadas y su posterior graficación.

### 1. Definición de Funciones Matemáticas 🔢

El código utiliza el módulo estándar `math` de Python para definir diferentes comportamientos matemáticos:


```python
import math

# Función Exponencial: Calcula e^(x/10). Genera una curva de crecimiento acelerado.
def exponencial(input):
  return math.exp(input/10)

# Función Exponencial Inversa: Resta un decaimiento exponencial a un valor base.
def exponencial_inversa(inicial, input):
  return inicial - math.exp(-input/10)

# Función Cuadrática: Representa una parábola (x^2).
def cuadratica(valor):
  return (valor * valor)

# Función de División (Inversa): Representa una función racional (1/x).
# Incorpora una estructura condicional (if/else) para evitar el error crítico de división por cero.
def division(valor):
  if valor != 0:
    return (1/valor)
  else:
    return 1/0.1  # Valor de contingencia

```

### 2. Generación del Gráfico de Líneas 📉

Para visualizar el comportamiento de la función exponencial, se combinan las capacidades de iteración de Python con Matplotlib:

```python
import matplotlib.pyplot as plt

# 1. Generación de Datos: 
# Se utiliza "List Comprehension" para iterar 50 veces (de 0 a 49).
# En cada iteración, se calcula el valor de la función exponencial.
valores = [exponencial(valor) for valor in range(50)]

# 2. Trazado:
# plt.plot() toma la lista generada. Al no especificar un eje X, 
# Matplotlib asume los índices (0 al 49) como eje X, y 'valores' como el eje Y.
plt.plot(valores)

# 3. Renderizado:
# Muestra la ventana final con la curva resultante.
plt.show()

```

### 📝 Resumen del Análisis

Las imágenes que compartiste muestran los fundamentos de **Matplotlib** 📊:
* **Fuentes de Datos 📂:** Explican que la librería es altamente versátil, permitiendo graficar desde listas simples y arrays de **NumPy** hasta estructuras más complejas como **DataFrames** de Pandas y diccionarios anidados.
* **Importación ⚙️:** Se muestra la sintaxis universal para importar la herramienta de graficado rápido: `import matplotlib.pyplot as plt`.
* **Ejecución y Visualización 💻:** Las capturas muestran dos entornos de ejecución. Uno integrado tipo Jupyter Notebook donde la línea `plt.plot(range(10))` genera el gráfico debajo de la celda de código, y otro entorno de script tradicional donde es obligatorio usar `plt.show()` para abrir la ventana gráfica ("Figure 1").

