# ⚡ Guía de Node-RED con Modbus (Por Steve's Node-RED Guide)

Integrar dispositivos industriales mediante el protocolo **Modbus** en Node-RED es un proceso directo gracias a bibliotecas especializadas. Esta guía te muestra cómo configurarlo paso a paso. 🛠️

---

## 📌 Puntos Clave para Comenzar

*   **📦 Instalación de la Biblioteca:** 
    *   Para trabajar con Modbus, el paquete más recomendado es **`node-red-contrib-modbus`**. 
    *   Puedes instalarlo fácilmente desde el administrador de paletas (*Manage Palette*) dentro del editor de Node-RED buscando su nombre. 🔍

*   **🔌 Configuración del Cliente (`Modbus Client`):**
    *   Antes de leer o escribir datos, necesitas definir los parámetros de conexión del dispositivo.
    *   **Para Modbus TCP:** Debes configurar la **Dirección IP** 🌐, el **Puerto** (por defecto el `502`) y el **ID de Unidad** (*Unit ID* / *Slave ID*).
    *   **Para Modbus Serial:** Debes configurar el puerto COM, la velocidad de baudios (*baud rate*), paridad y bits de parada. 🔌

*   **📖 Lectura de Datos (`Modbus Read`):**
    *   El nodo de lectura permite consultar registros de forma periódica (por ejemplo, cada pocos segundos).
    *   Configuras la función Modbus (como *Holding Registers* o *Input Registers*), la dirección de inicio (*Address*) y la cantidad de registros a leer. 📊

*   **✍️ Escritura de Datos (`Modbus Write` / `Modbus Flex Write`):**
    *   Permite enviar comandos o valores numéricos hacia el dispositivo esclavo (como cambiar un setpoint o activar una bobina). 🎯
    *   Los datos a enviar se estructuran típicamente dentro del objeto del mensaje (`msg.payload`).

---

## 🔗 Enlace Oficial

Puedes consultar la guía completa y detallada con ejemplos de flujos prácticos en el siguiente enlace:

* 🌐 [How to Use Node-Red with Modbus - Steve's Node-RED Guide](https://stevesnoderedguide.com/node-red-modbus) 📚
# 🧮 Manejo de Valores REAL y FLOAT en Modbus

Habrán visto que la representación de valores del tipo **REAL** o **FLOAT** en Modbus nos llevan a realizar una serie de pasos adicionales. 🔄

Esto ocurre porque el estándar Modbus maneja originalmente registros de 16 bits, mientras que un número flotante de precisión simple (IEEE 754) ocupa 32 bits, lo que requiere combinar dos registros consecutivos y lidiar con el orden de bytes (*Endianness* / *Byte Swapping*). ⚠️

---

## 📚 Enlaces de Interés y Recursos de Aprendizaje

Si quieren aprender un poco más sobre este tema y comprender cómo se estructuran estos datos a nivel de bits, les comparto los siguientes enlaces:

*   📖 **Wikipedia:** [Single-precision floating-point format](https://en.wikipedia.org/wiki/Single-precision_floating-point_format) 📐
*   🛠️ **Chipkin Articles:** [How Real (Floating Point) and 32-bit data is encoded in Modbus RTU messages](https://store.chipkin.com/articles/how-real-floating-point-and-32-bit-data-is-encoded-in-modbus-rtu-messages) 💻

## 🧮 Manejo de Valores REAL y FLOAT en Modbus

Habrán visto que la representación de valores del tipo **REAL** o **FLOAT** en Modbus nos llevan a realizar una serie de pasos adicionales. 🔄

Esto ocurre porque el estándar Modbus maneja originalmente registros de 16 bits, mientras que un número flotante de precisión simple (IEEE 754) ocupa 32 bits, lo que requiere combinar dos registros consecutivos y lidiar con el orden de bytes (*Endianness* / *Byte Swapping*). ⚠️

---

## 📚 Enlaces de Interés y Recursos de Aprendizaje

Si quieren aprender un poco más sobre este tema y comprender cómo se estructuran estos datos a nivel de bits, les comparto los siguientes enlaces:

*   📖 **Wikipedia:** [Single-precision floating-point format](https://en.wikipedia.org/wiki/Single-precision_floating-point_format) 📐
*   🛠️ **Chipkin Articles:** [How Real (Floating Point) and 32-bit data is encoded in Modbus RTU messages](https://store.chipkin.com/articles/how-real-floating-point-and-32-bit-data-is-encoded-in-modbus-rtu-messages) 💻
