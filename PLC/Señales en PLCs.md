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
