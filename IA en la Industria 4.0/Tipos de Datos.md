# 📊 Tipos de Datos en Inteligencia Artificial

A continuación, se presentan las referencias conceptuales esenciales mencionadas en el video respecto a las distintas estructuras de datos utilizadas para entrenar modelos de Machine Learning y Procesamiento de Lenguaje Natural (NLP).

---

## 🗃️ Clasificación de los Datos según su Estructura

### 📋 Datos Estructurados
Los **Datos Estructurados** son aquellos que tienen un formato altamente organizado, predefinido y rígido. Su estructura se rige por un modelo de datos lógico que facilita su almacenamiento, búsqueda y análisis rápido.

* 🔍 **Formato común:** Tablas compuestas por filas y columnas (como hojas de cálculo de Excel, archivos `.csv` o bases de datos relacionales SQL).
* ⚙️ **Características:** Cada columna representa una variable específica con un tipo de dato definido (número, fecha, texto corto), lo que permite que los algoritmos de Machine Learning los procesen directamente sin necesidad de transformaciones complejas.
* 🏭 **Ejemplo industrial:** Las lecturas históricas de telemetría de sensores, registros de tiempos de producción y listas de fallas codificadas.

### 📄 Datos No Estructurados
Los **Datos No Estructurados** representan la información que no posee una estructura interna identificable, un formato predefinido o una organización tabular nativa.

* 🔏 **Formato común:** Archivos binarios o colecciones de texto libre que no pueden almacenarse fácilmente en tablas relacionales convencionales.
* ⚙️ **Características:** Constituyen la gran mayoría de los datos generados en el mundo real (aproximadamente el 80%). Para ser utilizados en modelos de Inteligencia Artificial, requieren técnicas de preprocesamiento avanzadas como Deep Learning, Visión por Computadora o NLP para extraer características (*features*) numéricas significativas.
* 🏭 **Ejemplo industrial:** Archivos de audio con ruidos de motores, videos de cámaras de seguridad de la planta, imágenes de piezas para control de calidad o informes técnicos escritos a mano en formato PDF.

---

## 📝 Conceptos de Procesamiento de Lenguaje Natural (NLP)

### 📚 Corpus o Documento
En el contexto del Machine Learning aplicado al texto, un **Documento** es una unidad individual de información escrita (como un artículo, un mensaje o un informe), mientras que un **Corpus** es una colección o conjunto masivo de estos documentos estructurados lógicamente.

* ⚙️ **Función en IA:** El *Corpus* actúa como el "dataset de entrenamiento" especializado para los modelos de lenguaje. Sirve para que los algoritmos aprendan la semántica, la sintaxis, el vocabulario y el contexto de un idioma o de una industria en particular.
* 📊 **Tratamiento técnico:** Antes de entrenar un modelo, el corpus no estructurado pasa por un proceso de tokenización y vectorización para convertirse en una matriz numérica estructurada que la IA pueda comprender.

---

## ⚖️ Cuadro Comparativo de Resumen

| Característica | 📋 Datos Estructurados | 📄 Datos No Estructurados |
| :--- | :--- | :--- |
| **Formato** | Tablas, Filas y Columnas (`SQL`, `CSV`) | Texto libre, Audio, Video, Imágenes |
| **Almacenamiento** | Bases de datos relacionales | Almacenes de objetos (*Data Lakes*, NoSQL) |
| **Flexibilidad** | Esquema rígido y predefinido | Sin esquema o esquema dinámico |
| **Facilidad de Análisis** | Alta y directa por algoritmos tradicionales | Requiere preprocesamiento avanzado (IA/Deep Learning) |
