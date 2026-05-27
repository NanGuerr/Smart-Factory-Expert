# 📊  Algoritmia de Árboles de Decisión 🛠️

Este documento recopila de manera detallada el análisis de las imágenes provistas del material audiovisual sobre **Árboles de Decisión aplicados a la Predicción de Fallas** utilizando la librería de Python **Scikit-Learn**. 🧠

---

## 🔍 1. Análisis de las Imágenes Adjuntas

### 📌 Imagen 1: Hiperparámetros de un Árbol de Decisión en Scikit-Learn
En esta diapositiva se definen los parámetros clave para el control de la estructura y la prevención del sobreajuste (*overfitting*) en el modelo:
* **`max_depth`**: Profundidad máxima del árbol. Un valor menor hace al árbol más explicable pero menos complejo.
* **`min_samples_split`**: Mínimo de muestras en una hoja/nodo para hacer una división. Un mayor valor significa más generalización.
* **`min_samples_leaf`**: Mínimo de muestras en una hoja terminal. Evita que se creen hojas con datos muy específicos o ruidosos.
* **`max_features`**: Número de variables/características/columnas a considerar para buscar el mejor *split* (división) en cada nodo.

### 📐 Imagen 2: Dashboard del Modelo y Evaluación de Rendimiento
Muestra dos componentes fundamentales en el pipeline de un Científico de Datos:
1.  **Estructura del Árbol de Decisión**: Desglose visual de cómo las variables físicas de los sensores clasifican los eventos en "Sin Falla" o "Con Falla".
2.  **Matriz de Confusión**: Herramienta de validación del clasificador:
    * **Verdaderos Positivos (Falla correctamente predicha)**: 9
    * **Verdaderos Negativos (Normalidad correctamente predicha)**: 175
    * **Falsos Positivos (Falsa Alarma)**: 13
    * **Falsos Negativos (Falla no detectada)**: 1 (Crítico en mantenimiento predictivo)

### 🌳 Imagen 3: Árbol de Decisión Desglosado (Predicción de Fallas)
El nodo raíz inicia con la variable `pressure <= 0.265`. El árbol utiliza el **Índice Gini** para medir la impureza de los nodos. Las hojas finales (nodos naranjas y azules) dictaminan la clase de salida:
* 🟤 **Clase: Sin Falla** (Nodos naranjas)
* 🔵 **Clase: Con Falla** (Nodos azules)

---

## 📖 2. Glosario de Definiciones de la Clase

A continuación, se detallan las referencias conceptuales esenciales mencionadas en la sesión formativa:

### ⚙️ Algoritmo de clasificación
Se define como un modelo de inteligencia artificial que asigna una categoría o clase a un conjunto de datos de entrada, permitiendo en mantenimiento predictivo determinar, por ejemplo, si un equipo se encuentra en estado normal o en condición de falla.

### 🌿 Árbol de decisión
Se define como un modelo de clasificación basado en una estructura jerárquica de decisiones, donde los datos se dividen en función de reglas simples, facilitando la identificación de condiciones operativas que conducen a fallas en activos industriales.

### 📈 Score de probabilidad
Se define como el valor numérico que representa la probabilidad estimada por un algoritmo de que un evento ocurra, como la probabilidad de que un equipo falle dentro de un determinado horizonte de tiempo.

### 🛑 Threshold de probabilidad
Se define como el valor límite utilizado para convertir un score de probabilidad en una decisión binaria, determinando a partir de qué nivel de probabilidad se considera que existe una falla o condición anómala.

### 🐍 Scikit Learn
Se define como una biblioteca de programación en Python orientada al aprendizaje automático, ampliamente utilizada en Industria 4.0 para desarrollar modelos de clasificación, regresión y clustering aplicados al mantenimiento predictivo.

### 📏 Profundidad del árbol de decisión
Se define como el número máximo de niveles desde la raíz hasta la hoja más profunda en un árbol de decisión, controlando la complejidad del modelo y su capacidad para capturar patrones en los datos industriales.

### 🍃 Hojas del árbol de decisión
Se define como los nodos terminales de un árbol de decisión donde se asigna una predicción final, como la clasificación de un equipo en estado de falla o funcionamiento normal.

### 🔀 Nodo del árbol de decisión
Se define como cada punto de decisión dentro del árbol donde se evalúa una condición sobre una variable de entrada, permitiendo dividir los datos en subconjuntos más homogéneos para mejorar la precisión del modelo.

---

## 🛠️ 3. Procedimiento General del Algoritmo en la Industria
1. **Captura de datos**: Sensores de presión (`pressure`), flujo (`flow`), potencia (`power`) y revoluciones por minuto (`rpm`).
2. **Entrenamiento con Scikit-Learn**: Ajuste de hiperparámetros como `max_depth` y `min_samples_split` para balancear precisión y estabilidad.
3. **Evaluación de Métricas**: Uso de la matriz de confusión para asegurar que el porcentaje de fallas no detectadas sea el mínimo posible.
4. **Despliegue**: Conversión de las reglas del árbol en alertas automáticas de mantenimiento en planta.
