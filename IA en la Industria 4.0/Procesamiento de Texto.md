:flag-Br:
:troll-face:
# 🔤 Fundamentos de NLP y Procesamiento de Texto

A continuación, se presentan las referencias de las definiciones mencionadas en el video con respecto a las técnicas esenciales de preparación de datos textuales en Inteligencia Artificial. 🚀

---

## 📚 Glosario de Términos

### 🧩 Token
Un **Token** es la unidad mínima y básica de procesamiento en la que se divide una cadena de texto dentro de un modelo de Inteligencia Artificial.

* 🔍 **Formato:** Dependiendo de la estrategia del modelo, un token puede ser una palabra completa, una subpalabra (*subword*), un carácter individual o incluso un signo de puntuación.
* ⚙️ **Función:** Actúa como el "ladrillo" fundamental que la IA utiliza para analizar estructuras gramaticales, contar frecuencias e interpretar el significado de un mensaje.

### ✂️ Tokenización
La **Tokenización** es el proceso automatizado de segmentar, fragmentar y dividir un texto continuo (no estructurado) en una secuencia ordenada de tokens independientes.

* 💡 **Importancia:** Es el **primer paso mandatorio** en cualquier flujo de trabajo de Procesamiento de Lenguaje Natural (NLP). Sin la tokenización, los algoritmos no podrían aislar los componentes del lenguaje para convertirlos posteriormente en vectores numéricos.
* 🛠️ **Herramientas comunes:** Librerías como `NLTK`, `SpaCy`, `Hugging Face Tokenizers` o las capas nativas de preprocesamiento en `Keras`/`TensorFlow`.

---

## 🛠️ Ejemplo Práctico de Tokenización

Tomando como referencia el flujo técnico expuesto en las diapositivas de la clase, el proceso de segmentación a nivel de palabras funciona de la siguiente manera:

### 📄 1. Texto Crudo (Input)
```text
"La Inteligencia Artificial revoluciona la Industria 4.0."
