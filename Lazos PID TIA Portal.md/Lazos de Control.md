# 🎛️ Conceptos Generales de Lazos de Control (PID-0101 - 0103)

Este módulo introduce los fundamentos de la teoría de control automático, explicando cómo un sistema puede regularse a sí mismo para mantener una variable en un valor deseado frente a perturbaciones externas. 🧠🔄🏭

---

### 📌 Componentes Esenciales de un Lazo de Control

Para entender un control PID, primero se deben dominar los cuatro términos clave que definen cualquier lazo de regulación:

* **🎯 SP — Setpoint (Valor de Consigna):** Es el valor objetivo o deseado que queremos mantener en el proceso (por ejemplo, mantener la temperatura de un horno a 180°C o el nivel de un tanque al 70%).
  
* **📊 PV — Process Variable (Variable de Proceso):** Es el valor real actual del sistema medido en tiempo real por un sensor (por ejemplo, la temperatura actual del horno leyendo 175°C).
  
* **❌ Error (Desviación):** Es la diferencia matemática exacta entre lo que deseas y lo que tienes. Se calcula como:
  $$Error = SP - PV$$
  
* **🔄 Retroalimentación (Feedback):** Es el canal de comunicación que toma la lectura de la **PV** desde el sensor y la envía de regreso al controlador para comparar si se está cumpliendo el objetivo del **SP**. Es la base del lazo cerrado.

---

### 🔄 Lazo Abierto vs. Lazo Cerrado

El módulo analiza la diferencia crítica en la arquitectura de los sistemas de automatización:

* **👐 Lazo Abierto (Open Loop):** El sistema ejecuta una acción programada sin importar el resultado real. No hay sensor que retroalimente al controlador.
    * *Ejemplo:* Una lavadora que lava durante 30 minutos; no sabe si la ropa quedó limpia o sigue sucia, solo cumple el tiempo.
* **🔒 Lazo Cerrado (Closed Loop):** El sistema mide constantemente la salida mediante un sensor y reajusta la variable manipulada en función del error. **Los controles PID siempre trabajan en lazo cerrado.**
    * *Ejemplo:* Un sistema de aire acondicionado que mide la temperatura de la habitación y apaga o arranca el compresor para mantener los grados programados.

---

### 📐 Introducción a las Acciones PID

Breve vistazo conceptual a lo que hace cada componente del algoritmo:

1. **🔴 P — Proporcional:** Reacciona al error **actual**. A mayor error, mayor es la fuerza de la acción correctiva.
   
2. **🔵 I — Integral:** Reacciona al error **pasado** (acumulado en el tiempo). Se encarga de eliminar el pequeño error residual (offset) que la acción proporcional no logra corregir.
   
3. **🟢 D — Derivativa:** Reacciona al error **futuro** (predicción). Analiza la velocidad con la que cambia el error para frenar o acelerar la respuesta, evitando que el sistema se pase del objetivo (*overshoot*).

---

### 📝 Nota

💡 Este módulo es el pilar de la automatización industrial. Antes de abrir **TIA Portal** y arrastrar bloques tecnológicos de Siemens (como el *PID_Compact*), es obligatorio entender estos conceptos para saber qué variables enlazar y qué comportamiento esperar del proceso físico. 🚀

### 🔄 Tipos de Lazos de Control

* **🔓 Lazo Abierto (Open Loop):** 
    * El sistema ejecuta una acción de control basándose únicamente en una calibración previa o en el tiempo, sin importar el resultado real en la salida. No mide lo que está pasando.
    * *Ejemplo:* Una lavadora que lava durante 30 minutos sin importar si la ropa quedó limpia o sigue sucia.

* **🔒 Lazo Cerrado (Closed Loop):** 
    * El sistema mide constantemente la salida del proceso y utiliza esa información para corregir la acción de control en tiempo real. Busca reducir la diferencia entre lo que se quiere y lo que se tiene.
    * *Ejemplo:* Un sistema de aire acondicionado que mide la temperatura de la habitación y se enciende o apaga para mantenerla exacta.

---

### 📉 Comportamiento Dinámico y Errores

* **❌ Error ($e = SP - PV$):** Es la diferencia matemática entre lo que deseamos (**SP**) y lo que tenemos realmente (**PV**). El objetivo de cualquier controlador (y del algoritmo PID) es hacer que este error sea igual a cero ($e = 0$).
  
* **📈 Overshoot / Sobreimpulso:** Es el valor máximo que alcanza la variable de proceso (**PV**) al sobrepasar la consigna (**SP**) la primera vez que intenta alcanzarla. Se mide generalmente en porcentaje y un overshoot muy alto puede ser peligroso en la industria (ej. sobrecalentar un horno).
  
* **🔄 Oscilación:** Es el comportamiento donde la variable de proceso (**PV**) sube y baja constantemente alrededor del **SP** sin llegar a estabilizarse. Una oscilación descontrolada indica que el sistema está inestable.

---

### 📝 Nota (La esencia del PID)

💡 El algoritmo PID (Proporcional, Integral y Derivativo) que verás en TIA Portal vive para leer constantemente el **Error ($e$)**. Analizando el error en el presente (P), su acumulación en el pasado (I) y su velocidad de cambio hacia el futuro (D), calculará la salida perfecta hacia los actuadores para eliminar la oscilación y el overshoot, llevando el proceso a la estabilidad absoluta. 🚀
