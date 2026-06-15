# 📚 Protocolos de Comunicación Industrial


## 🏗️ 1. Arquitecturas Modbus
**¿Cuál NO es una arquitectura correspondiente a una variante Modbus?**

* **Respuesta:** Publicador - Suscriptor.
* **Explicación:** Modbus utiliza arquitecturas Maestro-Esclavo (Modbus RTU/ASCII) o Cliente-Servidor (Modbus TCP/IP). El modelo "Publicador-Suscriptor" es característico de protocolos como MQTT o DDS.

---

## 🔢 2. Códigos de Función
**¿Cuál código de función se utiliza para leer Holding Registers?**

* **Respuesta:** FC03.
* **Explicación:** Las funciones están estandarizadas: 
    * FC01: Leer bobinas (Coils).
    * FC02: Leer entradas discretas.
    * FC03: Leer Holding Registers.
    * FC04: Leer Input Registers.

---

## 🧠 3. Composición de un Protocolo
**Un protocolo de comunicación está compuesto por dos partes fundamentales. ¿Cuáles son?**

* **Respuesta:** Estructura y Codificación de datos.
* **Explicación:** Un protocolo define la **Sintaxis** (Estructura, orden de bits/bytes) y la **Semántica** (Codificación o significado de los datos).

---

## 🌐 4. Infraestructura Modbus TCP/IP
**¿Cuál es la infraestructura utilizada?**

* **Respuesta:** Ethernet.
* **Explicación:** Modbus TCP/IP encapsula las tramas dentro de paquetes TCP/IP, requiriendo redes basadas en Ethernet.

---

## ⚡ 5. Transmisión a Nivel de Campo
**¿A nivel de campo se transmiten una gran cantidad de datos con un tiempo de respuesta muy bajo?**

* **Respuesta:** Falso.
* **Explicación:** Aunque el tiempo de respuesta debe ser extremadamente bajo (tiempo real), la cantidad de datos por dispositivo suele ser pequeña (pocos bits o palabras), a diferencia de niveles superiores como SCADA o MES.

---

## 🔌 6. Selección del Medio de Transmisión
**¿De qué depende la selección del medio de transmisión?**

* **Respuesta:** Depende de todos los factores mencionados:
    * Distancia.
    * Velocidad de transmisión.
    * Interferencia electromagnética (EMI).
    * Interferencia mecánica.

---

## 🗺️ 7. Dispositivos y Modelo OSI
**Clasificación de dispositivos según el modelo OSI:**

| Dispositivo | Capa OSI | Función |
| :--- | :--- | :--- |
| **HUB** | Capa 1 (Física) | Repite la señal a todos los puertos. |
| **SWITCH** | Capa 2 (Enlace de datos) | Gestiona tráfico local vía direcciones MAC. |
| **ROUTER** | Capa 3 (Red) | Gestiona rutas entre redes vía direcciones IP. |
| **GATEWAY** | Capa 7 (Aplicación) | Traduce protocolos entre redes distintas. |

---

## 🔗 8. Diferencias TCP vs UDP
**Seleccione las características correspondientes:**

* **TCP (Transmission Control Protocol):** Orientado a conexión. Comprueba constantemente si la conexión es estable, asegura el orden de entrega y verifica que los datos no estén corruptos.
* **UDP (User Datagram Protocol):** Sin conexión (Connectionless). Envía paquetes sin verificar si llegan al destino o si se pierden en el camino. Es más rápido pero menos fiable.

---

## 📡 9. Protocolo HART
**¿HART permite la transmisión de datos digitales sobre una señal de 0-10v?**

* **Respuesta:** Falso.
* **Explicación:** El protocolo HART superpone datos digitales sobre un lazo de corriente estándar de **4-20 mA**, no sobre una señal de voltaje de 0-10V.
