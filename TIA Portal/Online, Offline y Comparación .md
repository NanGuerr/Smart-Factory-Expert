# 🔍 Gestión Online, Offline y Comparación 

Esta guía técnica describe los procedimientos fundamentales para la interacción entre tu proyecto (Offline) y el controlador físico (Online).

---

## 💻 1. Conceptos Online vs. Offline
* **Offline:** Es el proyecto que reside en tu computadora. Cualquier cambio aquí no afecta al PLC hasta que realices una carga (*Download*).
* **Online:** Estado en el que TIA Portal está conectado al hardware real. Permite monitorear el flujo de datos y estados de la máquina en tiempo real.

---

## 📥 2. Carga y Sincronización
### Descarga (Download) - De PC a PLC
Es el proceso de transferir tu configuración de hardware y software al equipo.
* **Sobreescritura:** Al cargar, el PLC sobrescribirá los bloques existentes. Ten cuidado con los **DBs (Data Blocks)**, ya que si cambias su estructura, los valores actuales del PLC podrían resetearse a sus valores iniciales si no se gestionan correctamente (Snapshot).

### Carga (Upload) - De PLC a PC
Si tienes un proyecto que solo existe en el PLC (por ejemplo, perdiste el archivo original o estás haciendo mantenimiento), puedes "traerlo" a TIA Portal:
* **Procedimiento:** `Online Access` -> Selecciona la interfaz -> `Upload device as new station`.
* **Limitación:** El código subido puede carecer de comentarios, nombres de variables simbólicas y estructuras de red si no fueron cargados originalmente con el proyecto.

---

## 🛠️ 3. Diagnóstico: "Main que difiere"
Si TIA Portal indica que el bloque `Main` (u otros bloques) **difiere**, significa que:
1.  Alguien modificó la lógica en el PLC directamente y no se actualizó el proyecto.
2.  La versión Offline no está sincronizada con la Online.
* **Corrección:** Debes comparar (ver sección 4) y decidir si realizar una carga (Download) para sobrescribir el PLC o una subida (Upload) para actualizar tu proyecto Offline.

---

## ⚖️ 4. Editor de Comparación Online
Es la herramienta más poderosa para solucionar discrepancias.

### Comparación de Bloques
1.  Haz clic derecho sobre el bloque o el PLC en el árbol del proyecto.
2.  Selecciona **"Compare"** -> **"Online/Offline"**.
3.  **Resultado:**
    * **Verde:** Los bloques son idénticos.
    * **Naranja:** Existen diferencias (logic, datos, timestamp).
    * **Rojo:** Bloque presente en un lado pero no en el otro.

### Editor de Comparación (Online Comparison Editor)
Al abrir el editor, verás una ventana dividida:
* **Lado Izquierdo (Offline):** Tu lógica actual en PC.
* **Lado Derecho (Online):** La lógica ejecutándose en el PLC.
* **Acciones:** Puedes ver exactamente qué línea de código cambió (ej. una entrada física, una constante o un tiempo en un timer). Puedes aplicar cambios selectivos o cargar la versión completa.

---

## ⚠️ 5. Consejos de Seguridad
* **Corrección de errores:** Antes de realizar una corrección, realiza una **Comparación Online** para asegurarte de que el código que estás editando es la versión más reciente del PLC.
* **Estado del PLC:** Si el PLC está en `RUN`, la carga de hardware o bloques críticos forzará un paso a `STOP` (dependiendo de la CPU y la configuración). **Siempre verifica el impacto operativo antes de cargar.**
