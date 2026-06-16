# 📉 Modelos de Planta y Simulación

Este módulo aborda cómo representar matemáticamente el comportamiento de un proceso físico real (la planta) dentro de un entorno de automatización, y cómo simularlo de forma práctica en TIA Portal utilizando bloques de organización cíclicos. 🏭💻🤖

---

### 🏛️ Modelos de Planta y Órdenes del Sistema de Control

Para que un controlador PID pueda sintonizarse, es necesario entender cómo reacciona la planta (un motor, un horno, una válvula) ante un estímulo. Los sistemas se clasifican según su orden matemático:

* **🥇 1er Orden (Sistemas PT1):** 
    * Representan procesos que tienen una sola capacidad de almacenamiento de energía o masa. No oscilan ante un cambio brusco; su respuesta es una curva exponencial suave que se estabiliza con el tiempo.
    * *Ejemplos industriales:* El llenado de un tanque de agua simple o la temperatura de un bloque metálico pequeño.
    * *Plantilla Siemens:* **`LSim_PT1`**

* **🥈 2do Orden Oscilatorio (Sistemas PT2osc):**
    * Involucran dos elementos que almacenan energía y que interactúan entre sí. Dependiendo de su coeficiente de amortiguamiento, la variable de proceso presentará un comportamiento oscilatorio (subes y bajas con *overshoot*) antes de estabilizarse en el Set Point.
    * *Ejemplos industriales:* Sistemas mecánicos con resortes/amortiguadores, o control de posición con alta inercia.
    * *Plantilla Siemens:* **`LSim_PT2osc`**

* **🥉 3er Orden / Orden Superior (Sistemas PT3):**
    * Representan sistemas complejos formados por múltiples etapas o retrasos consecutivos. Tienen una respuesta más lenta al inicio (un retardo de tiempo o "tiempo muerto" aparente) debido al arrastre de los órdenes inferiores combinados.
    * *Ejemplos industriales:* Intercambiadores de calor multietapa o reactores químicos complejos.
    * *Plantilla Siemens:* **`LSim_PT3`**

---

### 🛠️ Configuración de la Simulación en TIA Portal

El módulo explica la metodología para probar el lazo cerrado de control simulando la CPU (S7-1200 o S7-1500) a través de PLC-SIM:

1. **⏱️ Bloque de Interrupción Cíclica (Cyclic Interrupt - OB30 / OB35):** 
    * **Paso crítico:** Los bloques de simulación de planta y el propio algoritmo PID **nunca** deben programarse en el bloque principal (`Main OB1`). Se deben colocar obligatoriamente dentro de un bloque de interrupción cíclica.
    * **Razón:** Estos algoritmos requieren ejecutarse a un intervalo de tiempo estrictamente constante (por ejemplo, cada 100ms) para que los cálculos matemáticos de integrales y derivadas sean exactos.

---

### 🔌 Anatomía de las Plantillas Maestras (`LSim_PTx`)

Los bloques `LSim_PT1`, `LSim_PT2osc` y `LSim_PT3` comparten una arquitectura de pines comunes para configurar la simulación. Su descripción técnica es la siguiente:

#### 📥 Entradas (Inputs)
* **`input`:** La señal de control o actuación que viene directamente desde la salida del PID (normalmente la variable manipulada o del actuador).
* **`gain`:** La ganancia estática de la planta. Define cuánto escalará la salida de la planta en relación con la entrada (ej. si inyecto un 10% de entrada y la ganancia es 2, el proceso subirá un 20%).
* **`cycle`:** El tiempo de muestreo real en segundos (debe coincidir con el tiempo asignado a la interrupción cíclica del OB, por ejemplo, `0.1` para 100ms).
* **`reset`:** Entrada booleana para restablecer el modelo de la planta a sus valores iniciales de forma inmediata.

#### 📤 Salidas (Outputs)
* **`output`:** La variable de proceso simulada (**PV**). Esta es la pata que se conecta de vuelta a la entrada de realimentación del bloque PID.

#### ⚙️ Parámetros de Configuración Interna
* **`maxout` / `minout`:** Límites de saturación del modelo. Evitan que la salida simulada de la planta exceda límites físicos reales (por ejemplo, limitar a un máximo de 100°C o un mínimo de 0V).
* **`calcparam`:** Parámetro o comando interno que le indica al bloque que recalcule sus coeficientes internos basándose en las constantes de tiempo (como tau $\tau$ o el coeficiente de amortiguamiento D) configuradas en la estructura de datos del bloque.
