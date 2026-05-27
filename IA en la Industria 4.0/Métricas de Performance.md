# 📊 Métricas de Performance y Evaluación

A continuación, se presentan las referencias de las definiciones clave mencionadas en el video técnico para la correcta evaluación y selección de modelos de Machine Learning. 🚀

---

## 🧮 Fórmulas y Conceptos Clave (Referencia Técnica)

Basado en el material visual del curso, las métricas de clasificación se calculan a partir de la interacción de cuatro variables fundamentales en problemas binarios:
* **VP (Verdaderos Positivos):** Casos reales positivos que el modelo predijo correctamente como positivos.
* **VN (Verdaderos Negativos):** Casos reales negativos que el modelo predijo correctamente como negativos.
* **FP (Falsos Positivos):** Casos reales negativos que el modelo clasificó erróneamente como positivos (Error Tipo I).
* **FN (Falsos Negativos):** Casos reales positivos que el modelo clasificó erróneamente como negativos (Error Tipo II).

---

## 📚 Glosario de Métricas de Evaluación

### 🎯 Exactitud o Accuracy de un Modelo
La **Exactitud**, o *accuracy*, es una métrica de evaluación común en Machine Learning que representa la proporción de predicciones correctas realizadas por un modelo respecto al total de casos analizados.

* **Fórmula matemática:** $$\text{Accuracy} = \frac{\text{VP} + \text{VN}}{\text{VP} + \text{VN} + \text{FP} + \text{FN}}$$
* ⚖️ **Cuándo usarla:** La *accuracy* es especialmente útil cuando las clases están balanceadas en el conjunto de datos, ya que brinda una visión general de cuán frecuentemente el modelo acierta. 
* ⚠️ **Limitación:** Puede ser altamente engañosa si existe un desbalance significativo entre las clases del problema (por ejemplo, en mantenimiento predictivo donde hay un 99% de días normales y solo un 1% de fallas).

### 🔍 Precisión de un Modelo (Precision)
La **Precisión** (*precision*) es una métrica que indica la proporción de verdaderos positivos entre el total de casos que el modelo ha clasificado activamente como positivos.

* **Fórmula matemática:** $$\text{Precision} = \frac{\text{VP}}{\text{VP} + \text{FP}}$$
* 💡 **Pregunta clave que responde:** *“De todas las veces que el modelo predijo un resultado positivo, ¿cuántas veces acertó realmente?”*
* 🚨 **Importancia industrial:** Es fundamental en situaciones donde el **costo de un Falso Positivo es muy alto**. Por ejemplo, si detener una línea de producción por una falsa alarma de falla mecánica cuesta miles de dólares, se requiere un modelo con altísima precisión.

### 🗂️ Matriz de Confusión
La **Matriz de Confusión** es una herramienta visual y tabular de $2 \times 2$ (para casos binarios) que permite evaluar de forma minuciosa el rendimiento de un modelo de clasificación.

* **Estructura de cuadrantes:** Muestra de forma cruzada los valores reales frente a las predicciones del algoritmo, dividiéndolos en:
    * Verdaderos Positivos (VP)
    * Verdaderos Negativos (VN)
    * Falsos Positivos (FP)
    * Falsos Negativos (FN)
* 👁️ **Utilidad:** Ayuda a comprender en detalle los tipos y fuentes exactas de error del modelo, facilitando un análisis mucho más completo de su performance que la simple lectura de un porcentaje general.

### 🛠️ Selección de Modelos en Base a Métricas de Performance
La **Selección de Modelos** consiste en comparar múltiples algoritmos o configuraciones usando criterios cuantitativos estrictos que reflejan su capacidad de predecir correctamente los resultados sobre datos nuevos.

* 📐 **Métricas empleadas:** Entre las más comunes se encuentran la *accuracy*, *precisión*, *recall* (exhaustividad), *F1-score* (promedio armónico entre precisión y recall), el área bajo la curva ROC (AUC-ROC) y el error cuadrático medio (para problemas de regresión).
* 📌 **Criterio de decisión:** La elección del modelo final nunca es estática; depende estrictamente de la naturaleza del problema operativo, el balance de las clases y la importancia relativa de los costos asociados a los distintos tipos de error en el contexto de aplicación real, buscando siempre optimizar la métrica más crítica para los objetivos del negocio.
