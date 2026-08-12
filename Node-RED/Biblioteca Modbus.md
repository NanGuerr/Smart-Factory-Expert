## 📦 Biblioteca: `node-red-contrib-modbus`

`node-red-contrib-modbus` es la herramienta estándar, más completa y con mayor soporte a largo plazo (*Long Term Supported*) para integrar redes y dispositivos **Modbus** (TCP, RTU y Serial) directamente dentro de flujos en Node-RED.

---

### 🚀 Características Principales

* **Conectividad Dual:** Soporta tanto **Modbus TCP** (Ethernet industrial) como **Modbus Serial** (RTU/ASCII mediante puertos COM o convertidores).
* **Gestión de Cola Inteligente (*Queue*):** Incorpora una máquina de estados robusta (`XState`) para manejar colas de comandos, prevenir la saturación del bus de comunicación y gestionar reconexiones automáticas ante fallas de red.
* **Bloques Versátiles:**
* `modbus-client`: Nodo de configuración global para definir parámetros de conexión (IP, puerto, tiempos de espera).
* `modbus-read`: Realiza lecturas periódicas automáticas de registros o bobinas (FC1 a FC4).
* `modbus-getter`: Ejecuta lecturas **bajo demanda** (activadas solo al recibir un mensaje de entrada).
* `modbus-write`: Permite escribir valores individuales o múltiples (FC5, FC6, FC15, FC16).
* `modbus-server`: Permite simular un esclavo Modbus virtual directamente en Node-RED para pruebas y desarrollo offline.



---

### 💡 Ejemplo de Uso Típico

1. Se arrastra un nodo **`modbus-read`** al lienzo para consultar un bloque de *Holding Registers* cada 5 segundos.
2. Se asocia a un nodo **`modbus-client`** configurado con la dirección IP del PLC o instrumento.
3. La salida entrega un arreglo (`msg.payload`) con los valores numéricos leídos, los cuales se pueden procesar mediante nodos de función, convertir con `node-red-contrib-buffer-parser` o enviar directo a un panel visual (*Node-RED Dashboard*).
