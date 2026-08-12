```markdown
# 🧩 Creación de Subflows Modulares en Node-RED

Esta guía explica paso a paso cómo crear y configurar dos **Subflows** muy útiles en Node-RED: uno para leer **Coils Modbus** de forma dinámica y otro para calcular el **valor máximo de cualquier columna en un archivo CSV**. 📊⚙️

---

## 🔌 1. Subflow: Lector Modbus Dinámico de Coils

Este subflow permite leer *Coils* (Código de Función 1) de un servidor Modbus, permitiendo modificar de forma dinámica la dirección inicial (*Address*) y la cantidad (*Quantity*) desde las propiedades del subflow utilizando variables de entorno y un nodo `Modbus Flex Getter`. 🎛️

### 📄 Código JSON del Subflow (Para importar como `.txt`)

```json
[
{
"id": "subflow_modbus_reader",
"type": "subflow",
"name": "Lector Modbus Dinámico",
"info": "Subflow para leer coils con Address y Quantity configurables mediante Modbus Flex Getter.",
"category": "",
"in": [
{
"x": 60,
"y": 80,
"wires": [
{
"id": "config_flex_getter"
}
]
}
],
"out": [
{
"x": 580,
"y": 80,
"wires": [
{
"id": "modbus_flex_getter_node",
"port": 0
}
]
}
],
"env": [
{
"name": "address",
"type": "num",
"value": "0"
},
{
"name": "quantity",
"type": "num",
"value": "4"
}
]
},
{
"id": "config_flex_getter",
"type": "function",
"z": "subflow_modbus_reader",
"name": "Configurar Payload",
"func": "msg.payload = {\n 'fc': 1, // Function Code 1: Leer Coils\n 'unitid': 1,\n 'address': Number(env.get(\"address\") || 0), \n 'quantity': Number(env.get(\"quantity\") || 1)\n};\nreturn msg;",
"outputs": 1,
"timeout": 0,
"noerr": 0,
"initialize": "",
"finalize": "",
"libs": [],
"x": 210,
"y": 80,
"wires": [
[
"modbus_flex_getter_node"
]
]
},
{
"id": "modbus_flex_getter_node",
"type": "modbus-flex-getter",
"z": "subflow_modbus_reader",
"name": "Leer Coils Dinámico",
"showStatusActivities": false,
"showErrors": false,
"showWarnings": true,
"logIOActivities": false,
"server": "",
"useIOFile": false,
"ioFile": "",
"useIOForPayload": false,
"emptyMsgOnFail": false,
"keepMsgProperties": false,
"delayOnStart": false,
"startDelayTime": "",
"x": 420,
"y": 80,
"wires": [
[],
[]
]
}
]

```

---

## 📈 2. Subflow: Cálculo de Máximo en Columnas de un CSV

Este subflow modular lee un archivo CSV (como `datos.csv`) utilizando variables de entorno para definir tanto la ruta del archivo (`FILE_PATH`) como la columna objetivo de la cual se desea calcular el valor máximo (`TARGET_COLUMN`). 📂🔍

### 📄 Código JSON del Subflow (Para importar como `.txt`)

```json
[
{
"id": "subflow_max_csv",
"type": "subflow",
"name": "Max CSV Column",
"info": "Este subflow lee un archivo CSV y calcula el valor máximo de la columna especificada en las propiedades.",
"category": "function",
"in": [
{
"x": 60,
"y": 80,
"wires": [
{
"id": "file_read_node"
}
]
}
],
"out": [
{
"x": 720,
"y": 80,
"wires": [
{
"id": "calc_max_func",
"port": 0
}
]
}
],
"env": [
{
"name": "FILE_PATH",
"type": "str",
"value": "datos.csv",
"ui": {
"label": {
"en-US": "Ruta del Archivo"
},
"type": "input",
"opts": {
"types": [
"str",
"env"
]
}
}
},
{
"name": "TARGET_COLUMN",
"type": "str",
"value": "corriente",
"ui": {
"label": {
"en-US": "Columna Objetivo"
},
"type": "input",
"opts": {
"types": [
"str",
"env"
]
}
}
}
],
"meta": {},
"color": "#DDAA99"
},
{
"id": "file_read_node",
"type": "file in",
"z": "subflow_max_csv",
"name": "Leer Archivo",
"filename": "${FILE_PATH}",
"filenameType": "str",
"format": "utf8",
"chunk": false,
"sendError": false,
"encoding": "none",
"allProps": false,
"x": 210,
"y": 80,
"wires": [
[
"csv_parser_node"
]
]
},
{
"id": "csv_parser_node",
"type": "csv",
"z": "subflow_max_csv",
"name": "Parsear CSV",
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
"x": 390,
"y": 80,
"wires": [
[
"calc_max_func"
]
]
},
{
"id": "calc_max_func",
"type": "function",
"z": "subflow_max_csv",
"name": "Calcular Máximo Dinámico",
"func": "// Obtenemos la columna objetivo desde las variables de entorno del Subflow\nlet columna = env.get(\"TARGET_COLUMN\");\nlet maxVal = -Infinity;\n\n// Verificamos que el payload sea un arreglo (resultado del nodo CSV)\nif (Array.isArray(msg.payload)) {\n msg.payload.forEach(row => {\n // Accedemos dinámicamente a la propiedad usando corchetes: row[columna]\n let val = parseFloat(row[columna]);\n \n // Comparamos si es un número válido y si es mayor al actual\n if (!isNaN(val) && val > maxVal) {\n maxVal = val;\n }\n });\n}\n\n// Preparamos el mensaje de salida\nmsg.payload = maxVal;\nmsg.topic = \"Máximo de la columna: \" + columna;\n\nreturn msg;",
"outputs": 1,
"timeout": 0,
"noerr": 0,
"initialize": "",
"finalize": "",
"libs": [],
"x": 580,
"y": 80,
"wires": [
[]
]
}
]

```

> 💡 **Nota de entrega:** Recuerda guardar los códigos anteriores en un archivo con extensión **`.txt`** para importarlos sin problemas en tu entorno de Node-RED. 📝✨

```

```
