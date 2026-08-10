# 🔌 Introducción a PLCSim y PLCSim Advanced

## ⚠️ Nota importante para el curso
En este curso **sólo haremos uso del PLCSIM estándar**. ¡No es necesario que descarguen el PLCSIM Advanced! 🎓

---

## 💻 ¿Qué es PLCSIM?
**PLCSIM** es el entorno de simulación estándar de Siemens integrado dentro de TIA Portal. Permite simular el comportamiento de un PLC S7 sin necesidad de tener el hardware físico conectado.

Cuando compilas un proyecto para un S7-1200 o S7-1500, en lugar de descargarlo a un PLC real, puedes descargarlo a una **CPU virtual**. Esta CPU ejecuta tu programa exactamente igual que el hardware real en términos de:
*   🧠 Lógica y ciclos de scan.
*   📊 OBs, FBs y DBs.
*   ⏲️ Timers y contadores.

### 🛠️ ¿Qué puedes hacer con PLCSIM?
*   ✅ Probar la lógica del programa.
*   🎯 Forzar variables.
*   🎛️ Simular entradas digitales y analógicas.
*   👁️ Ver el estado online (monitorización).
*   🔍 Debuggear paso a paso.

**Clave:** PLCSIM estándar simula la CPU, pero **no el entorno industrial completo**. Es una simulación cerrada dentro de TIA Portal. 🔒

---

## 📉 Limitaciones de PLCSIM Estándar
*   🚫 No tiene red Ethernet real.
*   ❌ No se comporta como un dispositivo accesible desde otras máquinas.
*   🔌 No puedes integrarlo fácilmente con otros softwares externos.
*   🌐 No es ideal para arquitecturas distribuidas.

### Es perfecto para:
*   🎓 Estudiantes.
*   🚀 Desarrollo de lógica.
*   ⚡ Pruebas rápidas.
*   🏗️ Validación antes de descargar a campo.

*Si quieres simular una planta completa, esto empieza a quedarse corto.*

---

## 🚀 ¿Qué es PLCSim Advanced?
**PLCSIM Advanced** es otra categoría. Es un simulador mucho más profundo, orientado a ingeniería avanzada, integración y *Virtual Commissioning*. 🤖

### ✨ Características Principales
Crea una CPU virtual con **interfaz de red real**, lo que significa que:
*   🌐 **Tiene dirección IP propia.**
*   📡 **Puede comunicarse por Profinet.**
*   🖥️ **Puede conectarse con SCADA reales.**
*   🔗 **Puede hablar con sistemas externos vía OPC UA.**
*   🧪 **Puede integrarse con simuladores de proceso** (como MATLAB, etc.).

*En términos prácticos:* La CPU virtual se comporta como si fuera un **PLC físico** conectado a la red. 🏢

### 🏗️ Potencia Multiproceso
PLCSIM Advanced permite correr múltiples CPUs virtuales simultáneamente. Eso significa que puedes simular una arquitectura completa con:
*   🧠 PLC maestro.
*   ⛓️ PLC esclavos.
*   🔄 Comunicación entre ellos.
*   🖥️ HMI.
*   📊 OPC Server.

Todo esto en una sola PC potente. ¡Eso es excelente para laboratorios avanzados o para pruebas FAT virtuales! 🏆
