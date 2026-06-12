# 📈 Media Móvil (Rolling Average) en Pandas

En el análisis de series temporales o señales físicas continuas, es muy común encontrarse con "ruido" (picos y caídas bruscas temporales). La **Media Móvil (Rolling Average)** es una técnica matemática que suaviza estas fluctuaciones a corto plazo para revelar la tendencia real a largo plazo. Funciona creando una "ventana" de tamaño fijo que se desliza por los datos, calculando el promedio de los valores dentro de esa ventana en cada paso.

---

## ⚙️ Conceptos Clave del Procedimiento

* **Ventana (`window`):** 🪟 Determina cuántos registros hacia atrás se tomarán para calcular el promedio. Si tienes datos diarios y un `window=7`, estarás calculando la media móvil semanal.
* **Desplazamiento:** A medida que avanzas una fila en tu DataFrame, la ventana "suelta" el dato más antiguo y "agarra" el dato más nuevo.
* **Datos Faltantes (NaN):** Al inicio del dataset, como no hay suficientes datos históricos para llenar la ventana, Pandas colocará `NaN` (nulos) por defecto.

---

## 🛠️ Procedimiento Técnico y Sintaxis

La función principal en Pandas es `.rolling()`, la cual siempre debe ir acompañada de una función de agregación matemática al final (generalmente `.mean()`).

### Ejemplo Práctico: Suavizado de Señal
Imagina que estamos monitoreando el nivel de señal (RSSI) de un nodo de comunicación o el voltaje de una batería remota. Las lecturas brutas suelen saltar mucho por interferencias ambientales.


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Creamos un DataFrame con lecturas fluctuantes (con "ruido")
datos = {
    'Dia': range(1, 11),
    'Voltaje_Bateria': [13.2, 12.1, 13.5, 11.8, 13.1, 13.0, 12.2, 13.4, 12.9, 13.3]
}
df = pd.DataFrame(datos)

# 2. Aplicamos la Media Móvil (Rolling Average)
# Usaremos una ventana de 3 días para suavizar los saltos diarios.
df['Voltaje_Suavizado'] = df['Voltaje_Bateria'].rolling(window=3).mean()

# 3. Visualización de los resultados
print(df)

```

**Resultado Esperado:**

| Dia | Voltaje_Bateria | Voltaje_Suavizado |
| --- | --- | --- |
| 1 | 13.2 | NaN |
| 2 | 12.1 | NaN |
| 3 | 13.5 | 12.93 |
| 4 | 11.8 | 12.46 |

---

## 🎛️ Ajuste Fino: El parámetro `min_periods`

Si no quieres perder esos primeros registros (los que se vuelven `NaN`), puedes forzar a Pandas a calcular la media con los datos que tenga disponibles, aunque la ventana no esté llena.

```python
# Calculará el promedio incluso si solo tiene 1 o 2 datos iniciales
df['Media_Forzada'] = df['Voltaje_Bateria'].rolling(window=3, min_periods=1).mean()

```

---

## 🆚 Comparativa Rápida

| Estrategia | ¿Qué hace? | ¿Cuándo usarlo? |
| --- | --- | --- |
| **Datos Crudos** | Muestra cada pico e interferencia. | Detección de fallas críticas instantáneas. |
| **Media Móvil Corta (ej. 3)** | Suaviza un poco, reacciona rápido a cambios. | Monitoreo táctico de sistemas. |
| **Media Móvil Larga (ej. 30)** | Aplana la curva, muestra tendencias lentas. | Análisis de degradación a largo plazo o estacionalidad. |



## 📝 Resumen Analítico
La **Media Móvil** (o *Rolling Average*) es una técnica matemática fundamental en el procesamiento de datos temporales. Su propósito principal es **"suavizar"** fluctuaciones a corto plazo o el "ruido" en las mediciones, permitiendo que las tendencias reales a largo plazo sean claramente visibles. Es una herramienta indispensable cuando se analizan señales de campo que tienden a ser erráticas.

---

## ⚙️ 1. El Concepto de la "Ventana" (Window) 🪟
El corazón de la media móvil es la "ventana". Imagina que tienes lecturas capturadas cada hora. Si defines una ventana de tamaño `3`, el cálculo toma las primeras 3 lecturas, saca el promedio matemático y anota ese valor. Luego, la ventana "se desliza" (rolls) una posición hacia adelante: descarta la lectura más antigua, incluye la lectura nueva, calcula un nuevo promedio, y repite el proceso a lo largo de toda la matriz.

---

## 🛠️ 2. Procedimiento y Sintaxis
Pandas hace que este cálculo matricial sea ultra rápido mediante el método `.rolling()`.

### Parámetros Críticos
* **`window` (int):** El tamaño de la ventana móvil. Una ventana pequeña (ej. 3) sigue de cerca los datos originales (reacciona rápido). Una ventana grande (ej. 50) crea una curva muy plana y suave, pero reacciona con "lag" o retraso a los cambios reales del sistema.
* **`min_periods` (int):** Al inicio del DataFrame, no hay suficientes datos para llenar la ventana (ej. en el registro 2, no puedes calcular un promedio de 5 registros). Por defecto, Pandas coloca valores nulos (`NaN`). Usar `min_periods=1` obliga al sistema a calcular el promedio usando solo los datos que tenga disponibles hasta ese momento.

---
## 📡 3. Caso Práctico: Suavizado de Señales Industriales

Imaginemos que estamos monitoreando el voltaje de descarga de un banco de baterías LiFePO4 o capturando lecturas RSSI de un nodo LoRa remoto. Estas lecturas crudas suelen estar llenas de picos (ruido) por la interferencia térmica o electromagnética.

```python
import pandas as pd

# 1. DataFrame de lecturas de campo con ruido
datos_nodo = {
    'Tiempo': pd.date_range(start='2026-08-01', periods=10, freq='h'),
    'Voltaje_Crudo': [13.2, 12.1, 13.5, 12.3, 13.3, 13.8, 12.5, 13.1, 13.4, 12.9]
}
df_sistema = pd.DataFrame(datos_nodo)

# 2. Aplicación de la Media Móvil (Filtro de 3 horas)
df_sistema['Voltaje_Filtrado'] = df_sistema['Voltaje_Crudo'].rolling(window=3, min_periods=1).mean()

print(df_sistema)

```

### 🆚 El Resultado

Si graficaras ambas columnas:

* **`Voltaje_Crudo`:** 📉 Estaría lleno de "picos" agresivos, subiendo y bajando constantemente, lo que podría disparar falsas alarmas de batería baja.
* **`Voltaje_Filtrado`:** 🌊 Mostraría una curva suave y fluida. Esto te permite ver si la energía global del sistema realmente está cayendo, ignorando los ruidos esporádicos.

El procesamiento de señales a través de **Medias Móviles** (*Rolling Average*) es un concepto hermoso y vital, especialmente cuando tus datos provienen del mundo físico y están llenos de "ruido" 🌊.

### 📝 Resumen del Análisis

El principio fundamental que explican tus archivos es el concepto del **"Suavizado"**:

* **El Problema del Ruido 📉:** En el mundo real, si mides el voltaje de una batería LiFePO4, la señal de un nodo LoRa, o el precio de una acción, la gráfica original parecerá un electroencefalograma lleno de picos erráticos. Es muy difícil ver la tendencia real a simple vista.
* **La Solución (`df.rolling()`) 🪟:** El comando "Rolling" crea una **ventana** que se desliza por tus datos. Si le indicas `window=5`, tomará los primeros 5 datos, los promediará (`.mean()`) y pondrá ese puntito en la gráfica. Luego avanza un paso y repite.
* **El Efecto Mágico 🌊:** Al promediar un grupo pequeño de datos a medida que avanza el tiempo, los picos extremos hacia arriba se anulan con los picos extremos hacia abajo. El resultado es una línea curva suave y estable que te muestra la **verdadera dirección** (tendencia) hacia la que va tu sistema, sin dejar que la interferencia momentánea te engañe.

Es un filtro de software muy elegante y, usando el poder matricial de Pandas, se hace en una sola línea de código sin requerir bucles pesados. 🚀


```python

import pandas as pd
bomba = pd.read_csv("bomba_agua.csv")
import matplotlib.pyplot as plt
plt.figure(figsize=(30,10))
plt.style.use("ggplot")
plt.plot(bomba.valor)

filtrado = bomba.valor.rolling(30,15,center=True).mean()
​
plt.figure(figsize=(30,10))
plt.style.use("ggplot")
​
plt.plot(filtrado)

plt.figure(figsize=(30,10))
plt.style.use("ggplot")
​
plt.plot(bomba.valor,label="Sin filtrar")
plt.plot(filtrado, label="Filtrado")
plt.legend()
plt.show()

```


