# 🛠️ Guía de Comandos Esenciales: Contenedores y Máquinas Virtuales

Esta guía recopila los comandos más importantes para administrar los ciclos de vida, redes, almacenamiento y respaldos en entornos virtuales.

---

## 🐳 Comandos Esenciales para Docker (Contenedores)

### 🏃 de Ejecución y Ciclo de Vida

* **`docker run`**: Crea y arranca un contenedor nuevo a partir de una imagen.
* *Ejemplo:* `docker run -d -p 1880:1880 --name mi_nodered nodered/node-red` *(Corre Node-RED en segundo plano y mapea el puerto 1880)*.


* **`docker ps`**: Lista los contenedores que están activos en el sistema.
* *Ejemplo:* `docker ps -a` *(Muestra todos los contenedores, incluidos los que están apagados o detenidos)*.


* **`docker stop`**: Detiene la ejecución de un contenedor de manera ordenada.
* *Ejemplo:* `docker stop mi_nodered` *(Detiene el contenedor llamado mi_nodered)*.


* **`docker start`**: Vuelve a encender un contenedor existente que estaba detenido.
* *Ejemplo:* `docker start mi_nodered` *(Reanuda el contenedor sin perder su configuración previa)*.


* **`docker rm`**: Elimina definitivamente un contenedor del sistema.
* *Ejemplo:* `docker rm mi_nodered` *(El contenedor debe estar detenido antes de borrarlo)*.



### 🔍 Inspección y Diagnóstico

* **`docker exec`**: Permite ejecutar un comando dentro de un contenedor que ya está activo (ideal para abrir una consola interna).
* *Ejemplo:* `docker exec -it mi_nodered /bin/bash` *(Abre una terminal interactiva dentro del contenedor)*.


* **`docker logs`**: Muestra la salida estándar y los registros de eventos generados por la aplicación.
* *Ejemplo:* `docker logs --tail 50 mi_nodered` *(Muestra las últimas 50 líneas de log del contenedor)*.


* **`docker inspect`**: Devuelve toda la información técnica detallada de un contenedor o imagen en formato JSON (IPs, rutas, volúmenes).
* *Ejemplo:* `docker inspect mi_nodered`



### 📦 Respaldos, Imágenes y Transferencia

* **`docker commit`**: Toma los cambios realizados en un contenedor y genera una nueva imagen local (un snapshot de contenedor).
* *Ejemplo:* `sudo docker commit mi_nodered minored_backup` *(Crea una copia de seguridad como imagen)*.


* **`docker images`**: Muestra el listado de todas las imágenes que tienes descargadas o creadas localmente.
* *Ejemplo:* `docker images`


* **`docker rmi`**: Borra una imagen del disco local.
* *Ejemplo:* `docker rmi minored_backup`


* **`docker export`**: Empaqueta el sistema de archivos de un contenedor en un archivo comprimido `.tar`.
* *Ejemplo:* `docker export mi_nodered > respaldo_nodered.tar` *(Útil para transferir el contenedor a otra máquina)*.


* **`docker import`**: Crea una imagen de Docker a partir del archivo plano `.tar` exportado.
* *Ejemplo:* `docker import respaldo_nodered.tar mi_nueva_imagen:v1`



---

## 🖥️ Comandos Esenciales para VirtualBox (MVs vía CLI)

Aunque las Máquinas Virtuales suelen usarse con interfaz gráfica, la herramienta de comandos `VBoxManage` de VirtualBox es vital para automatizar laboratorios y servidores sin entorno gráfico.

### 🏃 Gestión y Control de MVs

* **`VBoxManage list`**: Lista los elementos virtuales registrados en el sistema.
* *Ejemplo:* `VBoxManage list vms` *(Muestra el nombre e ID de todas tus MVs)* o `VBoxManage list runningvms` *(Solo las encendidas)*.


* **`VBoxManage startvm`**: Enciende una máquina virtual.
* *Ejemplo:* `VBoxManage startvm "Ubuntu-Server" --type headless` *(Enciende la MV en segundo plano, sin abrir la ventana de interfaz gráfica)*.


* **`VBoxManage controlvm`**: Modifica el estado de energía de una máquina en tiempo real (apagar, pausar, resetear).
* *Ejemplo 1:* `VBoxManage controlvm "Ubuntu-Server" pause` *(Congela la CPU de la MV manteniendo la RAM)*.
* *Ejemplo 2:* `VBoxManage controlvm "Ubuntu-Server" resume` *(Reactiva la MV pausada)*.
* *Ejemplo 3:* `VBoxManage controlvm "Ubuntu-Server" acpipowerbutton` *(Apagado seguro por software)*.



### 📸 Respaldos e Instantáneas (Snapshots)

* **`VBoxManage snapshot`**: Gestiona las instantáneas de una máquina virtual para guardar o restaurar estados de forma rápida.
* *Ejemplo 1 (Crear):* `VBoxManage snapshot "Ubuntu-Server" take "AntesDeActualizar"` *(Toma un snapshot)*.
* *Ejemplo 2 (Restaurar):* `VBoxManage snapshot "Ubuntu-Server" restore "AntesDeActualizar"` *(Vuelve atrás en el tiempo tras un error)*.



### 🎛️ Modificación de Recursos de Hardware

* **`VBoxManage modifyvm`**: Cambia la configuración física asignada a la máquina virtual (debe estar apagada).
* *Ejemplo:* `VBoxManage modifyvm "Ubuntu-Server" --cpus 4 --memory 4096` *(Asigna 4 núcleos de CPU y 4GB de RAM de forma dinámica)*.



---

### 📝 Resumen de Bolsillo

> 💡 **Regla de oro:** Usa **Docker** cuando necesites levantar servicios ligeros y aislados rápidamente compartiendo el kernel (`docker run`). Usa **VBoxManage** cuando necesites automatizar o controlar sistemas operativos completos con aislamiento total de hardware (`VBoxManage startvm`).
