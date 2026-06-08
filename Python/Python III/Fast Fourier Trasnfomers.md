# 🛜 Fast Fourier Trasnfomers

```python

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
frecuencia_fundamental = 50  # Hz
amplitud_fundamental = 220
amplitud_3er_arm = 220*0.1  # 10% del valor de la fundamental
amplitud_5to_arm = 220*0.1  # 5% del valor de la fundamental
amplitud_7mo_arm = 220*0.2  # 2% del valor de la fundamental
amplitud_9no_arm = 220*0.2  # 2% del valor de la fundamental
amplitud_11vo_arm = 220*0.2  # 2% del valor de la fundamental
duración = 1.0  # segundos
frecuencia_muestreo = 8000  # Hz (frecuencia de muestreo)

# Generar tiempo discreto
t = np.linspace(0, duración, int(duración * frecuencia_muestreo), endpoint=False)

# Generar señal con armónicos
señal = (
    amplitud_fundamental * np.sin(2 * np.pi * frecuencia_fundamental * t) +
    amplitud_3er_arm * np.sin(2 * np.pi * 3 * frecuencia_fundamental * t) +
    amplitud_5to_arm * np.sin(2 * np.pi * 5 * frecuencia_fundamental * t) +
    amplitud_7mo_arm * np.sin(2 * np.pi * 7 * frecuencia_fundamental * t)+
    amplitud_9no_arm * np.sin(2 * np.pi * 9 * frecuencia_fundamental * t)+
    amplitud_11vo_arm * np.sin(2 * np.pi * 11 * frecuencia_fundamental * t)
)

seno = amplitud_fundamental * np.sin(2 * np.pi * frecuencia_fundamental * t)

# Graficar la señal
plt.plot(t[25:125], señal[25:125])
plt.plot(t[25:125], seno[25:125])
plt.title('Onda Senoidal con Armónicos')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()

# Realizar la Transformada Rápida de Fourier (FFT)
fft_resultado = np.fft.fft(señal)
frecuencias = np.fft.fftfreq(len(señal), d=1/frecuencia_muestreo)

# Obtener los valores de amplitud (magnitud) de la FFT
amplitudes = np.abs(fft_resultado)

# Graficar los resultados de la FFT
plt.figure(figsize=(10, 6))
plt.stem(frecuencias, amplitudes, use_line_collection=True)
plt.title('Espectro de Frecuencia')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.xlim(0, 1000)  # Mostrar hasta 1000 Hz para enfocarse en los armónicos bajos
plt.show()

```

# ⚗️ Filtros con Numpy y FFT

Otra forma interesante de procesar los datos es aprovechar los cálculos complejos que podemos realizar con Numpy y Pandas. Aquí hacemos una demostración de cómo una señal "contaminada" con armónicos de 50 Hz puede filtrarse analizando su espectro en frecuencia.
Prueben jugar con los valores en el filtro filtro[np.abs(frecuencias) == 50] = 0 , usando valores como filtro[np.abs(frecuencias) > 30] = 0 ó filtro[np.abs(frecuencias) < 40] = 0

```python

import numpy as np
import matplotlib.pyplot as plt
from scipy import fft, signal
​
# Crear una señal compuesta por un diente de sierra con una componente senoidal de 50 Hz
fs = 1000  # Frecuencia de muestreo
t = np.arange(0, 1, 1/fs)  # Vector de tiempo de 1 segundo
plt.style.use("ggplot")
frecuencia_senoidal = 50  # Frecuencia de la componente senoidal de 50 Hz
senal = signal.sawtooth(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * frecuencia_senoidal * t)
​
# Realizar el análisis de Fourier
frecuencias = fft.fftfreq(len(t), 1/fs)
espectro = fft.fft(senal)
​
# Graficar la señal original, el espectro y la señal filtrada
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, senal)
plt.title("Señal Original")

```
# 📊 Graficar el Espectro Original

```python

plt.figure(figsize=(10, 10))
plt.subplot(3, 1, 2)
plt.plot(frecuencias, np.abs(espectro))
plt.title("Espectro Original")

```
# 📶 Señal Filtrada

```python

# Crear un filtro para eliminar la componente de 50 Hz
filtro = np.ones(len(frecuencias))
filtro[np.abs(frecuencias) == 50] = 0

# Aplicar el filtro al espectro
espectro_filtrado = espectro * filtro

# Reconstruir la señal filtrada en el dominio del tiempo
senal_filtrada = np.real(fft.ifft(espectro_filtrado))

plt.subplot(3, 1, 1)
plt.plot(t, senal)
plt.title("Señal Original")
plt.subplot(3, 1, 2)
plt.plot(t, senal_filtrada)
plt.title("Señal Filtrada")

plt.tight_layout()
plt.show()

```

# ♨️ Espectro Filtrado

```python

# Realizar el análisis de Fourier
frecuencias_l = fft.fftfreq(len(t), 1/fs)
espectro_l = fft.fft(senal_filtrada)
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(frecuencias, np.abs(espectro))
plt.title("Espectro Original")
plt.subplot(3, 1, 2)
plt.plot(frecuencias_l, np.abs(espectro_l))
plt.title("Espectro filtrado")

```

```python
```
