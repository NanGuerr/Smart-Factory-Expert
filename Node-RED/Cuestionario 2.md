# 📚 Cuestionario

### 1. ¿Cuál NO es una arquitectura correspondiente a una variante Modbus?

**Respuesta:** **Publicador - Suscriptor**

* **Explicación:** Modbus utiliza arquitecturas **Maestro-Esclavo** (en su versión serial RTU/ASCII) o **Cliente-Servidor** (en su versión Modbus TCP/IP). El modelo "Publicador-Suscriptor" es típico de protocolos más modernos como MQTT o DDS.

### 2. ¿Cuál código de función se utiliza para leer Holding Registers?

**Respuesta:** **FC03**

* **Explicación:** En Modbus, las funciones están estandarizadas: `FC01` es para leer bobinas (coils), `FC02` para entradas discretas, **`FC03` para Holding Registers** y `FC04` para Input Registers.

### 3. Un protocolo de comunicación está compuesto por dos partes fundamentales. ¿Cuáles son?

**Respuesta:** **Codificación de datos y Estructura**

* **Explicación:** Aunque depende de la bibliografía, un protocolo define fundamentalmente la **Sintaxis** (Estructura, cómo se ordenan los bits/bytes) y la **Semántica** (Codificación o significado de los datos). El medio físico no es parte del protocolo en sí, sino el vehículo por donde viaja.

### 4. En Modbus TCP/IP, ¿cuál es la infraestructura utilizada?

**Respuesta:** **Ethernet**

* **Explicación:** Modbus TCP/IP encapsula las tramas Modbus dentro de paquetes TCP/IP, lo que requiere una infraestructura de red basada en Ethernet.

### 5. A nivel de campo se transmiten una gran cantidad de datos con un tiempo de respuesta muy bajo.

**Respuesta:** **Falso**

* **Explicación:** A nivel de campo (sensores/actuadores), el tiempo de respuesta debe ser extremadamente bajo (real-time), pero la **cantidad de datos** transmitida por dispositivo suele ser pequeña (pocos bits o palabras), a diferencia de los niveles superiores (SCADA/MES) donde se maneja mucha información.

### 6. ¿De qué depende la selección del medio de transmisión?

**Respuesta:** **Distancia, Velocidad de transmisión e Interferencia electromagnética**

* **Explicación:** Todos estos factores son críticos. No usarías fibra óptica para una conexión de 1 metro, ni cable telefónico sin blindaje en una zona con alta interferencia electromagnética (EMI) de motores o variadores de frecuencia.

### 7. Clasificación de dispositivos según modelo OSI

Aquí tienes la correspondencia correcta de los dispositivos con su capa del modelo OSI:

* **HUB:** **3 (Capa 1 - Física)**. Repite la señal a todos los puertos, opera en nivel físico.
* **SWITCH:** **4 (Capa 2 - Enlace de datos)**. Conoce las direcciones MAC, gestiona el tráfico local.
* **ROUTER:** **2 (Capa 3 - Red)**. Conoce las direcciones IP, gestiona rutas entre redes.
* **GATEWAY:** **1 (Capa 7 - Aplicación)**. Traduce protocolos entre redes totalmente distintas.

### 8. Diferencias TCP vs UDP

* **TCP:** **2** (Comprueba constantemente la conexión, asegura orden y entrega - *Connection-oriented*).
* **UDP:** **1** (Envía ciegamente, es más rápido pero sin verificación de entrega - *Connectionless*).

### 9. HART permite la transmisión de datos digitales sobre una señal de 0-10v

**Respuesta:** **Falso**

* **Explicación:** El protocolo HART (Highway Addressable Remote Transducer) utiliza una señal digital superpuesta sobre un lazo de corriente estándar de **4-20 mA**, no sobre una señal de voltaje de 0-10V.
