# 🏷️ Categorización Ordinal vs One-Hot

## 📝 Resumen Analítico
En el análisis de datos, los modelos matemáticos (especialmente el Machine Learning) no pueden procesar texto o categorías directamente; solo entienden números. La codificación es el procedimiento de transformar variables categóricas en formatos numéricos que una máquina pueda interpretar. 

---

## 1. Codificación One-Hot (Variables Nominales) 🟢
La técnica **One-Hot Encoding** se utiliza para variables **nominales**, es decir, categorías que **no tienen un orden jerárquico** entre sí (ej: colores, tipos de sensores, ciudades).

* **Procedimiento:** Crea una columna nueva por cada categoría posible. Si el dato pertenece a esa categoría, marca un `1`; si no, marca un `0`.
* **Uso en Pandas:** Se realiza mediante `pd.get_dummies()`.
* **Ventaja:** No asume que una categoría es "mayor" que otra, evitando sesgos matemáticos.
* **Desventaja:** Puede crear demasiadas columnas si tienes cientos de categorías (problema de la dimensionalidad).

**Ejemplo:**
`Temp_18`, `Temp_22`, `Temp_25`... cada una será `1` o `0`.

---

## 2. Codificación Ordinal (Variables Jerárquicas) 📈
La codificación **Ordinal** se utiliza para variables donde **el orden sí importa** (ej: nivel de satisfacción, rangos de temperatura, niveles de educación: Bajo, Medio, Alto).

* **Procedimiento:** Convierte valores continuos o etiquetas en rangos definidos mediante "cajones" (bins).
* **Uso en Pandas:** Se realiza mediante `pd.cut()`.
* **Ventaja:** Reduce la complejidad del modelo al agrupar datos similares y mantiene la lógica del orden natural.

---

## 🆚 Diferencias Clave

| Característica | One-Hot Encoding | Codificación Ordinal |
| :--- | :--- | :--- |
| **Tipo de Dato** | Nominal (Sin orden) | Ordinal (Con orden) |
| **Resultado** | Muchas columnas nuevas | Una sola columna categorizada |
| **Jerarquía** | No existe | Se preserva (Frío < Moderado < Caliente) |
| **Función Pandas** | `pd.get_dummies()` | `pd.cut()` |

---

## 🛠️ Procedimientos Técnicos

### Codificación One-Hot
Utilizamos `get_dummies` para expandir nuestra columna `Lectura` en múltiples columnas binarias, creando un indicador preciso para cada valor presente en el dataset.


``` python
df_encoded = pd.get_dummies(df, columns=['Lectura'], prefix='Temp')

```

### Codificación Ordinal
Utilizamos `pd.cut` para "segmentar" los datos. Definimos los límites (bins) y asignamos una etiqueta semántica a cada rango. Es fundamental usar `include_lowest=True` para asegurar que el valor mínimo sea incluido en la primera categoría.

```python
cajones = [0, 20, 25, 30]
etiquetas = ['Frío', 'Moderado', 'Caliente']
df['Categoria'] = pd.cut(df['Lectura'], bins=cajones, labels=etiquetas, include_lowest=True)

```

### 📝 Resumen del Análisis

La diferencia fundamental entre ambos métodos radica en **la naturaleza de la información**:

* **One-Hot Encoding 🟢:** Se usa cuando no hay jerarquía. Si categorizas "Manzana" y "Naranja", ninguna es mayor que la otra. El método crea columnas separadas (`es_manzana`, `es_naranja`) y coloca `1` o `0`. Es ideal para evitar que el modelo piense erróneamente que una categoría es "más grande" o "mejor" que otra simplemente por su valor numérico.
* **Codificación Ordinal 📈:** Se usa cuando los datos tienen un sentido de progresión. Al categorizar temperaturas como "Frío", "Moderado" y "Caliente", estás respetando un orden físico natural. Aquí `pd.cut` es la herramienta clave: te permite crear "recipientes" (bins) y asignar nombres significativos a esos rangos, transformando números continuos en una escala lógica.

```python

import pytesseract
from PIL import Image
import os

image_files = [
    "categorizacion.png", "categorizacion1.png", "categorizacion2.png", 
    "categorizacion3.png", "categorizacion4.png", "categorizacion5.png", 
    "categorizacion6.png", "categorizacion7.png"
]

texts = {}
for file in image_files:
    try:
        if os.path.exists(file):
            texts[file] = pytesseract.image_to_string(Image.open(file))
        else:
            texts[file] = "File not found"
    except Exception as e:
        texts[file] = str(e)

print(texts)


```

```text
Traceback (most recent call last):
  File "<xbox-string>", line 1, in <module>
    import pytesseract
ModuleNotFoundError: No module named 'pytesseract'


```

"# 🏷️Categorización y Codificación de Datos en Pandas

## 📝 Resumen Analítico
La preparación de datos requiere transformar la información en bruto en formatos numéricos estructurados que los algoritmos estadísticos puedan procesar. Los archivos analizados profundizan en las estrategias maestras para categorizar variables continuas y codificar correctamente las variables de texto según su naturaleza.

---

## 📊 1. Naturaleza de las Variables
Antes de aplicar cualquier transformación, es crucial identificar el tipo de dato al que nos enfrentamos:
* **Nominales:** 🏷️ Categorías sin un orden o jerarquía específica (ej. Protocolos de comunicación: LoRa, Wi-Fi, Zigbee).
* **Ordinales:** 📈 Categorías que poseen una jerarquía natural o nivel de magnitud (ej. Alarmas de un PLC: Baja, Media, Crítica).
* **Continuas:** 🌊 Valores numéricos que pueden tomar infinitos valores dentro de un rango (ej. Medición de voltaje de baterías: 12.1V, 13.2V).

---

## ✂️ 2. Discretización (Binning)
Procedimiento para transformar variables numéricas continuas en categorías discretas o "intervalos".

### A. Categorización por Intervalos Fijos (`pd.cut`)
Define fronteras o límites numéricos exactos (cajones o *bins*). Es ideal cuando existen reglas físicas o especificaciones técnicas estrictas.


```python

import pandas as pd

# Lecturas de voltaje de un banco de baterías LiFePO4

df = pd.DataFrame({'Voltaje': [11.5, 12.8, 13.5, 14.2, 10.5]})

# 1. Definición de límites y sus respectivas etiquetas

limites = [10.0, 12.0, 13.2, 15.0]
estados = ['Crítico', 'Nominal', 'Sobrecarga']

# 2. Aplicación de la discretización

df['Estado_Bateria'] = pd.cut(df['Voltaje'], bins=limites, labels=estados)

```

### B. Categorización por Cuantiles (`pd.qcut`)
A diferencia de `cut`, `qcut` divide los datos en grupos que contienen **la misma cantidad de muestras** (cuartiles, percentiles), ajustando los límites numéricos de forma dinámica. Útil para datos estadísticamente sesgados.

```python
# Divide las lecturas en 3 grupos con idéntica cantidad de datos
df['Rango_Estadistico'] = pd.qcut(df['Voltaje'], q=3, labels=['Bajo', 'Medio', 'Alto'])

```

---

## 🔢 3. Codificación Ordinal (Label / Ordinal Encoding)

Procedimiento para convertir categorías de texto en números secuenciales. Dado que existe un orden lógico de fondo, la asignación de pesos matemáticos ($1, 2, 3...$) es completamente válida.

### Mapeo Manual con `.map()`

Ofrece control absoluto sobre qué número corresponde a qué categoría jerárquica.

```python
df_alarmas = pd.DataFrame({'Nivel_Alarma': ['Baja', 'Crítica', 'Media', 'Baja']})

# Diccionario de jerarquías
mapa_jerarquia = {'Baja': 1, 'Media': 2, 'Crítica': 3}

# Aplicación del mapeo directo
df_alarmas['Alarma_Codificada'] = df_alarmas['Nivel_Alarma'].map(mapa_jerarquia)

```

---

## 🔀 4. Codificación One-Hot (Variables Dummy)

Se utiliza **estrictamente para variables nominales**. Si codificáramos nodos de red con números (LoRa = 1, Wi-Fi = 2, BLE = 3), el algoritmo asumiría erróneamente que BLE "vale el triple" que LoRa. One-Hot evita este error fatal creando una columna binaria independiente para cada categoría.

```python
df_nodos = pd.DataFrame({'Protocolo': ['LoRa', 'BLE', 'Wi-Fi', 'LoRa']})

# Crea columnas binarias independientes
df_dummies = pd.get_dummies(df_nodos, columns=['Protocolo'])

# Resultado: Tendremos nuevas columnas como 'Protocolo_LoRa', 'Protocolo_BLE', etc., rellenas de 1s y 0s.

```

---

## 🆚 Matriz de Decisión Rápida

| Condición de tus Datos | Procedimiento a Utilizar | Herramienta Pandas |
| --- | --- | --- |
| Tienes valores numéricos continuos y necesitas crear rangos. | **Discretización (Binning)** | `pd.cut()` o `pd.qcut()` |
| Tienes texto y existe una jerarquía obvia entre las categorías. | **Codificación Ordinal** | `.map()` |
| Tienes texto y las categorías NO tienen orden ni jerarquía. | **One-Hot Encoding** | `pd.get_dummies()` |
| """ |  |  |


### 📝 Resumen Práctico de los Procedimientos

Los procedimientos mostrados en las imágenes se pueden sintetizar en **tres reglas de oro** para tratar la información categórica:

* **Regla de los Rangos (`pd.cut` / `pd.qcut`):** ✂️ Si tienes una variable numérica continua (por ejemplo, el voltaje de un banco de baterías LiFePO4) y necesitas convertir esos números en estados legibles como "Bajo", "Nominal" o "Sobrecarga", utilizas la técnica de binning. `cut` usa fronteras matemáticas rígidas, mientras que `qcut` se basa en distribuciones estadísticas.

* **Regla de la Jerarquía (`map` o Label Encoding):** 📈 Si tu variable de texto tiene un orden de magnitud inherente (por ejemplo, las alertas de un PLC: Alerta Baja, Alerta Media, Alerta Crítica), puedes traducirlas directamente a números como 1, 2 y 3. El peso matemático de los números respeta la jerarquía lógica de los datos de campo.

* **Regla Nominal (`pd.get_dummies`):** 🔀 Si tu texto no tiene ningún orden jerárquico (por ejemplo, estás comparando protocolos de red: LoRa, Wi-Fi o Zigbee), nunca debes usar los números 1, 2 y 3. El modelo pensaría que el protocolo número 3 es "mayor" que el protocolo número 1. Para esto, se emplea el **One-Hot Encoding**, que divide el texto en columnas separadas de Verdadero (1) y Falso (0).

