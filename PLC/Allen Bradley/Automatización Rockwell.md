# 🏭 Automatización con Rockwell Automation 🚀

Este documento presenta una expansión técnica sobre los puntos clave para la ingeniería utilizando el ecosistema de **Rockwell Automation** y **Allen Bradley**.

---

### 1. Niveles de la Pirámide de Automatización 🪜
La automatización se organiza en una jerarquía de cinco niveles, conocida como la **Pirámide CIM**:

* **Nivel 1 (Campo):** Sensores y actuadores que interactúan con el proceso físico 📡.
* **Nivel 2 (Control):** PLCs y controladores que ejecutan la lógica de control 🧠.
* **Nivel 3 (Supervisión):** Sistemas **HMI** y **SCADA** para monitoreo y control por parte de operadores 🖥️.
* **Nivel 4 (Planificación/MES):** Gestión de la ejecución de la producción y control de calidad 📊.
* **Nivel 5 (Gestión/ERP):** Administración de recursos empresariales y logística global 🏦.

---

### 2. ¿Qué es Allen Bradley? 🏢
Es la marca de hardware de **Rockwell Automation**. Se especializa en controladores lógicos programables (**PLC**), interfaces hombre-máquina (**HMI**), variadores de frecuencia y componentes de control industrial, siendo el estándar predominante en la industria norteamericana 🇺🇸.

---

### 3. Diferencias entre CompactLogix y ControlLogix ⚖️
Ambos pertenecen a la familia **Logix**, pero tienen aplicaciones distintas:

* **CompactLogix:** Solución de rango medio. Ideal para máquinas independientes. No utiliza chasis (rack), los módulos se conectan lateralmente 🖇️.
* **ControlLogix:** Sistema de gama alta para procesos complejos. Basado en chasis, permite **redundancia** y tiene mayor velocidad de procesamiento ⚡.

---

### 4. Studio 5000 vs. RSLogix 5000 💻
La diferencia radica en la versión del firmware:
* **RSLogix 5000:** Versiones de firmware de la 7 a la 20 💾.
* **Studio 5000 Logix Designer:** Sucesor para versiones 21 en adelante. Entorno integrado para diseño de HMIs y red 🛠️.

---

### 5. Configuración de Comunicación (RSLinx y Drivers) 🔌
**RSLinx Classic** actúa como el servidor de comunicaciones entre el software y el hardware.

* **Configurar un driver:** `Communications > Configure Drivers`. Se elige el tipo (ej. **EtherNet/IP** para búsqueda automática 🔍).
* **Dirección MAC:** Visible en la etiqueta física o vía RSLinx en `Device Properties` 🏷️.

---

### 6. BootP DHCP Tool 🌐
Utilidad para asignar una **IP estática** a dispositivos nuevos de fábrica.
1. Detecta la **MAC** del dispositivo 🕵️.
2. Asocias la MAC a la IP deseada 📍.
3. **¡Importante!** Desactivar el modo BootP/DHCP para que la IP sea permanente 🔒.

---

### 7. Simulación y Conexión (Emulate 5000 / FactoryTalk Echo) 🕹️
Para trabajar sin hardware físico:
* **Software:** *Studio 5000 Logix Emulate* (antiguos) o *FactoryTalk Logix Echo* (modernos como ControlLogix 5580) 🖥️.
* **Conexión:** Crear controlador virtual -> Configurar driver *Virtual Backplane* en RSLinx -> `Who Active` en Studio 5000 -> **Download** 📥.

---

### 8. Diferencias entre Sink y Source ↕️
Definen la dirección del flujo de corriente en los módulos de E/S:
* **Source (Fuente):** El módulo entrega el voltaje positivo (+) al dispositivo ⬆️.
* **Sink (Sumidero):** El módulo recibe la corriente; el dispositivo cierra el circuito a tierra (0V) ⬇️.
* *Nota:* En América es común la lógica **Source** para salidas (24VDC) 💡.

---

### 9. Módulos en Factory I/O 🏭
Simulador de plantas industriales:
* **Digitales:** Señales booleanas (Start, Stop, Sensores) ✅/❌.
* **Analógicos:** Señales continuas (0-10V o 4-20mA). Requieren mapeo a registros enteros o reales 📈.

---

### 10. Backup y Errores Comunes 📂
* **Backup:** Archivos con extensión **.ACD**. Se recomienda usar `Save As` y comprimir 🤐.
* **Error de I/O Configuration:** Ocurre cuando el hardware real no coincide con el árbol del proyecto (ej. slot equivocado). Genera falla y un icono de advertencia ⚠️.

---

### 11. Máquinas Virtuales (Host y Compatibilidad) 💽
Debido al peso y conflictos de versiones, es estándar usar **VMWare** o **VirtualBox**:
* **Red:** Usar modo **Bridged** para que la VM tenga su propia IP y vea los PLCs reales 🌉.
* **Compatibilidad:** Asegurar que el Windows de la VM soporte la versión de Studio 5000 (ej. Win 10 Pro para v30+) ✔️.
