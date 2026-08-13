# 🤖 Configuración de Bot de Telegram: Conceptos

Recursos y notas útiles para la integración de **Telegram** y **WhatsApp** en **Node-RED**.

---

## 📦 Nodos y Librerías

* 🔗 **Nodo principal de Telegram:** [node-red-contrib-telegrambot](https://flows.nodered.org/node/node-red-node-telegrambot)

---

## ⚠️ Solución a Errores Comunes

### 🐛 Error en `telegram sender`: `"msg.payload.content is empty"`
Si experimentas este error de formato (posiblemente debido a una actualización del nodo que ahora requiere que el contenido sea un *string*), puedes solucionarlo agregando el siguiente código dentro de un nodo **Function** antes del nodo *Telegram Sender*:

```javascript
msg.payload = { 
    chatId: 8866498821, 
    type: "message", 
    content: String(flow.get("potenciamaxima")) 
}; 
return msg;

```

---

## 📚 Funcionalidades de Telegram en Node-RED

* 👥 **Enviar mensajes a un grupo de Telegram**
* 📤 **Enviar mensajes de Telegram desde Node-RED**
* 📜 **Crear una lista de comandos en Telegram**
* 📎 **Adjuntar archivos en Telegram desde Node-RED**

---

## 📲 Integración con WhatsApp

* 🟢 **API gratuita de WhatsApp:** [CallMeBot API](https://www.callmebot.com/blog/free-api-whatsapp-messages/)
* ⚠️ **Enviar mensajes de WhatsApp desde Node-RED y sus limitaciones:** [callmebot.com](https://www.callmebot.com/)

