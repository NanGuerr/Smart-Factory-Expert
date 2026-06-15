# 📦 Comunicación Basada en Paquetes y Modelos de Red

La información que viaja por nuestras redes no se envía como un bloque único; se subdivide en **paquetes individuales**. Al llegar al receptor, estos paquetes se recomponen para interpretar el mensaje correctamente. 🧩

## 🌐 El Modelo OSI (Open System Interconnection)
Desarrollado por la ISO en 1983, este modelo de **7 capas** no es una implementación real, sino una estructura de referencia para entender cómo deben funcionar las comunicaciones. 🏗️

| Capa | Nombre |
| :--- | :--- |
| 7 | Application Layer (Aplicación) |
| 6 | Presentation Layer (Presentación) |
| 5 | Session Layer (Sesión) |
| 4 | Transport Layer (Transporte) |
| 3 | Network Layer (Red) |
| 2 | Data Link Layer (Enlace de datos) |
| 1 | Physical Layer (Física) |

*Cada capa proporciona servicios a la siguiente y utiliza los de la anterior.* 🔄

---

## 🚚 La Capa de Transporte (Capa 4)
Es fundamental para una comunicación exitosa. Aquí operan los dos protocolos principales: **TCP** y **UDP**. 🚀

### 🆚 TCP vs. UDP: ¿Cuál elegir?

*   **TCP (Transmission Control Protocol)**:
    *   ✅ **Fiable**: Verifica constantemente si la conexión está bien, si los paquetes llegan en orden y si no están corruptos.
    *   🔄 **Reenvío**: Si un paquete se pierde, se solicita su reenvío.
    *   📉 **Desventaja**: Menor velocidad y mayor consumo de ancho de banda debido a las comprobaciones constantes.
*   **UDP (User Datagram Protocol)**:
    *   ⚡ **Rápido**: Envía los paquetes "a ciegas" sin preocuparse por la confirmación de recepción.
    *   🚫 **Sin Reenvío**: Si se pierde un paquete, se pierde. Ideal para streaming en tiempo real.

---

## 🛠️ TCP/IP: El estándar de facto
*   **TCP**: Garantiza que todo llegue correctamente. 📦
*   **IP**: Asegura que los paquetes se enruten a la dirección correcta. 🗺️

Nota: TCP/IP gestiona el transporte y el enrutamiento, pero no define cómo deben interpretarse los datos en sí.

---

# ⚙️ Protocolo de Comunicación Modbus

Modbus es un protocolo de comunicación abierto creado por **Modicon en 1979**. Es un estándar industrial fundamental que define reglas para organizar e interpretar datos, permitiendo que la mayoría de los dispositivos industriales se comuniquen entre sí. 🏭

## 🌐 Variantes de Modbus
Dependiendo de la infraestructura utilizada, existen dos variantes principales:

* **Modbus RTU**:
    * Arquitectura **maestro-esclavo**. 👑
    * Utiliza comunicación serie (**RS232 o RS485**).
    * Cada dispositivo tiene una dirección única y utiliza **CRC** para comprobar errores.
* **Modbus TCP/IP**:
    * Arquitectura **Cliente-Servidor**. 🖥️
    * Infraestructura basada en **Ethernet**.
    * Utiliza el puerto **502** por defecto.
    * Permite múltiples clientes conectados al mismo servidor.

## 🗄️ Objetos de Datos
Para acceder a la información, Modbus utiliza cuatro tipos de objetos estándar:

| Tipo de Objeto | Acceso | Tamaño |
| :--- | :--- | :--- |
| **Discrete input** | Solo lectura | 1 bit |
| **Coil** | Lectura/Escritura | 1 bit |
| **Input register** | Solo lectura | 16 bits |
| **Holding register** | Lectura/Escritura | 16 bits |

## 💡 Consideración Técnica: Datos REAL o FLOAT
* Modbus transfiere datos en bloques de **16 bits (WORD)**. 📏
* Un dato **REAL o FLOAT** ocupa **32 bits**.
* Para leer un dato REAL, es necesario leer **dos registros de 16 bits** consecutivos y unirlos para obtener el valor completo.
