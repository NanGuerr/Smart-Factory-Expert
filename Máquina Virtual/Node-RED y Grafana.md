# Operaciones: Docker, Node-RED y Grafana 🐳⚙️

Este documento resume las actividades técnicas realizadas en el entorno de línea de comandos, centradas en la gestión de contenedores con **Docker** en una máquina virtual.

## 1. Operaciones con Docker y Node-RED 📦
Se llevaron a cabo los siguientes pasos para desplegar y gestionar contenedores:
* **Despliegue de Node-RED:** Se utilizó el comando `sudo docker run -it -p 1880:1880 -v node_red_data:/data --name mynodered nodered/node-red`.
* **Proceso de ejecución:** El contenedor inició correctamente, configurando la persistencia de datos en `/data` y exponiendo el puerto 1880.
* **Logs del sistema:** Durante el inicio, se observó que el servidor Node-RED se ejecutaba exitosamente, aunque se detectó un aviso (*warning*) sobre la falta de credenciales cifradas, sugiriendo la configuración de un `credentialSecret` para mayor seguridad.
* **Gestión de procesos:** Se realizaron verificaciones mediante `sudo docker ps -a` para monitorear el estado de los contenedores (ejecutándose o detenidos).

## 2. Despliegue de Grafana 📊
Se intentó desplegar una instancia de Grafana Enterprise:
* **Comando:** `sudo docker run -d -p 80:3000 --name=grafana grafana/grafana-enterprise`.
* **Proceso:** Docker procedió a descargar la imagen (`pull complete`) al no encontrarla localmente. Una vez finalizada la descarga, el contenedor se inició exitosamente en el puerto 80 del host.

## 3. Gestión de Permisos y Firewall 🛡️
* **Permisos del Daemon:** Se presentaron errores de "permission denied" al intentar conectar con el socket de Docker (`/var/run/docker.sock`). Este inconveniente se resolvió utilizando `sudo` para ejecutar los comandos con privilegios elevados.
* **Seguridad en la Nube:** Se visualizó la consola de **Google Cloud (Network Security)**, mostrando la gestión de reglas de firewall para controlar el tráfico de entrada y salida (*ingress/egress*) en la VPC.

---
*Resumen técnico basado en el registro de actividades de despliegue.*

# Seguridad, Despliegue y Visualización 🛡️📊

Este informe resume la información educativa sobre vulnerabilidades y las actividades técnicas de despliegue de servicios en la nube.

## 1. Gestión de Vulnerabilidades 🛡️
Las vulnerabilidades en sistemas, particularmente los industriales, se derivan de:
* **Configuraciones deficientes:** Falta de prácticas de seguridad y persistencia de contraseñas por defecto.
* **Acceso remoto inseguro:** Conexiones mal protegidas.
* **Dependencias:** Uso de bibliotecas y marcos de trabajo de terceros no auditados.
* **Mitigación:** La actualización constante de software, firmware y sistemas operativos es crítica para parchear brechas conocidas y añadir nuevas funciones de seguridad frente a amenazas emergentes.

## 2. Implementación de Servicios (Docker) 🐳
Se documentó el uso de Docker para desplegar aplicaciones:
* **Node-RED:** Desplegado mediante el comando `docker run`. Se destaca la importancia de configurar un `credentialSecret` para la seguridad de las credenciales, ya que el sistema detectó su ausencia.
* **Grafana:** Instalación exitosa de Grafana Enterprise en el puerto 80 del host.

## 3. Seguridad de Red y Visualización 🌐📈
* **Firewall (Google Cloud):** Se configuraron reglas específicas de entrada (*ingress*) y salida (*egress*) para permitir el tráfico en el puerto 80, esencial para la operatividad de Grafana.
* **Visualización:** Se muestra un dashboard de Grafana con una serie temporal ("A-series"), confirmando que el servicio es capaz de recolectar y graficar datos correctamente tras su configuración de red.

---
*Resumen generado a partir de material educativo técnico.*
