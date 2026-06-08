# 🔀 Slider 

```python
import matplotlib.pyplot as plt
import matplotlib.widgets as wg
import math

# Crear una figura y un eje
fig, ax = plt.subplots()
# Plot inicial
line, = ax.plot([], [])
# Hacemos espacio con este comando
fig.subplots_adjust(bottom=0.25)
# Hacemos el eje horizontal para el slider
axfreq = fig.add_axes([0.2, 0.1, 0.65, 0.03])
# Creamos el slider
miSlider = wg.Slider(
  ax=axfreq,
  label="Frecuencia",
  valmin=1,
  valmax=10,
  valinit=1,
  valstep=1,
  orientation="horizontal"
)

def update(val):
  # Actualizamos los datos de la senoidal con el valor del slider
  frecuencia = int(val)
  x = [i for i in range(0, 360)]
  y = [math.sin(math.radians(i * frecuencia)) for i in x]
  line.set_data(x, y)
  ax.relim()
  ax.autoscale_view()
  fig.canvas.draw_idle()

# Registramos la función de actualización con el slider
miSlider.on_changed(update)
plt.show()
```

# 🔳 Button

```python
Botón
import matplotlib.pyplot as plt
import matplotlib.widgets as wg
​
# Creamos la figura y el eje
fig, ax = plt.subplots()
​
# Función que se ejecuta al hacer clic en el botón
def on_button_click(event):
    print("¡Botón presionado!")
​
# Definimos las coordenadas y dimensiones del botón
ax_button = plt.axes([0.7, 0.25, 0.1, 0.075])
button = wg.Button(ax_button, 'Presionar')
button.on_clicked(on_button_click)
​
plt.show()
```

# ✔️ CheckButtons

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as wg
​
# Datos para el gráfico
x = np.linspace(0, 2 * np.pi, 1000)
y1 = np.sin(x)
y2 = np.cos(x)
​
# Creamos la figura y el eje
fig, ax = plt.subplots()
​
# Dibujamos las líneas iniciales
line1, = ax.plot(x, y1, lw=2, color='blue', label='sin(x)')
line2, = ax.plot(x, y2, lw=2, color='red', label='cos(x)')
​
# Definimos las coordenadas y dimensiones de los CheckButtons
rax = plt.axes([0.65, 0.3, 0.2, 0.2])
check_buttons = wg.CheckButtons(rax, ['sin(x)', 'cos(x)'], [True, True])
​
# Función que se ejecuta al cambiar el estado de los CheckButtons
def on_check_buttons_change(label):
    if label == 'sin(x)':
        line1.set_visible(not line1.get_visible())
    elif label == 'cos(x)':
        line2.set_visible(not line2.get_visible())
    plt.draw()
​
check_buttons.on_clicked(on_check_buttons_change)
​
plt.legend()
plt.show()
```

# 🔘 RadioButtons

```python

import matplotlib.pyplot as plt
import matplotlib.widgets as wg
import numpy as np
​
# Crear una figura y un eje
fig, ax = plt.subplots()
​
# Datos de ejemplo
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
​
# Plot inicial (sin(x) como valor predeterminado)
line, = ax.plot(x, y1)
​
# Hacemos espacio con este comando
fig.subplots_adjust(bottom=0.25)
​
# Hacemos el eje horizontal para los radiobuttons
rax = fig.add_axes([0.2, 0.03, 0.65, 0.1])
​
# Creamos los radiobuttons
radio = wg.RadioButtons(rax, labels=['Sen(x)', 'Cos(x)'], active=0)
​
def update(label):
    if label == 'Sen(x)':
        line.set_ydata(y1)
    elif label == 'Cos(x)':
        line.set_ydata(y2)
    plt.draw()
​
# Registramos la función de actualización con los radiobuttons
radio.on_clicked(update)
​
plt.show()
```

# 🅰️ Textbox

```python
import matplotlib.pyplot as plt
import matplotlib.widgets as wg
​
# Crear una figura y un eje
fig, ax = plt.subplots()
​
# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 2]
​
# Plot inicial
line, = ax.plot(x, y)
​
# Hacemos espacio con este comando
fig.subplots_adjust(bottom=0.25)
​
# Hacemos el eje horizontal para el TextBox
axtext = fig.add_axes([0.2, 0.1, 0.65, 0.07])
​
# Creamos el TextBox
text_box = wg.TextBox(
    ax=axtext,
    label="Valor de Y",
    initial="0",
    color='lightgoldenrodyellow'
)
​
def update(text):
    try:
        val = float(text)
        line.set_ydata([val] * len(x))
        print(val)
        fig.canvas.draw_idle()
    except ValueError:
        pass
​
# Registramos la función de actualización con el TextBox
text_box.on_submit(update)
​
plt.show()
```

# 🖱️ Cursor

```python
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
​
# Datos para el gráfico
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 2]
​
# Creamos la figura y el eje
fig, ax = plt.subplots()
​
# Dibujamos la línea
line, = ax.plot(x, y, lw=2, color='blue')
​
# Agregamos el cursor
cursor = Cursor(ax, useblit=True, color='red', linewidth=1)
​
plt.show()
```
