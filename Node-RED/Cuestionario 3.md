# 📝 Cuestionario de Evaluación: Node-RED, Modbus y MQTT

A continuación se presenta el resumen resuelto del cuestionario con sus respectivas respuestas correctas y explicaciones clave. 🎯

---

### ⚙️ 1. Ejecución de Node-RED
*   **Pregunta:** ¿Cómo es la ejecución de Node-RED? 🖥️
*   **Respuesta Correcta:** En un servidor (dispositivo) a partir de eventos definidos. ⚡

---

### 🧠 2. Nodos Function en Node-RED
*   **Pregunta:** Marque la afirmación correcta sobre los nodos Function. 🧩
*   **Respuesta Correcta:** El nodo function únicamente puede retornar un objeto del tipo msg. 📦

---

### 🔄 3. Asignación de Variables con el Nodo Change
*   **Pregunta:** Quiero asignar el valor de `msg.payload` a la variable tipo flow "temperatura" con el nodo change, ¿Cuál es la opción correcta? 🔀
*   **Respuesta Correcta:** **Opción 2** (Configurar `Set` a `flow.temperature` con el valor de `msg.payload`). ✅

---

### 🔌 4. Puertos por Defecto en Automatización
*   **Pregunta:** Ordene de forma correcta los puertos utilizados por defecto: 🌐
    *   **Modbus TCP/IP:** `502` ⚡
    *   **Node-RED:** `1880` 🖥️
    *   **MQTT:** `1883` 📡
    *   **Protocolo S7:** `102` 🏭

---

### 📊 5. Estructura de Tópicos en MQTT
*   **Pregunta:** Mediante el siguiente topic `planta/produccion/linea1/#`, ¿A qué datos estoy accediendo? 🔍
*   **Respuesta Correcta:** Ambas variables de la línea 1. 📈

---

### 📡 6. Conceptos de MQTT
*   **Pregunta:** Marque la afirmación correcta sobre MQTT. 💬
*   **Respuesta Correcta:** En una comunicación MQTT hay un intermediario entre los clientes denominado Bróker. 🏢

---

### 🔢 7. Códigos de Función Modbus
*   **Pregunta:** ¿Cuál código de función se utiliza para leer *Holding Registers*? 📖
*   **Respuesta Correcta:** **FC03**. ⚙️

---

### 🌐 8. Arquitecturas Modbus
*   **Pregunta:** ¿Cuál NO es una arquitectura correspondiente a una variante Modbus? ❌
*   **Respuesta Correcta:** Publicador - Suscriptor (Esta arquitectura pertenece a MQTT, mientras que Modbus utiliza Maestro-Esclavo / Cliente-Servidor). 🔄

---

### 📥 9. Métodos de Solicitud (GET / PUT)
*   **Pregunta:** Ordene según corresponda los métodos: 📋
    *   **GET:** Utilizado para leer o recibir datos. 🔍
    *   **PUT:** Utilizado para escribir o enviar datos. ✍️
