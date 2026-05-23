## 🗄️ Gestión de Almacenamiento y Volúmenes (Docker)

* **`docker volume ls`**: Lista todos los volúmenes de datos creados en Docker. Los volúmenes son esenciales para que la información de tus contenedores (como las bases de datos de InfluxDB o los flujos de Node-RED) no se borre al apagar el contenedor.
* *Ejemplo:* `docker volume ls` *(Muestra una tabla con los nombres de todos los volúmenes locales).*


* **`docker volume rm`**: Elimina un volumen de datos que ya no estés utilizando para liberar espacio en el disco duro.
* *Ejemplo:* `docker volume rm mi_volumen_datos` *(El contenedor asociado debe estar borrado antes de eliminar su volumen).*



---

## 📁 Comandos de Sistema y Permisos (Linux / Host)

Cuando trabajas con contenedores y montas carpetas del sistema anfitrión (usando *Bind Mounts* con `-v`), es muy común chocar con problemas de permisos de lectura y escritura. Aquí entran estos comandos del sistema operativo:

* **`mkdir` (Make Directory)**: Crea una nueva carpeta en el sistema de archivos del *host*. Se usa para preparar los directorios que luego vas a compartir con tus contenedores.
* *Ejemplo:* `mkdir -p /home/usuario/data/nodered` *(Crea la ruta de carpetas completa para guardar los datos de Node-RED).*


* **`chmod 777` (Change Mode)**: Otorga permisos totales de **Lectura (4), Escritura (2) y Ejecución (1)** a todos los usuarios del sistema (Dueño, Grupo y Otros: $4+2+1=7$).
* *Ejemplo:* `sudo chmod 777 /home/usuario/data/nodered`
* *⚠️ Nota de seguridad:* El uso de `777` abre por completo los permisos. En entornos de producción es una mala práctica; se prefiere usar permisos más restrictivos como `755` o `775` y cambiar el propietario con `chown`. Sin embargo, en laboratorios de desarrollo se usa frecuentemente de forma rápida para descartar que Docker esté fallando por bloqueos de permisos del sistema operativo.



---

## 🔄 Políticas de Reinicio Automático (Docker Flags)

Al crear un contenedor con `docker run`, puedes definir qué debe hacer Docker si el contenedor falla, si el proceso se detiene o si el servidor físico se reinicia por completo.

* **`--restart unless-stopped`**: Es una de las políticas de reinicio más utilizadas en producción e Industria 4.0. Le ordena a Docker que reinicie el contenedor automáticamente bajo cualquier circunstancia, **a menos que** el usuario lo haya detenido manualmente con el comando `docker stop`.
* *Ejemplo:* `docker run -d --name broker_mqtt -p 1883:1883 --restart unless-stopped eclipse/mosquitto`
* *¿Por qué es útil?:* Si tu servidor sufre un corte de energía y se apaga, en cuanto la máquina vuelva a encender, Docker se iniciará y levantará automáticamente tu broker Mosquitto sin que tengas que entrar a la terminal a escribir ningún comando. Si tú escribes `docker stop broker_mqtt`, se quedará apagado pacíficamente.



---

### 💡 Ejemplo de integración total en un solo flujo de trabajo:

Imagina que vas a montar un laboratorio persistente y resistente a fallos de energía para Node-RED:

```bash
# 1. Creas la carpeta en tu computadora física
mkdir -p /home/usuario/nodered_data

# 2. Le das permisos totales para que el usuario interno de Docker pueda escribir los flujos
sudo chmod 777 /home/usuario/nodered_data

# 3. Lanzas el contenedor asociando la carpeta física y aplicando el reinicio automático
docker run -d \
  -p 1880:1880 \
  --name mi_nodered_industrial \
  -v /home/usuario/nodered_data:/data \
  --restart unless-stopped \
  nodered/node-red

```
¡Qué gran aporte! Has tocado los comandos exactos que se utilizan para el empaquetado, la migración "en frío" (sin internet) y la extracción de datos desde el interior de los contenedores.

Hay un par de detalles en la sintaxis de los comandos que pusiste (errores comunes de dedo al escribir rápido en la consola); los he corregido y organizado en formato Markdown con emojis para que te queden perfectos y listos para tu manual de comandos:

---

## 🚚 Transferencia de Imágenes y Contenedores

* **`docker save`**: Toma una **imagen** de Docker de tu catálogo local y la exporta a un archivo comprimido plano `.tar`. Es ideal para llevarte tus entornos a servidores aislados sin conexión a internet.
* *Ejemplo corregido:* `docker save -o noderedbackup.tar minored_backup` *(Guarda la imagen modificada en un archivo llamado noderedbackup.tar).*


* **`docker load`**: Toma el archivo comprimido `.tar` generado por `docker save` y lo desempaqueta, integrándolo de nuevo al catálogo de **imágenes** locales de Docker en la nueva máquina.
* *Ejemplo:* `sudo docker load -i noderedbackup.tar` *(Importa la imagen lista para ser usada con `docker run`).*



---

## 🗜️ Copias de Seguridad con la herramienta `tar` (En el Host o en la VM)

El comando `tar` (Tape Archive) es el estándar en Linux para empaquetar y comprimir carpetas de datos (como la carpeta `/data` de tus contenedores).

* **`tar -cvf`**: Crea un nuevo archivo contenedor `.tar` (las banderas significan: **C**reate, **V**erbose, **F**ile).
* *Ejemplo corregido 1:* `tar -cvf backup_data_nodered.tar /data` *(Empaqueta todo el contenido de la carpeta `/data` en un archivo llamado backup_data_nodered.tar).*
* *Ejemplo corregido 2 (En carpeta temporal `/tmp`):* `tar -cvf /tmp/backup_data_nodered.tar /data` *(Crea el paquete de respaldo directamente dentro del directorio temporal del sistema).*



---

## 🔄 Copia de Archivos entre el Host y el Contenedor

* **`docker cp` (Docker Copy)**: Permite copiar archivos o carpetas de forma bidireccional: desde tu máquina física hacia el interior de un contenedor activo, o extraer archivos desde el contenedor hacia tu máquina física.
* *Sintaxis:* `docker cp [ORIGEN] [DESTINO]`
* *Ejemplo corregido (Extraer del contenedor al host):* `sudo docker cp minodered:/tmp/backup_data_nodered.tar ./backupdata_nodered.tar` *(Entra al contenedor "minodered", busca el respaldo en su carpeta `/tmp` y lo extrae a la carpeta actual `./` de tu computadora física).*



---

### 💡 El flujo completo de respaldo industrial:

Imagina que quieres respaldar los datos internos de un Node-RED que no tenía volumen mapeado:

```bash
# 1. Entras al contenedor a comprimir los datos internos
docker exec -it minodered tar -cvf /tmp/backup_data.tar /data

# 2. Sacas ese archivo .tar desde el contenedor hacia tu computadora física (Host)
sudo docker cp minodered:/tmp/backup_data.tar ./backup_final_host.tar

# 3. ¡Listo! Ya tienes un respaldo de los datos a salvo en tu máquina anfitriona.

```
