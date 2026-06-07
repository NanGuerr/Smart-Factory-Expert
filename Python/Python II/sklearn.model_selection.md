# 📑 OCR (Reconocimiento Óptico de Caracteres

En esta ocasión, vamos a trabajar específicamente con un modelo muy simple de **reconocimiento de dígitos** (una versión rudimentaria de un OCR). 🧐

> 💡 **Recomendación:** Les recomiendo fuertemente que vayan pegando cada fragmento de código en una libreta de **Jupyter** (en distintos bloques) y ejecuten uno por uno en orden. 📑

Este tipo de algoritmos se usan para muchísimas tareas. Normalmente, requerirían de equipamiento complejo y especializado, como cámaras de IA industriales (por ejemplo, las que fabrica **Festo** 📸). Hoy, podemos implementar uno nosotros mismos con **Python**. 🐍✨

### 🛠️ Posibles Usos:
*   🚗 Reconocimiento de placas vehiculares.
*   📅 Reconocimiento automático de fechas de vencimiento.
*   🔢 Reconocimiento de dígitos en códigos de barras.
*   📦 Lectura de números de serie para inventarios.
*   📋 Digitalización de documentación.

---

## 1️⃣ Analizar los datos 📊

Primero, cargamos nuestras herramientas. Usaremos **Keras** dentro del módulo **Tensorflow**. 🧠

> ⚠️ **Instalación:** Deben instalar en sus computadoras los siguientes módulos: `pip install numpy pandas matplotlib scikit-learn tensorflow pillow`

```python
import numpy as np 
import pandas as pd
import os, warnings
import matplotlib.pyplot as plt
from matplotlib import gridspec
import random

from sklearn.model_selection import train_test_split
import keras
from keras import layers
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping

# Configuración de Matplotlib 🎨
plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large', titleweight='bold', titlesize=18, titlepad=10)
plt.rc('image', cmap='magma')
warnings.filterwarnings("ignore")

```

Cargamos los datasets desde Google Drive de forma automática: ☁️

```python
drive_test = "[https://drive.google.com/file/d/1hBoK0ONDI05BKZi3uO9S3Q6v-H0O9NsU/view?usp=sharing](https://drive.google.com/file/d/1hBoK0ONDI05BKZi3uO9S3Q6v-H0O9NsU/view?usp=sharing)"
drive_train = "[https://drive.google.com/file/d/1r7xj5Rq2Vtl_TDTgiDsgahM8-pJrk5w3/view?usp=sharing](https://drive.google.com/file/d/1r7xj5Rq2Vtl_TDTgiDsgahM8-pJrk5w3/view?usp=sharing)"

ruta_test = '[https://drive.google.com/uc?export=download&id='+drive_test.split('/](https://drive.google.com/uc?export=download&id='+drive_test.split('/)')[-2]
ruta_train = '[https://drive.google.com/uc?export=download&id='+drive_train.split('/](https://drive.google.com/uc?export=download&id='+drive_train.split('/)')[-2]

test = pd.read_csv(ruta_test)
train = pd.read_csv(ruta_train)
train2 = train.drop('label', axis=1)
labels = train.pop('label')

# Visualizamos el encabezado y las dimensiones 📏
print(train2.head())
print(f"Dimensiones - Test: {test.shape}, Train: {train.shape}")

```

---

## 2️⃣ Evaluar el proceso y preparar los datos 🔍

Cada fila tiene **784 columnas**, que representan los píxeles de una imagen de **28x28**. El valor va de 0 (negro) a 255 (blanco). 🔳🔲

```python
# Reestructuramos (reshape) a matrices de 28x28
test_RS = test.values.reshape(test.shape[0], 28, 28)
train_RS = train2.values.reshape(train2.shape[0], 28, 28)

# Graficamos una muestra aleatoria de números 🎲
plt.figure(figsize=(5,5))
for i in range(16):
    r = random.randint(0, train2.shape[0] - 1)
    image = train_RS[r]
    plt.subplot(4, 4, i+1)
    plt.imshow(tf.squeeze(image))
    plt.axis('off')
plt.show()

# Partimos los datos para entrenamiento y validación ✂️
X_train, X_test, y_train, y_test = train_test_split(train_RS, labels, test_size=0.2, random_state=42)

```

---

## 3️⃣ Generar el modelo 🏗️

Usaremos una **Red Neuronal** de varias capas. La salida tiene **10 neuronas**, una por cada dígito (0-9). 🔢

```python
modelo = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)), # Entrada 28x28
    layers.Dense(128, activation='relu'),
    layers.Dropout(rate=0.3),
    layers.BatchNormalization(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10) # Salida de 10 dígitos
])

modelo.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy'],
)

```

---

## 4️⃣ Entrenar el modelo 🏋️‍♂️

El sistema ajusta miles de funciones lineales (weights y bias) para minimizar el error automáticamente. 🤖

```python
modelo.fit(
    X_train, y_train,
    epochs=40,
)

```

---

## 5️⃣ Realizar inferencias 🧪

Comprobamos la precisión. Si obtenemos **0.97**, significa que el modelo acierta el 97% de las veces. ✅

```python
test_loss, test_acc = modelo.evaluate(X_test, y_test, verbose=2)
print('\nPrueba de precisión:', test_acc)

```

---

## 6️⃣ Crear predicciones / resultados 🔮

Le mostramos al modelo datos que jamás vio para ver si puede identificarlos.

```python
predicciones = modelo.predict(test_RS)

# Ejemplo visual de predicción
i = random.randint(0, test.shape[0])
pred = pd.Series(predicciones[i])
print(f"Predicción (ID máximo): {pred.idxmax()}")
plt.imshow(test_RS[i])

```

---

## 7️⃣ Procesar / Enviar / Mostrar los datos 🖥️

¡Prueba final con imágenes aleatorias! 🏁

```python
# Seleccionamos una imagen random
i = random.randint(0, test.shape[0])

# Predicción
pred = pd.Series(predicciones[i])
print(f"El número que se identificó en la imagen es: {pred.idxmax()}")
print("-----------------")
print("La imagen que el algoritmo vio es:")
plt.imshow(test_RS[i])
plt.show()

```
