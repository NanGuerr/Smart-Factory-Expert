# 🤖 Curso Introductorio de PLC

Este documento resume los **Conceptos Generales** enfocado en la estructura interna y los componentes principales de un **Controlador Lógico Programable (PLC)**.

---

## 🧠 1. Procesador (CPU)
Es el encargado de **dirigir y coordinar** toda la operación del PLC. Ejecuta el programa desde la memoria y realiza los cálculos e instrucciones necesarias para el funcionamiento del sistema.

* **🚀 Velocidad:** Un procesador moderno puede ejecutar una instrucción por microsegundo ($1 \,\mu\text{s}$) o menos. A mayor avance, mayor velocidad y capacidad de trabajo en simultáneo.
* **🐕 Watchdog (Perro Guardián):** Es un mecanismo interno que monitorea el estado de "vida" del procesador. Si detecta una falla grave o que este deja de responder, se encarga de reiniciarlo o dar aviso al operador ejecutando maniobras de seguridad (como desactivar salidas o activar alarmas).

---

## 🔌 2. Periferia I/O (Entradas y Salidas)
Actúa como la **interfaz** entre el procesador y las señales eléctricas del mundo exterior. Permite expandir la cantidad de conexiones mediante módulos adicionales.

### 📋 Clasificación Principal:
* **📥 Entradas (Inputs):** Señales desde el exterior hacia el PLC.
  * Mnemónica Americana: **I**
  * Mnemónica Alemana: **E** *(Eingang)*
* **📤 Salidas (Outputs):** Señales desde el PLC hacia el exterior.
  * Mnemónica Americana: **O / Q**
  * Mnemónica Alemana: **A** *(Ausgabe)*

### 📊 Subclasificación según el Tipo de Señal:
1. **🔢 Digitales:** Valores binarios discretos (0 o 1). Ejemplo: Módulos DQ (Salidas Digitales).
2. **📈 Analógicas:** Valores de rango variable y continuo. Ejemplo: Módulos AI (Entradas Analógicas).

💡 **Periferia Distribuida:** Permite separar físicamente el controlador de los módulos de periferia a varias decenas de metros para facilitar el montaje y mantenimiento, comunicándose a través de un enlace específico.

---

## 💾 3. Áreas de Memoria
Se encargan de almacenar el programa, las variables y todos los cálculos intermedios. Se dividen en tres grupos principales:

1. **📦 Memoria de Carga:** * **Función:** Donde se aloja el programa del PLC y los estados iniciales.
   * **Características:** **No volátil** (no se borra al apagar) y de **Sólo Lectura** (sólo modificable por el equipo de programación).
2. **⚙️ Memoria de Trabajo:** * **Función:** Área donde realmente se ejecuta el programa. Al arrancar, el procesador copia el contenido de la memoria de carga aquí.
   * **Características:** **Volátil** y de **Lectura/Escritura**. Guarda estados temporales y cálculos intermedios.
3. **🔋 Memoria Remanente:** * **Función:** Una zona pequeña reservada para salvar datos críticos ante un corte de energía o reinicio (parámetros, recetas, estados de procesos críticos).
   * **Características:** **No volátil** y de **Lectura/Escritura**.

---

## 🌐 4. Puertos de Comunicación
Son las vías que permiten al PLC conectarse e interactuar de forma avanzada con otros elementos de la automatización.

* **🖥️ Dispositivos conectables:** Paneles HMI *(Human-Machine Interface)*, variadores de frecuencia, sensores inteligentes, u otros PLCs.
* **🔧 Versatilidad:** Se pueden añadir módulos externos para sumar nuevos puertos o tipos de redes.
* **🔀 Multi-protocolo:** Un mismo puerto físico puede gestionar múltiples protocolos de comunicación conviviendo en simultáneo (por ejemplo, hablar con otra CPU y gestionar periferia distribuida a la vez).
