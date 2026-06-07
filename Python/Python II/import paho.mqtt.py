import paho.mqtt.client as paho
import time

def on_connect(client, userdata, flags, rc, properties=None):
    if str(rc) == "Success":
        print("Conexion exitosa!")
    else:
        print("Falla al conectar. Razón:", str(rc))
    
def on_publish(client, userdata, num, properties=None, data=None):
    print("Publicación OK - No.:", str(num))

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Suscripción exitosa")


def on_message(client, userdata, msg):
    print(" --- MENSAJE RECIBIDO --- ")
    print(f"Desde: {msg.topic}")
    print(f"QoS: {msg.qos}")
    print(f"Mensaje: {msg.payload.decode('utf-8')}")
    print(" ------------------------ ")
    
client = paho.Client(paho.CallbackAPIVersion.VERSION2,client_id="", userdata=None, protocol=paho.MQTTv5)

client.on_connect = on_connect

client.username_pw_set("Python", "Python1234") # Comentar si no usamos usuarios / acceso anónimo
client.tls_set(tls_version=paho.ssl.PROTOCOL_TLS) # Comentar si no usamos usuarios / acceso anónimo
client.connect("127.0.0.1", 1883)

client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# --------------------------------------------------------------

client.subscribe("sierra", qos=0)
client.loop_start()


try:
    while True: 
        for i in range(50):
            client.publish("sierra",i,qos=0)
            time.sleep(0.5)
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
    print("Desconectado")
