Nnúcleo práctico del laboratorio. En Siemens TIA Portal, ver cómo interactúan la $K_p$ y la $K_i$ es el momento donde "hace clic" la teoría. El comportamiento que describes —donde un valor numérico más chico de la constante produce una acción integral más grande y rápida— es el concepto clave que confunde a muchos programadores, pero tú ya lo tienes clarísimo.

---

# 💻 Constante Integral – Demostración Práctica (PID-0110)

Este módulo práctico en TIA Portal valida experimentalmente cómo la **Acción Integral** interactúa con la Proporcional para eliminar el error estacionario, y demuestra de forma empírica la relación matemática inversa de su constante en el objeto tecnológico `PID_Compact`. 📈🕹️⚙️

---

### 🧪 Desarrollo del Experimento en el Video

La práctica sigue una secuencia lógica de sintonización manual para mostrar el efecto acumulativo del área del error:

#### 📉 Paso 1: Establecer el Error Estacionario (Lazo P Puro)

* **Acción:** El instructor comienza configurando únicamente la constante proporcional ($K_p$) a un nivel moderado, dejando la acción integral desactivada.
* **Resultado:** En la ventana de monitorización se observa el comportamiento estudiado en módulos anteriores: la Variable de Proceso (**PV**) se estabiliza en una línea recta horizontal, pero queda congelada por debajo del Set Point (SP). Existe un **error estacionario permanente** (Offset) y el actuador no se mueve más porque el error dejó de cambiar.

#### 🚀 Paso 2: Activación de la Acción Integral (Lazo PI)

* **Acción:** Se introduce un valor en la constante integral ($K_i$).
* **Resultado (El efecto "Lodge" o acople del sistema):** Al activarse la integral, el sistema experimenta un cambio de comportamiento dinámico inmediato. El bloque empieza a calcular el área bajo la curva del error residual. Aunque el error es pequeño, la suma continua en el tiempo acumula el valor suficiente para darle un "empujón" extra al actuador. La curva de la **PV** rompe su estancamiento y empieza a subir de forma progresiva hasta **alcanzar exactamente la línea de la consigna o Set Point**, extinguiendo el error por completo ($e = 0$).

#### 🔄 Paso 3: La Regla Inversa (Más chico = Más rápido)

* **Demostración:** En el software se comprueba visualmente que **entre más chico es el valor numérico ingresado en la constante $K_i$, más grande y agresiva es la acción integral**.
* **Efecto:** Al reducir el número de la constante, la velocidad con la que el sistema corrige el error aumenta drásticamente (la pendiente de aproximación final hacia el SP se vuelve más vertical).

#### ⚠️ Paso 4: Exageración de Parámetros e Inestabilidad

* **Acción:** Se exageran los valores conjuntos de $K_p$ y $K_i$ (poniendo una ganancia muy alta y una constante integral muy pequeña).
* **Resultado:** La salida del PID empieza a **oscilar de forma salvaje** alrededor del Set Point, demostrando que el exceso de energía integral acumulada sumado a una proporcional agresiva desestabilizan cualquier planta.
* **Corrección:** El instructor demuestra cómo mitigar esto modificando/suavizando la acción integral (aumentando el valor numérico de la constante $K_i$) hasta que la oscilación se amortigua y el valor del proceso se asienta pacíficamente sobre la consigna requerida.

---

### 📌 Conclusiones Críticas de la Práctica

💡 **El poder del Lazo PI:** En la gran mayoría de los procesos industriales reales (como control de nivel de tanques, presión en tuberías o flujo de fluidos), **las acciones $K_p$ y $K_i$ trabajando juntas son más que suficientes** para lograr un control perfecto y exacto, sin necesidad de activar la acción derivativa ($K_d$).

```text
Configuración Visual del PID_Compact:
   - K_p Moderada + K_i Inactiva  -->  Línea horizontal con Error (Offset).
   - K_p Moderada + K_i Correcta  -->  La curva se acopla y llega exactamente al SP.
   - K_p Exagerada + K_i Muy Baja -->  Onda senoidal (Oscilación inestable).

```

---

**Reset Windup** : A ese fenómeno se le conoce también en el mundo del control automático como la saturación integral.

Explicado de forma sencilla con tu analogía: cuando el sistema se queda "atascado" abajo y no puede subir, la acción integral se pone a **"enroscar"** y acumular fuerza de manera desesperada. Para que el sistema pueda volver a bajar o estabilizarse, primero tiene que **"desenroscar"** toda esa fuerza acumulada, lo que causa un retraso y un descontrol en el proceso.

Aquí tienes el resumen técnico de este fenómeno para que lo agregues a tus notas de TIA Portal:

---

# 🚨 El Fenómeno del Reset Windup (Saturación Integral)

El **Windup** (que se traduce literalmente como "enrollar" o "cargar un resorte") ocurre exclusivamente debido a la **Acción Integral** cuando el proceso se topa con un límite físico real.

---

### 🪵 ¿Por qué ocurre? (El efecto "Enroscar")

Imagina que tienes un sistema de control de temperatura (un horno) y abres la puerta por completo. La temperatura se va a desplomar.

1. El controlador PID detectará un **error gigantesco** entre el Setpoint y la temperatura real.
2. Como la acción integral calcula el **área bajo la curva del error**, empezará a sumar y sumar ese error de forma continua en el tiempo.
3. El PLC le ordenará a la resistencia del horno que trabaje al **100% de su capacidad (Saturación)**.
4. **Aquí viene el problema:** Aunque la resistencia física ya dio todo lo que tenía (llegó a su límite del 100%), la temperatura no sube rápido porque la puerta está abierta. La acción integral no sabe de límites físicos; ella solo ve que sigue habiendo error, por lo que sigue calculando e integrando internamente, "enroscando" el valor matemático de la integral hasta números astronómicos (por ejemplo, un equivalente teórico a un 500% o 1000% de salida).

---

### 🔄 La Recuperación (El efecto "Desenroscar")

Cuando por fin cierras la puerta del horno, la temperatura empieza a subir rápidamente y alcanza el Setpoint. En ese instante, esperarías que el PID apagara la resistencia para no pasarse, pero **no lo hace**.

* Como la integral se quedó "enroscada" en un valor gigantesco, el error instantáneo ahora es cero ($e=0$), pero el historial acumulado en el pasado sigue siendo enorme.
* Para que el controlador pueda empezar a cerrar la salida de energía, primero necesita que la temperatura **supere por mucho el Setpoint**. Al pasarse de la consigna, el error se vuelve *negativo*, y ese error negativo es el que empieza a **"desenroscar"** o restar el valor acumulado en la integral.
* **El resultado industrial:** Un *overshoot* (sobreimpulso) gigantesco y peligroso, donde el proceso se descontrola simplemente porque el PID tardó demasiado tiempo en vaciar su memoria interna.

---

### 🛡️ ¿Cómo lo soluciona TIA Portal? (Anti-Windup)

El objeto tecnológico `PID_Compact` de Siemens viene con un sistema de protección nativo llamado **Anti-Windup**.

Cuando configuras los límites de salida en la pestaña de parámetros del bloque (por ejemplo, límite máximo de 100% y mínimo de 0%), el algoritmo interno de TIA Portal le dice a la integral: *"Si la salida física ya llegó al 100%, deja de sumar error de inmediato; quédate congelada ahí hasta que el error cambie de signo"*.

De esta manera, el resorte nunca se "enrosca" de más y el sistema puede reaccionar de forma instantánea en cuanto el proceso lo requiera.
