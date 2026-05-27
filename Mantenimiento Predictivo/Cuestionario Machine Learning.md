# 📊 Cuestionario Machine Learning ⚙️

Este documento contiene una serie de preguntas y respuestas justificadas sobre los fundamentos de **Mantenimiento Predictivo (PdM)** y la aplicación de modelos de **Inteligencia Artificial / Machine Learning** en la industria.

---

### 1. ¿Qué se entiende por mantenimiento predictivo? 🔍

* **A.** Estrategia de mantenimiento basada en el monitoreo del estado real de los equipos.
* **B.** Método que utiliza sensores y análisis de datos para anticipar fallas.
* **C.** Enfoque que predice cuándo un activo puede fallar para intervenir antes de la avería.
* **D.** Sistema de mantenimiento apoyado en inteligencia artificial, IIoT y analítica avanzada.
* **E.** Evolución del mantenimiento preventivo hacia decisiones basadas en condición y datos.
* **F. Todas las anteriores** ✅

👉 **Respuesta correcta:** **F. Todas las anteriores** *Justificación:* El mantenimiento predictivo es un concepto integral. Engloba desde el uso de hardware (sensores e IIoT) hasta técnicas avanzadas de software (analítica e IA) con el único objetivo de monitorear la condición real del activo para adelantarse a los fallos de manera óptima.

---

### 2. ¿Qué resultados se esperaría ver en el corto o mediano plazo al aplicar Mantenimiento Predictivo? 📈

* **A.** Disminución de paradas no programadas.
* **B.** Mejor visibilidad del estado de los activos.
* **C.** Alertas tempranas más confiables.
* **D.** Mejor uso del personal técnico.
* **E.** Reducción del gasto en correctivos.
* **F. Todas las anteriores** ✅

👉 **Respuesta correcta:** **F. Todas las anteriores** *Justificación:* Desde los primeros meses de implementación se genera un impacto positivo en la operación. Se reducen los "apagados de incendios" (correctivos urgentes), los técnicos trabajan bajo planificación inteligente y la visibilidad basada en datos en tiempo real minimiza drásticamente los paros inesperados de producción.

---

### 3. ¿Qué es un modelo de datos? 🗺️

* **A.** Un archivo donde se guardan datos en Excel.
* **B.** Una representación estructurada de los datos, sus relaciones y reglas dentro de un sistema. 📑
* **C.** Un sensor que captura información en tiempo real.
* **D.** Un algoritmo que siempre predice fallas.

👉 **Respuesta correcta:** **B. Una representación estructurada de los datos, sus relaciones y reglas dentro de un sistema.** *Justificación:* Un modelo de datos actúa como el plano arquitectónico de la información. Define de forma lógica qué datos se recolectan, las características de estos y cómo se interconectan las diferentes tablas o entidades del negocio.

---

### 4. ¿Qué es un algoritmo de clasificación? 🏷️

* **A.** Un método que predice valores continuos como temperatura o costo.
* **B.** Un algoritmo que aprende a asignar una categoría o clase a cada observación. 🗂️
* **C.** Un proceso para eliminar datos duplicados.
* **D.** Un sistema que únicamente almacena datos históricos.

👉 **Respuesta correcta:** **B. Un algoritmo que aprende a asignar una categoría o clase a cada observación.** *Justificación:* Los algoritmos de clasificación pertenecen al aprendizaje supervisado y su meta es asignar etiquetas discretas o categorías predefinidas a los nuevos datos (por ejemplo: clasificar si un equipo está "Sano" o "En Falla").

---

### 5. ¿Cómo se mide el "recall" de un modelo? 🎯

* **A.** Verdaderos positivos / (Verdaderos positivos + Falsos positivos)
* **B.** Verdaderos positivos / (Verdaderos positivos + Falsos negativos) 📐
* **C.** (Verdaderos positivos + Verdaderos negativos) / Total de observaciones
* **D.** 2 × (Precisión × Recall) / (Precisión + Recall)

👉 **Respuesta correcta:** **B. Verdaderos positivos / (Verdaderos positivos + Falsos negativos)** *Justificación:* El *Recall* (o sensibilidad) mide la capacidad del modelo para identificar todos los casos reales positivos. En mantenimiento predictivo, un alto recall asegura que el modelo detecte casi todas las fallas reales del sistema, minimizando los peligrosos falsos negativos.

---

### 6. ¿Cómo está compuesta una solución de Mantenimiento Predictivo extremo a extremo? 🌐

* **A.** Solo por sensores y un tablero de control.
* **B.** Únicamente por un software en la nube.
* **C.** Captura de datos, almacenamiento, limpieza/procesamiento, ingeniería de variables, entrenamiento del modelo, despliegue, alertas e integración con operación/mantenimiento. 🛠️
* **D.** Solo por órdenes de trabajo y técnicos de mantenimiento.

👉 **Respuesta correcta:** **C. Captura de datos, almacenamiento, limpieza/procesamiento, ingeniería de variables, entrenamiento del modelo, despliegue, alertas e integración con operación/mantenimiento.** *Justificación:* Una solución *end-to-end* (extremo a extremo) requiere conectar toda la cadena de valor del dato: desde la extracción física en la máquina por sensores, pasando por los pipelines de inteligencia artificial en la nube/servidor, hasta desencadenar una acción u orden de trabajo en el sistema de mantenimiento de la planta.

---

### 7. ¿Qué es una variable target en un modelo de predicción de fallas? 🎯

* **A.** La variable con más datos faltantes.
* **B.** La variable que tiene más columnas relacionadas.
* **C.** La variable objetivo que el modelo busca predecir, por ejemplo “falla” o “no falla”. 🏁
* **D.** La variable que siempre proviene de un sensor de temperatura.

👉 **Respuesta correcta:** **C. La variable objetivo que el modelo busca predecir, por ejemplo “falla” o “no falla”.** *Justificación:* La variable *target* u objetivo representa la etiqueta o el valor final que queremos que el algoritmo aprenda a calcular de manera autónoma utilizando las variables predictoras (o *features*).

---

### 8. ¿Qué comportamientos o características tiene un modelo de predicción de fallas? ⚡

* **A.** Variables como vibración, temperatura, presión, corriente, horas de operación, tendencias, picos y estadísticas derivadas de las señales. 📊
* **B.** Solo el nombre del equipo y su código interno.
* **C.** Únicamente la fecha de compra del activo.
* **D.** Solo la variable target.
* **F.** Todas las anteriores

👉 **Respuesta correcta:** **A. Variables como vibración, temperatura, presión, corriente, horas de operación, tendencias, picos y estadísticas derivadas de las señales.** *Justificación:* Los modelos de mantenimiento predictivo necesitan datos de alta densidad que describan las condiciones operativas y el desgaste real de la maquinaria. Los metadatos administrativos (como el código o la fecha de compra) no son suficientes para pronosticar un fallo técnico inminente.

---

### 9. ¿Cuál método Python de la clase debería usarse para predecir el modelo? 🐍

* **A.** adaptar()
* **B.** puntaje()
* **C.** predecir() 🧠
* **D.** tren()

👉 **Respuesta correcta:** **C. predecir()** *Justificación:* En las librerías estándar de Data Science en Python (como *Scikit-Learn*), el método nativo utilizado para generar estimaciones o inferencias con nuevos datos es `.predict()`, que traducido conceptualmente al español corresponde a `predecir()`.

---

### 10. ¿Qué algoritmo debemos usar para predecir categóricamente? 🤖

* **A.** Un algoritmo de clasificación, como Regresión Logística, Árbol de Decisión o RandomForestClassifier. 🌲
* **B.** Un algoritmo de regresión lineal.
* **C.** Un método de reducción de dimensionalidad como PCA.
* **D.** Un algoritmo de agrupamiento como K-Means.

👉 **Respuesta correcta:** **A. Un algoritmo de clasificación, como Regresión Logística, Árbol de Decisión o RandomForestClassifier.** *Justificación:* Para resolver problemas donde la variable de salida es discreta o cualitativa (categorías), se implementan algoritmos de clasificación. La regresión lineal maneja datos continuos, mientras que PCA y K-Means pertenecen al aprendizaje no supervisado.
