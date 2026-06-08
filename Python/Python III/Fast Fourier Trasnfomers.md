# 📡 Transformada Rápida de Fourier (FFT) y Filtrado de Señales

El material proporcionado es una inmersión práctica en el procesamiento digital de señales (DSP) utilizando **NumPy** y **SciPy**. Aborda el problema clásico de la ingeniería eléctrica y de telecomunicaciones: analizar una señal en el **dominio del tiempo** y trasladarla al **dominio de la frecuencia** para identificar "ruido" o armónicos indeseados y, posteriormente, eliminarlos mediante técnicas de filtrado espectral.

---

## 🔬 ¿Qué es la Transformada de Fourier?
La Transformada de Fourier es una herramienta matemática que descompone cualquier forma de onda (por más compleja que parezca) en una suma de ondas senoidales puras de diferentes frecuencias y amplitudes. 

La **FFT (Fast Fourier Transform)**, o Transformada Rápida de Fourier, es simplemente un algoritmo altamente optimizado que permite a las computadoras calcular esta descomposición matemática a una velocidad extrema.

### 🔌 1. Análisis de Armónicos
En el primer bloque de código, se genera un escenario clásico de ruido eléctrico.
* **La Señal Base:** Se establece una onda "pura" (fundamental) de $50\\text{ Hz}$ con una amplitud de $220\\text{ V}$ (típica de redes eléctricas).
* **Contaminación (Armónicos):** Se le suman deliberadamente ondas senoidales de frecuencias múltiples ($3\\times50$, $5\\times50$, $7\\times50$, etc.) simulando ruido de alta frecuencia o perturbaciones en la red.
* **Uso de la FFT:** Al aplicar `np.fft.fft(señal)` y graficar sus magnitudes con un diagrama de tallos (`plt.stem`), el "espectro de frecuencia" muestra picos (barras verticales) exactamente en las frecuencias donde inyectamos el ruido ($50\\text{ Hz}$, $150\\text{ Hz}$, $250\\text{ Hz}$, etc.). Esto permite **ver visualmente de qué está compuesto el ruido**.

### 🧹 2. Construcción de un Filtro Digital Manual
El segundo escenario es más avanzado: se tiene una onda de "diente de sierra" ensuciada intencionalmente con una componente de $50\\text{ Hz}$.

El procedimiento de filtrado es el siguiente:
1. **Paso al Dominio de Frecuencia:** Se usa `fft.fft(senal)` para descomponer la señal en un espectro.
2. **Creación de la Máscara (El Filtro):** Se crea un array de unos (`filtro = np.ones(...)`). Un "uno" significa que dejamos pasar esa frecuencia.
3. **Atenuación o Corte:** La línea crítica es `filtro[np.abs(frecuencias) == 50] = 0`. Esto significa: "Busca exactamente la frecuencia de $50\\text{ Hz}$ en el espectro y pon su multiplicador en cero". Al multiplicar el espectro original por este filtro (`espectro * filtro`), **eliminamos matemáticamente** el ruido de $50\\text{ Hz}$. (Nota: Puedes cambiar la lógica para hacer filtros *Pasa-Altos* como `frecuencias < 40 = 0`).
4. **Transformada Inversa (IFFT):** El paso final y "mágico" es usar la Transformada Inversa `fft.ifft(espectro_filtrado)`. Esto toma los datos "limpios" (sin los $50\\text{ Hz}$) y los devuelve al dominio del tiempo. El resultado es una señal de diente de sierra mucho más limpia.

---

## 🛠️ Catálogo de Funciones Clave Utilizadas

* **`np.fft.fft()`:** Transforma un array de valores (dominio del tiempo) en un espectro complejo (dominio de la frecuencia).
* **`np.fft.ifft()` o `scipy.fft.ifft()`:** Realiza la operación inversa, reconstruyendo una señal de tiempo a partir de sus componentes de frecuencia. Fundamental después de aplicar un filtro digital.
* **`np.fft.fftfreq()`:** Esta función no hace el cálculo matemático de la transformada; su trabajo es generar el *Eje X* del espectro. Calcula exactamente qué frecuencia (en Hertz) corresponde a cada punto devuelto por `np.fft.fft()`.
* **`np.abs(fft_resultado)`:** Dado que la FFT devuelve números complejos (que contienen amplitud y fase), se necesita el valor absoluto para graficar la **Amplitud** (magnitud real) de cada componente frecuencial.
* **`np.real(...)`:** Al hacer la transformada inversa (IFFT), pueden quedar pequeños artefactos imaginarios por errores de redondeo de la máquina. `np.real()` asegura que nos quedemos solo con la señal física y real para graficar en el tiempo.


### 🌊 ¿Qué hace la Transformada Rápida de Fourier (FFT)?

Imagina que estás escuchando un acorde tocado en un piano. Tu oído escucha un solo sonido complejo. La **Transformada de Fourier** es como un prisma matemático: toma ese sonido complejo (la onda en el dominio del tiempo) y lo separa en las notas individuales puras que lo componen (el dominio de la frecuencia).

1. **Síntesis (Sumar Ondas):** Como viste en tu código de Python, puedes crear una señal ruidosa sumando una onda fundamental (por ejemplo, 50 Hz) con ondas armónicas más rápidas (150 Hz, 250 Hz).
2. **Análisis (FFT):** La computadora no sabe cómo se creó esa onda. Para descubrirlo, usa la función `np.fft.fft()`. El resultado es un "Espectro", un gráfico que te muestra picos exactos en las frecuencias ocultas dentro de la señal.
3. **Filtrado e IFFT:** Una vez en el dominio de la frecuencia, puedes usar programación para borrar literalmente el ruido (haciendo que la amplitud del ruido sea 0). Luego, usas la Transformada Inversa (`ifft`) para devolver la señal limpia al dominio del tiempo.

