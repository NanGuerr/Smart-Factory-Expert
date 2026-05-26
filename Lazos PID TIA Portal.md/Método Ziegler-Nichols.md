# 📋 Método de la Curva de Reacción de Ziegler-Nichols (Sintonización por Lazo Abierto)

### 1. Estado de Partida en Lazo Abierto 

* **Transcripción:** El bloque `PID_Compact` tiene activada la pata `ManualEnable` (`TRUE`). Se inyecta una consigna manual (`ManualValue`) fija de `20.0%` que se envía directamente a la variable `"Proceso".Actuador`. La gráfica de la derecha registra la respuesta del sistema: partiendo de 0 °C, la temperatura sube siguiendo una curva asintótica (tipo S) hasta estabilizarse cerca de los 70 °C ante ese estímulo escalón del 20%.
* **Análisis:** Para aplicar el método matemático de sintonización manual, el lazo debe abrirse. Al pasar el PID a modo manual y dar un salto brusco en la salida (escalón), se registra la **curva de reacción pura de la planta** sin la intervención del algoritmo PID.

### 2. Trazado de la Tangente y Variables $T_g$ y $T_u$ 

* **Transcripción:** El instructor utiliza una herramienta de dibujo para superponer el modelo clásico de Ziegler-Nichols sobre la gráfica real de TIA Portal. Traza una línea recta azul tangente al **punto de inflexión** de la curva verde.
* Se rotulan dos tiempos críticos en el eje horizontal:
* $T_u$ (Tiempo de retardo / retraso inicial).
* $T_g$ (Tiempo de recuperación / constante de tiempo).


* Se indica un cambio total en la temperatura de $70\text{ °C}$. Las fórmulas en pantalla muestran:
* $\text{Kp} = 0.9 \cdot (T_g / T_u) \cdot k_s$ *(con una corrección manual en la lámina)*.
* $\text{Ti} = 3.33 \cdot T_u$.

* **Análisis:** El punto de inflexión es el momento donde la curva cambia de acelerar a frenar. La recta tangente en ese punto corta el eje del tiempo y el valor final. La distancia desde el salto escalón hasta el corte con el eje es el retraso muerto ($T_u$), y el tiempo que tarda en alcanzar idealmente el valor final siguiendo esa pendiente es $T_g$.

### 3. Cálculo de las Constantes con Valores Reales 

* **Transcripción:** Se sustituyen las variables por los tiempos exactos medidos con las reglas de TIA Portal: $T_u = 0.33\text{ s}$ y $T_g = 6.43\text{ s}$. El valor final alcanzado es de 70 °C. Las cajas de texto muestran el cálculo numérico directo:
* $\text{Kp} = 0.9 \cdot (0.33 / 6.43) \cdot 70 \implies \mathbf{0.2505}$ *(Nota técnica: Representa la adaptación matemática para la ganancia del proceso)* $k_s$
* $\text{Ti} = 3.33 \cdot 0.33 \implies \mathbf{1.098\text{ s}}$.


* **Análisis:** El instructor convierte la respuesta gráfica de la planta en números puros. Estos valores de $K_p = 0.2505$ y $T_i = 1.098\text{ s}$ no son aleatorios; son el óptimo matemático calculado para que este sistema específico no oscile y sea rápido.

### 4. Carga de Parámetros en el `PID_Compact`

* **Transcripción:** El software regresa al modo de configuración de *Parámetros PID*. El instructor desmarca la casilla "Activar entrada manual" para devolver el PID a Modo Automático y escribe los valores calculados directamente en las celdas naranjas: **Ganancia proporcional:** `0.2505` y **Tiempo de integración:** `1.098 s`. El tiempo derivativo se mantiene en `0.0 s`.
* **Análisis:** Se completa la puesta en marcha. Los valores obtenidos mediante el análisis gráfico de Ziegler-Nichols se cargan en la memoria del controlador para pasar a la prueba en lazo cerrado.

---

# 🎛️ Sintonización Manual - Método Ziegler-Nichols (PID-0114)

Este módulo práctico enseña cómo utilizar el **método de la curva de reacción (Ziegler-Nichols)** para calcular matemáticamente los parámetros de ganancia proporcional ($K_p$) e integral ($T_i$) en TIA Portal, eliminando las conjeturas o el "tanteo a ciegas" al sintonizar un lazo de control. 🏭📐📊

---

### 📉 El Proceso de Sintonización por Curva de Reacción

Cuando se arranca una planta industrial por primera vez, no se conocen los valores ideales de $K_p$, $K_i$ o $K_d$. El método ejecutado en el video sigue estos pasos rigurosos:

1. **🔓 Apertura del Lazo (Modo Manual):** Se fuerza la salida del PID (`Output`) a un valor constante (ej. 20%) mediante `ManualEnable`. El sistema reacciona libremente sin correcciones.
2. **⏱️ Captura Dinámica:** Se espera a que la Variable de Proceso (**PV**) se estabilice por completo para registrar el impacto total del actuador en el proceso (en este caso, subir hasta los 70 °C).
3. **📐 Análisis Geométrico en el Gráfico:** Utilizando las herramientas de medición del visor de TIA Portal, se traza la línea tangente en el punto de máxima pendiente de la curva de respuesta.

A partir de los puntos de cruce de esta línea con los ejes temporales, se extraen los dos valores maestros del proceso:

* **$T_u$ (Tiempo Muerto):** Los segundos que tarda la planta en empezar a reaccionar físicamente desde que se le dio la orden.
* **$T_g$ (Tiempo de Recuperación):** El tiempo que le toma a la planta desarrollar su velocidad de cambio característica.

---

### 🧮 De la Geometría a los Parámetros del PLC

Con los tiempos medidos de forma exacta ($T_u = 0.33\text{ s}$ y $T_g = 6.43\text{ s}$), se aplican las ecuaciones de sintonización de Ziegler-Nichols para un controlador tipo **PI** (Proporcional-Integral):

* **Acción Proporcional ($K_p$):** Se calcula una ganancia moderada-baja inicial para tantear el proceso con seguridad, evitando que el controlador sobre-reaccione.
* **Acción Integral ($T_i$):** Se calcula un tiempo de integración rápido enfocado en destruir el error estacionario de forma inmediata.

Al cargar estos valores en la pestaña de parámetros avanzados, el operador pasa el controlador a **Modo Automático** y le introduce un Setpoint. El sistema se acopla perfectamente, corrigiendo el desvío sin caer en las peligrosas oscilaciones cíclicas que ocurren cuando ambos parámetros se incrementan de forma desmedida y sin un criterio matemático detrás.

---

💡 **Nota de estudio:** El método de la curva de reacción es sumamente popular porque permite sintonizar un PID realizando **una sola prueba en modo manual**, protegiendo la integridad de la máquina al evitar llevar el lazo cerrado al punto de oscilación destructiva. 
Utiliza la regla digital de TIA Portal para trazar la línea tangente en el *punto de inflexión* de la respuesta temporal de la planta y calcular los parámetros críticos del proceso.
---
