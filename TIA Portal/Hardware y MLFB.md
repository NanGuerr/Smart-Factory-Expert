# 🏷️ Estructura de Hardware y MLFB en Siemens

Esta guía detalla los componentes críticos para la identificación, selección y configuración de hardware en el entorno Siemens TIA Portal.

---

## 📦 1. MLFB (Machine-Readable Product Code)
El **MLFB** (Machine-Readable Product Code) es el **código de pedido** (o número de artículo) que identifica unívocamente a cada producto de Siemens.
* **¿Por qué es vital?:** Es el "DNI" del equipo. Al ingresar este código en el TIA Portal, el software identifica exactamente qué hardware tienes, qué capacidades tiene y qué versión de configuración necesitas.
* **Ejemplo:** `6ES7 214-1AG40-0XB0` (S7-1200 CPU 1214C DC/DC/DC).

---

## 🏗️ 2. Familias de CPU
Siemens clasifica sus controladores por familias según el rendimiento y la aplicación:
* **SIMATIC S7-1200:** Gama básica/media. Ideal para máquinas compactas, automatización de plantas pequeñas y tareas sencillas de comunicación.
* **SIMATIC S7-1500:** Gama alta/performance. Pensado para aplicaciones complejas, alta velocidad de procesamiento, gran cantidad de E/S y sistemas distribuidos.
* **SIMATIC S7-300 / S7-400:** Familias clásicas (legacy). Aún presentes en muchas plantas, aunque el TIA Portal da prioridad a la migración hacia S7-1500.
* **ET 200SP CPU:** Controlador distribuido. Combina la potencia de un S7-1500 con un diseño extremadamente compacto para montaje en rack.

---

## ⚙️ 3. Gamas y Subtipos de PLC
Dentro de cada familia, encontramos variaciones que definen la funcionalidad:
* **CPU Estándar:** Control lógico convencional.
* **CPU Fail-safe (F):** Identificadas con la letra **"F"** (ej. 1516F). Tienen hardware y firmware dedicado para funciones de **Seguridad (Safety)** (Paradas de emergencia, barreras fotoeléctricas, etc.).
* **CPU Technology (T):** Optimizadas para control de movimiento avanzado (Motion Control) y sincronismo complejo.
* **Compacta (C):** CPUs con E/S integradas (entradas/salidas digitales y analógicas) en el mismo módulo.

---

## 🔄 4. Versiones de Firmware
El firmware es el sistema operativo del PLC.
* **Importancia:** Define qué funciones de TIA Portal puedes usar. Una CPU con firmware antiguo puede no soportar funciones nuevas (como ciertos bloques de comunicación o seguridad).
* **Configuración:** En el TIA Portal, debes seleccionar **exactamente** la versión de firmware que tiene tu equipo físico. Si seleccionas una versión superior a la real, el proyecto no cargará en el PLC.
* **Actualización:** Se puede actualizar mediante la tarjeta de memoria (Memory Card) o a través de TIA Portal si hay comunicación establecida.

---

## 🔒 5. Configuración de Seguridad y Funcionalidad
El hardware moderno permite una integración avanzada:

### Funcionalidad Integrada
* **Web Server:** Acceso a diagnóstico y datos desde cualquier navegador.
* **OPC UA:** Protocolo estándar para comunicación con sistemas IT (SCADA, MES, Cloud).
* **Motion Control:** Bloques integrados (MC_MoveAbsolute, etc.) para control de servomotores y motores paso a paso.
* **PID:** Control de lazos integrados para regulación de temperatura, presión, etc.

### Configuración de Seguridad (Safety)
* Las **F-CPU** requieren una configuración específica en TIA Portal (Step 7 Safety Advanced).
* **F-Signature:** El proyecto de seguridad debe compilarse y firmarse. Cualquier cambio en la lógica de seguridad invalida la firma y requiere una descarga completa.
* **Acceso:** Protección mediante contraseña a nivel de hardware para evitar accesos no autorizados a la lógica de control.
