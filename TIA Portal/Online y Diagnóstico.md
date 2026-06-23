# 🛠️ Online y Diagnóstico en TIA Portal

Esta guía detalla los pasos críticos para la gestión de comunicación, carga de programas y mantenimiento preventivo/correctivo en TIA Portal de Siemens.

---

## 🔌 1. Establecer Conexión Online
La conexión online es el puente entre tu PC y el PLC.

1.  **Configuración de Interfaz:** Asegúrate de que la interfaz PG/PC en el panel de control de Windows coincida con tu adaptador físico (ej. Tarjeta de red Ethernet).
2.  **Búsqueda de dispositivos:** Haz clic en el botón **"Go online"** o utiliza el ícono de "Online access" en el árbol del proyecto.
3.  **Selección:** TIA Portal escaneará la red. Selecciona tu PLC y haz clic en **"Connect"**.
4.  **Estado:** Una vez conectado, los íconos de los bloques cambiarán a verde (si el código coincide) o naranja (si hay diferencias).

---

## 🏗️ 2. Insertar o Reemplazar PLC
Es común actualizar el hardware durante el ciclo de vida de un proyecto.

* **Insertar:** En "Add new device", selecciona la CPU y asegúrate de elegir la **versión de firmware exacta** que tiene el equipo físico.
* **Reemplazar (Device Replacement):**
    * Haz clic derecho sobre el PLC en el árbol del proyecto.
    * Selecciona **"Replace device"**.
    * Elige el nuevo modelo. El software intentará migrar la configuración de hardware y las direcciones de E/S.
    * *Nota:* Siempre verifica la consistencia después de un reemplazo para evitar errores de dirección.

---

## 📥 3. Carga de Programas (Download to Device)
El proceso de carga es crítico para la operación de la planta.

### A. Vista Preliminar de Carga (Load Preview)
Antes de cargar, TIA Portal muestra una ventana de resumen (Load Preview). **No la ignores:**
* **Verificación:** Comprueba qué módulos se detendrán.
* **Configuraciones:** Puedes seleccionar si deseas "Load with consistency check" (recomendado para asegurar que todo el bloque de código sea válido).

### B. Usar el Parpadeo de LED (Flash LED)
Al cargar un programa en un PLC nuevo o en una planta con múltiples CPUs, **es vital confirmar que estás conectado al equipo correcto**.
1.  En la ventana de carga, selecciona el PLC detectado.
2.  Haz clic en el botón **"Flash LED"** (o ícono de identificación).
3.  El LED de la CPU física comenzará a parpadear.
4.  Confirma visualmente que es el PLC correcto antes de presionar "Load".

---

## ⚙️ 4. Configuración de Carga y Módulos
* **Cargar Módulos:** Al cargar, puedes elegir "Hardware configuration" (para cambios físicos, tarjetas nuevas) o "Software (only changes)" para agilizar la carga si solo editaste lógica.
* **Carga completa:** Necesaria si cambiaste bloques de datos (DBs) o configuración de hardware.
* **Acciones:** Define si el PLC debe pasar a STOP antes de la carga (automáticamente) y si debe volver a RUN después de finalizar.

---

## 🩺 5. Diagnóstico y Monitoreo
Una vez online, utiliza las herramientas de diagnóstico:

* **Online & Diagnostics:** Haz doble clic en el PLC online.
    * **Buffer de diagnóstico:** Muestra el historial de errores (fallos de sistema, errores de comunicación, paradas de CPU).
    * **Estado del ciclo:** Monitorea el tiempo de ciclo del PLC.
* **Monitoreo de bloques:** Abre cualquier bloque (OB, FC, FB) y activa los **"Monitor glasses"** (ícono de gafas). Verás el flujo de datos en tiempo real.
* **Tablas de variables:** Úsalas para forzar valores (Force) o simplemente monitorizar entradas/salidas físicas sin necesidad de abrir el código.
