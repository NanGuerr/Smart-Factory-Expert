# 🧠 Algoritmos, Métricas y Evaluación 📈

Este documento detalla los conceptos fundamentales del campo de la Inteligencia Artificial y la analítica de datos aplicados a la predicción de fallas industriales, complementando el marco operativo y estratégico de la gestión de activos.

---

## 🔮 1. Conceptos Fundamentales de Inteligencia Artificial en Activos

El diseño de un sistema inteligente de monitoreo de condición requiere la articulación de tres pilares lógicos:

### 🎯 A. Predicción
* **Definición:** Es la estimación cuantitativa o cualitativa anticipada de un evento futuro o de un estado desconocido del activo.
* **Mecanismo:** Toma como entradas (*inputs*) los datos históricos del proceso (vibraciones, temperaturas, presiones) y variables operacionales actuales para inferir la probabilidad de degradación mecánica o electrónica antes de que ocurra una parada funcional.

### 🎲 B. Probabilidad
* **Definición:** Es el indicador matemático que cuantifica el nivel de incertidumbre o certeza sobre la ocurrencia de un evento.
* **Escala:** Se expresa en valores numéricos continuos entre `0` y `1` (o del `0%` al `100%`).
* **Ejemplo Práctico:** Una salida algorítmica de **0.85** indica un **85% de probabilidad de falla** en el rodamiento principal dentro de una ventana operativa de 15 días, justificando una intervención en la próxima parada programada.

### ⚙️ C. Algoritmo
* **Definición:** Es la secuencia lógica y ordenada de instrucciones, reglas y cálculos matemáticos diseñados para transformar datos de entrada en salidas accionables.
* **Evolución Tecnológica:** Puede transitar desde sencillos sistemas basados en umbrales estáticos (*if/else*) hasta modelos avanzados de Aprendizaje Automático (*Machine Learning*) como Redes Neuronales o Bosques Aleatorios (*Random Forests*).

---

## 📊 2. Evaluación del Desempeño: Exactitud y Métricas

Desarrollar un algoritmo predictivo es solo la primera mitad del desafío; la segunda consiste en validar estadísticamente si sus salidas son confiables y útiles para el negocio.

### 🎯 Exactitud de una Predicción
Es el grado de correspondencia entre el valor o estado pronosticado por el algoritmo y lo que realmente ocurrió en la planta (*Ground Truth*). Se divide según la naturaleza de la salida:
1. **Clasificación:** Acertar si el equipo fallará o no fallará.
2. **Regresión (Valor numérico):** Qué tan cerca estuvo la estimación de temperatura o vibración del valor real.
3. **Pronóstico (Tiempo - RUL):** Qué tan preciso fue el cálculo del tiempo de vida útil remanente (*Remaining Useful Life*).

### 📐 Métricas de un Algoritmo
Indicadores estandarizados empleados para decidir si el modelo de IA está listo para producción. Se dividen en dos categorías principales según el tipo de problema:

#### 1. Métricas de Clasificación (¿Fallará o No?)
* **Precisión / Accuracy:** Proporción total de predicciones correctas sobre el total de casos. Puede ser engañosa si el conjunto de datos está muy desbalanceado (pocas fallas históricas).
* **Sensibilidad / Recall:** Capacidad del algoritmo para detectar **todas** las fallas reales. Es la métrica más crítica en mantenimiento (un Recall bajo significa que pasamos por alto una falla catastrófica).
* **Precisión Positiva / Precision:** De todas las alarmas lanzadas por el algoritmo, cuántas eran fallas reales. Un valor bajo genera una alta tasa de falsas alarmas, desgastando la confianza del equipo humano.
* **F1-Score:** Promedio armónico entre la Precisión y el Recall; proporciona un balance ideal en datos desbalanceados.
* **Matriz de Confusión:** Tabla cruzada que clasifica los resultados en Verdaderos Positivos (VP), Falsos Positivos (FP), Verdaderos Negativos (VN) y Falsos Negativos (FN).

#### 2. Métricas de Regresión (Predicción Numérica Continua)
Cuando el algoritmo estima valores analógicos o la degradación de un parámetro técnico, se utilizan penalizaciones de error:
* **MAE (Error Absoluto Medio):** Promedio de las diferencias absolutas entre la predicción y el valor real.
* **MSE / RMSE (Error Cuadrático Medio / Raíz del Error Cuadrático Medio):** Penaliza de forma más severa los errores grandes o desviaciones extremas.
* **MAPE (Error Porcentual Absoluto Medio):** Expresa el error en términos de porcentaje, facilitando la interpretación gerencial.

---

## 💡 Métricas Operativas y Costo del Error
Un algoritmo industrial no solo se evalúa por su rendimiento matemático, sino por su viabilidad económica en el centro de control:
* **Tasa de Falsas Alarmas:** Detener un proceso crítico debido a un error del algoritmo genera costos de oportunidad innecesarios.
* **Tiempo de Cómputo:** Capacidad del modelo de procesar los datos de sensores en tiempo real (Edge/Cloud) y emitir alertas antes de que la degradación física sea irreversible.
