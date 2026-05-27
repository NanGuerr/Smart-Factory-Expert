# 🛠️ Práctica: Mantenimiento Predictivo (PARTE 1)

## 📌 Materiales de la Práctica y Definiciones
Accede a la notebook de la práctica y descarga los conjuntos de datos necesarios para la sesión:
* 🌐 **Notebook en Google Colab:** [IA 4.0 - Mtto Predictivo.ipynb](https://colab.research.google.com/drive/1gU-kIOp9m9-BkoMM2rdhuFuxZnvfNUAU?usp=sharing#scrollTo=QJJDo-OpFzqR)
* 🗃️ **Curso:** Workshop en vivo "Inteligencia Artificial en la Industria 4.0" — **Ingelearn**
* 👨‍🏫 **Instructor:** Ing. Carlos D. Rodríguez
* 📅 **Fecha de la clase:** 31 de Julio de 2025

> 🚀 **Objetivo:** Dar nuestros primeros pasos con la Inteligencia Artificial, utilizando modelos de aprendizaje automático para **predecir fallas en una bomba de agua** industrial.

---

## 🗂️ 1. Configuración del Entorno e Ingesta de Datos

### 📦 Importamos las librerías de Python necesarias
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, ConfusionMatrixDisplay

```

### 📥 Leemos los datos que necesitamos para trabajar

```python
df = pd.read_csv("/content/data_clase_1.csv")
df.shape

```

📦 **Dimensión del Dataset Original:** `(944, 10)` — Contiene 944 registros y 10 columnas de información.

---

## 🔍 2. Análisis Exploratorio de Datos (EDA)

### 🔌 Identificamos los datos de sensor y la variable objetivo (`fail`)

A continuación, se detalla el diccionario técnico de variables registradas por la telemetría de la bomba de agua:

* 👣 **`footfall`**: Cantidad de personas u objetos que pasan cerca de la maquinaria.
* ⚙️ **`tempMode`**: Modo de configuración o setpoint de temperatura de la máquina.
* 💨 **`AQ`**: Índice de calidad del aire (*Air Quality*) en el entorno operativo.
* 🔊 **`USS`**: Datos de sensor ultrasónico (*Ultrasonic Sensor*), mide proximidad o distancias.
* ⚡ **`CS`**: Lecturas del sensor de corriente (*Current Sensor*), consumo eléctrico de la máquina.
* 🧪 **`VOC`**: Nivel de componentes orgánicos volátiles detectados en el aire ambiente.
* 🔄 **`RP`**: Posición rotacional o velocidad de giro en RPM (*Revoluciones por Minuto*).
* 🎈 **`IP`**: Presión de entrada (*Input Pressure*) suministrada al sistema.
* 🌡️ **`Temperature`**: Temperatura operativa interna de la máquina.
* 🚨 **`fail`**: Indicador binario de falla del equipo (**1** si falló, **0** si operó con normalidad).

```python
df.head()

```

### 🔤 Renombrado de columnas para mejorar la interpretación

Para facilitar la lectura del código, traducimos las características técnicas al español:

```python
df = df.rename(columns={
    "footfall": "n_procesados",
    "tempMode": "config_maquina",
    "AQ": "calidad_aire",
    "USS": "sensor_proximidad",
    "sensor_corriente" if "CS" not in df.columns else "CS": "sensor_corriente",
    "CS": "sensor_corriente",
    "VOC": "comp_organicos",
    "RP": "RPM",
    "IP": "presion",
    "Temperature": "temperatura",
    "fail": "falla_objetivo"
})

df.head()

```

### 📊 Graficamos las señales de todos los sensores y la variable de falla

Visualizamos las series temporales de cada variable de manera independiente para identificar patrones visuales rápidos:

```python
df.plot(subplots=True, sharex=True, figsize=(15, 15))
plt.show()

```

### 📈 Inspección Estadística Exhaustiva

Creamos una función personalizada para obtener un resumen del estado de los tipos de datos, valores nulos y duplicados:

```python
def get_summary(df):
    df_desc = pd.DataFrame(df.describe(include='all').transpose())
    df_summary = pd.DataFrame({
        'Tipo de dato': df.dtypes,
        'Faltantes': df.isnull().sum().values,
        'Duplicados': df.duplicated().sum(),
        'Únicos': df.nunique().values,
        'Mínimo': df_desc['min'].values,
        'Máximo': df_desc['max'].values,
        'Media': df_desc['mean'].values,
        'Desviación estandar': df_desc['std'].values,
    })
    return df_summary.style.background_gradient(cmap='Accent_r')

# Observamos los valores estadísticos de cada sensor y categoría
get_summary(df)

```

### 🧼 Limpieza de datos: Eliminación de duplicados

Eliminamos las filas idénticas repetidas para evitar sobreajustar artificialmente el modelo predictivo:

```python
df.drop_duplicates(keep='first', inplace=True)

```

### 🕸️ Análisis de Correlación Lineal (Mapa de Calor)

Evaluamos el nivel de relación lineal entre las variables numéricas mediante una matriz triangular:

```python
mask = np.zeros_like(df.corr())
mask[np.triu_indices_from(mask)] = True

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='viridis', mask=mask)
plt.tight_layout()
plt.show()

```

### 📊 Análisis Distribucional de las Características

Graficamos histogramas y diagramas de barras con intervalos de confianza para examinar el impacto de cada sensor sobre la variable objetivo:

```python
def bar_graph(data: pd.DataFrame):
    _, ax = plt.subplots(5, 2, figsize=(15, 22))  
    ax = ax.flatten()
    for i, col in enumerate(data.columns.tolist()):
        if col == 'n_procesados' or col == 'RPM':
            sns.histplot(data=data, x=data[col], ax=ax[i], bins=14)
            ax[i].set_title(f'{col} hist graph')
        elif col == 'falla_objetivo':
            pass
        else:
            sns.barplot(data=data, x=data[col], y=data['falla_objetivo'], ax=ax[i], errorbar=('ci', 10))
            ax[i].set_title(f'{col} bar graph')
            for p in ax[i].patches:
                ax[i].annotate(format(p.get_height(), '.2f'),
                               (p.get_x() + p.get_width() / 2., p.get_height()),
                               ha='center', va='center',
                               xytext=(0, 9),
                               textcoords='offset points')
    plt.delaxes()
    plt.tight_layout()  
    plt.show()

bar_graph(df)

```

---

## 🛠️ 3. Ingeniería de Características y Partición (*Train/Test Split*)

### 🧪 Creación de nuevas variables (*Feature Engineering*)

Diseñamos variables sintéticas que ayuden al árbol de decisión a segmentar los datos de manera más óptima:

```python
# 1. Diferencial absoluto de temperatura vs configuración teórica
df['temp_diff'] = np.abs(df['temperatura'] - df['config_maquina'])

# 2. Desviación de las RPM respecto al promedio del activo
df['RP_Avg'] = np.round((df['RPM'] - df['RPM'].mean()))

# Separación de variables predictoras (X) y etiqueta objetivo (y)
X = df.drop('falla_objetivo', axis=1)
y = df['falla_objetivo']

# División estratificada para asegurar proporciones idénticas de fallas en ambos conjuntos
seed = 10256
train_x, valid_x, train_y, valid_y = train_test_split(X, y, test_size=0.2, stratify=y, random_state=seed)

train_x.shape, valid_x.shape

```

📐 **Dimensiones resultantes:** Conjunto de entrenamiento = `(754, 11)` | Conjunto de validación = `(189, 11)`.

---

## 🤖 4. Entrenamiento y Estructura del Modelo

### 🌲 Instanciación del Árbol de Decisión Clasificador

```python
clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(train_x, train_y)

```

### 🗺️ Graficamos la estructura lógica del Árbol Clasificador

Exportamos el esquema gráfico en alta resolución para comprender las reglas lógicas que el algoritmo dedujo para clasificar las fallas:

```python
fig, ax = plt.subplots(figsize=(30, 15), dpi=200)  
plot_tree(clf,
          feature_names=train_x.columns,
          class_names=[str(cls) for cls in clf.classes_],
          filled=True,
          rounded=True,
          fontsize=8)
plt.show()

```

---

## 📈 5. Evaluación de Métricas de Eficiencia

### 🧮 Función de evaluación y Matriz de Confusión

```python
def evaluate_classifier(model, X_test, y_test):
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    rec = recall_score(y_test, y_pred, average='weighted', zero_division=0)

    print(f"Accuracy (Exactitud): {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall (Efectividad retroactiva): {rec:.4f}")

    # Despliegue visual de la Matriz de Confusión
    cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot(cmap=plt.cm.Blues)
    plt.show()

# Evaluamos el rendimiento en el conjunto de entrenamiento
evaluate_classifier(clf, train_x, train_y)

```

---

## 🔮 6. Simulación de Predicciones en Tiempo Real

### 🎲 Función para predecir un registro aleatorio del histórico

```python
def predict_random_row(model, df_features, df_target):
    random_index = np.random.randint(0, len(df_features))
    row = df_features.iloc[random_index]
    prediction = model.predict([row])
    print("🎯 Fila aleatoria elegida:", random_index)
    print(" ")
    print("📋 Columnas de datos ingresadas:\n", row)
    print("\n🚨 Valor objetivo real de falla:", df_target.iloc[random_index])
    print("🔮 Predicción arrojada por la IA:", prediction[0])

# Simulación de uso:
predict_random_row(clf, train_x, train_y)

```

### 🖥️ Salida de la simulación (*Output*):

```text
🎯 Fila aleatoria elegida: 551
 
📋 Columnas de datos ingresadas:
n_procesados         1600.0
config_maquina          7.0
calidad_aire            5.0
sensor_proximidad       3.0
sensor_corriente        6.0
comp_organicos          6.0
RPM                    50.0
presion                 7.0
temperatura            23.0
temp_diff              16.0
RP_Avg                  3.0
Name: 851, dtype: float64

🚨 Valor objetivo real de falla: 1
🔮 Predicción arrojada por la IA: 0

```

> ⚠️ **Nota de Análisis Técnico:** En esta corrida específica, observamos un **Falso Negativo** (el valor real era `1` pero la IA predijo `0`). Esto indica que el modelo requiere un ajuste de hiperparámetros avanzado (*Hyperparameter Tuning*) o la inclusión de más datos complejos de fallas para refinar su precisión en las fronteras de decisión del árbol.

---
