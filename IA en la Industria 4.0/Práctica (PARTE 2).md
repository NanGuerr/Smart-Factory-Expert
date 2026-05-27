# 🧠 Materiales de la Práctica y Definiciones (Parte 2)

A continuación, se presentan las referencias conceptuales esenciales mencionadas en la clase para el desarrollo de modelos de **Deep Learning** y análisis de **Series de Tiempo**. ⚙️🚀

---

## 🌐 Recursos de la Práctica
Antes de comenzar, asegúrate de acceder a los entornos de trabajo y descargar los conjuntos de datos del curso:
* 💻 **Notebook en Google Colab:** [IA 4.0 - Mtto Predictivo.ipynb](https://colab.research.google.com/drive/1gU-kIOp9m9-BkoMM2rdhuFuxZnvfNUAU?usp=sharing)
* 🗃️ **Datos de la práctica:** Disponibles dentro del repositorio oficial del curso.

---

## 📚 Glosario de Términos Técnicos

### 📦 Keras
**Keras** es una biblioteca de alto nivel para el desarrollo de redes neuronales profundas, escrita en Python. Ofrece una interfaz sencilla e intuitiva para crear, entrenar y evaluar modelos de *Machine Learning* y *Deep Learning*, permitiendo a investigadores y desarrolladores experimentar rápidamente con diferentes arquitecturas. 

* 🌟 **Ventajas:** Se destaca por su facilidad de uso, modularidad y diseño amigable para el programador.
* ⚙️ **Motores de ejecución:** Tiene la capacidad de ejecutarse sobre motores de cómputo más complejos y avanzados como **TensorFlow**, *Theano* o *Microsoft Cognitive Toolkit (CNTK)*, lo que la convierte en una herramienta estándar para el prototipado rápido y la producción industrial de IA.

### 🕸️ LSTM (Long Short-Term Memory)
Las redes **LSTM** (Memoria a Largo Corto Plazo) son un tipo avanzado de Red Neuronal Recurrente (**RNN**) diseñado específicamente para procesar, analizar y predecir secuencias de datos o datos con dependencia temporal.

* 🔏 **Arquitectura interna:** Incorpora un sistema de "puertas" (*gates*) lógicas que controlan el flujo de información. Esto le permite decidir qué datos recordar por largos períodos y, por el contrario, olvidar la información que ya no es relevante.
* 🛡️ **Solución técnica:** Resuelve de manera eficiente el clásico problema del desvanecimiento o explosión del gradiente (*vanishing gradient*) que sufren las RNN tradicionales.
* 🏭 **Aplicaciones industriales:** Es ampliamente empleada en la predicción de series de tiempo (como consumos eléctricos en plantas), modelado del lenguaje, reconocimiento de voz y generación de texto.

### 📉 Mean Squared Error (MSE)
El **Error Cuadrático Medio** ($MSE$) es una métrica matemática fundamental utilizada para evaluar la calidad y precisión de los modelos de **regresión** en *Machine Learning* y redes neuronales.

* 🧮 **Cálculo:** Mide el promedio de los cuadrados de las diferencias (errores) entre los valores predichos por el modelo y los valores reales observados en el terreno.
* ⚠️ **Efecto de penalización:** Al elevar los errores al cuadrado, esta métrica **penaliza de manera mucho más severa los errores grandes o valores atípicos (*outliers*)**, lo que obliga al modelo a buscar un ajuste más uniforme.
* 🎯 **Interpretación:** Un valor de $MSE$ cercano a cero indica que el modelo tiene un excelente ajuste predictivo y comete un margen de error mínimo.

### ⚖️ MinMaxScaler
**MinMaxScaler** es una técnica de preprocesamiento y normalización de datos utilizada para alterar la escala de las características numéricas de un dataset, ajustándolas estrictamente dentro de un rango determinado, por lo general entre **0 y 1**.

* 🚀 **Impacto en Redes Neuronales:** Las arquitecturas de *Deep Learning* son altamente sensibles a las diferencias de magnitudes entre variables. Lograr homogeneidad en las escalas de los sensores facilita y **acelera drásticamente la convergencia del entrenamiento** al optimizar el descenso de gradiente.
* 📐 **Mecánica matemática:** La transformación resta el valor mínimo de la variable y lo divide por su rango dinámico (máximo - mínimo). Esto garantiza que todas las variables de entrada tengan exactamente la misma importancia jerárquica durante la fase de aprendizaje.
