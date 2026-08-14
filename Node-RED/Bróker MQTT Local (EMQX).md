# 📡 Configuración de un Bróker MQTT Local (EMQX)

---

## 📝 Introducción

Una comunicación **MQTT** requiere obligatoriamente de un **bróker** que gestione la transferencia de datos entre clientes. Frente a esta necesidad, existen dos opciones principales:

---

### 🏠 Opción 1: Bróker Local
* **Ventajas:** No requiere conexión a Internet; basta con una red local (**LAN** o **WLAN**).
* **Casos de uso:** Ideal para entornos de planta o industrias donde se busca evitar que los equipos se conecten a la red pública, manteniendo la seguridad e interconexión.
* **Costo:** El servicio es totalmente gratuito de por vida.

---

### 🌐 Opción 2: Bróker en Línea
* **Ventajas:** Accesible desde cualquier lugar del mundo con muy poca configuración previa.
* **Modalidades:**
  * 🆓 **Gratuitas / Sin registro:** Para pruebas rápidas.
  * 📝 **Con registro gratuito:** Ofrecen capas gratuitas con ciertas limitaciones.
  * 💳 **De pago:** Ofrecen funcionalidades avanzadas, escalabilidad e infraestructura dedicada.

---

## ⚙️ Comparativa de Opciones de Bróker

| Bróker | Tipo | Servidor de Prueba (Si aplica) | Puerto | Observaciones |
| :--- | :--- | :--- | :--- | :--- |
| 🦟 **Mosquitto** | Gratuito sin registro | `test.mosquitto.org` | `1883` | Excelente para pruebas rápidas. ⚠️ **NO USAR PARA INFORMACIÓN SENSIBLE.** |
| 🐝 **HiveMQ** | Gratuito con registro | Provisto en la plataforma (único por proyecto) | `1883` / `8883` | Excelente para despliegue rápido. Capa gratuita con limitaciones. |
| 🚀 **EMQX** | Gratuito con registro | Provisto en la plataforma (único por proyecto) | `1883` / `8883` | Plataforma sólida y amigable. Versión local disponible (no nativa para Windows). |
| ❄️ **MQTT Cool** | Gratuito | `broker.mqtt.cool` | `1883` | Versión local disponible. Excelente para pruebas rápidas. ⚠️ **NO USAR SERVIDOR DE PRUEBA PARA INFORMACIÓN SENSIBLE.** |

> ⚠️ **Atención:** EMQX actualizó su plataforma y ya no ofrece una opción de instalación directa (*installer/exe*) para Windows. Sigue funcionando con **Docker** o **Linux**, pero para Windows 10/11 se puede ejecutar mediante descompresión manual de binarios o contenedores.

---

## 🚀 Paso 1: Selección y Despliegue de Bróker EMQX (Windows)

1. 🌐 Ingrese a [emqx.io](https://www.emqx.io) y haga clic en **"Download"**.
2. 💻 Seleccione el sistema operativo (**Windows** en este ejemplo).
3. 📦 Descargue el paquete comprimido y extráigalo en su equipo.

### 🖥️ Ejecución desde la Consola
1. Ingrese a la carpeta descomprimida.
2. Haga clic derecho en un espacio vacío y seleccione **"Abrir en Terminal"**.
3. Inicie el bróker ejecutando:
   ```cmd
   .\emqx start

```

4. 🛑 Para detener el bróker en cualquier momento, ejecute:
```cmd
.\emqx stop

```



> 📌 **Nota:** El bróker debe ejecutarse cada vez que se reinicie el dispositivo (salvo que se configure como servicio de inicio en Windows). Una vez iniciado, puede conectar clientes MQTT a `localhost` o a la **IP local** en el puerto **`1883`**.

---

## 📊 Paso 2: Administración mediante Panel Web (Dashboard)

EMQX incluye una interfaz gráfica para administrar la plataforma:

* 🔗 **Dirección de acceso:** `http://localhost:18083` o `http://IP_DEL_EQUIPO:18083`
* 🔑 **Credenciales iniciales:**
* **Usuario:** `admin`
* **Contraseña:** `public`



⚠️ **Importante:** El sistema solicitará cambiar la contraseña en el primer inicio. **Guarde bien sus credenciales**, ya que recuperarlas una vez perdidas es un proceso complejo.

---

## 🔒 Paso 3: Configuración de Autenticación de Clientes

Para evitar conexiones no autorizadas o tráfico *spam*, se debe activar la autenticación de usuarios:

### 🗄️ 1. Crear la Base de Datos de Usuarios (Solo una vez)

1. Diríjase al menú lateral **"Authentication"**.
2. Haga clic en el botón **"Create"**.
3. Acepte los valores por defecto presionando **"Next"** hasta finalizar.

### 👤 2. Agregar Usuarios para los Clientes MQTT

1. Dentro del menú de autenticación, haga clic en **"Users"**.
2. Presione el botón **"ADD"**.
3. Complete el nombre de usuario y contraseña para el nuevo cliente.

¡Listo! Repita este paso para cada nuevo dispositivo o cliente que necesite conectarse de forma segura a su red local.
