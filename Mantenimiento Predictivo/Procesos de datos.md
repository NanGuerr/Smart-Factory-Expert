# ⚙️ Procesos de Datos y Pipelines ETL 🧠

Este documento detalla el entorno de desarrollo analítico en Python y el procedimiento metodológico para la extracción, transformación y carga (ETL) de datos de sensórica e historial de fallas, orientado al entrenamiento de modelos de Inteligencia Artificial.

---

## 🛠️ 1. Entorno de Desarrollo y Bibliotecas del Ecosistema Python

Para procesar grandes volúmenes de series de tiempo provenientes de activos industriales, se requiere un conjunto de herramientas estandarizadas que faciliten el Análisis Exploratorio de Datos (EDA) y el prototipado rápido:

* **📊 EDA (Análisis Exploratorio de Datos):** Fase inicial crítica donde se examinan, limpian y comprenden los conjuntos de datos. Permite identificar anomalías físicas, tendencias de desgaste, valores faltantes y correlaciones directas entre variables antes de entrenar algoritmos.
* **📜 Script Python (`.py`):** Archivos de código plano estructurado orientados a la automatización de pipelines de datos y tareas repetitivas en servidores de producción (como el pipeline ETL adjunto).
* **📓 Notebook Jupyter (`.ipynb`):** Documento interactivo que unifica bloques de código ejecutable, visualizaciones dinámicas, fórmulas matemáticas y documentación narrativa, ideal para fases de investigación y prototipado.
* **🐼 Pandas:** Biblioteca estándar para la estructuración y manipulación de datos a través de estructuras multidimensionales denominadas **DataFrames**. Esencial para tareas de limpieza, pivoteo y agregaciones temporales.
* **🔢 NumPy:** Motor de cómputo numérico de alta eficiencia basado en arreglos vectorizados. Permite realizar transformaciones matemáticas y procesamiento de señales a gran velocidad.
* **📉 Matplotlib:** Biblioteca de graficación matemática fundamental para trazar las tendencias analógicas de las variables y evaluar visualmente el desempeño de los modelos predictivos.

---

## 🏗️ 2. Arquitectura del Pipeline ETL (Granularidad Diaria)

El script analizado implementa un proceso **ETL (Extract, Transform, Load)** en Python que compila vectores de características operativas de motores y bombas industriales para predecir si un activo fallará en una ventana de tiempo futura.

```
[ Base de Datos Operativa ]
  ├── plc_sensor_readings
  ├── assets_faliures
  └── mantainance_orders
           │
           ▼ (Extracción por día y activo)
[ Transformación en Pandas / NumPy ] ───> Promedios móviles de 30 días y cálculo de "edad"
           │
           ▼ (Inyección masiva)
[ Tabla Analítica Destino ] ───> `faliure_probability_base` (Lista para Machine Learning)
```

### 📥 A. Fase de Extracción (Extract)
El script se conecta a una base de datos relacional MySQL (`palantir_maintenance`) y extrae información de tres fuentes principales en un rango de fechas determinado (ej. `2022-01-01` a `2023-01-31`):
1. **Lecturas de Sensores:** Datos del PLC recopilados en la tabla `plc_sensor_readings`.
2. **Eventos Históricos:** Registro de paradas catastróficas en `assets_faliures`.
3. **Mantenimiento Preventivo:** Órdenes completadas registradas en `mantainance_orders`.

### 🔄 B. Fase de Transformación e Ingeniería de Características (Transform)
Por cada activo y por cada día del calendario, la función `extract_features_for_asset_date` calcula un vector de **10 características clave** utilizando agregaciones temporales y lógica condicional:

1. **Variables de Proceso (Promedio de los últimos 30 días):**
   * Vibración mecánica, velocidad angular (RPM), potencia, corriente eléctrica, presión y caudal.
2. **Métricas de Tiempo y Envejecimiento:**
   * **Días y horas de servicio:** Tiempo transcurrido desde la fecha de instalación inicial (`installation_date`).
   * **Días desde la última falla:** Tiempo transcurrido desde el último registro en la tabla de fallas.
   * **Días desde la última inspección:** Tiempo transcurrido desde la última orden de trabajo preventiva completada con éxito.

#### 🎯 Definición de la Variable Objetivo (Labeling)
El script aplica una lógica de ventana deslizante hacia el futuro para etiquetar los datos de entrenamiento mediante la función `check_failure_in_next_week`. La columna objetivo **`faliure`** se establece como **`True` (1)** si el activo experimentó una falla real dentro de los **siguientes 7 días** a la fecha de la observación, y **`False` (0)** si operó de manera estable.

### 📤 C. Fase de Carga (Load)
Una vez estructurado el **DataFrame** en Pandas y validados los tipos de datos compatibles con SQL (reemplazando valores nulos `NaN` por `None`), el pipeline ejecuta los siguientes pasos:
1. **Truncar:** Limpia por completo la tabla destino mediante la instrucción `TRUNCATE TABLE faliure_probability_base`.
2. **Validación de Esquema:** Consulta `INFORMATION_SCHEMA.COLUMNS` para asegurar que las columnas generadas coincidan con la estructura de la base de datos.
3. **Inserción Iterativa:** Utiliza la sentencia `INSERT INTO` en bucle para escribir los vectores de características enriquecidos.
4. **Confirmación:** Ejecuta `connection.commit()` al finalizar de forma exitosa o realiza un `rollback()` ante fallas para mantener la integridad relacional.

---

## 📈 3. Métricas de Control del Pipeline
Durante la ejecución, el script imprime métricas clave de balanceo de datos para el analista, calculando la **tasa de fallas (Failure Rate)**: 

$$\text{Tasa de Fallas} = \left( \frac{\text{Filas con falla en siguientes 7 días}}{\text{Total de registros generados}} \right) \times 100$$

Este porcentaje es crucial para detectar problemas de desbalanceo de clases antes de entrenar modelos de Machine Learning de clasificación.


## 🛠️ Entorno de Desarrollo (EDA y Bibliotecas)

Se definen los componentes esenciales para manipular los datos históricos. Bibliotecas como Pandas y NumPy son el motor que permite transformar datos tabulares crudos en matrices legibles, mientras que Matplotlib ayuda a graficar el comportamiento de las señales físicas detectadas en la fase de Análisis Exploratorio de Datos (EDA).

## 🏗️ Lógica del Pipeline ETL

El script extrae registros de sensores de los últimos 30 días (vibration, rpm, pressure, etc.) y calcula métricas de envejecimiento (como los días desde la última falla o inspección). El aspecto más crítico de este script es el etiquetado predictivo (Labeling): calcula si el activo fallará en una ventana de 7 días hacia el futuro, marcando la variable objetivo (faliure) con un 1 o 0. Finalmente, realiza una carga limpia (TRUNCATE + INSERT) de este dataset consolidado en la tabla final.
