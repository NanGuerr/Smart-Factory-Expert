# 🚀 Procedimiento de Carga de Programa en Siemens LOGO!

Este documento detalla los pasos necesarios para transferir un programa desde el entorno **LOGO! Soft Comfort** hacia un autómata programable (PLC) Siemens LOGO!.

---

## 🛠️ Requisitos Previos
* Tener el programa finalizado y compilado en **LOGO! Soft Comfort**.
* Cable de comunicación (Ethernet o cable específico de Siemens) conectado entre el PC y el PLC.
* PLC alimentado eléctricamente.

---

## 📋 Pasos Detallados

### 1. Acceso al Menú de Transferencia 🖱️
Para comenzar, dirígete a la barra de menú superior del software:
* Selecciona **Tools** (Herramientas).
* Haz clic en **Transfer** (Transferir).
* Selecciona **PC <-> LOGO!**.
* *Análisis:* Este comando abre el asistente que gestiona la comunicación bidireccional entre tu estación de trabajo y el dispositivo físico.

### 2. Configuración de la Conexión 🔌
Una vez abierta la ventana de transferencia:
* Elige la **Interfaz** (Interface) correcta según el cable que estés utilizando (ej. Ethernet/IP).
* Haz clic en el botón de búsqueda o refrescar si el dispositivo no aparece en la lista.
* *Análisis:* Aquí se asegura que el software "encuentre" físicamente al PLC en la red. Sin este paso, la transferencia fallará.

### 3. Ejecución de la Transferencia 🔄
* Selecciona el programa que deseas enviar.
* Haz clic en **OK** o **Transfer** para iniciar.
* Observarás una barra de progreso: **"Transferring"**.
* *Advertencia:* No desconectes el cable ni cortes la energía del PLC mientras la barra de progreso esté activa, ya que podría corromper el firmware o la memoria.

### 4. Finalización y Puesta en Marcha ✅
* Al concluir, el software mostrará un mensaje confirmando que la transferencia ha sido exitosa.
* Se te preguntará si deseas cambiar el PLC a modo **RUN** (Ejecución).
* Haz clic en **Yes** para que el PLC comience a ejecutar la lógica programada inmediatamente.

---

## ⚠️ Resolución de Problemas Comunes
* **PLC no detectado:** Verifica la dirección IP del PC y del PLC. Deben estar en el mismo segmento de red (ej. 192.168.0.x).
* **Error de escritura:** Asegúrate de que el PLC no esté protegido contra escritura mediante contraseña.
* **Timeout:** Revisa el estado del cable Ethernet/USB; un falso contacto es la causa más común de desconexión.
