# 🧠 Conceptos Avanzados de Machine Learning e Industria 4.0

A continuación, se presentan las definiciones técnicas explicadas en la clase, enriquecidas con la analogía del **"Entrenamiento de un Aprendiz"** que utiliza el instructor en sus diapositivas. ⚙️👨‍🏫

---

## 🧑‍🏫 La Analogía del Aprendiz: ¿Cómo entrena un Modelo?

Para entender cómo se realiza una predicción en Inteligencia Artificial, el instructor plantea una excelente analogía basada en cómo entrenamos a un operador técnico o aprendiz en la planta:

1. **Definir Herramientas (Análogo a *Feature Engineering*):** Le decimos con qué variables o herramientas tiene que trabajar y le armamos la tabla de datos. 🛠️
2. **Definir Objetivos (Análogo a *Target Labeling*):** Le marcamos qué es lo que tiene que lograr o predecir (las etiquetas objetivo). 🎯
3. **Definir Metodologías (Análogo a *Model Selection*):** Elegimos qué método o algoritmo usará según la complejidad de la tarea. 📋
4. **Supervisar Aprendizaje (Análogo a *Hyperparameter Tuning*):** Le reforzamos lo bueno, le pedimos no repetir lo malo y afinamos los parámetros que él no puede aprender por sí mismo. 🔍

---

## 📚 Glosario de Términos Técnicos

### 🛠️ ¿Qué es el Feature Engineering?
El **Feature Engineering** (Ingeniería de Características) es el proceso de seleccionar, transformar, crear o combinar variables relevantes a partir de los datos originales, con el fin de mejorar el desempeño de los modelos de Machine Learning. 

* **Importancia:** Esta etapa es fundamental porque la calidad y pertinencia de las características utilizadas afectan significativamente la capacidad predictiva.
* **Técnicas comunes:** Normalización, codificación de variables categóricas, generación de interacciones entre variables, manejo de valores faltantes y extracción de información clave.

### 🎯 Target Labeling
El **Target Labeling** es el proceso de asignar o identificar cuál es el objetivo o variable de interés (etiqueta llamada *"target"*) en un conjunto de datos que se desea predecir o clasificar.

* **Rol clave:** Define claramente lo que el modelo debe aprender (especialmente en Aprendizaje Supervisado).
* **Formatos:** En tareas de clasificación, implica convertir resultados en categorías (ej. *“falla”* o *“no falla”*), mientras que en regresión se refiere a valores numéricos continuos.

### 📋 Model Selection
El **Model Selection** (Selección de Modelos) es el proceso de comparar múltiples algoritmos o arquitecturas de Machine Learning para determinar cuál se adapta mejor al problema específico y a los datos disponibles.

* **Criterios de evaluación:** Se comparan los algoritmos mediante métricas de validación, balanceando la precisión, la capacidad de generalización frente a datos nuevos, la complejidad computacional y la facilidad de interpretación.

### 🔍 Hyperparameter Tuning
El **Hyperparameter Tuning** (Ajuste de Hiperparámetros) es la búsqueda de los valores óptimos para los parámetros que controlan el funcionamiento interno de un modelo, pero que **no se aprenden de forma automática** durante el entrenamiento.

* **Ejemplos:** La tasa de aprendizaje (*learning rate*), el número de árboles en un Random Forest, o la cantidad de capas de una red neuronal.
* **Estrategias:** Puede hacerse manualmente o mediante algoritmos automáticos como *Grid Search* o *Random Search*.

### 🔀 Algoritmo de Clasificación
Un **Algoritmo de Clasificación** es una técnica de Machine Learning utilizada para asignar una observación a una o más categorías predeterminadas en función de sus características.

* **Resultados:** El output es una etiqueta discreta o booleana (ej. Producto adecuado/defectuoso, llueve/no llueve).
* **Algoritmos populares:** Árboles de decisión, Máquinas de Soporte Vectorial (SVM) o redes neuronales de clasificación.

### 📉 Algoritmo de Regresión
Un **Algoritmo de Regresión** es una metodología de aprendizaje supervisado diseñada para predecir **valores numéricos continuos** en lugar de categorías discretas.

* **Objetivo:** Modelar matemáticamente la relación entre las variables independientes (características) y una variable dependiente continua (ej. Previsión de ventas, estimación de precios o kWh de consumo eléctrico).

### 👥 Aprendizaje Supervisado
Es un paradigma de Machine Learning en el que el modelo es entrenado utilizando un conjunto de datos donde **cada entrada ya está asociada a una etiqueta o respuesta conocida**. El objetivo es que la IA aprenda la relación matemática subyacente para predecir correctamente la salida de datos futuros nunca antes vistos.

### 🕵️ Aprendizaje No Supervisado
Es un enfoque donde el modelo trabaja con **datos no etiquetados**, es decir, sin una variable objetivo explícita. El propósito es que el algoritmo descubra patrones, estructuras o agrupaciones ocultas por sí mismo.

* **Técnicas comunes:** Agrupamiento (*Clustering* como K-Means) y reducción de dimensionalidad (como PCA).

### ✂️ Train Test Split
El **Train Test Split** es la práctica estándar en ciencia de datos donde el dataset inicial se divide en dos subconjuntos independientes:
1. **Train (Entrenamiento):** Generalmente el 70% o 80% de los datos, usado para que el modelo aprenda.
2. **Test (Evaluación):** El porcentaje restante, usado de forma aislada para medir la capacidad real del modelo y evitar el sobreajuste (*overfitting*).

### 📅 Serie de Tiempo
Una **Serie de Tiempo** es una secuencia de datos recolectados, medidos y organizados de forma cronológica (en el tiempo).

* **Aplicación industrial:** Análisis de vibraciones de sensores en tiempo real, tendencias de temperatura o consumos energéticos en plantas.
* **Modelos típicos:** ARIMA, Prophet o redes neuronales recurrentes (RNN/LSTM).
