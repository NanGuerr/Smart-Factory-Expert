# 📡 Cuestionario 3: MQTT, Modbus Avanzado y Análisis de CSV en Node-RED

Este documento recopila procedimientos clave para publicar datos por MQTT, diferencias entre nodos Modbus y flujos para procesar archivos CSV. ⚙️

---

## 📤 1. Publicación de Datos en un Topic usando MQTT

Para publicar un dato en un *topic* utilizando MQTT dentro de Node-RED, realiza el siguiente procedimiento:

1. **Arrastra el nodo MQTT Out** (`mqtt out`) al espacio de trabajo. 🌐
2. **Configura el Bróker:** Haz doble clic en el nodo, y en la sección *Server*, haz clic en el icono de lápiz ✏️ para configurar la dirección IP del Bróker, el puerto por defecto (`1883`) y las credenciales si son requeridas. 🔑
3. **Define el Topic:** Configura una ruta clara, por ejemplo: `planta/produccion/linea1/sensor`. 🏷️
4. **Conecta una fuente de datos:** Conecta un nodo de entrada como `inject` o `function` hacia el nodo MQTT. El valor que llegue a la propiedad `msg.payload` será lo que se publique automáticamente en el Bróker. 📦

> **¿Es necesario descargar alguna biblioteca?**
> Sí, se requiere el nodo oficial o estándar de MQTT. Para instalarlo, ve al menú de Node-RED (tres líneas horizontales ≡), selecciona **Manage palette**, ve a la pestaña **Install** y busca la biblioteca `node-red-contrib-mqtt`. 🔍

---

## ⚖️ 2. Diferencias entre Modbus Getter y Modbus Flex Getter

*   **Modbus Getter:** Es una versión estática donde sus parámetros (dirección del registro, cantidad de registros, ID de unidad) se configuran directamente de forma fija en la ventana de propiedades del nodo. Se utiliza para tareas predefinidas y constantes. 📌
*   **Modbus Flex Getter:** Es una versión dinámica. La configuración espera recibir los parámetros de lectura directamente a través del mensaje de entrada (`msg.fc`, `msg.unitid`, `msg.address`, `msg.quantity`), lo que permite modificar los parámetros de lectura en tiempo de ejecución de manera flexible. 🔄

---

## 📊 3. Procesamiento de Archivos CSV en Node-RED

Para analizar archivos con datos tabulares (como calcular valores máximos o promedios), se puede utilizar un archivo `.csv` y estructurarlo mediante flujos lógicos con nodos *File in*, *CSV* y *Function*. 📂

### 💻 Ejemplo de Flujo en Formato JSON (Para importar como texto `.txt`)

```json
[
{
"id": "inject_datos",
"type": "inject",
"z": "flow_analisis_csv",
"name": "Iniciar Análisis",
"props": [
{
"p": "payload"
}
],
"repeat": "",
"crontab": "",
"once": false,
"onceDelay": 0.1,
"topic": "",
"payload": "",
"payloadType": "date",
"x": 140,
"y": 120,
"wires": [
[
"read_csv_file"
]
]
},
{
"id": "read_csv_file",
"type": "file in",
"z": "flow_analisis_csv",
"name": "Leer datos.csv",
"filename": "datos.csv",
"filenameType": "str",
"format": "utf8",
"chunk": false,
"sendError": false,
"encoding": "none",
"allProps": false,
"x": 320,
"y": 120,
"wires": [
[
"parse_csv"
]
]
},
{
"id": "parse_csv",
"type": "csv",
"z": "flow_analisis_csv",
"name": "Parsear a Array",
"sep": ",",
"hdrin": true,
"hdrout": "none",
"multi": "mult",
"ret": "\\n",
"temp": "",
"skip": "0",
"strings": true,
"include_empty_strings": "",
"include_null_values": "",
"x": 500,
"y": 120,
"wires": [
[
"calc_max_potencia",
"calc_avg_corriente"
]
]
},
{
"id": "calc_max_potencia",
"type": "function",
"z": "flow_analisis_csv",
"name": "a) Max Potencia",
"func": "let maxPot = -Infinity;\n\n// Iteramos sobre todos los registros del CSV\nmsg.payload.forEach(row => {\n // Convertimos el string a un número decimal\n let p = parseFloat(row.potencia);\n // Verificamos que sea un número válido y si es mayor al actual\n if (!isNaN(p) && p > maxPot) {\n maxPot = p;\n }\n});\n\nmsg.payload = \"La potencia máxima registrada es: \" + maxPot;\nreturn msg;",
"outputs": 1,
"timeout": 0,
"noerr": 0,
"initialize": "",
"finalize": "",
"libs": [],
"x": 720,
"y": 80,
"wires": [
[
"debug_max"
]
]
},
{
"id": "calc_avg_corriente",
"type": "function",
"z": "flow_analisis_csv",
"name": "b) Promedio Corriente",
"func": "let sum = 0;\nlet count = 0;\n\n// Iteramos sobre todos los registros\nmsg.payload.forEach(row => {\n let c = parseFloat(row.corriente);\n if (!isNaN(c)) {\n sum += c;\n count++;\n }\n});\n\n// Calculamos el promedio y evitamos división por cero\nlet avg = count > 0 ? (sum / count) : 0;\n\n// Formateamos a 2 decimales para mayor legibilidad\nmsg.payload = \"La corriente promedio es: \" + avg.toFixed(2);\nreturn msg;",
"outputs": 1,
"timeout": 0,
"noerr": 0,
"initialize": "",
"finalize": "",
"libs": [],
"x": 740,
"y": 160,
"wires": [
[
"debug_avg"
]
]
},
{
"id": "debug_max",
"type": "debug",
"z": "flow_analisis_csv",
"name": "Resultado Máxima",
"active": true,
"tosidebar": true,
"console": false,
"tostatus": false,
"complete": "payload",
"targetType": "msg",
"statusVal": "",
"statusType": "auto",
"x": 950,
"y": 80,
"wires": []
},
{
"id": "debug_avg",
"type": "debug",
"z": "flow_analisis_csv",
"name": "Resultado Promedio",
"active": true,
"tosidebar": true,
"console": false,
"tostatus": false,
"complete": "payload",
"targetType": "msg",
"statusVal": "",
"statusType": "auto",
"x": 960,
"y": 160,
"wires": []
}
]
