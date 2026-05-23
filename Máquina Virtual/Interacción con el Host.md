# 🔄 Sistema Operativo Host (VIR-0217 - 0220)

Este módulo se enfoca en cómo conectar y hacer interactuar un contenedor aislado con el sistema operativo de la máquina anfitriona (*host*), permitiendo el intercambio de archivos, la persistencia de datos y la exposición de servicios. 🖥️🔌📂

---

### 📌 Mecanismos de Interacción Principales

* **🔌 Mapeo de Puertos (Port Mapping):**
    * **¿Cómo funciona?:** Se utiliza la bandera `-p [Puerto_Host]:[Puerto_Contenedor]` (por ejemplo, `-p 8080:80`).
    * **Propósito:** Permite enlazar un puerto de la máquina física con un puerto interno del contenedor. De esta forma, cualquier solicitud que llegue al host a través de ese puerto será redirigida automáticamente al servicio dentro del contenedor, haciéndolo accesible desde la red local o Internet.

* **📁 Montajes de Volúmenes y Carpetas (Bind Mounts):**
    * **¿Cómo funciona?:** Se utiliza habitualmente la bandera `-v [Ruta_Host]:[Ruta_Contenedor]`.
    * **Propósito:** Vincula de forma directa un directorio físico de tu computadora con un directorio interno del contenedor. Si modificas un archivo en tu máquina, el cambio se refleja instantáneamente dentro del contenedor (y viceversa). Es la técnica esencial para el desarrollo de software en tiempo real.

* **⚙️ Compartición de Variables de Entorno:**
    * **¿Cómo funciona?:** Se inyectan configuraciones usando la bandera `-e NOMBRE_VARIABLE=valor`.
    * **Propósito:** Permite pasar datos dinámicos desde el sistema host hacia el contenedor en el momento de su ejecución (como credenciales de bases de datos, configuraciones de idioma o llaves de API), evitando tener que escribir datos sensibles directamente en el código del contenedor.

* **🧠 Recursos Compartidos (Límites de Hardware):**
    * El módulo analiza cómo el contenedor interactúa de forma nativa con los recursos del host. A diferencia de una VM que reserva RAM de forma estricta, un contenedor consume los recursos de la CPU y la memoria del host bajo demanda, a menos que se le configuren limitadores específicos en la interacción.

---

### 📝 Nota

💡 Aprender a gestionar la interacción con el sistema host es lo que transforma a los contenedores de simples cajas aisladas en herramientas útiles para flujos de trabajo reales, permitiéndote programar en tu sistema operativo favorito mientras tu código se ejecuta dentro del contenedor. 🚀

# 📦 Gestión de Contenedores, Backup y Transferencia (VIR-0218)

Este módulo se centra en las operaciones de administración avanzadas para controlar el ciclo de vida de los contenedores, crear copias de seguridad de sus estados actuales y exportarlos para transferirlos a otros servidores o entornos. 🗄️🔄🚚

---

### 📌 Puntos Clave de la Gestión y Respaldo

* **🎛️ Comandos de Gestión del Ciclo de Vida:**
    * **`docker ps -a`:** Permite auditar todos los contenedores del sistema, tanto los que están activos como los que se han detenido.
    * **`docker stop` / `docker start`:** Detener de forma segura el proceso del contenedor o volver a levantarlo manteniendo su configuración original.
    * **`docker rm`:** Eliminación definitiva de contenedores que ya no son necesarios para liberar recursos.

* **📸 Creación de Backups mediante Instantáneas (`docker commit`):**
    * **¿Cómo funciona?:** Toma un contenedor modificado que está en ejecución (por ejemplo, uno donde instalaste herramientas adicionales) y lo convierte en una **nueva imagen local**.
    * **Propósito:** Funciona de forma similar a un snapshot en MVs. Permite congelar el estado exacto de la aplicación en un punto del tiempo para crear réplicas idénticas en el futuro.

* **🚚 Transferencia de Contenedores (Exportar e Importar):**
    * El módulo detalla cómo empaquetar contenedores sin depender de un registro en la nube (como Docker Hub), usando dos comandos clave:
    * **`docker export`:** Toma el sistema de archivos de un contenedor y lo empaqueta en un archivo comprimido plano (`.tar`). Es ideal para clonar la estructura actual del contenedor.
    * **`docker import`:** Toma ese archivo `.tar` en cualquier otra máquina (con Docker instalado) y reconstruye la imagen al instante para poder ejecutarla.

* **💾 Respaldos de Volúmenes de Datos (Data Backups):**
    * Recordatorio de que el código de la aplicación se almacena en el contenedor, pero los datos persistentes viven en los volúmenes. Se enseñan técnicas para empaquetar los directorios de datos en archivos comprimidos para guardias de seguridad o migraciones de bases de datos.

---

### 📝 Nota

💡 Dominar la exportación e importación manual es una habilidad invaluable para administradores de sistemas. Te permite mover infraestructuras completas en un "pendrive" o a través de redes cerradas (entornos *air-gapped*) donde no hay acceso a Internet para descargar imágenes. 🚀

# 🐚 Acceso a Contenedores desde Consola (VIR-0219)

Este módulo se enfoca en las técnicas y comandos esenciales para abrir una línea de comandos (*shell*) dentro de un contenedor en ejecución, permitiendo realizar tareas de diagnóstico, auditoría y administración directa. 💻⚡🛠️

---

### 📌 El Comando Estrella: `docker exec`

A diferencia de `docker run` (que crea un contenedor nuevo desde cero), el comando clave en este módulo es **`docker exec`**, diseñado para ejecutar un nuevo proceso dentro de un contenedor que ya está corriendo.

* **💻 Sintaxis Común:** 

```bash
  docker exec -it [ID_o_Nombre_Contenedor] /bin/bash
```

# 🏭 Servicios en Contenedores para la Industria 4.0 (VIR-0220)

Este módulo práctico presenta una selección de las herramientas y plataformas más potentes y utilizadas en el ecosistema de la **Industria 4.0 (I4.0)** y el **IIoT**, detallando sus funciones y sus imágenes oficiales en Docker Hub para su despliegue inmediato. 📊🔌⚙️

---

### 🛠️ Ecosistema de Contenedores para I4.0

* **🟢 Node-RED (Integración y Flujos):**
    * **Descripción:** Plataforma de programación visual basada en flujos, ideal para conectar dispositivos de hardware, APIs y servicios en línea de forma ágil.
    * **Imagen en Docker Hub:** `nodered/node-red`

* **🚀 EMQX (Mensajería MQTT de Alta Disponibilidad):**
    * **Descripción:** Un broker MQTT empresarial, masivamente escalable y de alto rendimiento, diseñado para conectar millones de dispositivos IoT simultáneos.
    * **Imagen en Docker Hub:** `emqx/emqx`

* **💾 InfluxDB (Almacenamiento de Métricas):**
    * **Descripción:** Base de datos de series temporales (*Time Series Database*), optimizada específicamente para almacenar y consultar métricas, eventos y datos con marcas de tiempo provenientes de sensores industriales.
    * **Imagen en Docker Hub:** `influxdb`

* **📊 Grafana (Visualización y Analítica):**
    * **Descripción:** La herramienta reina para la creación de tableros (*dashboards*) interactivos. Permite consultar, visualizar y alertar sobre métricas sin importar dónde estén almacenadas (se conecta nativamente con InfluxDB).
    * **Imagen en Docker Hub:** `grafana/grafana`

* **🦟 Mosquitto (Broker MQTT Ligero):**
    * **Descripción:** Un broker de mensajería que implementa el protocolo MQTT. Es sumamente ligero y eficiente, ideal para servidores pequeños, computadoras embebidas (como Raspberry Pi) o redes de baja potencia.
    * **Imagen en Docker Hub:** `eclipse/mosquitto`

* **🏢 ThingsBoard (Plataforma IIoT Integral):**
    * **Descripción:** Plataforma de Internet de las Cosas Industrial de código abierto para la gestión de dispositivos, recopilación de datos, procesamiento y visualización a gran escala.
    * **Imagen en Docker Hub:** `thingsboard/tb-postgres`

* **🛡️ Conpot (Seguridad Industrial):**
    * **Descripción:** Un *Honeypot* (sistema trampa) diseñado para simular sistemas de control industrial (SCADA) e infraestructuras críticas, con el fin de registrar, analizar y desviar ataques informáticos dirigidos a fábricas.
    * **Imagen en Docker Hub:** `honeynet/conpot`

---

### 📝 Nota (La combinación ganadora)

💡 En proyectos reales de IoT e Industria 4.0, es sumamente común ver estos contenedores trabajando juntos en un mismo servidor. Una arquitectura clásica (llamada el *Stack TIG* o variaciones) consiste en usar **Mosquitto/EMQX** para recibir los datos de los sensores, **Node-RED** para procesar y limpiar esos datos, **InfluxDB** para guardarlos históricamente y **Grafana** para mostrárselos al operador en una pantalla. ¡Docker hace que montar todo esto tome segundos! 🚀
