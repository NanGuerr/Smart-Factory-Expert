# ⚡ Componentes Básicos

La electrónica es la rama de la ingeniería que estudia y diseña sistemas que utilizan la electricidad para procesar, transmitir y almacenar información. A diferencia de la electricidad de potencia, aquí nos enfocamos en **controlar señales eléctricas de baja potencia**.

---

## 🏗️ 1. Materiales Semiconductores
El corazón de la electrónica moderna. Son materiales (como el **Silicio** o el **Germanio**) que pueden actuar como conductores o aislantes según las condiciones.

* **Tipo P (Positivo):** Dopaje con impurezas que crean "huecos" con carga positiva. ➕
* **Tipo N (Negativo):** Dopaje con impurezas que proporcionan exceso de electrones libres con carga negativa. ➖

---

## 🟢 2. El Diodo: El "Semáforo" Eléctrico
Es un componente de dos terminales (Ánodo y Cátodo) que permite el paso de la corriente en un solo sentido.

* **Polarización Directa:** El diodo conduce.
* **Polarización Inversa:** El diodo bloquea el paso de la corriente.
* **Aplicaciones:** Rectificadores de corriente, protección contra picos de voltaje y compuertas lógicas. 🛡️

---

## 🤖 3. El Transistor: El Cerebro del Control
El transistor bipolar (NPN o PNP) es el componente clave para la electrónica digital y de control. Tiene tres terminales: **Base, Colector y Emisor**.

* **Como Interruptor:** Controla el paso de corriente entre Colector y Emisor mediante una pequeña corriente en la Base. 🔛
* **Como Amplificador:** Permite que una señal pequeña controle una señal mucho más grande. 🔊

---

## 🔒 4. El Optoacoplador
Dispositivo que combina un diodo LED y un fototransistor para lograr **aislamiento galvánico** entre dos circuitos. Es fundamental para proteger la circuitería delicada (como un PLC) de posibles interferencias o voltajes elevados. ⚡🚫

---

Aquí tienes el archivo en formato Markdown sobre el funcionamiento de los relés, basado en el contenido del documento adjunto:

---

## ⚙️ ¿Qué es un relé?

Un relé es un interruptor controlado eléctricamente. Funciona como un puente entre un circuito de control (de baja potencia) y un circuito de carga (de mayor potencia).

### Partes fundamentales del relé:

* **Bobina:** Es un electroimán que, al recibir corriente, genera un campo magnético.
* **Armadura (parte móvil):** Pieza metálica que es atraída por el campo magnético de la bobina.
* **Contactos:** Son los interruptores mecánicos que se abren o cierran cuando la armadura se mueve.
* **Normalmente Abierto (NO):** El circuito está abierto (apagado) cuando el relé no recibe energía.
* **Normalmente Cerrado (NC):** El circuito está cerrado (encendido) cuando el relé no recibe energía.

---

## 🛠️ ¿Cómo funciona?

1. **Estado de reposo:** Cuando la bobina no está energizada, el resorte mantiene los contactos en su posición inicial.
2. **Activación:** Al aplicar un voltaje a la bobina, esta crea un campo magnético que atrae la armadura.
3. **Acción de conmutación:** El movimiento de la armadura desplaza los contactos, cerrando el circuito "normalmente abierto" y/o abriendo el "normalmente cerrado".

---

## 💡 Aplicaciones típicas

* **Automatización industrial:** Control de motores y luces desde PLCs.
* **Seguridad:** Aislamiento eléctrico entre la parte de control y la parte de potencia.
* **Electrónica:** Permite que componentes electrónicos delicados controlen dispositivos de alto voltaje de forma segura.

---

