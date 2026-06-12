# ☁️ Guía de Configuración de Máquinas Virtuales (VM)

## 1. Definición de Recursos (Sizing)
* **CPU y RAM:** Evalúa el peso de tu dashboard. Una aplicación de análisis de datos intensivo requiere más memoria que una interfaz de visualización simple.
* **Almacenamiento:** Configura el disco virtual asegurando espacio suficiente para el sistema operativo, las librerías de Python y el historial de datos.

## 2. Configuración de Red y Acceso
* **Reglas de Firewall:** Es crítico abrir los puertos necesarios (usualmente el puerto 80/443 para tráfico web o un puerto personalizado como el 8050 para Dash).
* **Direccionamiento IP:** Asigna una IP estática si necesitas que el dashboard tenga una dirección permanente y pública.

## 3. Preparación del Sistema Operativo
Una vez creada la VM, el procedimiento estándar es:
1.  **Actualización:** `sudo apt update && sudo apt upgrade` para asegurar parches de seguridad.
2.  **Instalación de Python y venv:** Asegurar un entorno aislado para las librerías del proyecto.
3.  **Servidor WSGI:** Instalar `gunicorn` o `nginx` para gestionar la concurrencia de usuarios.

## 4. Despliegue del Proyecto
* **Clonación:** Utiliza Git para bajar tu repositorio de código a la VM.
* **Instalación:** Ejecuta `pip install -r requirements.txt`.
* **Automatización:** Configura servicios (como `systemd`) para que tu dashboard inicie automáticamente cuando la máquina virtual se reinicie.

La configuración de máquinas virtuales (VM) es el proceso fundamental para implementar infraestructuras en la nube. A diferencia de un entorno local, una máquina virtual te permite aislar recursos, escalar según la demanda y garantizar que tu entorno de desarrollo o producción sea idéntico en cualquier lugar 🖥️.

### 📝 Resumen Analítico

Las imágenes detallan el procedimiento para preparar una infraestructura robusta. Los puntos clave identificados son:

* **Virtualización de Hardware:** Se define la capacidad de procesamiento (CPU) y memoria RAM, permitiendo optimizar el rendimiento de la aplicación según sus necesidades reales.
* **Gestión de Redes:** La configuración de puertos y direcciones IP es vital para que tu dashboard sea accesible desde el exterior (hacia internet) de forma segura.
* **Entorno Operativo:** El proceso incluye la selección del sistema operativo (generalmente Linux) y la instalación de dependencias necesarias para que Python y el servidor web (como Gunicorn o Nginx) operen sin errores.
* **Escalabilidad:** Al ser una máquina virtual, los parámetros pueden modificarse posteriormente si el tráfico de tu aplicación aumenta, una ventaja clave de la computación en la nube.

### 💡 Nota importante

El procedimiento de configurar una máquina virtual de forma manual es excelente para aprender. Sin embargo, para entornos de producción, considera migrar hacia soluciones de **Infraestructura como Código (IaC)** como Terraform o plantillas de despliegue automatizado, lo que te permite recrear toda esta configuración con un solo comando en lugar de hacerlo paso a paso manualmente.

El despliegue de un **Gemelo Digital** en la nube requiere una configuración precisa de infraestructura para garantizar que la simulación (como el modelo de la turbina que analizamos anteriormente) corra de forma continua y accesible 🌐.

### 📝 Resumen Analítico

Las imágenes muestran el proceso detallado para pasar de una aplicación local a un entorno de producción en una Máquina Virtual (VM). Los procedimientos clave identificados son:

* **Aprovisionamiento de Infraestructura:** Selección del tamaño de la instancia (CPU/RAM) y sistema operativo (Linux).
* **Gestión de Seguridad:** Configuración de reglas de firewall (Security Groups) para exponer únicamente los puertos necesarios (ej. puerto 80/443 para web y 8050 para Dash).
* **Instalación del Entorno:** Preparación de un entorno de ejecución limpio mediante `venv` para aislar las librerías de Python.
* **Servidor de Producción:** Configuración de un servidor robusto (como Nginx o Gunicorn) que actúe como puente entre la red pública y tu aplicación Python.

# ☁️ Despliegue de Gemelo Digital en Máquina Virtual

## 1. Configuración de la Instancia (Sizing)
1. **Acceso al Proveedor:** Entrar a la consola de la nube (AWS, Azure, GCP, etc.).
2. **Selección de Imagen:** Elegir una distribución Linux (ej. Ubuntu Server LTS).
3. **Hardware:** Seleccionar el tamaño (Instance Type) según los requerimientos de cómputo del modelo PID de tu turbina.

## 2. Red y Seguridad (Connectivity)
* **IP Pública:** Asignar una dirección estática para que el dashboard sea localizable.
* **Firewall:** * Permitir tráfico **SSH (Port 22)** para gestión remota.
    * Permitir tráfico **HTTP/HTTPS (Port 80/443)** para el acceso público al dashboard.

## 3. Preparación del Entorno Python

```bash

# Actualización del sistema
sudo apt update && sudo apt upgrade -y

# Instalación de dependencias
sudo apt install python3-pip python3-venv -y

# Clonación del proyecto
git clone <url-de-tu-repositorio>
cd <proyecto>

# Creación de entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalación de librerías
pip install -r requirements.txt

```

## 4. Puesta en Producción con Gunicorn

Nunca usar `app.run()` directamente en producción. Se utiliza Gunicorn para gestionar las peticiones:

1. **Comando de inicio:** `gunicorn --workers 3 app:server`
2. **Persistencia:** Crear un servicio de `systemd` para que la aplicación se inicie automáticamente tras un reinicio de la máquina.

## 5. Monitoreo y Mantenimiento

* **Logs:** Revisar los logs del servidor para detectar fallos en la simulación o problemas de conexión del gemelo digital.

### 💡 Nota estratégica
La configuración reflejada en tus imágenes garantiza que el "Gemelo Digital" no sea solo un script ejecutándose en tu PC, sino un **servicio industrial** capaz de procesar los datos del modelo de la turbina de forma persistente y segura.
