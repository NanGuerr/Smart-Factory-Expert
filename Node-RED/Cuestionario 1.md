# 📚 Cuestionario: Automatización e IIoT

### 1. ¿Cuál NO es un pilar de la Industria 4.0? 🏭
* **Respuesta:** Automatización
* **Explicación:** Si bien la automatización es el fundamento y la base sobre la que se construye la Industria 4.0, esta última se define precisamente por ir más allá de la automatización tradicional, integrando tecnologías disruptivas como Big Data, Cloud Computing, IoT, Manufactura Aditiva (impresión 3D), Robótica autónoma, Simulación, Realidad Aumentada y Ciberseguridad. 🚀

---

### 2. Seleccione las opciones correctas (Modelo ISA-95) 🏗️
Para entender mejor esta estructura, se utiliza la "Pirámide de la Automatización", que jerarquiza los sistemas desde el nivel de campo hasta el de gestión:

* **ERP:** 2. Planificación (Nivel corporativo/gestión de recursos). 📅
* **MES:** 1. Gestión (Nivel de ejecución de manufactura). ⚙️
* **SCADA, HMI:** 3. Supervisión (Monitoreo de procesos). 🖥️
* **PLCs, DCS:** 4. Control (Lógica de control directo). 🧠
* **Sensores, Actuadores:** 5. Campo (Nivel de campo, interacción física). 🔌

---

### 3. El atributo payload de un mensaje, ¿siempre tiene que estar? 📦
* **Respuesta:** No, es opcional de acuerdo a la lógica que realicemos y el funcionamiento de los nodos utilizados.
* **Explicación:** En Node-RED, aunque `msg.payload` es el lugar estándar donde la mayoría de los nodos esperan encontrar los datos, el objeto `msg` es simplemente un objeto JavaScript. Puedes pasar información en otras propiedades (por ejemplo, `msg.topic`, `msg.timestamp` o propiedades personalizadas) dependiendo de la necesidad de tu flujo. 🛠️

---

### 4. En caso de que Node-RED se encuentre ejecutándose en un PLC, para acceder a su interfaz gráfica de forma externa, ¿utilizo localhost:1880 o 127.0.0.1:1880? 🌐
* **Respuesta:** Ninguna opción es correcta.
* **Explicación:** Tanto `localhost` como `127.0.0.1` son direcciones de "loopback". Esto significa que solo funcionan para conexiones internas realizadas desde el mismo dispositivo (el PLC). Para acceder desde fuera (externamente) a través de una red, debes usar la dirección IP física o asignada de ese PLC en la red (ejemplo: `192.168.1.10:1880`). 📡

---

### 5. Marque la afirmación correcta. 🔗
* **Respuesta:** En una comunicación MQTT hay un intermediario entre los clientes denominado Bróker.
* **Explicación:** MQTT funciona bajo un modelo de Publicador-Suscriptor donde los dispositivos (clientes) nunca se conectan directamente entre sí. Todos envían o reciben mensajes a través de un nodo central llamado Bróker, que gestiona el enrutamiento de los datos según los "tópicos" (temas) a los que los clientes están suscritos. ✉️
