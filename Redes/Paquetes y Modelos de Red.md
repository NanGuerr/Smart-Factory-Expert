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

🛠️ TCP/IP: El estándar de facto
* **TCP:** Garantiza que todo llegue correctamente. 📦
* **IP:** Asegura que los paquetes se enruten a la dirección correcta. 🗺️

Nota: TCP/IP gestiona el transporte y el enrutamiento, pero no define cómo deben interpretarse los datos en sí.
