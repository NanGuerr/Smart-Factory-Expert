# 📝 Cuestionario: Industria 4.0 y Node-RED 🚀


Este documento contiene las preguntas, opciones y respuestas correctas del cuestionario sobre los pilares de la Industria 4.0 y el entorno de desarrollo Node-RED.

---

### 1. 🌐 ¿Cuál de los siguientes no es un pilar de la Industria 4.0?
* 📊 Big Data
* ☁️ Cloud Computing
* 🖨️ Manufactura aditiva
* 🤖 Automatización
* 🔌 IoT

* **✔️ Respuesta correcta:** `Automatización`
* **💯 Puntuación:** 1 / 1

---

### 2. 🔄 Ordene los pasos necesarios a realizar para instalar Node-RED en Windows:
1. 🟢 **Descargar e Instalar Node.js**
2. 🔍 **Verificar instalación mediante el comando:** `node --version`
3. 📦 **Verificar instalación de npm mediante el comando:** `npm --version`
4. ⚙️ **Ejecutar el comando:** `npm install -g --unsafe-perm node-red`
5. 🚀 **Ejecutar el comando:** `node-red`
6. 🌐 **Acceder a un navegador mediante:** `http://localhost:1880`

* **✔️ Respuesta correcta:** El orden secuencial mencionado arriba.
* **💯 Puntuación:** 1 / 1

---

### 3. 🏗️ Relación de Capas e Instrumentación (Pirámide de la Automatización / ISA-95):
* 🏢 **ERP** ➡️ 📊 Gestión / Planificación
* 🏭 **MES** ➡️ 📈 Planificación / Gestión de Operaciones
* 🖥️ **SCADA, HMI** ➡️ 👁️ Supervisión
* 🎛️ **PLCs, DCS** ➡️ ⚙️ Control
* 🔌 **Sensores, Actuadores** ➡️ 🏗️ Campo

---

### 4. 🎯 Seleccione la opción correcta:
* ❌ Node-RED no es independiente de la plataforma donde se utiliza, es por ello que la instalación en Windows y Linux es diferente.
* ✔️ **Node-RED está creado sobre Node.js, un entorno open-source que nos permite ejecución de JavaScript en un servidor.**
* ❌ Dentro de Node-RED no es posible ejecutar código JavaScript, a pesar de estar basado en este lenguaje.
* ❌ El uso de objetos JavaScript en Node-RED no resulta relevante.

* **✔️ Respuesta correcta:** `Node-RED está creado sobre Node.js, un entorno open-source que nos permite ejecución de JavaScript en un servidor.`
* **💯 Puntuación:** 1 / 1

---

### 5. 🔌 En caso de que Node-RED se encuentre ejecutándose en un PLC, para acceder a su interfaz gráfica de forma externa al mismo ¿Utilizo `localhost:1880` o `127.0.0.1:1880`?
* ❌ `localhost:1880`
* ❌ `127.0.0.1:1880`
* ✔️ **Ninguna opción es correcta**

* **✔️ Respuesta correcta:** `Ninguna opción es correcta` *(Nota: Se debe utilizar la dirección IP estática o asignada al PLC en la red local, por ejemplo: `http://192.168.1.50:1880`)*.

---

### 6. ✉️ Si tengo el siguiente mensaje y quiero acceder al valor del atributo payload, ¿cómo puedo hacer?

```

```text
Archivo creado con éxito.

```javascript
msg = {
    msg_id: 12345,
    payload: "Hola a todos",
    topic: "Mensaje de prueba",
    otro_atributo: true,
}

```

* ❌ `msg:payload`
* ❌ `msg_payload`
* ❌ `msg=payload`
* ✔️ **`msg.payload`**
* ❌ `msg[payload]`
* ❌ `msg{payload}`
* **✔️ Respuesta correcta:** `msg.payload`
* **💯 Puntuación:** 1 / 1

---

### 7. ⚖️ El atributo payload de un mensaje, ¿siempre tiene que estar?

* ❌ Sí, es fundamental para el funcionamiento de cada flow que creamos.
* ✔️ **No, es opcional de acuerdo a la lógica que realicemos y el funcionamiento de los nodos utilizados.**
* **✔️ Respuesta correcta:** `No, es opcional de acuerdo a la lógica que realicemos y el funcionamiento de los nodos utilizados.`

---

### 8. 🖥️ ¿Cuál de la siguiente información NO se muestra en la consola cuando se inicia Node-RED?

* ❌ Node-RED version
* ✔️ **Node Library file**
* ❌ Node.js version
* ❌ User directory
* ❌ Flows file
* ❌ Settings file
* **✔️ Respuesta correcta:** `Node Library file`
* **💯 Puntuación:** 1 / 1

---

### 9. 📂 Especifique el directorio donde se guarda el archivo `flow.json`:

* **✏️ Respuesta:** `~/.node-red` en sistemas Linux / macOS (o `%USERPROFILE%\\.node-red` en sistemas Windows).

---

### 10. 🔢 ¿Cuántos nodos tiene la biblioteca `node-red-contrib-modbus` version 5.30.0?

*(Verificar la cantidad desde el Manage Palette)*

* ❌ 16
* ❌ 10
* ❌ 5
* ✔️ **15**
* ❌ 12
* **✔️ Respuesta correcta:** `15`
* **💯 Puntuación:** 0 / 1 *(Corrección según plantilla)*
