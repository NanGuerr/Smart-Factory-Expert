# ⚡ Operación y Control de Motores Asíncronos Trifásicos

Este documento detalla las etapas clave del ciclo de operación, los métodos de arranque y los sistemas de control para motores eléctricos asíncronos con rotor en cortocircuito.

---

## 🌀 1. Arranque, Aceleración y Carga

El arranque, aceleración y carga de un motor asíncrono con rotor en cortocircuito son las tres etapas clave del ciclo de operación de este motor.

* **🚀 Arranque:** Cuando el motor está detenido y se conecta a la red, el campo magnético del estator empieza a girar a la velocidad de sincronismo. Como el rotor está quieto, la diferencia de velocidad es máxima. Esto induce un voltaje muy alto en las barras del rotor, generando una corriente de arranque elevada.
* **📈 Aceleración:** Cuando la corriente genera un fuerte par motriz que hace que el rotor empiece a girar y a ganar velocidad rápidamente. A medida que la velocidad del rotor se acerca a la del campo magnético, la corriente empieza a disminuir hasta estabilizarse.
* **💼 Carga:** Al acoplar una carga mecánica el motor tiende a frenarse ligeramente. Al bajar un poco su velocidad, aumenta el deslizamiento, lo que hace que absorba la corriente justa de la red para mantener la fuerza necesaria y mover la carga de forma estable.

---

## 🔄 2. Inversión de Giro de un Motor Trifásico Asíncrono

El sentido de giro del rotor depende directamente del orden en que las fases de la corriente eléctrica (L1, L2, L3) llegan al estator, lo que determina la dirección del campo magnético giratorio. Para invertir el giro del motor, se intercambia la conexión de dos de las tres fases de alimentación entre sí. 

* **🕐 Giro Horario:** Es la conexión estándar donde se conecta L1 con U, L2 con V y L3 con W.
* **↩️ Giro Antihorario:** Se intercambian dos fases mediante el uso de dos contactores eléctricos enclavados entre sí para evitar que ocurra un cortocircuito.

---

## 📐 3. Conexión Estrella y Triángulo

Para realizar la conexión estrella y triángulo de un motor trifásico, ubicamos en la caja de bornes del motor los 6 terminales correspondientes a los principios y finales de las tres bobinas internas. Para configurarlo, se usan unas chapas metálicas llamadas puentes:

* **⭐ Conexión Estrella:** Se unen los tres terminales de salida en un solo punto, formando un nodo común, y se alimenta con las fases L1, L2 y L3 por los terminales de entrada.
* **🔺 Conexión Triángulo:** Se conecta el final de cada bobina con el principio de la siguiente de forma consecutiva. Las tres fases de la red se conectan a estos tres puntos de unión, donde cada bobina interna recibe la tensión total de la línea de la red.

---

## ⏱️ 4. Arranque Estrella / Triángulo: ¿Cómo y por qué?

### 🤔 ¿Por qué se realiza?
Un motor grande conectado directamente en triángulo consume una corriente de arranque brutal. Esto puede provocar caídas de tensión en la instalación de la fábrica o casa, dañar las protecciones eléctricas y desgastar mecánicamente el motor de forma prematura. El arranque estrella-triángulo es un método para reducir esa corriente de arranque a una tercera parte haciendo que el encendido sea mucho más suave.

### ⚙️ ¿Cómo se realiza?
Mediante contactores y un temporizador, el motor realiza el siguiente proceso de forma automática en tres etapas consecutivas:

1.  **⭐ Arranque:** El motor se conecta en estrella para recibir un voltaje reducido en sus bobinas, lo que disminuye la corriente inicial y permite que comience a girar sin sobrecargar la red eléctrica.
2.  **⏳ Transición:** El rotor gana velocidad hasta alcanzar el 70-80% de su capacidad nominal.
3.  **🔺 Régimen:** Un temporizador automático desconecta la configuración en estrella y pasa a triángulo, donde el motor recibe la tensión completa de la red en forma estable.

---

## 🔌 5. Arranque por Autotransformador

El arranque por autotransformador consiste en interponer un transformador con tomas variables de voltaje, como 50%, 65% u 80% (autotransformador) entre la red eléctrica y el motor durante los primeros segundos del encendido. 

Al pulsar el botón de encendido, el motor recibe un voltaje reducido a través del autotransformador (por ejemplo, el 65% de la tensión real). Esto disminuye la corriente de arranque proporcionalmente hasta que el motor ha acelerado lo suficiente y un contactor desconecta el autotransformador de la línea y conecta el motor directamente a la tensión completa de la red eléctrica para que trabaje a su máxima capacidad. 🛠️
