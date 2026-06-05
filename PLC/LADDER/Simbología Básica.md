# 🏗️ Simbología Básica de Ladder en PLC

La programación de PLC mediante el lenguaje **Ladder** (escalera) se basa en la lógica de contactos y bobinas. El principio fundamental es: "SI... ENTONCES...". La corriente fluye a través de una red de contactos hasta alcanzar las bobinas, que usualmente se ubican en el lado derecho.

---

## 🟢 Contacto Normalmente Abierto (NO)
Los contactos Normalmente Abiertos funcionan como interruptores que esperan una activación.
*   **Estado 0 (FALSE):** El contacto "bloquea" el paso de la corriente.
*   **Estado 1 (TRUE):** El contacto "conmuta", permitiendo el paso de la corriente.

## 🔴 Contacto Normalmente Cerrado (NC)
Los contactos Normalmente Cerrados permiten el paso de la energía de forma predeterminada.
*   **Estado 0 (FALSE):** El contacto "permite" el paso de la corriente.
*   **Estado 1 (TRUE):** El contacto "conmuta" y corta el paso de la corriente.

## 🔌 Bobinas (Coils)
Las bobinas representan las salidas del sistema y se energizan según la lógica de los contactos previos.
*   **Bobina Estándar `()`:** Se energizan cuando reciben una señal por su lado izquierdo. Si la variable es una salida digital, el PLC energiza el borne físico correspondiente.
*   **Bobina Negada:** Funciona de forma inversa; se mantienen energizadas siempre y cuando **no** reciban una señal en su lado izquierdo.

---

## ⏱️ Ejemplo Aplicado: Temporizadores (TON)
Es posible añadir componentes como temporizadores para lograr efectos avanzados, como un retraso en la activación.

*   **Configuración:** Se utiliza un bloque de tiempo (`TON`) donde se define un valor (`PT`) para el *delay*.
*   **Funcionamiento:** Al accionar el interruptor (`IN`), el temporizador inicia el conteo. Una vez cumplido el tiempo, la salida (`Q`) se energiza y enciende la lámpara.
