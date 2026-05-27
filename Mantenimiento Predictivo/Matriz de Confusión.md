# 📊 Indicadores de Rendimiento y Matriz de Confusión 🧮

Este documento técnico consolida los conceptos de evaluación de algoritmos de clasificación para el mantenimiento predictivo, detallando el impacto operacional y financiero de cada métrica en entornos industriales.

---

## 🧩 1. Los Cuatro Cuadrantes de la Verdad (Matriz de Confusión)

Cuando un algoritmo de Inteligencia Artificial procesa variables de sensores para clasificar si un activo industrial va a fallar en una ventana de tiempo (ej. los siguientes 7 días), los resultados se contrastan con la realidad usando una **Matriz de Confusión**.

### 🟢 Verdadero Positivo (TP - True Positive)
* **Definición:** El algoritmo emite una alerta de falla y el equipo efectivamente falla (o se detiene justo a tiempo confirmando la degradación).
* **Impacto:** **Éxito total.** Se ejecuta un mantenimiento predictivo planificado, minimizando el costo de reparación y evitando paradas catastróficas.

### 🟡 Falso Positivo (FP - False Positive)
* **Definición:** El algoritmo genera una alerta de falla, pero el activo se encuentra en perfecto estado operativo.
* **Impacto:** **Falsa alarma.** Provoca inspecciones innecesarias, gasto de horas-hombre y posibles detenciones programadas que restan disponibilidad real a la planta.

### 🔵 Verdadero Negativo (TN - True Negative)
* **Definición:** El algoritmo predice que el activo operará de forma segura y el equipo funciona con normalidad sin presentar anomalías.
* **Impacto:** **Operación estable.** Garantiza la continuidad del proceso productivo con alta confiabilidad en el monitoreo.

### 🔴 Falso Negativo (FN - False Negative)
* **Definición:** El algoritmo indica que todo marcha bien, pero el activo sufre una falla inesperada.
* **Impacto:** **Riesgo crítico / Catástrofe.** Es el escenario más costoso en ingeniería de mantenimiento, ya que implica mantenimiento correctivo de emergencia, daños colaterales en cascada y lucro cesante por pérdida de producción.

---

## 📐 2. Fórmulas Matemáticas e Indicadores de Rendimiento

A partir de los cuadrantes anteriores, se calculan las métricas globales para auditar si el modelo predictivo es apto para producción:

### 🎯 Exactitud (Accuracy)
Mide la proporción total de aciertos del algoritmo (tanto para identificar fallas como estados estables) sobre el universo completo de evaluaciones.

$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$

* **Limitación:** Si en tu histórico de datos el 99% del tiempo los equipos operan bien y solo el 1% falla, un algoritmo defectuoso que siempre diga "No fallará" tendrá un 99% de Exactitud, pero será completamente inútil para prevenir desastres.

### 🧲 Sensibilidad (Recall)
Mide la capacidad del modelo para capturar y detectar **todas** las fallas reales que ocurrieron en la planta. Conocido como la tasa de verdaderos positivos.

$$Recall = \frac{TP}{TP + FN}$$

* **Relevancia:** Es el KPI más crítico en mantenimiento predictivo. Buscamos un Recall cercano al 100% para reducir los Falsos Negativos a cero.

### 🔍 Precisión (Precision)
Mide el grado de confianza de las alertas generadas por el algoritmo. De todas las veces que el modelo encendió la luz de alarma, cuántas resultaron ser fallas verdaderas.

$$Precision = \frac{TP}{TP + FP}$$

* **Relevancia:** Una precisión baja inunda el centro de control con falsas alarmas, provocando que el personal de mantenimiento ignore el software (*fatiga de alarmas*).

---

## 🛠️ 3. Resumen de Impacto Operacional

En el mantenimiento predictivo basado en datos, existe un balance de compensación (*trade-off*) entre el **Recall** y la **Precision**:

* Si ajustas el algoritmo para que sea muy sensible (**Alto Recall**), atraparás todas las fallas, pero aumentarás el riesgo de lanzar falsas alarmas (**Baja Precisión**).
* Si lo ajustas para que solo alerte cuando esté 100% seguro (**Alta Precisión**), evitarás falsas alarmas, pero podrías pasar por alto fallas incipientes rápidas (**Bajo Recall**).

La meta de la analítica en la Industria 4.0 es calibrar los umbrales del modelo buscando el punto óptimo que minimice el costo total del error para el negocio.
