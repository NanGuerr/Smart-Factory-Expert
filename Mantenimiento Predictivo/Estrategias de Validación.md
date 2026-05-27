# 🛠️ Ingeniería de Características y Estrategias de Validación de Modelos

Este documento recopila el análisis detallado y descriptivo del segundo conjunto de imágenes proporcionadas, enfocado en las etapas críticas de la preparación de datos (**Ingeniería de Características**) y la correcta metodología de **División de Datos (Data Splitting)** para entornos productivos de Mantenimiento Predictivo. 🧠📈

---

## 📋Ingeniería de Características
Esta diapositiva enumera la lista de comprobación técnica e indispensable antes de entrenar cualquier modelo en la Industria 4.0:
* **Target Balanceado**: Asegurar que las muestras de fallas y normalidad permitan al modelo aprender ambas condiciones por igual.
* **Variables con sesgo eliminadas**: Remoción de aquellas características que desvían la objetividad del algoritmo.
* **Valores faltantes sustituidos**: Proceso de imputación de datos perdidos por cortes de sensor o fallas de red.
* **Variables Numéricas "Escaladas"**: Uniformidad en las magnitudes físicas.
* **Train/Test/Split Balanceado a nivel de target**: Garantía de la misma proporción de fallas en cada subconjunto.

## ⚖️ Escalado (Min-Max Scaling y Standard Scaler)
Se presenta la formalización matemática del escalado y su impacto en las distribuciones de los sensores:
* **Ecuación de Normalización (Min-Max)**: 
    $$\text{x}_{scaled} = \frac{x - x_{min}}{x_{max} - x_{min}}$$
    Transforma los datos a un rango estricto entre $0$ y $1$.
* **Gráficos de Distribución (Antes y Después)**: Muestra visualmente cómo variables con diferentes centros y dispersiones (gráfico *Before Scaling*) se alinean a una misma escala matemática tras aplicar un escalador estándar (*After Standard Scaler*), un paso fundamental para que variables como la potencia (grandes magnitudes) no eclipsen a variables como la presión (pequeñas magnitudes).

## 📐 Train/Test Split (División Simple)
Se detalla la regla de oro clásica en el aprendizaje automático:
* **Conjunto Total (100%)**: Contiene el histórico crudo de Fallas + Normalidad.
* **Datos de Entrenamiento (60% - 90%)**: Base de conocimiento principal que el algoritmo utiliza para estructurar sus reglas o árboles de decisión.
* **Datos de Prueba (10% - 40%)**: Bloque de datos aislado del entrenamiento para auditar de forma objetiva la precisión inicial del modelo.

## 🧪 Train Test Valid Split (División con Validación)
Muestra una evolución metodológica más robusta:
* El histórico total se fragmenta ahora en tres partes esenciales para optimizar hiperparámetros sin incurrir en fugas de datos (*data leakage*):
    * **Entrenamiento**: 60% - 80%
    * **Prueba**: 10% - 20%
    * **Validación**: 10% - 20%

## 🚀 Modelo Productivo (Arquitectura en Operación)
Ilustra el ciclo de vida completo de un modelo de machine learning cruzando la línea del tiempo entre el **Pasado (Histórico)** y el **Presente (Hoy)**:
* **Fase Histórica**: El bloque de datos histórico segmentado en *Entrenamiento*, *Prueba* y *Validación* (Fallas + Normalidad) se utiliza para construir un modelo maduro.
* **Fase de Producción (Hoy)**: Al ingresar **Datos Nuevos** en tiempo real (bloque verde), el modelo los procesa instantáneamente para generar **Nuevas Predicciones** (bloque naranja), alertando de forma oportuna a los equipos de mantenimiento en planta.

---

## 📖 Glosario de Definiciones de la Clase

A continuación, se detallan las definiciones teóricas fundamentales para el desarrollo del procedimiento:

### ⚙️ Ingeniería de características (Feature Engineering)
Se define como el proceso de transformación, creación y selección de variables a partir de datos crudos provenientes de sensores industriales, con el objetivo de mejorar el desempeño de los modelos predictivos en la detección de fallas y anomalías.

### 📉 Variable sesgada
Se define como una variable cuya distribución de datos no es uniforme o está desbalanceada hacia ciertos valores, lo que puede afectar negativamente el aprendizaje del modelo y generar predicciones poco representativas en escenarios industriales.

### ⚖️ Balanceo de variables
Se define como el proceso de ajustar la distribución de las clases o valores en un conjunto de datos, especialmente en problemas de clasificación, para evitar que el modelo se incline hacia la clase mayoritaria y mejore la detección de eventos poco frecuentes como fallas.

### 📏 Escalado de una variable
Se define como la transformación de los valores de una variable a un rango común, con el objetivo de mejorar la estabilidad y el rendimiento de los algoritmos de aprendizaje automático que utilizan datos de diferentes magnitudes provenientes de sensores industriales.

### 🔀 Train/Test Split
Se define como la técnica de división de un conjunto de datos en dos subconjuntos: uno para entrenar el modelo y otro para evaluar su desempeño, permitiendo validar su capacidad de generalización en la predicción de fallas en sistemas industriales.

---

## 📋 Procedimiento Paso a Paso para la Preparación de Datos

1.  **Limpieza e Imputación 🧼**: Identificar registros nulos provenientes de la telemetría industrial y sustituirlos mediante técnicas estadísticas (medias, medianas o interpolación temporal).
2.  **Mitigación de Sesgos 📉**: Evaluar curvas de distribución. Si una variable está fuertemente sesgada, se aplican transformaciones logarítmicas o remociones estratégicas para no confundir al modelo.
3.  **Normalización/Escalado 📏**: Correr algoritmos de escalado (Min-Max o Standard Scaler) sobre las lecturas físicas para homologar rangos (ej. llevar temperaturas de $0$-$150^\circ\text{C}$ y presiones de $0$-$1\text{ bar}$ a una misma escala).
4.  **Estratificación de Datos (Split) 🔀**: Segmentar la información resguardando que tanto el set de *Train*, *Test* y *Valid* cuenten con el mismo porcentaje estricto de la variable objetivo ("Falla").
5.  **Puesta en Producción 🚀**: Conectar el pipeline de transformación con el flujo de datos en tiempo real para evaluar de manera continua la salud de los activos.
