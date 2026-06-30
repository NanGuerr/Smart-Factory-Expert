# 🌐 Activación y Diagnóstico con el Web Server (PLC Siemens)

El Web Server integrado convierte a tu PLC en un dispositivo con su propia página web de monitoreo, ideal para emergencias y diagnósticos rápidos sin necesidad de tener el software TIA Portal instalado en el PC de mantenimiento.

---

## ⚙️ 1. Configuración Hardware
Para habilitar esta función en TIA Portal, sigue estos pasos:

1.  **Acceso:** En la "Vista de dispositivos", haz clic derecho sobre el PLC y selecciona **Propiedades**.
2.  **Activación:** Dirígete a la sección **Web Server**. Marca la casilla **"Enable the use of the web server on all modules"**.
3.  **Seguridad:** Dependiendo de tu entorno de red, puedes destildar la casilla **"Permitir acceso solo vía HTTPS"** si necesitas acceso más flexible en redes locales cerradas (aunque por buenas prácticas se recomienda mantenerla activa en entornos productivos).
4.  **Gestión de Usuarios:** En la sección **"User management"**, crea los usuarios, asigna contraseñas robustas y, lo más importante, define el **nivel de acceso** otorgado (solo lectura, operador, administrador).

---

## 💻 2. Acceso y Navegación
* **Requisito:** El Web Server solo es accesible si estás conectado a un PLC físico.
* **Acceso:** Abre cualquier navegador web y escribe la dirección IP de tu PLC (ej. `192.168.1.12`).
* **Interfaz:** La navegación es intuitiva y similar a TIA Portal. Tendrás acceso a:
    * Visualización del estado del PLC.
    * Información detallada de módulos.
    * Alarmas del sistema.

---

## 🛠️ 3. Herramientas de Diagnóstico y Control
Desde el Web Server puedes realizar operaciones críticas en situaciones de emergencia:
* **Flashear luces:** Puedes identificar físicamente el PLC en el gabinete haciendo que sus LEDs parpadeen.
* **Diagnóstico:** Accede al **Diagnostic Buffer** (el registro de eventos) para identificar el origen de un error o paro de máquina.
* **Tag Status:** Permite visualizar y **modificar** variables del programa (requiere permiso de **Administrador**).
* **Herramientas avanzadas:** Puedes configurar tablas de observación y traces para capturar comportamientos de la máquina sin estar conectado con TIA Portal.

---

## ⚠️ 4. ¡Advertencia de Seguridad!
El Web Server no es solo informativo; es una ventana de control directo:
* **Riesgo:** Un usuario con nivel "Administrador" tiene la capacidad de modificar valores que podrían afectar el funcionamiento seguro de la máquina.
* **Prevención:** Asigna los privilegios de acceso con el principio de "mínimo privilegio necesario". No otorgues acceso administrativo si el personal solo necesita visualizar diagnósticos.
* **Control:** Trata al acceso web como una puerta de entrada crítica; mantén el control de quién tiene acceso a la red donde está el PLC.
