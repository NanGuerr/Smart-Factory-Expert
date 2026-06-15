# 🌐 Introducción a la Comunicación MQTT

MQTT es un estándar de comunicación abierto, diseñado para ser extremadamente **simple** y **liviano**. Es la solución ideal para el intercambio de información entre dispositivos y redes con recursos limitados. 🚀

## 🏗️ ¿Cómo funciona?
El protocolo utiliza un modelo de comunicación **Publicador/Suscriptor** que involucra a tres actores principales:

1.  **Clientes**: Dispositivos que envían o reciben información. 📱
2.  **Broker**: El intermediario centralizado que gestiona el tráfico de mensajes. 🏢
3.  **Topics**: El canal donde se publica y se suscribe la información. 📌

### 💡 Características Clave
*   **Basado en Eventos**: No hay transmisión continua de datos. El cliente solo publica cuando realmente hay información nueva para enviar. ⚡
*   **Sensibilidad**: Los *topics* son sensibles a mayúsculas y minúsculas (¡cuidado con esto! ⚠️).
*   **Ubicación Flexible**: El Broker puede estar alojado de forma local o en la nube (ej. AWS, HiveMQ, Mosquitto). ☁️

## 📈 ¿Por qué elegir MQTT? (Ventajas)
*   🔋 **Eficiencia**: Bajo consumo de energía, recursos y ancho de banda.
*   🔌 **Conectividad**: Utiliza el puerto **1883** por defecto.
*   ✅ **Fiabilidad**: Soporta Calidad de Servicio (QoS) para garantizar la entrega de mensajes.

---
# 🛠️ Node-RED en la Industria

Node-RED es una poderosa herramienta de **programación visual basada en flujos**, diseñada originalmente por desarrolladores de IBM en 2013. Hoy en día, es un proyecto fundamental gestionado por la **OpenJS Foundation**.

## 💡 ¿Qué es Node-RED?

Es una interfaz que permite conectar dispositivos, servicios web y software de forma sencilla mediante bloques visuales.

* **Programación Visual**: Construyes lógica uniendo nodos en un lienzo (Workspace).
* **Acceso**: Se accede a través de cualquier navegador web usando la dirección IP del dispositivo y el puerto **1880** (por ejemplo: `localhost:1880`).

## 🏗️ Los Pilares de Node-RED

El funcionamiento se basa en tres conceptos fundamentales:

1. **Nodos**: Son las unidades básicas que realizan tareas específicas (lectura de PLC, filtros, generación de archivos, etc.).
2. **Mensajes (msg)**: Es el objeto de datos que viaja entre los nodos. Contiene atributos como el `payload` (la carga o dato principal) y el `topic`.
3. **Flujos (Flows)**: La secuencia conectada de nodos que define la lógica de la aplicación.

---

## 🔗 ¿Cómo se relaciona Node-RED con MQTT?

La combinación de **Node-RED** y **MQTT** es extremadamente común en la industria por su eficiencia y versatilidad. Su relación se da de la siguiente manera:

* **Node-RED como Cliente**: Node-RED actúa como un "Cliente" (o múltiples clientes) dentro de la arquitectura MQTT. Puede suscribirse a temas (*topics*) para recibir datos de sensores o publicar información procesada hacia otros sistemas.
* **Gestión de Datos (OT/IT)**: Node-RED permite realizar la "puente" entre el mundo industrial (PLC) y el mundo digital. Por ejemplo, puedes leer datos de un PLC (usando nodos específicos), filtrarlos o transformarlos, y luego enviarlos vía MQTT a un broker en la nube (como AWS o HiveMQ).
* **Basado en Eventos**: Dado que MQTT solo transmite cuando hay datos nuevos, Node-RED es ideal para procesar estos eventos de forma asíncrona, ahorrando recursos y ancho de banda.

### Ejemplo de flujo industrial:

1. **Lectura**: El nodo de *Lectura PLC* obtiene datos de la máquina.
2. **Procesamiento**: Se usan nodos para *Filtrar datos* o realizar cálculos.
3. **Comunicación**: Un nodo MQTT publica el resultado en un *topic* específico para que otros sistemas puedan consumirlo.
