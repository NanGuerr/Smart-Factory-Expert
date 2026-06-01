# 🔄 Conversión de Señales en PLCs

Para que un controlador pueda interactuar con el mundo exterior, es necesario realizar conversiones entre señales analógicas y digitales. 🔌

---

### 📥 Conversión Analógica a Digital (ADC)
Los procesadores solo entienden señales digitales, por lo que las señales analógicas deben convertirse mediante un **ADC**.

*   **Tipos de ADC:** Flash, Sigma-Delta, Simple/Doble Rampa y Aproximaciones Sucesivas. ⚡
*   **¿Qué es la Resolución?:** Es el nivel de detalle o precisión al convertir. Se define por el número de bits (`n`), permitiendo dividir el rango en `2^n` niveles. 📏
*   **Etapas del Proceso:**
    1.  **Adquisición:** Se releva la señal desde el borne.
    2.  **Muestreo:** Se toma una muestra en intervalos de tiempo. ⏱️
    3.  **Cuantización:** Se asigna un valor discreto basado en la resolución.
    4.  **Codificación:** Se convierte a binario. 🔢
    5.  **Almacenamiento:** Se guarda en un registro del PLC.

---

### 📤 Conversión Digital a Analógica (DAC)
Para comandar dispositivos analógicos (como motores o lámparas) desde un PLC, se requiere convertir señales digitales de comando.

*   **Métodos principales:**
    *   **Uso de DAC:** Utiliza redes de resistencias (ej. R2R) para alta resolución. 🏗️
    *   **PWM (Modulación por Ancho de Pulso):** Alternativa que usa salidas digitales. Se basa en un *Período* y un *Ciclo de Trabajo* (Duty Cycle) para simular un valor analógico promedio. 💡
*   **Etapas de conversión DAC:**
    1.  **Direccionamiento:** Se asigna el borne de salida.
    2.  **Codificación:** Valor numérico en binario.
    3.  **Cuantización:** Determinación del nivel de tensión/corriente.
    4.  **Decodificación:** Se energiza el conversor.
    5.  **Filtrado:** Se suaviza la salida eliminando el escalonamiento. 🌊
 
  # ⚡ Entradas y Salidas (E/S) Digitales en PLCs

En el mundo industrial, los PLCs se comunican con el entorno a través de módulos de entradas y salidas (E/S) digitales. El estándar de tensión industrial es de **24 VCC** por seguridad, compatibilidad y calidad de señal. 🔌

---

### 📥 Entradas Digitales
Aceptan señales de dispositivos como interruptores o sensores, detectando estados de "abierto" o "cerrado".

*   **Configuraciones:**
    *   **Sinking:** El módulo recibe la corriente (requiere un sensor PNP). 📉
    *   **Sourcing:** El módulo es la fuente de la corriente (requiere un sensor NPN). 📈
*   **Ejemplos de Sensores:** Pulsadores (NA/NC), sensores de proximidad inductivos (PNP/NPN), presostatos, termostatos y vacuostatos. 🔘

---

### 📤 Salidas Digitales
Controlan dispositivos físicos basándose en la lógica del programa del PLC.

*   **Tipos de Salidas:**
    *   **Relé:** Ideales para corrientes mayores, operan tanto en CA como en CC. Son de acción más lenta y sufren desgaste mecánico. ⚙️
    *   **Estado Sólido:**
        *   **BJT (NPN/PNP):** Respuesta rápida, sin desgaste mecánico, usados en CC.
        *   **Triac:** Diseñados para controlar cargas de CA. 💡
*   **Configuraciones:**
    *   **Sinking (NPN):** El módulo recibe la corriente del dispositivo.
    *   **Sourcing (PNP):** El módulo suministra la corriente hacia el dispositivo.

---

### 🔍 Resumen Técnico
| Característica | Sinking | Sourcing |
| :--- | :--- | :--- |
| **Flujo de Corriente** | Hacia el módulo | Desde el módulo |
| **Entrada (PNP)** | El sensor es la fuente | - |
| **Entrada (NPN)** | - | El módulo es la fuente |

---

# 🌊 El Mundo Analógico en PLCs

Para que un PLC interactúe con el entorno real, utiliza señales analógicas que representan valores continuos (variables) en lugar de solo estados encendido/apagado. 🔄

---

### 📡 Tipos de Señales Industriales
*   **Voltaje:** 0-10V, ±10V, ±5V. Son fáciles de medir, pero más vulnerables a interferencias y caídas de tensión en cables largos. 📉
*   **Corriente:** 0-20mA, 4-20mA, ±20mA. Altamente recomendadas por su inmunidad al ruido y capacidad para cubrir largas distancias. Un valor de 0mA indica un fallo (cable roto o sensor desconectado). 🛡️

---

### 🧩 ADC y DAC: La Magia de la Conversión
Como los procesadores son digitales, necesitan traductores:
*   **ADC (Analógico a Digital):** Convierte la señal del sensor al formato digital que el PLC entiende. La calidad de esta conversión depende de la **resolución** (número de bits). 🧠
*   **DAC (Digital a Analógico):** Convierte el valor digital del programa en una señal analógica para controlar actuadores físicos. 🛠️

---

### 🔌 Conexión de Sensores Analógicos
Dependiendo del tipo de señal, la conexión varía:
*   **Sensores de Corriente (2 hilos):** El PLC alimenta al sensor a través del mismo lazo de señal. ⚡
*   **Sensores de Corriente (4 hilos):** Requieren una fuente de alimentación externa independiente para el sensor, separando el lazo de alimentación del lazo de señal. 🔋
*   **Adaptación de señales:**
    *   **Adaptación (4 hilos a 2 hilos):** Se requiere conectar la fuente externa en serie con la entrada del PLC.
    *   **Adaptación (Corriente a Tensión):** Se usa una resistencia *shunt* (típicamente 250Ω) en paralelo para convertir la corriente en una tensión medible por el PLC mediante la Ley de Ohm ($V=I 	imes R$). 📐
