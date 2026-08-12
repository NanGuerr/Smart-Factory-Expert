## 🧠 Resumen de Node-RED: Working with Context

El **Contexto** en Node-RED es un mecanismo que permite almacenar y compartir información entre diferentes nodos sin necesidad de enviarla a través de los mensajes (`msg`) que circulan por los flujos.

### 🎯 Puntos Clave:

* **🔍 Alcances del Contexto (Scopes):**
* **Node (Nodo):** Los datos solo son visibles para el nodo específico que los creó.
* **Flow (Flujo):** Los datos se comparten entre todos los nodos que están en la misma pestaña o flujo.
* **Global:** Los datos son accesibles por cualquier nodo en toda la instancia de Node-RED.


* **💾 Almacenamiento (Stores):**
* Por defecto, el contexto se guarda **en memoria** (se borra si se reinicia Node-RED).
* Se puede configurar en el archivo `settings.js` para usar almacenamiento persistente en el **sistema de archivos** (`localfilesystem`) u otros módulos personalizados.


* **🛠️ Cómo se utiliza:**
* Se gestiona de forma sencilla mediante nodos como el **Change node**, escribiendo código JavaScript en nodos **Function** (`flow.get()` / `flow.set()`), o visualizándolo directamente desde la barra lateral de contexto (*Context Sidebar*) en el editor.
