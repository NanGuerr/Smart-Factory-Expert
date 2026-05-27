# ⚡ Materiales de la Práctica y Definiciones (Predicción de Consumo Eléctrico)

A continuación, se presentan las referencias de las definiciones clave mencionadas en el video técnico para comprender el comportamiento de la energía y el análisis de señales temporales. 🚀

---

## 🔗 Recursos de la Práctica
Antes de iniciar tu análisis, accede a los entornos de desarrollo y descarga los conjuntos de datos del curso:
* 💻 **Notebook en Google Colab:** [IA 4.0 - Predicción de Consumo Eléctrico](https://colab.research.google.com/drive/1QqmOZjb7knP1jn8YkKXBGrgXIefLeezf?usp=sharing)
* 🗃 **Datos de la práctica:** Disponibles para su descarga directa dentro de la sesión de Colab.

---

## 🔌 Conceptos Fundamentales de Electricidad

### 🔋 Voltaje
El **Voltaje** es la diferencia de potencial eléctrico existente entre dos puntos de un circuito. 

* 📐 **Unidad de medida:** Se mide en voltios (**V**) y representa de forma figurada la "fuerza" que impulsa a los electrones a moverse a través de un material conductor.
* 📈 **En Ciencia de Datos:** En el contexto del consumo eléctrico, el voltaje es una de las variables fundamentales para calcular cuánta energía se consume en un sistema. En análisis de series de tiempo, puede ser una variable relevante si se presentan fluctuaciones críticas que impacten el consumo total, aunque normalmente en entornos residenciales o industriales estables permanece constante.

### 🔌 Amperaje
El **Amperaje** (o corriente eléctrica) representa la cantidad de carga eléctrica (flujo de electrones) que pasa por un punto específico de un circuito por cada unidad de tiempo.

* 📐 **Unidad de medida:** Se mide en amperios (**A**).
* 🔮 **En Modelado Predictivo:** Es una variable crucial para determinar cuánta electricidad se está utilizando en un instante dado. En la predicción de demanda, el amperaje puede transformarse en una serie temporal independiente, o bien utilizarse como una característica (*feature*) para computar el consumo total junto con el voltaje.

### 🧮 Cálculo de Consumo Eléctrico
El cálculo del consumo de energía se divide en dos etapas matemáticas fundamentales:

1. **Potencia Instantánea:** Se calcula multiplicando el voltaje por el amperaje, dando como resultado la potencia real en Watts ($W$).
$$\text{Consumo (Watts)} = \text{Voltaje (V)} \times \text{Amperaje (A)}$$

2. **Energía Acumulada:** Si queremos conocer el consumo integrado durante un período específico (por ejemplo, en kilovatios-hora o $kWh$), multiplicamos la potencia convertida a kW por el tiempo de uso:
$$\text{Energía (kWh)} = \text{Potencia (kW)} \times \text{Tiempo (h)}$$

> 📅 **Nota de IA:** En problemas de series temporales, solemos estructurar y trabajar con estos registros de consumo eléctrico en intervalos regulares de muestreo (minutos, horas, días) para entrenar con éxito nuestros modelos de predicción.

---

## 📅 Componentes de una Serie de Tiempo

### 🔄 Estacionalidad
La **Estacionalidad** en una serie temporal es un patrón de comportamiento cíclico que se repite de manera exacta en intervalos regulares y predecibles de tiempo (ej. ciertas horas del día, días de la semana, o meses del año).

* 🏭 **Causa en consumo eléctrico:** Se genera principalmente por la actividad humana (mayor demanda en las horas de turnos diurnos que en la noche, o picos de consumo estacionales debido al uso intensivo de calefacción o sistemas de aire acondicionado). Detectar y modelar estas curvas cíclicas es la clave para lograr predicciones precisas.

### 📈 Tendencia
La **Tendencia** es el componente de la serie temporal que describe la dirección macro o general del consumo a largo plazo, mostrando si el fenómeno experimenta un aumento, una disminución o una estabilidad sostenida.

* 💡 **Ejemplo:** Una tendencia creciente continua en una planta industrial debido a la expansión de la infraestructura o la incorporación de nueva maquinaria pesada. Su identificación ayuda a entender el comportamiento a largo plazo de la red y a ajustar los sesgos del modelo.

### 📊 Varianza
La **Varianza** es una métrica estadística que mide el grado de dispersión que presentan los datos de consumo eléctrico con respecto a su valor medio central.

* ⚖️ **Interpretación:** Una varianza alta indica que los valores de demanda fluctúan drásticamente en cortos periodos de tiempo (alta inestabilidad), mientras que una varianza baja sugiere que los datos se agrupan de forma compacta alrededor del promedio. Gestionar la varianza sirve para entender la fuerza de la estacionalidad, detectar anomalías operativas y ajustar la complejidad requerida de los modelos predictivos.

### 💨 Ruido
El **Ruido** en las series temporales representa todas aquellas fluctuaciones de datos aleatorias, impredecibles o que pertenecen a factores externos no modelados (tales como errores de lectura en los medidores, interferencias o eventos inesperados puntuales).

* 🧠 **Objetivo de la IA:** Una gran parte del preprocesamiento de datos consiste en separar la "señal auténtica" (tendencia y estacionalidad) del ruido residual, evitando así que los algoritmos sufran de sobreaprendizaje (*overfitting*) al intentar memorizar anomalías atípicas.

---

## 🛠️ Herramientas de Programación

### 🧪 Seasonal Decompose (Librería `statsmodels`)
`seasonal_decompose` es una función analítica avanzada perteneciente al paquete de Python **`statsmodels`** diseñada para realizar la descomposición matemática de una señal.

* ✂️ **Mecánica:** Permite separar una serie temporal cruda en sus tres componentes geométricos aislados: **Tendencia**, **Estacionalidad** y **Residuo (Ruido)**.
* 📋 **Buenas Prácticas:** Su uso es una práctica mandatoria antes de entrenar modelos de Inteligencia Artificial. Permite visualizar detalladamente cuánta variación se debe al calendario, cómo evoluciona la tendencia subyacente y el volumen real del ruido presente en las mediciones. 
* 🎯 **Resultado:** Diagnosticar estos patrones de forma visual ayuda al científico de datos a seleccionar y parametrizar de manera óptima algoritmos avanzados de predicción como **LSTM** (Redes Neuronales Recurrentes) o modelos estadísticos como **ARIMA**.
