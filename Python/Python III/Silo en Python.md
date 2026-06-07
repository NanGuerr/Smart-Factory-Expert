# 🚰 Simulación Dinámica 

El script proporcionado es una excelente demostración de **Programación Orientada a Objetos (POO)** combinada con **visualización de datos en tiempo real** utilizando Matplotlib. 

El objetivo principal es simular el comportamiento de un silo de almacenamiento (como un tanque de granos, cemento o líquidos), modelando su llenado y vaciado a lo largo del tiempo, y mostrando una gráfica animada de su estado físico en vivo.

---

## 🏗️ Procedimientos Detallados

### 1. Modelado del Silo (Clase `Silo`) 🏭
Se define una clase para encapsular el estado y el comportamiento del contenedor:
* **Atributos de Inicialización:**
    * `capacidad`: El límite máximo que puede contener el tanque (configurado en 2000 kg).
    * `cargaActual`: La cantidad de material presente en el momento (inicia en 0).
    * `cantidad`: La tasa de flujo de entrada/salida por cada actualización de la simulación.
* **Métodos de Acción (Válvulas):**
    * `cargar()`: Simula la apertura de la válvula de entrada, estableciendo un flujo de `+20` kg por ciclo.
    * `vaciar()`: Simula la apertura de la válvula de salida, estableciendo un flujo de `-20` kg por ciclo.
    * `cerrarValvulas()`: Detiene todo el flujo estableciendo la tasa en `0`.
* **Actualización del Estado (`update()`):** En cada ciclo del programa, suma algebraicamente la `cantidad` a la `cargaActual`. Incluye mecanismos lógicos para evitar que la carga sea un número negativo (`if self.cargaActual < 0: self.cargaActual = 0`).

### 2. Animación Gráfica en Tiempo Real 📈
La función `graficar(listaValores)` introduce la técnica estándar para crear gráficos "vivos" en Matplotlib:
* `plt.clf()`: **Clear Figure**. Borra el gráfico del ciclo inmediatamente anterior. Sin esta línea, los gráficos se sobrepondrían unos sobre otros, saturando la memoria y distorsionando la imagen.
* `plt.plot(listaValores)`: Dibuja todo el historial de los valores registrados del silo frente al tiempo.
* `plt.pause(1/30)`: Pausa momentáneamente la ejecución de Python (equivalente a unos 30 FPS). Esta función es crítica porque obliga al backend de Matplotlib a renderizar la ventana gráfica; sin ella, la ventana se congelaría.

### 3. El Bucle Principal de Simulación 🔄
El script utiliza un bucle infinito (`while True`) protegido por un bloque `try...except KeyboardInterrupt` que permite abortar la simulación de forma limpia y segura presionando `Ctrl+C` en la consola.

**Lógica de Control Temporal:**
1.  **Arranque:** Se instancia el silo (`tk1 = Silo(2000)`) y se ordena su llenado (`tk1.cargar()`).
2.  **Ciclo iterativo:** El nivel sube y se registra cada 0.2 segundos gracias al comando `time.sleep(0.2)`.
3.  **Condición de Cambio (Threshold):** Se vigila constantemente el nivel del silo. Si la `cargaActual` alcanza o supera los **200 kg**, el sistema reacciona y llama inmediatamente a la función `tk1.vaciar()`. 
4.  **Descarga:** A partir de ese umbral, la gráfica empieza a descender 20 kg por ciclo hasta vaciarse. Al llegar a 0, las restricciones del método `update()` evitan números negativos, manteniendo el tanque vacío y mostrando una línea plana en el gráfico de ahí en adelante.

### 📝 Resumen de la Transcripción del Código

El código que compartiste es un script muy ingenioso 🧠 que une dos conceptos importantes: la lógica física y la visualización de datos dinámica.

* **La Lógica Orientada a Objetos 📦:** Creaste un modelo virtual de un contenedor (`class Silo`) que tiene una capacidad máxima y puede llenarse o vaciarse abriendo "válvulas" digitales (sumando o restando de 20 en 20).
* **Animación Gráfica 🎬:** El código no solo hace los cálculos en el fondo de la consola, sino que usa `matplotlib.pyplot` en modo interactivo. Al combinar `plt.clf()` para limpiar el lienzo en cada paso y `plt.pause()` para forzar el redibujado de la ventana, logras construir una gráfica de líneas que se mueve y actualiza en tiempo real frente al usuario.
* **Bucle de Control ⚙️:** El bloque `while True` llena el silo gradualmente hasta un límite lógico de **200 kg**, momento en el cual ordena su vaciado, creando el clásico "pico" en la gráfica que luego desciende hasta el nivel cero.

He detallado paso a paso el funcionamiento de este algoritmo, incluyendo cómo el bloque `try...except` previene cierres abruptos, en el archivo adjunto. ¡Espero que te sea de mucha utilidad para documentar el procedimiento! 🚀

```python
import time
import matplotlib.pyplot as plt
class Silo:

    def __init__(self,capacidad):
        self.capacidad = capacidad
        self.cargaActual = 0
        self.cantidad = 0


    def cargar(self):
        self.cantidad = 20

​    def vaciar(self):
        self.cantidad = -20
​
    def cerrarValvulas(self):
        self.cantidad = 0
    
    def update(self):
        if self.cargaActual < self.capacidad and self.cargaActual >= 0:
            self.cargaActual += self.cantidad

        if self.cargaActual < 0:
            self.cargaActual = 0
​
tk1 = Silo(2000)

def graficar(listaValores):
    plt.clf()
    plt.plot(listaValores)
    plt.pause(1/30)

​valores = []
tk1.cargar()

try:
    while True:
        tk1.update()
        print(f"Total cargado: {tk1.cargaActual} kilogramos")

        if tk1.cargaActual >= 200:
            tk1.vaciar()

        valores.append(tk1.cargaActual)
        graficar(valores)
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Simulacion Finalizada") 
```
