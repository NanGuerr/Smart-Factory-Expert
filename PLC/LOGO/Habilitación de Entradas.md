# 🎛️ Guía Simulación y Habilitación de Entradas en LOGO!

En LOGO! Soft Comfort, probar tu lógica de programación antes de transferirla al PLC es vital. Para que esta simulación sea realista y refleje fielmente lo que ocurrirá en el tablero físico, el software te permite configurar el comportamiento físico virtual de cada entrada (ya sea digital o analógica).

A continuación, te explico los tipos de habilitaciones y cómo configurar específicamente un pulsador normalmente cerrado. 

---

### 🔘 Tipos de Simulación para Entradas Digitales

Al hacer doble clic sobre un bloque de entrada digital (`I`) y dirigirte a la pestaña de **Simulación**, encontrarás cuatro opciones. Cada una imita un dispositivo de campo distinto:

* **Interruptor (Switch):** 🔛
    * **Funcionamiento:** Al hacer clic en la barra de simulación, cambia de estado (de 0 a 1, o de 1 a 0) y se queda "enclavado" en ese estado hasta que lo vuelvas a presionar.
    * **Uso:** Se utiliza para simular selectores de posición (ej. Manual/Automático), interruptores de encendido fijo o sensores de presencia estáticos (como un final de carrera accionado por una caja que se queda detenida sobre él).
* **Pulsador (Contacto Normalmente Abierto - NA/NO):** 🟢
    * **Funcionamiento:** En reposo envía un `0` lógico. Solo envía un `1` lógico *mientras* mantienes presionado el clic del ratón. Al soltarlo, vuelve a `0`.
    * **Uso:** Es el clásico botón verde de "Marcha" (Start), botones de reseteo de alarmas o sensores que detectan un paso rápido (como una botella pasando por una cinta transportadora).
* **Pulsador (Contacto Normalmente Cerrado - NC):** 🔴
    * **Funcionamiento:** En reposo, el software simula que el contacto está cerrado, enviando un `1` lógico permanentemente al PLC. Al hacer clic, interrumpe físicamente la señal, enviando un `0`.
    * **Uso:** Imprescindible para botones de "Parada" (Stop), paradas de emergencia o sensores de seguridad industrial. 
* **Frecuencia (Frequency):** ⚡
    * **Funcionamiento:** Genera un tren de pulsos (encendido y apagado constante) a una velocidad que tú defines (en Hz).
    * **Uso:** Ideal para simular caudalímetros de pulsos o encoders rotativos para medir velocidades en motores.

---

### 🛠️ Configuración Práctica: Pulsador Normalmente Cerrado (NC)

Configurar un botón de parada correctamente es el error de novato más común al empezar a programar. En la industria, por normativa de seguridad humana, **los botones de parada y emergencia siempre se cablean físicamente cerrados**. Esto asegura que si se rompe un cable, el PLC detecta la pérdida de señal y apaga la máquina por seguridad (lógica de falla segura).

Para que tu simulación en la computadora respete esto, debes configurarlo así:

1.  Haz **doble clic** sobre el bloque de tu entrada (por ejemplo, `I2` asignada a Parada).
2.  En la ventana de propiedades, haz clic en la pestaña **Simulación**.
3.  En la lista, selecciona la opción **Pulsador (contacto normalmente cerrado)**.
4.  Haz clic en **Aceptar**. 

**¿Qué pasará al simular (F3)?** Verás que esa entrada en particular ya estará enviando señal (la línea se pondrá de color rojo) sin que tú hagas absolutamente nada. Para "detener" tu motor en la simulación, tendrás que hacer clic en el botón de esa entrada en la parte inferior de la pantalla; verás cómo la señal se corta instantáneamente mientras mantienes el clic, "botando" el enclavamiento de tu lógica.

---

### 🎚️ Habilitación y Simulación Analógica (AI)

Además de las entradas digitales, LOGO! Soft Comfort permite habilitar valores simulados para las **Entradas Analógicas (`AI`)**.

* **Funcionamiento:** Al ir a las propiedades de una entrada analógica, la pestaña de simulación cambia. Aquí no eliges interruptores, sino que **defines un valor numérico**. Durante la simulación, en la barra inferior aparecerá un potenciómetro deslizable (slider).
* **Uso:** Imita el comportamiento de variables físicas reales captadas por sensores de 0-10V o 4-20mA (como PT100 para temperatura, o ultrasónicos para nivel de agua). Moviendo el slider de izquierda a derecha, puedes probar si tus comparadores analógicos o tus bloques de control PI reaccionan correctamente cuando la temperatura del horno "sube" o el nivel del tanque "baja".
