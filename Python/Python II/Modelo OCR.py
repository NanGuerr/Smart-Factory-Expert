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

# Matplotlib
plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large',
       titleweight='bold', titlesize=18, titlepad=10)
plt.rc('image', cmap='magma')
warnings.filterwarnings("ignore")

drive_test = "https://drive.google.com/file/d/1hBoK0ONDI05BKZi3uO9S3Q6v-H0O9NsU/view?usp=sharing"
drive_train = "https://drive.google.com/file/d/1r7xj5Rq2Vtl_TDTgiDsgahM8-pJrk5w3/view?usp=sharing"

ruta_test = 'https://drive.google.com/uc?export=download&id='+drive_test.split('/')[-2]
ruta_train = 'https://drive.google.com/uc?export=download&id='+drive_train.split('/')[-2]
test = pd.read_csv(ruta_test)
train = pd.read_csv(ruta_train)
train2 = train.drop('label',axis=1)
labels = train.pop('label')
# De paso, vemos qué tienen
train2.head()
test.shape,train.shape

test_RS = test.values.reshape(test.shape[0],28,28)
test_RS.shape

i = random.randint(0, test.shape[0])

plt.imshow(test_RS[i])

train_RS = train2.values.reshape(train2.shape[0],28,28)
train_RS.shape

r = random.randint(0, train2.shape[0])


plt.figure(figsize=(5,5))
for i in range(16):
    r = random.randint(0, train2.shape[0])
    image = train_RS[r]
    plt.subplot(4, 4, i+1)
    plt.imshow(tf.squeeze(image))
    plt.axis('off')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(train_RS, labels, test_size=0.2, random_state=42)
X_train.shape,y_train.shape
modelo = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(rate=0.3),
    layers.BatchNormalization(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10)
])

modelo.compile(
    optimizer = 'adam',
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy'],
)

modelo.fit(
    X_train,y_train,
    epochs=40,
)

test_loss, test_acc = modelo.evaluate(X_test, y_test, verbose=2)

print('\nPrueba de precisión:', test_acc)

predicciones = modelo.predict(test_RS)
df2 = pd.DataFrame(predicciones)
df2.head()
i = random.randint(0, test.shape[0])
pred=pd.Series(predicciones[i])
plt.imshow(test_RS[i]),print(pred.idxmax())

# Seleccionamos una imagen random
i = random.randint(0, test.shape[0])

# Le decimos al algoritmo que trate de predecir, y nos indique qué número es.
pred=pd.Series(predicciones[i])
print (f"El número que se identificó en la imagen es {pred.idxmax()}")
print("-----------------")
# y finalmente le pedimos a Python que grafique... A ver si es cierto
print("La imagen que el algoritmo vio es: ")
plt.imshow(test_RS[i])
