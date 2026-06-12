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

