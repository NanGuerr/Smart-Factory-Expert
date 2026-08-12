# 🔗 Nodos Esenciales de Control, Flujo y Configuración en Node-RED

Esta guía recopila información clave sobre nodos fundamentales de control de flujo (*Delay*, *Trigger*, *Switch*, *Link*) y conceptos avanzados de configuración en Node-RED, complementado con la importancia de mantener pausas estratégicas para optimizar el aprendizaje. 🧠⚡

---

## 📚 El Valor de las Pausas en el Estudio
> Tomar descansos intencionales entre las sesiones de estudio es más que solo una pausa momentánea; es un enfoque estratégico para optimizar tu experiencia de aprendizaje. Al brindarte intervalos periódicos de descanso, le permites a tu cerebro recargarse, consolidar la información y mejorar tu rendimiento general. 🌿⏳

---

## 🎛️ Nodos Core y de Control en Node-RED

*   **🔗 Link Nodes (`link in` / `link out`):** 
    *   Permiten conectar flujos de manera virtual sin necesidad de trazar líneas físicas visibles entre los nodos, facilitando la organización de lienzos complejos en diferentes pestañas o áreas de trabajo. 🌐
    *   🔗 [FlowFuse Link Node Guide](https://flowfuse.com/node-red/core-nodes/link/) 📄

*   **⏱️ Delay Node:** 
    *   Sirve para retrasar la llegada de los mensajes por un tiempo determinado, limitar la tasa de envío (*rate limit*) o retrasar la salida según reglas lógicas. ⏳
    *   🔗 [FlowFuse Delay Node Guide](https://flowfuse.com/node-red/core-nodes/delay/) 📊

*   **⚡ Trigger Node:** 
    *   Actúa como un generador de pulsos o un temporizador avanzado que puede enviar un mensaje, esperar un tiempo, y opcionalmente enviar un segundo mensaje (ideal para reiniciar estados, enviar pulsos de *watchdog* o simular relés). ⏱️🔔
    *   🔗 [FlowFuse Trigger Node Guide](https://flowfuse.com/node-red/core-nodes/trigger/) ⚙️

*   **🔀 Switch Node:** 
    *   Permite enrutar los mensajes basándose en reglas condicionales aplicadas sobre propiedades específicas (como `msg.payload`), evaluando igualdades, rangos o expresiones regulares. 🔀🎯
    *   🔗 [Tech Explorations - Node-RED Range & Switch](https://techexplorations.com/guides/esp32/node-red-esp32-project/node-red-range/) 📐

---

## 🛠️ Configuración Global y Arquitectura

*   **🧩 Configuration Nodes (Nodos de Configuración):** 
    *   Son elementos invisibles en el lienzo principal pero vitales para almacenar parámetros compartidos (como credenciales de MQTT, conexiones Modbus o accesos a bases de datos) que múltiples nodos pueden reutilizar de forma centralizada. 🗂️🔒
    *   🔗 [Steve's Node-RED Guide - Configuration Nodes Overview](https://stevesnoderedguide.com/node-red-configuration-nodes-overview) 📚
