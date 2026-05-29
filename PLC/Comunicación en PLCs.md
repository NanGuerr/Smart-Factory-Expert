# 📡 Conceptos Avanzados de Comunicación

## 🔌 Introducción a la Comunicación en PLCs
Comunicar el PLC con otros dispositivos, incluyendo otros PLCs, es una práctica muy común y esencial en la industria.

* **Medios de transmisión:** La comunicación se puede realizar a través de cables de cobre (lo más común), por aire (sistemas inalámbricos) o mediante fibra óptica.
* **Propósito:** Permite transmitir desde grandes volúmenes de información hasta pequeñas señales críticas para mantener "vivo" un sistema de control.
* **Decisión de diseño:** Es fundamental para el programador saber cuándo utilizar protocolos para grandes paquetes de datos y cuándo es más prudente usar una señal física (cableada) para controlar o analizar el estado de un dispositivo.

---

## 🌐 Protocolos de Comunicación
Un protocolo de comunicación es un conjunto de reglas que permite a dos o más dispositivos comunicarse mediante la variación de una magnitud física (normalmente, la tensión).

* **Uso principal:** Se utilizan fundamentalmente para transmitir una gran cantidad de datos.
* **Transmisión por paquetes:** Los protocolos modernos agrupan y envían esta información estructurada en forma de paquetes.
* **Ventajas:** Dependiendo del protocolo elegido, se pueden lograr altísimas velocidades de transmisión y una excelente fiabilidad de los datos.
* **Flexibilidad:** Un mismo PLC puede "entender" varios protocolos a la vez, y estos pueden llegar a convivir a través del mismo medio físico.
* **Especificaciones:** Cada protocolo define el medio de transmisión, las velocidades típicas, los niveles de señal y la forma en que se decodifica cada paquete.
* **Ejemplos destacados:** Modbus (TCP y RTU), TCP/UDP, PROFINET, HART, MPI y CAN.

---

## 🪢 Cableado Físico (Hardwired)
El cableado físico entre dispositivos se emplea cuando se necesita enviar una sola magnitud de forma continua a través del medio.

* **Aplicaciones:** Principalmente para conectar sensores simples (digitales o analógicos) a un PLC, o para enviar señales directas a un equipo superior.
* **Interoperabilidad:** Al ser una conexión directa, permite enviar información entre equipos de distintos modelos o que no comparten los mismos protocolos de comunicación.
* **Fiabilidad independiente:** Como no depende del estado del bus de comunicaciones, se utiliza como una doble comprobación física para asegurar que un equipo está en marcha y respondiendo.

---

## 💓 Estrategia de "Keepalive" (Señal de Vida)
Una de las aplicaciones más útiles del cableado directo es la señal de *keepalive*.

* **Topología:** Se cablea un juego de entradas y salidas digitales entre dos PLCs.
* **Funcionamiento normal:** El PLC "Maestro" hace oscilar continuamente la señal entre `0` y `1`. El segundo PLC recibe esta señal y la replica en su propia salida digital.
* **Detección de fallas:** Si por alguna razón uno de los dos PLCs detecta que la señal recibida se mantiene fija (congelada) durante un tiempo determinado, se acciona una alarma indicando que la conexión física con el otro PLC se ha perdido.

# Protocolos de Comunicación Industrial

## 🌐 Introducción a los Protocolos
Los protocolos son el conjunto de reglas que permiten que los dispositivos se comuniquen entre sí mediante variaciones de magnitudes físicas (tensión).

* **Hardware necesario:** Cada protocolo requiere un puerto específico (Ethernet RJ-45, RS-485/422/232).
* **Escalabilidad:** Si el PLC no tiene el puerto necesario, se utilizan módulos de expansión, Routers o Gateways.
* **Implementación:** Se utilizan bloques de funciones específicos en el software de programación de cada fabricante.

---

## 🏗️ Protocolos Industriales Comunes

### 🔧 Modbus (TCP y RTU)
* **Modbus TCP:** Protocolo robusto y ampliamente utilizado que opera sobre redes Ethernet.
* **Modbus RTU:** Versión serie (RS-485/232), fundamental en la arquitectura de automatización clásica.

### ⚡ TCP vs UDP
La diferencia principal radica en la fiabilidad frente a la velocidad:

* **TCP (Transmission Control Protocol):**
    * ✅ **Muy fiable:** Comprueba constantemente la conexión, ordena los paquetes y reenvía los datos corruptos o perdidos.
    * ⚖️ **Menor velocidad:** Consume más ancho de banda y tiempo debido a sus comprobaciones constantes.
* **UDP (User Datagram Protocol):**
    * 🚀 **Alta velocidad:** Envía los paquetes "ciegamente" sin confirmar si llegan al receptor.
    * ⚠️ **Menor fiabilidad:** Si un paquete se pierde en el camino, no se recupera. Se usa principalmente en streaming.

---

## 💡 Conceptos de Programación
* **Estructura de datos:** El programador debe definir una estructura o grupo de variables (DBs o registros) que se enviarán a través del bus de comunicación.
* **Diagnóstico:** Es esencial monitorear el estado de la conexión para asegurar que los datos procesados por el PLC sean válidos.

Basado en el documento proporcionado, los "Códigos de función" (FC - *Function Codes*) son los comandos utilizados para especificar qué acción desea realizar el dispositivo cliente (como un PLC) sobre la tabla de registros del dispositivo servidor.

* FC01 - Leer estado de salidas 
* FC02 - Leer estado de entradas digitales 
* FC03 - Leer *Holding Register* (registro de retención) 
* FC05 - Escribir en una salida 
* FC06 - Escribir en un solo *Holding register* 
* FC15 - Escribir en múltiples salidas 
* FC16 - Escribir en varios *Holding register* 

---

### Nota técnica sobre el Modbus RTU

Para complementar, el documento presenta una tabla que ilustra cómo se estructura la **Unidad de datos de protocolo (PDU)** en el Modbus RTU, la cual incluye el código de función:

| Unidad de datos de protocolo | CRC |
| --- | --- |
| **Dirección esclavo** (1 byte) |  |
| **Código de función** (1 byte) |  |
| **Datos** (0... 252 bytes) |  |
|  | **CRC baja / CRC alta** (2 bytes) |
