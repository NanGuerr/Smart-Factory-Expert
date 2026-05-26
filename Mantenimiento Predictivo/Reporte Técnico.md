# 📊 Gestión de Registro de Fallas y Arquitectura de Datos SQL

Este documento consolida el análisis de la gestión de registros de averías, la ingeniería de datos aplicada a la confiabilidad y la documentación de consultas relacionales a partir del material analítico proporcionado.

---

## 🖼️ 1. Transcripción y Análisis Avanzado de las Imágenes

### 📑 Imagen 1: Diapositiva Conceptual — "REGISTRO DE FALLAS"
* **Texto Principal:**
    > "Ya sea de forma sistematizada o en un reporte no estructurado, la información de las fallas nos ayudará a entender los comportamientos de peligro en los datos recabados, y entrenar mejor los algoritmos de predicción."
* **Sección ¿Cómo Llevar Registro?:**
    * 💻 Interfaz de sistema de fallas (CMMS/GMAO)
    * 📊 Excel
    * 📋 Reporte
    * ✍️ Registro manual *(Marcado explícitamente como **No recomendado**)*
* **Bloque Informativo Destacado (Recuadro Fucsia):**
    > "Documentar causa, activo, costos, downtime... Toda la información servirá para entender mejor el fenómeno y entregar al modelo 'datos' de mejor calidad. ¡Más es mejor!"

#### 🔍 Análisis de la Diapositiva:
La presentación establece la premisa fundamental del **Mantenimiento Predictivo 4.0**: los algoritmos de Inteligencia Artificial y Machine Learning son tan buenos como la calidad de los datos con los que se entrenan (*Garbage In, Garbage Out*). Se penaliza el registro manual debido a su propensión a errores de transcripción, pérdida de trazabilidad y falta de estandarización. El enfoque se centra en capturar la mayor cantidad de variables descriptivas por evento para decodificar patrones ocultos previos a una falla catastrófica.

---

### 💻 Imágenes 2 y 3: Script de Base de Datos (Inserción masiva de Datos SQL)
Las imágenes muestran un fragmento de código estructurado en lenguaje SQL para poblar una tabla relacional denominada `assets_failures`. 

#### 🛠️ Estructura del Query (`INSERT INTO`):
El comando define de manera explícita los siguientes campos estructurados para la tabla:
`asset_id`, `failure_date`, `failure_type`, `severity`, `description`, `root_cause`, `downtime_hours`, `resolved`, `resolution_date`.

#### 📋 Datos Transcritos y Clasificados por Activo (Assets):

##### 🔹 Activos 1 al 4: Bombas Hidráulicas (`Hydraulic Pump`)
* **Asset 1:**
    * `(1, '2022-02-14 08:30:00', 'Ball Bearing Failure', 'medium', 'Pump ball bearing wear detected', 'Normal wear from continuous operation', 4.0, TRUE, '2022-02-14 12:30:00')`
    * `(1, '2023-06-22 14:00:00', 'Cavitation', 'high', 'Cavitation damage to impeller', 'Low inlet pressure and NPSH', 8.0, TRUE, '2022-06-23 22:00:00')` *(Nota: Presenta una anomalía lógica en el año de resolución del script original 2022 vs 2023)*
    * `(1, '2024-11-03 06:45:00', 'Ball Bearing Failure', 'low', 'Ball bearing noise increase', 'Lubrication degradation', 2.5, TRUE, '2022-11-03 09:15:00')`
* **Asset 2:**
    * `(2, '2022-03-08 09:00:00', 'Cavitation', 'medium', 'Cavitation pitting on casing', 'Air ingress in suction line', 5.0, TRUE, '2022-03-08 14:00:00')`
    * `(2, '2023-07-18 11:20:00', 'Ball Bearing Failure', 'medium', 'Bearing cage failure', 'Contamination', 6.0, TRUE, '2022-07-18 17:20:00')`
    * `(2, '2024-10-28 07:00:00', 'Cavitation', 'low', 'Minor cavitation noise', 'Temperature rise', 1.5, TRUE, '2022-10-28 08:30:00')`
* **Asset 3:**
    * `(3, '2022-01-25 10:15:00', 'Ball Bearing Failure', 'high', 'Ball bearing seizure', 'Lack of lubrication', 12.0, TRUE, '2022-01-25 22:15:00')`
    * `(3, '2023-05-12 16:30:00', 'Cavitation', 'medium', 'Cavitation erosion', 'High fluid temperature', 4.5, TRUE, '2022-05-12 21:00:00')`
    * `(3, '2024-09-20 08:00:00', 'Ball Bearing Failure', 'medium', 'Inner race spalling', 'Fatigue', 5.5, TRUE, '2022-09-20 13:30:00')`
* **Asset 4:**
    * `(4, '2022-04-05 07:45:00', 'Cavitation', 'critical', 'Severe cavitation damage', 'Blocked suction filter', 16.0, TRUE, '2022-04-06 23:45:00')`
    * `(4, '2023-08-14 13:20:00', 'Ball Bearing Failure', 'medium', 'Bearing vibration spike', 'Wear', 3.0, TRUE, '2022-08-14 16:20:00')`
    * `(4, '2024-12-01 09:30:00', 'Cavitation', 'low', 'Cavitation onset', 'Low flow operation', 2.0, TRUE, '2022-12-01 11:30:00')`

##### 🔹 Activos 5 al 8: Motores Eléctricos (`Electric Motor`)
* **Asset 5:**
    * `(5, '2022-02-28 11:00:00', 'Ball Bearing Failure', 'medium', 'Motor ball bearing failure', 'Overload and heat', 5.0, TRUE, '2022-02-28 16:00:00')`
    * `(5, '2023-06-10 08:15:00', 'Motor Overload', 'high', 'Winding burnout from overload', 'Sustained overload', 24.0, TRUE, '2022-06-11 08:15:00')`
    * `(5, '2024-10-15 14:30:00', 'Ball Bearing Failure', 'low', 'Bearing grease degradation', 'High ambient temperature', 3.0, TRUE, '2022-10-15 17:30:00')`
* **Asset 6:**
    * `(6, '2022-03-18 06:00:00', 'Motor Overload', 'medium', 'Stator burnout', 'Electrical overload', 18.0, TRUE, '2022-03-18 00:00:00')`
    * `(6, '2023-07-25 10:45:00', 'Ball Bearing Failure', 'high', 'Bearing inner race failure', 'Misalignment', 8.0, TRUE, '2022-07-25 18:45:00')`
    * `(6, '2024-11-08 09:20:00', 'Motor Overload', 'low', 'Thermal overload trip', 'Blocked cooling', 2.0, TRUE, '2022-11-08 11:20:00')`
* **Asset 7:**
    * `(7, '2022-01-12 15:00:00', 'Ball Bearing Failure', 'critical', 'Bearing seizure', 'Lubrication failure', 14.0, TRUE, '2022-01-13 05:00:00')`
    * `(7, '2023-05-30 07:30:00', 'Motor Overload', 'high', 'Winding insulation burnout', 'Overload', 20.0, TRUE, '2022-05-31 03:30:00')`
    * `(7, '2024-09-05 12:00:00', 'Ball Bearing Failure', 'medium', 'Bearing outer race damage', 'Vibration', 4.5, TRUE, '2022-09-05 16:30:00')`
* **Asset 8:**
    * `(8, '2022-04-22 08:00:00', 'Motor Overload', 'medium', 'Rotor bar damage from overload', 'Starting overload', 10.0, TRUE, '2022-04-22 18:00:00')`
    * `(8, '2023-08-08 11:30:00', 'Ball Bearing Failure', 'medium', 'Ball bearing wear', 'Normal wear', 5.0, TRUE, '2022-08-08 16:30:00')`
    * `(8, '2024-12-12 06:45:00', 'Motor Overload', 'low', 'Overload relay trip', 'Peak load', 1.0, TRUE, '2022-12-12 07:45:00')`

---

## 📚 2. Marco Conceptual y Glosario Tecnológico

A continuación se definen los términos fundamentales de ingeniería de confiabilidad y bases de datos requeridos para estructurar la solución predictiva:

### 📑 Registro de Fallas
* **Definición:** Es el historial documentado y trazable de las averías o incidencias sufridas por un activo físico durante su ciclo operativo.
* **Información que contiene:** Incluye campos estructurados indispensables: fecha/hora de inicio, ID del activo afectado, síntomas observados, modo de falla estandarizado (ej: Cavitación, Falla de Rodamiento), severidad del impacto, causa raíz analizada, tiempo total fuera de servicio (*downtime*) y la marca de resolución técnica. Constituye el pilar maestro para auditorías de confiabilidad y entrenamiento de modelos analíticos.

### 🎯 Objetivo de Confiabilidad
* **Definición:** Es la meta medible y cuantificable que define el nivel de rendimiento esperado de un activo o sistema industrial dentro de un período dado.
* **Información que contiene:** Se expresa a través de indicadores clave de rendimiento (KPIs) como la Disponibilidad Operacional, el Tiempo Medio Entre Fallas (MTBF), el Tiempo Medio de Reparación (MTTR) o tasas porcentuales de probabilidad de falla. Funciona como el marco de referencia para justificar las inversiones en mantenimiento preventivo/predictivo.

### 📊 Dataset
* **Definición:** Es una colección estructurada de datos organizada en una matriz de filas (registros u observaciones) y columnas (variables o atributos), depurada y lista para procesos de analítica avanzada.
* **Información que contiene:** Reúne series temporales de sensores (presión, vibración, temperatura), metadatos de las órdenes de trabajo, características estáticas del equipo y etiquetas lógicas de estado (ej: "0" para operación normal, "1" para falla imprevista), esenciales para entrenar modelos supervisados de Machine Learning.

### 📐 Modelo de Datos
* **Definición:** Es la representación abstracta y arquitectónica que determina cómo se estructuran, organizan, validan y relacionan los datos dentro de un sistema de gestión informática.
* **Información que contiene:** Establece las tablas del ecosistema (hechos y dimensiones), los tipos de datos admitidos en cada celda, las restricciones de integridad y las llaves primarias/foráneas (*Primary/Foreign Keys*) que vinculan las lecturas de los sensores con los históricos de falla de los equipos.

### 💻 SQL (Structured Query Language)
* **Definición:** Es el lenguaje de programación estándar e internacional utilizado para administrar, consultar, manipular y extraer información residente en Sistemas de Gestión de Bases de Datos Relacionales (RDBMS).
* **Información que contiene:** Permite ejecutar operaciones mediante sublenguajes internos: DDL (Data Definition Language) para crear tablas y DML (Data Manipulation Language) para interactuar con los registros a través de sentencias estructuradas como `SELECT`, `INSERT`, `UPDATE` y `DELETE`.

### ⚡ INSERT en SQL
* **Definición:** Es la instrucción de manipulación de datos (DML) diseñada para incorporar de forma segura nuevas filas o registros de información dentro de una tabla preexistente.
* **Información que contiene:** Exige declarar el nombre de la tabla destino, la lista ordenada de los campos que se van a poblar y la cláusula `VALUES` que contiene los datos duros correspondientes a ingresar (cadenas de texto, valores numéricos, fechas o booleanos). Es el comando con el que los sistemas automáticos registran una nueva avería o una alerta de sensor en el repositorio central.

---

## 🛠️ 3. Procedimiento Operativo para el Análisis de Datos de Confiabilidad

Para transformar las líneas de código SQL transcritas en información predictiva útil, se establece el siguiente procedimiento técnico estandarizado:

### 📉 Paso 1: Cálculo del MTBF y Análisis de Modos de Falla
Al procesar el dataset de la tabla `assets_failures`, el ingeniero de confiabilidad debe extraer la frecuencia entre eventos de un mismo `asset_id`. Por ejemplo, en las **Bombas Hidráulicas (IDs 1-4)** los dos modos de falla dominantes son `Ball Bearing Failure` (Falla de rodamientos) y `Cavitation` (Cavitación).
* **Cavitación:** Asociada sistemáticamente a la causa raíz `Blocked suction filter` (Filtro de succión obstruido) o `Low inlet pressure` (Baja presión de entrada).
* **Falla de Rodamiento:** Causada por `Lubrication degradation` (Degradación de lubricante) o `Contamination` (Contaminación).

### ⏳ Paso 2: Análisis de Severidad e Impacto en Disponibilidad
El campo `downtime_hours` permite clasificar el impacto real sobre la línea de producción:
* Las fallas marcadas como **`critical`** (como la cavitación severa del Asset 4) generan paradas prolongadas de hasta **16 horas**, afectando drásticamente el *Objetivo de Confiabilidad*.
* Las sobrecargas de motor (**`Motor Overload`**) en los **Motores Eléctricos (IDs 5-8)** reflejan un downtime crítico de hasta **24 horas** (Asset 5, quemadura de devanado), lo que exige la implementación inmediata de sensores de corriente o relés térmicos mejor calibrados.

### 🤖 Paso 3: Pipeline de Carga hacia el Dataset de Machine Learning
El comando `INSERT` es el punto final del flujo de datos en caliente. Para el entrenamiento de un modelo de IA, estas filas se extraen y se cruzan con las tablas de telemetría para crear ventanas temporales de predicción. Si un rodamiento reporta un incremento en la severidad de un síntoma (ej: de *low* a *medium* en ruido/vibración), el algoritmo puede anticipar cuántas horas operacionales restan antes del bloqueo total del componente.
