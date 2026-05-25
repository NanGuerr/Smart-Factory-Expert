## 📥 1. Comandos de Instalación 💻

### 🪟 En Windows
Para realizar una instalación global en entornos Windows a través de la terminal (CMD o PowerShell con permisos de Administrador):

```bash
Archivo guardado exitosamente como guia_instalacion_nodered.md
npm install -g node-red
```

### 🐧 En Linux

Para distribuciones generales de Linux, se requiere utilizar `sudo` junto con el flag `--unsafe-perm` para evitar errores de permisos al compilar módulos nativos:

```bash
sudo npm install -g --unsafe-perm node-red

```

### 🍓 En Sistemas basados en Debian / Raspberry Pi

Existe un script oficial optimizado que actualiza tanto Node.js como Node-RED de forma segura:

```bash
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)

```

---

## 🔒 2. Seguridad y Permisos del Archivo de Configuración 🛡️

Para prevenir modificaciones no autorizadas por parte de usuarios o procesos maliciosos en entornos Linux/OT, se recomienda transferir la propiedad del archivo de configuración `settings.js` al usuario **root**:

```bash
sudo chown root:root ~/.node-red/settings.js

```

*Nota: Asegúrate de configurar los parámetros por defecto de manera segura (`y` / `n` según tus políticas de acceso corporativo).*

---

## ⚙️ 3. Comandos de Gestión y Ciclo de Vida 🔄

El control del flujo y servicio de Node-RED varía según la plataforma sobre la que esté corriendo:

### 🪟 Operación en Windows (Consola Interactiva)

* 🟢 **Iniciar ejecución:**
* 
```bash
node-red

```

* 🛑 **Detener ejecución:** Presionar la combinación de teclas: `Ctrl + C`

### 🐧 Operación en Linux / Raspberry Pi (Servicio en Segundo Plano)

En entornos Linux, Node-RED se administra típicamente como un servicio de sistema para garantizar su persistencia y disponibilidad:

* 🟢 **`node-red-start`** Inicia la ejecución de Node-RED como un servicio daemonizado en segundo plano.
* 🛑 **`node-red-stop`** Detiene de forma segura el servicio activo de Node-RED.
* ⚡ **`node-red-restart`** Detiene y reinicia de manera inmediata la instancia de Node-RED (útil tras aplicar cambios estructurales).
* 📋 **`node-red-log`** Muestra el volcado de registros (logs) en tiempo real para tareas de auditoría y diagnóstico de errores en los nodos o flujos.
