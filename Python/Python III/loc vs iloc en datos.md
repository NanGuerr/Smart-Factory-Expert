# 🐼 Indexación y Filtrado en Pandas: `loc` vs `iloc`

## 📝 Resumen Analítico
Una de las tareas más comunes en el análisis de datos es la selección de filas y columnas específicas. Para ello, Pandas proporciona dos potentes indexadores: `.loc` e `.iloc`. Comprender la diferencia entre ellos es fundamental para evitar errores de selección.

---

## 🆚 Diferencias Fundamentales: `loc` vs `iloc`

* **`.iloc` (Index Location):** 🔢 Selecciona datos basándose exclusivamente en su **posición numérica entera**, similar a cómo funcionan las listas o arrays en Python. El primer elemento siempre es el índice `0`.
* **`.loc` (Location):** 🏷️ Selecciona datos basándose en la **etiqueta (label) del índice** o mediante **condiciones lógicas (máscaras booleanas)**.

### Ejemplos Conceptuales
* `df.iloc[0]` → Extrae la primera fila física del DataFrame, sin importar cómo se llame su índice.
* `df.loc['Fila A']` → Extrae la fila cuyo nombre o etiqueta de índice sea exactamente 'Fila A'.

---

## 🛠️ Práctica: Uso de `loc` para Filtrado Lógico

El método `.loc` brilla cuando se utiliza junto con condiciones lógicas, permitiendo filtrar bases de datos inmensas de forma ultra rápida (vectorizada), sin la necesidad de escribir lentos bucles `for` o estructuras `if`.

### 1. Definición del DataFrame de Sensores 🏭


```python

import pandas as pd

sensores = {
'Tiempo': ['2023-08-01 08:00', '2023-08-01 09:00', '2023-08-01 10:00', '2023-08-01 11:00', '2023-08-01 12:00', '2023-08-01 13:00'],
'Sensor': ['FT-001', 'FT-002', 'FT-001', 'FT-002', 'FT-001', 'FT-002'],
'Temperatura': [35.2, 36.5, 34.8, 37.2, 33.6, 37.9],
'Presión': [2.1, 2.0, 2.2, 1.9, 2.5, 1.8]
}

df_sensores = pd.DataFrame(sensores)

```

### 2. Creación de una Máscara Booleana 🎭

Al aplicar un operador relacional (`>`, `<`, `==`, `>=`) directamente sobre una columna, Pandas no devuelve un solo valor, sino una **Serie de valores booleanos (`True` o `False`)** que indica si la condición se cumple fila por fila.

```python
alarma = df_sensores.Temperatura >= 36
print(alarma)
# Esto devuelve: False, True, False, True, False, True

```

### 3. Filtrado Vectorizado con `.loc` 🎯

Al pasar esta "máscara booleana" al indexador `.loc`, Pandas imprimirá únicamente las filas donde la condición haya resultado en `True`.

**Método A (Usando variable intermedia):**

```python
# Muestra solo los registros donde la temperatura fue >= 36
df_sensores.loc[alarma]

```

**Método B (Directo y optimizado):**
Se puede inyectar la condición directamente dentro de los corchetes, ahorrando código y variables intermedias.

```python
# Muestra solo los registros donde la presión sea >= 2.0
df_sensores.loc[df_sensores.Presión >= 2.0]

```


### 📝 Resumen del Contenido

El texto que me compartiste explica uno de los "súperpoderes" de Pandas: el **filtrado lógico** sin necesidad de bucles 🐼.

* **La Diferencia Clave 🔑:** Aunque ambos se usan para seleccionar datos, **`iloc`** es estrictamente numérico (como el índice de una lista clásica en Python), mientras que **`loc`** entiende etiquetas, nombres de columnas y, lo más importante, operaciones booleanas.
* **Máscaras Booleanas 🎭:** Explica que si escribes `df.Temperatura >= 36`, el programa no te da un número, sino una lista de Verdaderos y Falsos indicando qué filas cumplen la regla. A esto se le llama "máscara".
* **Filtros de una línea ⚡:** Al colocar esa máscara (o la ecuación directa) dentro de los corchetes de `.loc[]`, Pandas recorta la tabla instantáneamente. Es la forma correcta y profesional de buscar datos, evadiendo por completo el uso del ineficiente ciclo `for` de Python estándar.
