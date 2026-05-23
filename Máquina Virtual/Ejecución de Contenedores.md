# 📥 Resumen: Instalación de Contenedores (VIR-0215 - 0216)

Este módulo es de carácter práctico y se enfoca en preparar el entorno de trabajo mediante la instalación y configuración del motor de contenedores en los diferentes sistemas operativos principales. 💻🛠️🚀

---

### 📌 Puntos Clave de la Instalación

* **🐧 Instalación en Linux (Ubuntu/Debian):**
    * Se detalla el proceso recomendado a través de la terminal pública, actualizando el índice de paquetes (`apt-get update`).
    * Instalación de requisitos previos (como certificados `ca-certificates` y `curl`).
    * Adición de la clave GPG oficial y el repositorio de Docker para asegurar que se descargue la versión estable más reciente directamente del proveedor.
    * Instalación de los paquetes clave: `docker-ce` (Community Edition), `docker-ce-cli` y `containerd.io`.

* **🪟 Instalación en Windows y macOS (Docker Desktop):**
    * Uso de **Docker Desktop**, la aplicación de interfaz gráfica oficial.
    * **Requisito crítico en Windows:** Configuración y habilitación de **WSL 2** (Windows Subsystem for Linux), que permite a Docker correr contenedores de forma nativa sobre un kernel de Linux real dentro de Windows, garantizando la máxima velocidad y compatibilidad.

* **👥 Configuraciones Post-Instalación (Esencial en Linux):**
    * Gestión de permisos para evitar tener que usar el comando `sudo` antes de cada instrucción de Docker.
    * Creación del grupo `docker` y adición del usuario actual al grupo (`sudo usermod -aG docker $USER`), permitiendo una administración mucho más ágil y segura en el día a día.

* **🧪 Verificación del Entorno:**
    * Comprobación de que el demonio de Docker está activo y respondiendo mediante comandos de estado del sistema.
    * Ejecución del clásico contenedor de prueba:
```bash
      docker run hello-world
      ```
Este comando valida todo el ciclo básico: busca la imagen localmente, la descarga desde Docker Hub si no existe, crea el contenedor, lo ejecuta para mostrar un mensaje de éxito y finaliza.

---

### 📝 Nota

💡 Tener un entorno bien instalado y configurado sin depender de permisos de superusuario (`sudo`) en cada comando es el cimiento indispensable para trabajar de forma fluida y profesional en los siguientes módulos prácticos del curso. 🏁

# 🏃‍♂️ Tipos de Ejecución de Contenedores (VIR-0216)

Este módulo se centra en las diferentes modalidades para lanzar y ejecutar contenedores en Docker, permitiendo elegir si queremos interactuar directamente con ellos o dejarlos corriendo en segundo plano como servicios del sistema. 🖥️⚡🔄

---

### 📌 Los Modos de Ejecución Principales

* **📡 Modo Destacado o en Primer Plano (Attached Mode / Foreground):**
    * **¿Cómo funciona?:** Es el comportamiento por defecto de Docker si no se especifica lo contrario. La terminal actual se "engancha" al contenedor.
    * **Características:** Verás la salida estándar de la aplicación (logs) directamente en tu pantalla en tiempo real. Si cierras la terminal o presionas `Ctrl + C`, el proceso principal se detiene y el contenedor se apaga.
    * **Uso típico:** Tareas rápidas, scripts de automatización, compilaciones o cuando estás depurando (*debugging*) errores de arranque.

* **👤 Modo Interactivo (Interactive Mode):**
    * **¿Cómo funciona?:** Se ejecuta combinando las banderas `-i` (interactivo, mantiene `STDIN` abierto) y `-t` (asigna una pseudo-TTY o terminal virtual), típicamente usando `docker run -it`.
    * **Características:** Te permite "entrar" al contenedor y te otorga una línea de comandos (shell) dentro de él como si estuvieras usando SSH.
    * **Uso típico:** Explorar el sistema de archivos del contenedor, instalar paquetes manualmente para pruebas o realizar tareas de administración directa dentro del entorno aislado.

* **⚙️ Modo Desacoplado o en Segundo Plano (Detached Mode / Background):**
    * **¿Cómo funciona?:** Se ejecuta utilizando la bandera `-d` (`docker run -d`).
    * **Características:** El contenedor se inicia, Docker te devuelve el ID único del proceso en la terminal y te libera la consola inmediatamente. El contenedor sigue ejecutándose de forma silenciosa en segundo plano.
    * **Uso típico:** El 90% de las aplicaciones en producción, como servidores web (Nginx, Apache), bases de datos (PostgreSQL, MySQL) o APIs que deben prestar servicio continuo sin bloquear tu terminal.

---

### 🛠️ Comandos Esenciales Relacionados

* **`docker ps`:** Permite listar los contenedores que están activos y verificar en qué modo se encuentran operando.
* **`docker logs [ID_Contenedor]`:** Fundamental para ver qué está pasando dentro de un contenedor que corre en *Modo Desacoplado* sin necesidad de detenerlo.
* **`docker attach [ID_Contenedor]`:** Permite volver a enganchar tu terminal a un contenedor que se estaba ejecutando en segundo plano.

---

### 📝 Nota

💡 Dominar los tipos de ejecución te permite entender el ciclo de vida de un contenedor. Recuerda la regla de oro: un contenedor solo vivirá mientras el proceso principal que lo ejecuta en primer o segundo plano se mantenga activo. 🚀
