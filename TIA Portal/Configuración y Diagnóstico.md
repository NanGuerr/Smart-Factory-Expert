# ⚙️ Configuración Avanzada y Diagnóstico 

Esta guía detalla los parámetros críticos de configuración en el entorno TIA Portal para la parametrización de hardware y seguridad industrial.

---

## 📊 1. Configuración de Entradas Analógicas (AI)
La parametrización correcta de las entradas analógicas es vital para asegurar la integridad de las señales de proceso.

* **Canales:** Define la cantidad de puntos de medición activos. Se pueden configurar de forma individual o agrupada, dependiendo del módulo.
* **Tipo de Medición:** Selección del tipo de señal física:
    * 🔌 **Tensión:** (ej. ±10V, 0-10V).
    * ⚡ **Corriente:** (ej. 4-20mA, ±20mA).
    * 🌡️ **Resistencia/Termopares:** (PT100, TC).
* **Rango de Tensión/Corriente:** Se selecciona en el catálogo de hardware según el sensor conectado.
* **Filtrado (Smoothing):** Configuración de suavizado de valores medidos mediante el filtrado por cantidad de ciclos (ej. ninguno, débil, medio, fuerte). Esto ayuda a estabilizar lecturas ruidosas promediando las muestras a través del tiempo.

---

## 🩺 2. Diagnóstico de Señales
Permite detectar fallos en tiempo real mediante la activación de alertas en el bloque de diagnóstico:

* **Rebase por exceso (Overflow):** Se activa cuando la señal supera el límite superior de medición (ej. > 27648 en formato normalizado).
* **Rebase por defecto (Underflow):** Se activa cuando la señal cae por debajo del límite inferior (ej. < 0 en 0-10V o < 4mA en 4-20mA).
* **Rotura de hilo (Wire Break):** Detecta si el circuito está abierto (típico en sensores de 4-20mA). Si la corriente es 0mA, el sistema lanza una alarma inmediata.

---

## 🌐 3. Configuración de Red (PROFINET / IP)
Para que el PLC se comunique en la red industrial, es necesario establecer:

* **Dirección IP:** Debe ser única en la red. Se configura en las propiedades del dispositivo bajo `PROFINET interface [X1] -> Ethernet addresses`.
* **Nombre de dispositivo (Device Name):** Es el identificador único para la asignación de PROFINET (debe coincidir exactamente con el nombre asignado en el hardware físico).
* **Subred y Gateway:** Configuración estándar de TCP/IP para asegurar la enrutabilidad si el PLC debe salir a otras redes o servidores.

---

## 🔒 4. Seguridad y Acceso
Protección contra accesos no autorizados y gestión de comunicación.

* **Protección del PLC:** Se puede establecer una contraseña para:
    * **Full Access:** Acceso total.
    * **HMI Access:** Acceso solo para pantallas HMI.
    * **Read Access:** Solo lectura (bloquea cambios de lógica).
* **Web Server:** Configuración del servidor web integrado.
    * **Permisos:** Habilitar acceso HTTPS, permitir actualización de firmware, y definir usuarios con permisos específicos.
* **Conexión de seguridad:** Uso de certificados digitales y cifrado en la comunicación (TLS) para evitar el "man-in-the-middle".

---
*Nota: Recuerda siempre compilar (Hardware y Software) después de realizar estos cambios para que los parámetros se carguen correctamente al PLC en la siguiente descarga.*
