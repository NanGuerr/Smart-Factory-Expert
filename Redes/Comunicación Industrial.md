# 🏭 Resumen Protocolos de Comunicación Industrial 📡

## 🎛️ 1. Protocolo MODBUS: Fundamentos y Modos de Transmisión

**MODBUS** es uno de los protocolos pioneros más utilizados a nivel global en la automatización industrial debido a su simplicidad, diseño abierto y estructura jerárquica **Maestro/Esclavo (Master/Slave)**.

### 🔄 Modos de Transmisión Serial
Las imágenes detallan las dos variantes esenciales del protocolo en entornos seriales (RS-485/RS-232):

* **🔤 MODBUS ASCII:**
    * **Codificación:** Cada byte de un mensaje se transmite como **dos caracteres ASCII** de 7 bits (por ejemplo, el número hexadecimal `3A` se codifica usando los caracteres ASCII '3' y 'A').
    * **Ventaja:** Permite intervalos de tiempo de hasta un segundo entre caracteres sin generar un error de tiempo de espera (*timeout*).
* **🔢 MODBUS RTU (Remote Terminal Unit):**
    * **Codificación:** Cada byte de 8 bits del mensaje contiene **dos caracteres hexadecimales** de 4 bits. Los datos se transmiten de forma binaria pura.
    * **Ventaja:** Mayor eficiencia de rendimiento de datos (*throughput*) en comparación con el modo ASCII a la misma velocidad de transmisión (baudios).

### 📐 Formato del Frame / Trama de Datos (PDU y ADU)
El bloque genérico de datos Modbus se compone de la siguiente forma:
1.  **🆔 Dirección (Address):** Identificador del dispositivo esclavo (1 byte).
2.  **🛠️ Código de Función (Function Code):** Indica la acción a ejecutar (ej. leer bobinas, escribir registros). (1 byte).
3.  **📊 Datos (Data):** Carga útil con las variables o registros seleccionados. (Variable).
4.  **🔍 Comprobación de Errores:** Utiliza **LRC** (Longitudinal Redundancy Check) para el modo ASCII y **CRC** (Cyclic Redundancy Check) de 16 bits para el modo RTU.

---

## 🏎️ 2. Protocolo PROFIBUS: Variantes DP y PA

**PROFIBUS** (Process Field Bus) es un estándar de red de campo abierto de alta velocidad desarrollado por Siemens y estandarizado bajo IEC 61158. Las diapositivas analizan sus dos variantes principales según la aplicación en planta:

### ⚙️ PROFIBUS DP (Decentralized Periphery)
* **Propósito:** Optimizado para la comunicación rápida de alta velocidad entre controladores centrales (PLCs/PACs) y dispositivos de E/S descentralizados (módulos remotos, variadores de frecuencia, arrancadores).
* **Capa Física:** Basado típicamente en **RS-485** con topología en bus o árbol mediante cable apantallado de par trenzado (color púrpura característico).
* **Velocidad:** Capaz de alcanzar hasta **12 Mbps**.

### 🧪 PROFIBUS PA (Process Automation)
* **Propósito:** Diseñado específicamente para la automatización de procesos continuos y químicos, donde se requiere la conexión de instrumentación de campo (transmisores de presión, temperatura, flujo, actuadores de válvulas).
* **Capa Física:** Cumple con la norma **IEC 61158-2**, transmitiendo datos y energía simultáneamente sobre el mismo par de hilos.
* **Seguridad Intrínseca (Ex):** Permite su uso seguro en **áreas clasificadas con riesgo de explosión** (Zonas 0, 1 y 2) limitando la corriente y el voltaje para evitar chispa física.
* **Velocidad:** Fija a **31.25 kbps**.

---

## 🌐 3. Protocolo PROFINET: La Evolución hacia Ethernet Industrial

**PROFINET** representa la evolución tecnológica de PROFIBUS hacia redes con base **Industrial Ethernet (IEEE 802.3)**, integrando la flexibilidad de TI con la robustez requerida en manufactura automatizada.

### 📈 Características Clave
* **🌐 Integración Total:** Conecta dispositivos desde el nivel de campo (sensores/actuadores) hasta el nivel de supervisión y gestión corporativa (SCADA/MES/ERP).
* **⚡ Arquitectura LAN/WLAN:** Soporta medios físicos tradicionales (cables de cobre RJ45/M12), enlaces ópticos de fibra y transmisiones inalámbricas seguras (Wi-Fi/Bluetooth Industrial).
* **⏱️ Canales de Comunicación Diferenciados:**
    1.  **Canal Estándar (TCP/IP o UDP/IP):** Para tareas de configuración, diagnóstico y parametrización no críticas en tiempo real.
    2.  **Tiempo Real (RT - Real Time):** Omite las capas de red tradicionales para enviar datos directamente a la capa de enlace, garantizando tiempos de ciclo críticos de periféricos.
    3.  **Tiempo Real Isócrono (IRT - Isochronous Real Time):** Diseñado para aplicaciones de control de movimiento (*Motion Control*) de alta precisión con tiempos de sincronización menores a un microsegundo.

---

## 🩺 4. Protocolo HART: Comunicación Híbrida

El protocolo **HART** (Highway Addressable Remote Transducer) es un estándar industrial híbrido ampliamente implementado para la actualización digital de lazos de control analógicos tradicionales.

### 📶 Principio de Operación (Modulación FSK)
* **Señal Analógica:** Transmite la variable de proceso primaria (PV) de forma continua mediante el lazo convencional de corriente de **4 a 20 mA**.
* **Señal Digital:** Superpone una señal digital modulada por desplazamiento de frecuencia (**FSK - Frequency Shift Keying**), basada en el estándar telefónico Bell 202.
    * Un valor lógico **1** se representa por una frecuencia de **1200 Hz**.
    * Un valor lógico **0** se representa por una frecuencia de **2200 Hz**.
* **Ventaja Operativa:** Al ser una señal simétrica y de bajo voltaje, el promedio de corriente es cero, permitiendo la comunicación digital simultánea de datos secundarios (diagnósticos, calibración, tags) **sin interferir** con la medición analógica analógica de 4-20 mA en tiempo real.

---

## ⚖️ Cuadro Resumen Comparativo de Protocolos

| Parámetro | MODBUS RTU 🔢 | PROFIBUS DP/PA 🏎️ | PROFINET 🌐 | HART 🩺 |
| :--- | :--- | :--- | :--- | :--- |
| **Capa Física** | RS-485 / RS-232 | RS-485 / IEC 61158-2 | Industrial Ethernet | Lazo 4-20 mA + FSK |
| **Topología** | Bus lineal | Bus / Árbol | Estrella, Árbol, Anillo | Punto a punto / Multidrop |
| **Velocidad Máx.**| Hasta 115.2 kbps | 12 Mbps (DP) / 31.25 kbps (PA) | 100 Mbps / 1 Gbps | 1200 bps |
| **Estructura** | Maestro / Esclavo | Maestro / Esclavo | Controlador / Dispositivo | Maestro / Esclavo |
| **Uso Principal** | Integración genérica de PLCs | Periferia y procesos en planta | Fábricas digitales integradas | Instrumentación de procesos |

---
*Nota: Este análisis técnico consolida los conceptos de interconectividad, tramas digitales y capas físicas de los sistemas distribuidos ilustrados en las imágenes provistas.* 🚀🧱
