# 📑 Clasificación de Reportes de Auditoría con NLP

Este documento reúne las referencias conceptuales y el código base del workshop práctico enfocado en predecir la severidad de reportes de auditoría ISO mediante Procesamiento de Lenguaje Natural (NLP) y Machine Learning. ⚙️🚀

---

## 📚 1. Glosario de Términos Técnicos

### 📋 Reporte de Auditoría
En el contexto de consumo eléctrico, mantenimiento industrial y series de tiempo, un **Reporte de Auditoría** es un documento (manual o automático) donde se analizan y presentan resultados sobre el uso de la energía, patrones detectados, anomalías, cumplimiento de normativas o eficiencia energética. 

* **Aplicación de IA:** Estos reportes pueden crearse de forma automatizada usando modelos que procesan las series de tiempo e identifican patrones anómalos (picos sospechosos, consumos fuera de rango, fallas latentes). 
* **Uso de NLP:** La automatización implica muchas veces el uso de Procesamiento de Lenguaje Natural (NLP) para interpretar descripciones técnicas o generar texto automatizado que explique de forma clara los hallazgos a los encargados de mantenimiento.

### 🐍 NLTK (Natural Language Toolkit)
**NLTK** es una de las bibliotecas de Python más importantes y utilizadas para el procesamiento de lenguaje natural. Está diseñada para limpiar, analizar y transformar texto libre en estructuras procesables.

* **Caso de Uso:** En modelos predictivos industriales, NLTK se utiliza para analizar reportes escritos, descripciones de incidentes mecánicos o comentarios de operadores en planta. Permite extraer información relevante, clasificar la gravedad del texto y limpiar los datos antes de introducirlos a un modelo matemático.

### 🛑 Stopwords
Las **Stopwords** (palabras de parada) son palabras funcionalmente necesarias pero gramaticalmente muy comunes en un idioma (como *"el"*, *"la"*, *"de"*, *"en"* en español). Por lo general, no aportan ningún significado semántico relevante para el análisis automatizado de texto.

* **Optimización:** Eliminar las stopwords ayuda a reducir el ruido del dataset y permite que los modelos de IA se concentren exclusivamente en términos altamente informativos (por ejemplo: *“anomalía”*, *“pico”*, *“apagón”*, *“falla”*).

### ✂️ WordNetLemmatizer
Es una clase especializada de la librería NLTK que utiliza la base de datos léxica *WordNet* para **lematizar** palabras. La lematización consiste en remover las flexiones morfológicas para llevar una palabra a su forma base o raíz canónica (por ejemplo: *"consumidos"*, *"consumiendo"* y *"consume"* se unifican bajo el lema *"consumir"*).

* **Ventaja:** Permite agrupar diferentes variantes de una palabra para analizarlas como una entidad única, mejorando la calidad de clasificación del modelo.

### 🔢 TfidfVectorizer
Herramienta de la biblioteca `scikit-learn` utilizada para convertir texto plano en vectores numéricos mediante el algoritmo **TF-IDF** (*Term Frequency - Inverse Document Frequency*). 

* **Mecánica:** Mide la frecuencia de una palabra dentro de un documento individual y la contrasta con la frecuencia de esa misma palabra en todo el conjunto de reportes (*corpus*). De esta forma, penaliza las palabras comunes y destaca los términos específicos y relevantes.
* **Aplicación:** Transforma los reportes narrativos de auditorías en matrices matemáticas que pueden ser interpretadas por clasificadores automáticos.

### 🧠 MultinomialNB (Naive Bayes Multinomial)
Es una implementación de un clasificador basado en el **Teorema de Naive Bayes**, ideal para trabajar con datos discretos estructurados en conteos o frecuencias de palabras (como los vectores arrojados por *TF-IDF*).

* **Ventaja:** Es un algoritmo sumamente rápido, eficiente y con excelente rendimiento para tareas de clasificación de texto (como categorizar un reporte en *"anomalía detectada"*, *"consumo normal"* o *"urgente"*).

---

## 💻 2. Código de la Práctica (Script de Entrenamiento)

### 📂 Información del Workshop
* **Plataforma:** [Notebook en Google Colab](https://colab.research.google.com/drive/1QqmOZjb7knP1jn8YkKXBGrgXIefLeezf?usp=sharing)
* **Entorno:** Inteligencia Artificial en la Industria 4.0 — Ingelearn
* **Instructor:** Carlos D. Rodríguez
* **Fecha de simulación:** 23/08/2025
* **Objetivo:** Predecir de forma automatizada la severidad de un reporte de auditoría de calidad ISO en una planta industrial.

```python
# ==============================================================================
# 🧠 1. IMPORTACIÓN DE LIBRERÍAS Y RECURSOS
# ==============================================================================
# Aritmética y transformación de datos
import pandas as pd
import numpy as np
import json

# Gráficos
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# NLP: Procesamiento de lenguaje natural
import nltk
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Machine Learning
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Otras librerías
import re
import warnings
warnings.filterwarnings("ignore")

# ==============================================================================
# 📂 2. CARGA Y EXPLORACIÓN DEL DATASET
# ==============================================================================
# Carga del corpus etiquetado
df = pd.read_json("/content/corpus_clase_3.txt")
print(f"Dimensiones iniciales del dataset: {df.shape}")

# Visualización de muestra aleatoria
random_doc = df.sample(n=1)
print(f"\n📄 Documento Aleatorio:\n{random_doc.documento.iloc[0]}")
print(f"🎯 Severidad Real (Target): {random_doc.target.iloc[0]}")

# ==============================================================================
# 📈 3. ANÁLISIS EXPLORATORIO DE DATOS (EDA)
# ==============================================================================
target_counts = df['target'].value_counts()
plt.figure(figsize=(15, 5))

# Gráfico 1: Distribución de Severidad
plt.subplot(1, 3, 1)
target_counts.plot(kind='bar', color='skyblue')
plt.title('Frecuencia de observaciones por target')
plt.xlabel('Categoría de severidad')
plt.ylabel('Frecuencia')
plt.xticks(rotation=0)

# Gráfico 2: Frecuencia de palabras clave en la planta
categorias = ['temperatura', 'capacitación', 'limpieza', 'desorden', 'seguridad', 'higiene', 'incumplimiento']
cat_counts = {cat: df['documento'].str.lower().str.contains(cat).sum() for cat in categorias}

plt.subplot(1, 3, 2)
plt.bar(cat_counts.keys(), cat_counts.values(), color='lightcoral')
plt.title('Frecuencia de palabras clave en reportes')
plt.xlabel('Categoría de auditoría')
plt.ylabel('Frecuencia')
plt.xticks(rotation=30)

# Gráfico 3: Palabras clave cruzadas por nivel de severidad
cat_target_counts = {}
for cat in categorias:
    cat_target_counts[cat] = df.groupby("target")["documento"].apply(
        lambda docs: docs.str.lower().str.contains(cat).sum()
    )

cat_target_df = pd.DataFrame(cat_target_counts).T

plt.subplot(1, 3, 3)
cat_target_df.plot(kind="bar", stacked=False, ax=plt.gca())
plt.title("Frecuencia de palabras clave por target")
plt.xlabel("Categoría de auditoría")
plt.ylabel("Frecuencia")
plt.xticks(rotation=30)
plt.legend(title="Target")

plt.tight_layout()
plt.show()

# ==============================================================================
# 🧪 4. AUMENTO SINTÉTICO DE DATOS Y PIPELINE DE NLP
# ==============================================================================
def augment_data(df, N):
    """Duplica el dataset de forma controlada para mejorar el entrenamiento"""
    augmented_df = pd.concat([df] * (N + 1), ignore_index=True)
    augmented_df = shuffle(augmented_df, random_state=42).reset_index(drop=True)
    return augmented_df

df = augment_data(df, 3) 
print(f"Dimensiones tras el aumento de datos: {df.shape}")

# Inicialización de componentes NLP
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('spanish'))

def preprocess_text(text):
    """Pipeline de limpieza: tokenización, remoción de puntuación, stopwords y lematización"""
    tokens = nltk.word_tokenize(text)
    tokens = [t for t in tokens if t.isalpha()] # Conservar solo palabras
    tokens = [lemmatizer.lemmatize(t.lower()) for t in tokens if t.lower() not in stop_words]
    return ' '.join(tokens)

# Aplicar limpieza de texto
df['documento'] = df['documento'].apply(preprocess_text)

X = df['documento']
y = df['target']

# Extracción de características numéricas con TF-IDF
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# ==============================================================================
# 🏋️‍♂️ 5. ENTRENAMIENTO INCREMENTAL Y EVALUACIÓN
# ==============================================================================
# División del dataset (60% entrenamiento, 40% prueba)
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.4, random_state=42)

model = MultinomialNB()
n_epochs = 5
train_accuracy = []
test_accuracy = []

y_train = np.array(y_train)
classes = np.unique(y_train)

# Simulación de entrenamiento por épocas usando partial_fit
for epoch in range(n_epochs):
    indices = np.arange(X_train.shape[0])
    np.random.shuffle(indices)
    X_train_shuffled = X_train[indices]
    y_train_shuffled = y_train[indices]

    if epoch == 0:
        model.partial_fit(X_train_shuffled, y_train_shuffled, classes=classes)
    else:
        model.partial_fit(X_train_shuffled, y_train_shuffled)

    # Evaluación por época
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    acc_train = accuracy_score(y_train, y_train_pred)
    acc_test = accuracy_score(y_test, y_test_pred)
    
    train_accuracy.append(acc_train)
    test_accuracy.append(acc_test)
    print(f"Época {epoch+1}/{n_epochs}: Train accuracy = {acc_train:.3f} | Test accuracy = {acc_test:.3f}")

# Muestra de métricas finales
print(f"\n🎯 Precisión final en test: {test_accuracy[-1]:.4f}")
print("\n📋 Informe de clasificación detallado:")
print(classification_report(y_test, model.predict(X_test)))
