# 📐 Espacios Vectoriales y Similitud Coseno

A continuación, se presentan las referencias conceptuales para comprender cómo la geometría y la trigonometría se aplican en la Inteligencia Artificial para medir qué tan parecidos son dos elementos (textos, usuarios o productos). 🚀

---

## 🧭 Conceptos Geométricos Básicos

### 📐 Ángulo
El **Ángulo** es la amplitud de la rotación o la separación comprendida entre dos líneas o vectores que se intersectan en un punto común llamado vértice (u origen $0,0$).

* **En Machine Learning:** El ángulo formado entre dos vectores de características nos indica la dirección de sus datos. Si dos vectores apuntan exactamente en la misma dirección, el ángulo entre ellos es de $0^\circ$, lo que denota un comportamiento idéntico en sus patrones, sin importar el tamaño o magnitud de los datos.

### 📊 Coseno
El **Coseno** (denotado como $\cos$) es una función trigonométrica fundamental. En un triángulo rectángulo, se define como la razón entre el cateto adyacente a un ángulo agudo y la hipotenusa.

* **En Espacios Vectoriales:** El cosenó de un ángulo se calcula usando el producto punto (o producto escalar) de dos vectores dividido por el producto de sus magnitudes (longitudes). Su valor numérico oscila estrictamente en el rango cerrado de $[-1, 1]$.

---

## 🧮 Métricas de Comparación en Inteligencia Artificial

### 🎯 Similitud de Coseno (Cosine Similarity)
La **Similitud de Coseno** es una métrica matemática que mide el grado de orientación y semejanza que existe entre dos vectores dentro de un espacio multidimensional. 

* **Independencia de Magnitud:** Su gran ventaja en la IA es que **no toma en cuenta el tamaño o longitud de los vectores**, sino únicamente su dirección. Por ejemplo, en NLP, si un documento corto y un documento largo hablan exactamente del mismo tema, la similitud de coseno será muy alta ($1.0$), ignorando el hecho de que uno tiene más palabras que el otro.
* **Fórmula matemática:** $$\text{Similitud Coseno}(A, B) = \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|}$$

* **Interpretación de Resultados:**
  * **$1$ ($\cos 0^\circ$):** Los vectores son colineales y apuntan en la misma dirección exacta (Similitud máxima/Totalmente parecidos).
  * **$0$ ($\cos 90^\circ$):** Los vectores son ortogonales (perpendiculares). No existe ninguna relación ni coincidencia entre ellos.
  * **$-1$ ($\cos 180^\circ$):** Los vectores son diametralmente opuestos (Comportamiento totalmente inverso).

### 📏 Distancia de Coseno (Cosine Distance)
La **Distancia de Coseno** es el complemento directo de la similitud de coseno. Representa la medida de disimilitud o separación orientativa entre los vectores.

* **Cálculo:** Se obtiene restándole a la unidad ($1$) el valor obtenido en la similitud de coseno:
$$\text{Distancia Coseno} = 1 - \text{Similitud Coseno}$$
* **Interpretación:** Si dos vectores son idénticos, su similitud es $1$, por lo tanto, su distancia de coseno es $0$. Un valor alto de distancia indica que los elementos comparados son geométricamente muy dispares.

---

## 👁️ Resumen Gráfico de Orientación de Vectores

Basado en el plano bidimensional analizado en clase, podemos resumir el comportamiento de los sensores o textos según la apertura de sus vectores:

```text
       ▲ (Variable Y)
       │       
       │     ↗ Vector A (Mantenimiento OK)
       │    / 
       │   / ) θ = Ángulo pequeño (Alta Similitud)
       │  /   \ 
       │ /     \ 
       │/       ➔ Vector B (Mantenimiento OK)
───────┼────────────────────────► (Variable X)
       │
