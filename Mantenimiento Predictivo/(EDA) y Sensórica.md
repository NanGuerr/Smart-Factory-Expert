# 📊 Análisis Exploratorio de Datos (EDA) y Sensórica en Mantenimiento Predictivo 🧠

Este documento técnico consolida los conceptos de análisis estadístico, herramientas de visualización y las variables físicas fundamentales capturadas por sensores para el diagnóstico de salud en activos industriales.

---

## 📈 1. Herramientas de Visualización y Análisis Estadístico

Para construir un algoritmo predictivo, primero se debe comprender el comportamiento estadístico de los datos extraídos mediante el Análisis Exploratorio de Datos (EDA).

### 📐 Distribución de una Variable
Es la forma en que los valores numéricos de un parámetro se dispersan y con qué frecuencia ocurren. Su estudio abarca la tendencia central (media, mediana), la dispersión (desviación estándar), la asimetría y el comportamiento de las colas. Permite entender qué es "normal" en el proceso.

### 📊 Histograma
Gráfico de barras que agrupa los datos continuos en intervalos (*bins*) para mostrar su frecuencia. Es vital para identificar visualmente la variabilidad del proceso, la forma de la distribución (ej. Normal o Gaussiana) y la presencia de datos aislados.

### 📉 Gráfico de Línea
Visualización que conecta puntos de datos ordenados cronológicamente. En el entorno industrial, es la herramienta por excelencia para monitorizar series de tiempo, permitiendo identificar de un vistazo tendencias de desgaste, ciclos operativos, cambios bruscos de régimen y señales de degradación inminente.

### 🔗 Correlación
Medida estadística (que oscila entre `-1` y `1`) que describe cómo cambian dos variables de forma conjunta.
* **Correlación Positiva:** Al subir la carga/velocidad, sube la vibración.
* **Correlación Negativa:** Al aumentar la obstrucción, disminuye el caudal.
* **Aplicación:** Esencial para no confundir un incremento operativo normal con una falla real.

### 🚨 Outliers (Valores Atípicos)
Puntos de datos que se desvían de manera extrema del comportamiento normal del resto del conjunto. En mantenimiento, un outlier puede significar:
1. Una falla incipiente o transitorio anómalo.
2. Un error de lectura o ruido en el sensor.
3. Un cambio drástico en las condiciones de operación de la planta.

---

## ⚙️ 2. Variables Físicas y Operacionales del Activo

Las siguientes variables constituyen las entradas estructurales (*features*) que procesan los nodos de Node-RED, se almacenan en SQL y alimentan a los algoritmos de Machine Learning:

| Variable | Unidad Común | Descripción Técnico-Predictiva |
| :--- | :--- | :--- |
| **⏳ Días de Servicio** | Días | Tiempo acumulado de operación desde el último arranque o mantenimiento mayor. Representa la "edad" del equipo para calcular tasas de falla de la curva de la bañera. |
| **🌀 Vibración Mecánica** | mm/s (RMS) / $g$ | Medición de la oscilación de la máquina. Detecta de forma temprana desbalances, desalineaciones, holguras mecánicas y fallas severas en las pistas de los rodamientos. |
| **🔄 RPM** | min⁻¹ / rev/min | Revoluciones por minuto. Contextualiza la velocidad angular de los ejes para correlacionar y aislar las frecuencias de vibración síncronas. |
| **⚡ Potencia (Power)** | kW / HP | Consumo o entrega de energía del sistema. Un incremento de potencia para mantener el mismo caudal o velocidad suele indicar fricción interna o desgaste mecánico. |
| **💥 Presión (Pressure)** | bar / psi | Fuerza por unidad de área en fluidos. Crucial para diagnosticar restricciones en tuberías, cavitación en impulsores, fugas en líneas o pérdida de eficiencia en compresores. |
| **🌊 Caudal (Flow)** | m³/h / GPM | Volumen de fluido por unidad de tiempo. Permite evaluar el rendimiento hidráulico del proceso y detectar obstrucciones o pérdidas de eficiencia por desgaste de anillos de desgaste. |

---

## 🛠️ Procedimiento Metodológico para el Análisis de Datos

1. **Adquisición:** Extraer las series de tiempo mediante SQL (`SELECT`) de variables acopladas (ej. RPM, Potencia y Vibración).
2. **Limpieza:** Filtrar los *outliers* que correspondan a errores de comunicación para evitar sesgar el algoritmo.
3. **Perfilado (EDA):** Generar *histogramas* para validar los rangos de operación estándar y *gráficos de línea* para observar la evolución temporal de las variables físicas.
4. **Correlación:** Evaluar la relación cruzada entre variables de proceso (Presión vs. Caudal) para establecer las firmas base del estado de salud del equipo.
