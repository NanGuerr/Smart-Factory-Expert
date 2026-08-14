# ⚙️ Control de Motor HMI en Node-RED Dashboard

Este proyecto permite la creación de una interfaz HMI (*Human-Machine Interface*) interactiva en Node-RED para el control y monitoreo en tiempo real del estado de un motor industrial.

---

## 📋 Requisitos Mínimos Cumplidos

* 🖼️ **Imagen representativa del motor:** Visualización del equipo en la interfaz gráfica.
* 🔘 **Botones de control:** Comandos táctiles para **INICIAR** (Encendido) y **DETENER** (Apagado).
* 🚥 **LED de estado dinámico:** Indicador visual en vivo para reflejar el estado operativo actual (Verde = Activo / Rojo = Detenido).

---

## 🎨 Estructura del Panel Visual


```

---

|              🏭 Panel de Motor Principal            |
|***|
|                                                     |
|                  🖼️ [Imagen Motor]                   |
|                                                     |
|***|
|                         |                           |
|      🟢 [ INICIAR ]     |      🔴 [ DETENER ]       |
|***|*****|
|                                                     |
|                🚥 [ LED de Estado ]                 |
|**___________________________________________________|

```

---

## 📦 Código JSON del Flujo (Node-RED)

Copia y pega el siguiente código en la opción **Importar** de Node-RED para desplegar el flujo completo:

```json
[
    {
        "id": "tab_motor",
        "type": "ui_tab",
        "name": "Control de Planta",
        "icon": "dashboard",
        "disabled": false,
        "hidden": false
    },
    {
        "id": "group_motor",
        "type": "ui_group",
        "name": "Panel de Motor Principal",
        "tab": "tab_motor",
        "order": 1,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "btn_start",
        "type": "ui_button",
        "z": "flow_hmi_motor",
        "name": "INICIAR",
        "group": "group_motor",
        "order": 2,
        "width": 3,
        "height": 1,
        "passthru": false,
        "label": "INICIAR",
        "tooltip": "",
        "color": "white",
        "bgcolor": "#28a745",
        "className": "",
        "icon": "",
        "payload": "true",
        "payloadType": "bool",
        "topic": "motor/estado",
        "topicType": "str",
        "x": 240,
        "y": 180,
        "wires": [
            [
                "tpl_led"
            ]
        ]
    },
    {
        "id": "btn_stop",
        "type": "ui_button",
        "z": "flow_hmi_motor",
        "name": "DETENER",
        "group": "group_motor",
        "order": 3,
        "width": 3,
        "height": 1,
        "passthru": false,
        "label": "DETENER",
        "tooltip": "",
        "color": "white",
        "bgcolor": "#dc3545",
        "className": "",
        "icon": "",
        "payload": "false",
        "payloadType": "bool",
        "topic": "motor/estado",
        "topicType": "str",
        "x": 240,
        "y": 260,
        "wires": [
            [
                "tpl_led"
            ]
        ]
    },
    {
        "id": "tpl_image",
        "type": "ui_template",
        "z": "flow_hmi_motor",
        "group": "group_motor",
        "name": "Imagen del Motor",
        "order": 1,
        "width": 6,
        "height": 4,
        "format": "<div style=\"text-align: center;\">\n  <img src=\"[https://upload.wikimedia.org/wikipedia/commons/](https://upload.wikimedia.org/wikipedia/commons/) thumb/8/82/Electric_motor.jpg/640px-Electric_motor.jpg\" style=\"max-width: 100%; height: auto; border-radius: 8px;\">\n</div>",
        "storeOutMessages": true,
        "fwdInMessages": true,
        "reservesSpace": true,
        "templateScope": "local",
        "className": "",
        "x": 250,
        "y": 100,
        "wires": [
            []
        ]
    },
    {
        "id": "tpl_led",
        "type": "ui_template",
        "z": "flow_hmi_motor",
        "group": "group_motor",
        "name": "LED Estado Dinámico",
        "order": 4,
        "width": 6,
        "height": 3,
        "format": "<div style=\"text-align: center; padding: 10px;\">\n  <div style=\"width: 50px; height: 50px; border-radius: 50%; display: inline-block; background-color: {{msg.payload ? '#28a745' : '#dc3545'}}; box-shadow: 0 0 15px {{msg.payload ? '#28a745' : '#dc3545'}};\"></div>\n  <p style=\"margin-top: 10px; font-weight: bold;\">ESTADO: {{msg.payload ? 'MOTOR ENCENDIDO' : 'MOTOR DETENIDO'}}</p>\n</div>",
        "storeOutMessages": true,
        "fwdInMessages": true,
        "reservesSpace": true,
        "templateScope": "local",
        "className": "",
        "x": 480,
        "y": 220,
        "wires": [
            []
        ]
    }
]

```

---

## 🛠️ Pasos de Instalación

1. 📥 Abre tu instancia de **Node-RED**.
2. ↗️ Haz clic en el menú superior derecho y selecciona **Importar** (o `Ctrl + I`).
3. 📋 Pega el código JSON mostrado arriba dentro del cuadro de texto.
4. 🟢 Presiona el botón **Importar** y ubica el flujo en el lienzo.
5. 🚀 Presiona **Deploy** para aplicar los cambios.
6. 🌐 Accede a tu dashboard mediante la dirección `http://localhost:1880/ui` (o la IP correspondiente de tu servidor).
