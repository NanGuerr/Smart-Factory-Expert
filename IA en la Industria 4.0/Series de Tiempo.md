# 📊 Relaciones de Datos y Series de Tiempo

A continuación se presentan las referencias conceptuales mencionadas en la clase, organizadas de manera visual para facilitar el estudio y repaso de los temas. 🚀

---

## 🔗 Relaciones entre Variables

### 🔀 Correlación
La **Correlación** es una medida estadística que cuantifica la fuerza y el sentido (positivo o negativo) de la relación lineal entre dos variables.

* **En Machine Learning:** Analizar la correlación es esencial para comprender cómo varían conjuntamente determinadas características, identificar redundancias en los datos (multicolinealidad) y seleccionar las variables más influyentes para los modelos predictivos.
* ⚠️ **Regla de Oro:** Es sumamente importante recordar que **correlación no implica causalidad**. Two variables pueden moverse de forma idéntica sin que una sea la causa de la otra.

### 🎯 Causalidad
La **Causalidad** se refiere a la relación en la que una variable directamente influye o provoca cambios reales en otra. 

* A diferencia de la correlación, que únicamente indica que dos variables se mueven juntas de manera estadística, la causalidad implica la existencia de un mecanismo físico o lógico de **causa y efecto**.
* **En Machine Learning:** Identificar relaciones causales es clave para tomar decisiones informadas en la industria, diseñar experimentos y construir modelos robustos que puedan anticipar el impacto exacto de intervenciones específicas en el sistema analizado.

### 📏 Linealidad
La **Linealidad** describe la relación entre variables en la que el cambio en una de ellas produce un cambio directamente proporcional en la otra, dibujando una línea recta perfecta al representarse gráficamente.

* Muchos algoritmos tradicionales de Machine Learning asumen linealidad en los datos para simplificar los cálculos y facilitar la interpretación del modelo. Determinar su existencia ayuda a elegir si se debe abordar el problema con un enfoque lineal o con modelos más complejos (no lineales).

### 📉 Regresión Lineal
La **Regresión Lineal** es una técnica estadística y de Machine Learning utilizada para modelar la relación matemática entre una variable dependiente continua (*target*) y una o más variables independientes (*features*), bajo la suposición de que dicha relación es lineal.

* 🎯 **Objetivo Principal:** Encontrar la línea recta (hiperplano) que mejor se ajuste a la nube de puntos dispersos, minimizando la distancia o error entre las predicciones del algoritmo y los valores reales observables. Es una herramienta fundamental para la previsión y análisis de tendencias.

---

## 📅 Análisis de Series de Tiempo

### ⏱️ Series de Tiempo
Las **Series de Tiempo** son colecciones de observaciones indexadas u ordenadas cronológicamente y tomadas de manera secuencial a intervalos regulares de tiempo (ej. por segundo, por hora, diariamente).

* **Aplicación en Industria 4.0:** Son fundamentales para analizar y predecir el comportamiento de variables que evolucionan de forma continua, como los precios de activos, la demanda energética de una planta o las telemetrías climáticas. Permiten proyectar comportamientos futuros con base en patrones del pasado.

### 🔍 Descomposición de una Serie o Señal
La **Descomposición** es el proceso de desagregar y separar una serie de tiempo en sus componentes matemáticos fundamentales. Típicamente se descompone de forma aditiva o multiplicativa en tres ejes principales: **Tendencia, Estacionalidad y Ruido**.

* Esta técnica facilita enormemente el análisis y la interpretación de las fuerzas subyacentes en las mediciones, aislando los efectos individuales para alimentar modelos predictivos más precisos.

### 📈 Componente 1: Tendencia
La **Tendencia** representa el movimiento o patrón a largo plazo que presenta una serie de tiempo, indicando si el fenómeno muestra un comportamiento general de aumento, disminución o estabilidad sostenida.

* Su identificación permite entender la dirección macro de la variable y ayuda a eliminar el impacto distorsionador de las fluctuaciones menores de corto plazo.

### 🔄 Componente 2: Estacionalidad
La **Estacionalidad** se refiere a las fluctuaciones y patrones cíclicos que se repiten de manera regular y predecible a lo largo de intervalos específicos de tiempo (ciclos diarios, semanales, mensuales o anuales).

* **Ejemplo:** El pico de consumo eléctrico de una planta a una hora determinada del turno, o el aumento de ventas en una temporada del año. Capturar este componente previene errores drásticos en las previsiones dependientes del calendario.

### ⚡ Componente 3: Volatilidad
La **Volatilidad** es una medida de la variabilidad, dispersión o tasa de cambio de una serie temporal. Indica cuán abruptamente y con qué frecuencia varía el valor de una variable en un periodo corto.

* Altos niveles de volatilidad representan incertidumbre, riesgo o inestabilidad. Su cálculo es crucial en el **mantenimiento predictivo** para detectar variaciones extremas en sensores que preceden a una falla mecánica catastrófica.

### 💨 Componente 4: Ruido
El **Ruido** es la variabilidad aleatoria, residual e impredecible presente en las mediciones. Representa componentes de datos que no obedecen a ningún patrón sistemático y que no pueden ser explicados por la tendencia ni por la estacionalidad.

* En Machine Learning se aplican filtros de señales para minimizar la influencia del ruido, permitiendo que los modelos se concentren únicamente en detectar patrones significativos y estables.

---

## 🔌 Aplicaciones Eléctricas e Industriales

### 🌀 Corrientes Parasitarias
Las **Corrientes Parasitarias** (también conocidas como *corrientes de Foucault*) son corrientes eléctricas que se inducen de forma local en materiales conductores cuando estos se ven expuestos a una variación en los campos magnéticos del entorno.

* 🛠️ **En Mantenimiento Predictivo:** Se emplean de forma activa como una técnica de ensayo no destructivo (END) para fisuras, permitiendo detectar defectos superficiales o anomalías en materiales sin dañar la integridad de los componentes mecánicos.
* ⚠️ **Como Ruido Técnico:** Por otro lado, si estas corrientes inducidas indeseadas afectan las lecturas de los instrumentos de medición eléctrica o los sensores de los equipos de planta, actúan como una fuente de interferencia o "ruido de datos" que debe ser identificada y filtrada para evitar diagnósticos falsos del estado de la maquinaria.
