# 🐙 Ejercicios Prácticos Nodo Function y Gestión de Paletas

Este documento recopila de manera detallada la resolución técnica y la infraestructura en formato JSON para la importación de flujos en Node-RED, cubriendo operaciones con el nodo `function`, lógica condicional multinivel y la auditoría de instalación de paquetes del ecosistema de automatización.

---

## 🛠️ 1. Ejercicios con el Nodo Function

El nodo `Function` en Node-RED es un componente avanzado que permite ejecutar código JavaScript directamente sobre el objeto `msg` (mensaje) que fluye a través del ecosistema. A continuación, se detallan los tres procedimientos solicitados:

### ➕ a) Suma Simple de Dos Números
* **Procedimiento:** Se utiliza un nodo `Inject` que envía un objeto JSON con dos propiedades numéricas (`num1` y `num2`). El nodo `Function` intercepta este objeto, suma ambos valores y sobrescribe la propiedad principal `msg.payload` con el resultado numérico total, enviándolo finalmente a la consola de depuración (`Debug`).
* **Código JavaScript Interno:**
  ```javascript
  msg.payload = msg.payload.num1 + msg.payload.num2;
  return msg;
  ```

### 🛑 b) Filtrado Condicional (Retorno Selectivo)
* **Procedimiento:** En este escenario se requiere evaluar el resultado antes de propagarlo. Si la suma de las propiedades del payload supera el valor de **50**, el nodo actualiza el mensaje y lo retorna para que continúe hacia el nodo `Debug`. En caso contrario (valores menores o iguales a 50), el nodo ejecuta un `return null;`. Al retornar un valor nulo, Node-RED interrumpe de inmediato el flujo de ese mensaje específico, evitando que se registre en la consola.
* **Código JavaScript Interno:**
  ```javascript
  var sum = msg.payload.num1 + msg.payload.num2;
  if (sum > 50) {
      msg.payload = "Resultado mayor a 50: " + sum;
      return msg;
  } else {
      return null; // Interrupción física del flujo
  }
  ```

### 🔀 c) Enrutamiento Dinámico con Multi-Salidas
* **Procedimiento:** El nodo `Function` se configura internamente para admitir **2 salidas físicas independientes**. Al evaluar la condición matemática, el nodo retorna un arreglo bidimensional `[salida1, salida2]`. 
  * Si el cálculo es mayor a 50, se envía el objeto a la primera posición y un nulo a la segunda: `return [msg, null];`.
  * Si es menor o igual, se invierten las posiciones: `return [null, msg];`. Esto permite conmutar cargas y alertas dinámicamente.
* **Código JavaScript Interno:**
  ```javascript
  var sum = msg.payload.num1 + msg.payload.num2;
  msg.payload = {
      resultado: sum,
      detalle: "Cálculo de dos salidas"
  };

  if (sum > 50) {
      return [msg, null]; // Se propaga por el borne superior (Salida 1)
  } else {
      return [null, msg]; // Se propaga por el borne inferior (Salida 2)
  }
  ```

---

## 📦 2. Código de Configuración del Flujo (Formato JSON)

Para importar estos ejercicios directamente en su servidor Node-RED, vaya al menú de hamburguesa en la esquina superior derecha, seleccione **Import** y pegue el siguiente bloque de datos. *Recuerde que para guardarlo localmente puede copiar esta estructura a un archivo de texto plano con extensión `.txt`.*

```json
[
  {
    "id": "tab_ejercicios_function",
    "type": "tab",
    "label": "Ejercicios Nodo Function",
    "disabled": false,
    "info": "Flows para resolver los ejercicios a, b y c utilizando el nodo Function."
  },
  {
    "id": "inject_a",
    "type": "inject",
    "z": "tab_ejercicios_function",
    "name": "Inyectar Números (20 y 15)",
    "props": [{ "p": "payload" }],
    "repeat": "",
    "crontab": "",
    "once": false,
    "onceDelay": 0.1,
    "topic": "",
    "payload": "{\"num1\":20,\"num2\":15}",
    "payloadType": "json",
    "x": 180,
    "y": 100,
    "wires": [["func_a"]]
  },
  {
    "id": "func_a",
    "type": "function",
    "z": "tab_ejercicios_function",
    "name": "Suma Simple",
    "func": "msg.payload = msg.payload.num1 + msg.payload.num2;\nreturn msg;",
    "outputs": 1,
    "timeout": 0,
    "noerr": 0,
    "initialize": "",
    "finalize": "",
    "libs": [],
    "x": 410,
    "y": 100,
    "wires": [["debug_a"]]
  },
  {
    "id": "debug_a",
    "type": "debug",
    "z": "tab_ejercicios_function",
    "name": "Resultado Suma A",
    "active": true,
    "tosidebar": true,
    "console": false,
    "tostatus": false,
    "complete": "payload",
    "targetType": "msg",
    "statusVal": "",
    "statusType": "auto",
    "x": 630,
    "y": 100,
    "wires": []
  },
  {
    "id": "inject_b_true",
    "type": "inject",
    "z": "tab_ejercicios_function",
    "name": "Suma > 50 (40 y 25)",
    "props": [{ "p": "payload" }],
    "repeat": "",
    "crontab": "",
    "once": false,
    "onceDelay": 0.1,
    "topic": "",
    "payload": "{\"num1\":40,\"num2\":25}",
    "payloadType": "json",
    "x": 170,
    "y": 200,
    "wires": [["func_b"]]
  },
  {
    "id": "inject_b_false",
    "type": "inject",
    "z": "tab_ejercicios_function",
    "name": "Suma <= 50 (10 y 15)",
    "props": [{ "p": "payload" }],
    "repeat": "",
    "crontab": "",
    "once": false,
    "onceDelay": 0.1,
    "topic": "",
    "payload": "{\"num1\":10,\"num2\":15}",
    "payloadType": "json",
    "x": 170,
    "y": 240,
    "wires": [["func_b"]]
  },
  {
    "id": "func_b",
    "type": "function",
    "z": "tab_ejercicios_function",
    "name": "Filtrar > 50",
    "func": "var sum = msg.payload.num1 + msg.payload.num2;\nif (sum > 50) {\n msg.payload = \"Resultado mayor a 50: \" + sum;\n return msg;\n} else {\n return null;\n}",
    "outputs": 1,
    "timeout": 0,
    "noerr": 0,
    "initialize": "",
    "finalize": "",
    "libs": [],
    "x": 410,
    "y": 220,
    "wires": [["debug_b"]]
  },
  {
    "id": "debug_b",
    "type": "debug",
    "z": "tab_ejercicios_function",
    "name": "Resultado B (>50)",
    "active": true,
    "tosidebar": true,
    "console": false,
    "tostatus": false,
    "complete": "payload",
    "targetType": "msg",
    "statusVal": "",
    "statusType": "auto",
    "x": 630,
    "y": 220,
    "wires": []
  },
  {
    "id": "inject_c",
    "type": "inject",
    "z": "tab_ejercicios_function",
    "name": "Inyectar Datos (Prueba ambas)",
    "props": [{ "p": "payload" }],
    "repeat": "",
    "crontab": "",
    "once": false,
    "onceDelay": 0.1,
    "topic": "",
    "payload": "{\"num1\":30,\"num2\":30}",
    "payloadType": "json",
    "x": 170,
    "y": 360,
    "wires": [["func_c"]]
  },
  {
    "id": "func_c",
    "type": "function",
    "z": "tab_ejercicios_function",
    "name": "Dos Salidas (Condicional)",
    "func": "var sum = msg.payload.num1 + msg.payload.num2;\nmsg.payload = {\n resultado: sum,\n detalle: \"Cálculo de dos salidas\"\n};\n\nif (sum > 50) {\n return [msg, null];\n} else {\n return [null, msg];\n}",
    "outputs": 2,
    "timeout": 0,
    "noerr": 0,
    "initialize": "",
    "finalize": "",
    "libs": [],
    "x": 430,
    "y": 360,
    "wires": [["debug_c_alta"], ["debug_c_baja"]]
  },
  {
    "id": "debug_c_alta",
    "type": "debug",
    "z": "tab_ejercicios_function",
    "name": "Salida 1: Mayor a 50",
    "active": true,
    "tosidebar": true,
    "console": false,
    "tostatus": false,
    "complete": "payload",
    "targetType": "msg",
    "statusVal": "",
    "statusType": "auto",
    "x": 660,
    "y": 340,
    "wires": []
  },
  {
    "id": "debug_c_baja",
    "type": "debug",
    "z": "tab_ejercicios_function",
    "name": "Salida 2: Menor o igual a 50",
    "active": true,
    "tosidebar": true,
    "console": false,
    "tostatus": false,
    "complete": "payload",
    "targetType": "msg",
    "statusVal": "",
    "statusType": "auto",
    "x": 680,
    "y": 380,
    "wires": []
  }
]
```

---

## 🌐 3. Auditoría de Instalación: Bibliotecas de Nodos Online

Se procedió a validar e instalar de forma online las librerías periféricas a través del Gestor de Paletas (*Manage Palette*) o mediante la terminal usando comandos `npm install`.

### 📋 Estado de Disponibilidad de Módulos:
1. **`node-red-contrib-fs` (📁 Archivos locales):** **Disponible.** Facilita la interacción directa con el sistema de archivos del servidor (lectura, escritura y monitoreo de directorios).
2. **`node-red-contrib-modbus` (📡 Comunicación Industrial):** **Disponible.** Bloque maestro indispensable para adquirir variables analíticas de PLCs y controladores de campo vía Modbus TCP/RTU.
3. **`node-red-contrib-s7` (🏭 Integración Siemens):** **Disponible.** Conectividad nativa por Ethernet hacia PLCs de las familias Siemens S7-300, S7-1200 y S7-1500.
4. **`node-red-contrib-telegrambot` (🤖 Alertas Telegram):** **Disponible.** Habilita el envío automático de telemetría y alarmas críticas y la recepción de comandos remotos mediante un bot interactivo.
5. **`node-red-contrib-whatsapp-cmb` (💬 Mensajería WhatsApp):** **Disponible.** Integración simplificada con la API de *CallMeBot* para notificar incidencias técnicas directamente a grupos de soporte.
6. **`node-red-node-email` (✉️ Protocolos SMTP/IMAP):** **Disponible.** Módulo nativo oficial para despachar reportes adjuntos o correos electrónicos ante fallas operativas de severidad alta.
7. **`@flowfuse/node-red-dashboard` (📊 HMI de Nueva Generación):** **Disponible.** La nueva paleta oficial que reemplaza al dashboard clásico v1, proporcionando componentes responsivos ideales para interfaces gráficas industriales.

### ⚠️ Reporte de Inconvenientes Técnicos Detectados:
Durante el proceso de instalación online, se deben prever los siguientes puntos críticos para asegurar la consistencia del entorno:
* **Dependencias del Sistema Operativo en Modbus y S7:** Módulos avanzados como `node-red-contrib-modbus` compilan paquetes binarios de NodeJS en segundo plano. Si el servidor no posee instalado las herramientas de compilación (`build-essential` en Linux o Python/Visual Studio Build Tools en Windows), la instalación por interfaz gráfica fallará.
* **Permisos de Escritura en el Directorio `node_modules`:** Al utilizar plataformas contenerizadas como **Docker**, es común experimentar errores de acceso denegado (`EACCES`). Se soluciona ingresando a la consola del contenedor y ejecutando la instalación con privilegios de usuario (`npm install --unsafe-perm`).
* **Conflictos del Dashboard:** Al instalar `@flowfuse/node-red-dashboard`, es mandatario no tener flujos activos que dependan de la biblioteca obsoleta `node-red-dashboard` para evitar solapamientos en las rutas del servidor web local (`/ui`).

## 🔍 Errores corregidos:

* Comillas sin escapar en cadenas JSON: En los campos "payload", había un string JSON anidado dentro de otro string sin escapar (por ejemplo: "{"num1":20}"). Para corregirlo, se deben añadir barras invertidas a las comillas internas `("{\"num1\":20}")`.

* Saltos de línea en strings (\n): En los campos "func", el código JavaScript tenía saltos de línea literales. En el formato estandarizado de JSON, las cadenas deben ir en una sola línea y los saltos de línea deben representarse explícitamente con el caracter de escape `\n`.
