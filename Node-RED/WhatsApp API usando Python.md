# 🐍 Integración de MySQL con WhatsApp API usando Python

¡Excelente elección! **Python** es uno de los lenguajes más potentes y sencillos para integrar bases de datos con APIs, y usarlo para enviar mensajes de WhatsApp a través de una API corporativa es un caso de uso muy común. 🚀

Para lograrlo, crearemos un script en Python que actúe como puente entre tu base de datos MySQL y la API de WhatsApp que te proporcionaron. 🌉

---

## 📦 Paso 1: Instalar las librerías necesarias

Abre tu terminal o consola y ejecuta el siguiente comando para instalar las herramientas que usaremos para conectar MySQL (`mysql-connector-python`) y hacer peticiones HTTP (`requests`):

```bash
pip install mysql-connector-python requests

```

---

## 💻 Paso 2: El Script de Python

Crea un archivo llamado `enviar_whatsapp.py` y pega el siguiente código. Recuerda ajustar los datos de tu base de datos y la URL/Token de la API de la empresa:

```python
import mysql.connector
import requests

# 1. Configuración de tu base de datos MySQL
db_config = {
    'host': 'localhost',
    'user': 'tu_usuario_mysql',
    'password': 'tu_contraseña_mysql',
    'database': 'nombre_de_tu_base'
}

# 2. Configuración de la API de WhatsApp de la empresa
WHATSAPP_API_URL = "[https://api.tuempresa-whatsapp.com/v1/send](https://api.tuempresa-whatsapp.com/v1/send)"  # Cambia esto por la URL real
API_HEADERS = {
    "Authorization": "Bearer TU_TOKEN_DE_ACCESO",  # Cambia esto por el token o clave que te dieron
    "Content-Type": "application/json"
}

def procesar_cola_mensajes():
    try:
        # Conectar a la base de datos
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor(dictionary=True)

        # Buscar mensajes pendientes (tomamos de 10 en 10 para no saturar)
        cursor.execute("SELECT id, destinatario, mensaje FROM cola_mensajes WHERE estado = 'PENDIENTE' LIMIT 10")
        mensajes = cursor.fetchall()

        if not mensajes:
            print("📭 No hay mensajes pendientes en la cola.")
            return

        for msg in mensajes:
            msg_id = msg['id']
            telefono = msg['destinatario']
            texto = msg['mensaje']

            # Estructura del JSON que espera la API (revisa la documentación de tu empresa)
            payload = {
                "to": telefono,
                "message": texto
            }

            try:
                # Enviar petición HTTP POST a la API de WhatsApp
                response = requests.post(WHATSAPP_API_URL, json=payload, headers=API_HEADERS)

                # Verificar si la API respondió con éxito (códigos 200 o 201)
                if response.status_code in [200, 201]:
                    cursor.execute("UPDATE cola_mensajes SET estado = 'ENVIADO' WHERE id = %s", (msg_id,))
                    conexion.commit()
                    print(f"✅ Mensaje {msg_id} enviado con éxito a {telefono}")
                else:
                    cursor.execute("UPDATE cola_mensajes SET estado = 'ERROR', intentos = intentos + 1 WHERE id = %s", (msg_id,))
                    conexion.commit()
                    print(f"⚠️ Error al enviar mensaje {msg_id}: {response.text}")

            except requests.exceptions.RequestException as e:
                print(f"❌ Error de conexión HTTP con la API: {e}")

        cursor.close()
        conexion.close()

    except mysql.connector.Error as err:
        print(f"❌ Error al conectar con MySQL: {err}")

if __name__ == "__main__":
    procesar_cola_mensajes()

```

---

## ⏱️ Paso 3: ¿Cómo automatizarlo?

Dado que este script procesa los mensajes pendientes cada vez que lo ejecutas, puedes programarlo para que corra de manera automática:

* 🐧 **En Linux:** Puedes configurar un **Cron Job** para que ejecute el script cada 1 o 5 minutos (ej. `*/5 * * * * python3 /ruta/a/enviar_whatsapp.py`).
* 🪟 **En Windows:** Puedes usar el **Programador de Tareas** (*Task Scheduler*) para que lance el script de Python de forma periódica.

> **💡 Nota importante:** Los campos del JSON (`"to"`, `"message"`) y el tipo de autenticación (`Bearer`) dependen enteramente de la documentación técnica que te haya entregado la empresa dueña de la API. Asegúrate de adaptar esas líneas según su manual. 📄

---

