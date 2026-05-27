# 📚 Definiciones Básicas

A continuación, se presentan las referencias de las definiciones clave mencionadas en el video técnico para repasar los fundamentos del curso.

---

## 🤖 ¿Qué es un Algoritmo?
Un **Algoritmo** es una serie de instrucciones que permiten procesar datos. En el caso de la ciencia de datos e inteligencia artificial, el producto final del procesamiento de datos es el de realizar una predicción. 

*   **Uso del término:** El término *"Modelo"* también suele ser usado de forma intercambiable con *"Algoritmo"*.
*   ⚠️ **No confundir:** Evite confundirlo con *"Modelo de datos"*, el cual es un concepto relacionado puramente con la ingeniería de datos y no con la ciencia de datos.
*   **Definición de Modelo:** Es una representación matemática o computacional de un proceso real, que se utiliza para predecir, clasificar o analizar datos. En ciencia de datos e inteligencia artificial, los modelos se entrenan con datos históricos y se usan para realizar inferencias o predicciones sobre datos nuevos.

---

## 📊 ¿Qué son los Datos?
Los **Datos** son representaciones variables de un atributo o magnitud cuantitativa o cualitativa. Suelen tener un formato clásico de tabla (datos estructurados), pero pueden presentarse también sin una estructura aparente.

---

## ⚖️ ¿Qué es un Sesgo?
Un **Sesgo** es un peso desproporcionado a favor o en contra de un atributo. También puede entenderse como un desbalance crítico entre las categorías de los datos recopilados.

> 💡 **Ejemplo práctico en la industria:** En un modelo de IA, si contamos con demasiados datos de cierta categoría específica (por ejemplo, registrar muy pocas fallas y mucho funcionamiento regular en una máquina), el modelo aprenderá por inercia que lo más probable que ocurra siempre es la categoría sesgada (el funcionamiento normal), ignorando las anomalías reales.

---

## 🔮 ¿Qué es una Predicción?
Una **Predicción** es una declaración de un evento que se cree que ocurrirá en el futuro con un cierto grado de probabilidad. El objetivo principal de un modelo de inteligencia artificial es generar estas predicciones, ya sea:
*   Una **categoría** (falla o no falla).
*   Una **magnitud** (kWh de consumo eléctrico).
*   **Texto** (la respuesta automatizada a una pregunta).

---

## 🎲 ¿Qué es la Probabilidad?
La **Probabilidad** es una rama de las matemáticas que mide la posibilidad de que ocurra un evento específico. 

*   Se expresa generalmente como un valor numérico entre **0 y 1** (o del **0% al 100%** de probabilidad).
*   Donde `0` significa un evento imposible y `1` significa una certeza absoluta.
*   En ciencia de datos se utiliza activamente para modelar la incertidumbre y tomar decisiones o predicciones en escenarios donde los resultados no son estrictamente deterministas.

---

## 🧪 ¿Qué es la Ciencia de Datos?
La **Ciencia de Datos** es un campo interdisciplinario que utiliza métodos, procesos, algoritmos y sistemas complejos para extraer conocimiento y valor a partir de datos estructurados y no estructurados. Combina la estadística, la informática y el conocimiento de un dominio específico (como los procesos industriales) para analizar grandes volúmenes de información y obtener conclusiones útiles para la toma de decisiones estratégicas.

---

## 🧠 ¿Qué es la Inteligencia Artificial?
La **Inteligencia Artificial (IA)** es el campo de la informática que se enfoca en el desarrollo de sistemas capaces de realizar tareas que normalmente requieren de la intervención o el razonamiento humano, tales como el reconocimiento de patrones complejos, el aprendizaje autónomo, la planificación y la toma de decisiones. La IA abarca subcampos fundamentales como el aprendizaje automático, el procesamiento del lenguaje natural (PLN) y la visión por computadora.

---

## ⚙️ ¿Qué es el Aprendizaje Automático?
El **Aprendizaje Automático** (*Machine Learning*) es una rama directa de la inteligencia artificial que permite a las computadoras aprender patrones ocultos a partir de los datos y mejorar su propio rendimiento en tareas específicas, sin necesidad de ser programadas explícitamente para cada posible situación. Utiliza algoritmos que identifican relaciones matemáticas en los datos y ejecutan predicciones o decisiones basadas en nueva información entrante.

---

## 🎯 ¿Qué es una Variable Objetivo?
Una **Variable Objetivo** (también llamada *variable dependiente* o *variable de respuesta*) es aquella categoría o valor específico que se busca predecir o explicar a través de un modelo de ciencia de datos. 

*   **Ejemplo:** En un modelo enfocado en la predicción de fallas de una máquina, la variable objetivo será la variable `"falla"` o `"no falla"` (de tipo Binaria / Booleana), la cual describe un instante exacto de la historia del activo en el cual ocurrió (o no) una avería.

---

## 🗺️ ¿Cuáles Tipos de Modelos existen?
Existen varios tipos de modelos de acuerdo a la naturaleza de los datos y del problema a resolver. Entre los más comunes se encuentran:
1.  **Modelos Supervisados:** Como los modelos de regresión y de clasificación.
2.  **Modelos No Supervisados:** Como el agrupamiento o *clustering*.
3.  **Modelos de Aprendizaje por Refuerzo.**

> 🛠️ **Nota del curso:** En esta capacitación nos enfocaremos principalmente en los **modelos de clasificación** y en los **modelos no supervisados**.

---

## 📈 ¿Qué son las Métricas de Eficiencia del Modelo?
Las **Métricas de Eficiencia** son indicadores cuantitativos estrictos que permiten evaluar con precisión el desempeño real de un modelo predictivo o de clasificación.

*   **Para Clasificación:** Se utilizan métricas como la *precisión*, *exactitud*, *recall* y el *F1-score*.
*   **Para Regresión:** Se analizan valores como el *error cuadrático medio (MSE)* o el coeficiente de determinación ($R^2$).

Estas métricas son la herramienta principal del científico de datos para comparar objetivamente distintos modelos y elegir el algoritmo más óptimo para una tarea específica en producción.
