# ⚙️ Expansión de Hardware en TIA Portal

La capacidad de ampliar el PLC más allá de sus entradas y salidas integradas es fundamental para cualquier proyecto de automatización escalable. A continuación, detallamos cómo gestionar esta configuración.

---

## 🧩 Tipos de Módulos (DI / DQ / AI / AQ)

En el mundo Siemens, clasificamos los módulos según el tipo de señal que manejan:

* **📥 DI (Digital Input):** Entradas digitales (sensores, pulsadores, finales de carrera).
* **⚡ DQ (Digital Output/Quantity):** Salidas digitales (lámparas, contactores, relés). *Nota: Siemens utiliza "Q" para salidas.*
* **🌡️ AI (Analog Input):** Entradas analógicas (sensores de temperatura, presión, sensores de nivel, sensores de 4-20mA o 0-10V).
* **📊 AQ (Analog Output):** Salidas analógicas (variadores de frecuencia, válvulas proporcionales).

---

## 🛠️ Signal Boards y Módulos de Comunicación

### 🏷️ ¿Qué es una Signal Board?
Es una pequeña placa (SB) que se inserta directamente en el **frontal** de la CPU S7-1200.
* **Ventaja:** No ocupa espacio a los lados del PLC.
* **Uso:** Ideal para añadir un par de entradas/salidas extra o una entrada analógica sin necesidad de un módulo de expansión completo.

### 📡 Módulos de Comunicación (CM / CP)
Se utilizan para protocolos externos.
* **CM (Communication Module):** Ej. CM 1241 para RS232/RS485.
* **CP (Communication Processor):** Ej. CP 1243-1 para conexión a redes especiales o telegestión.
* En TIA Portal, los configuras en la "Network View" arrastrándolos al lado izquierdo de la CPU.

---

## 📝 Ejemplos y Ejercicios Prácticos

### Ejemplo Base: El reto de los 20 DI / 4 DQ / 2 AI
Si tenemos una **CPU 1214C DC/DC/DC**, esta trae de fábrica: **14 DI / 10 DQ**.

* **Necesidad:** 20 DI (Tenemos 14, nos faltan 6).
* **Necesidad:** 4 DQ (Tenemos 10, **estamos cubiertos**).
* **Necesidad:** 2 AI (Tenemos 0, **necesitamos módulos**).

**Solución:** Agregar un módulo SM 1221 (DI) para las entradas faltantes y un SM 1231 (AI) para las analógicas.

---

### 🏋️ Ejercicio 01: Selección de Hardware
**Requisitos:** 29 DI, 4 DQ (transistor), 7 DQ (relé), 10 AI (4-20mA).

1.  **Análisis:**
    * La CPU 1214C tiene 14 DI. Necesitamos añadir 15 DI extra (Módulo SM 1221 DI 16).
    * Salidas digitales: 4 (transistor) + 7 (relé) = 11 DQ. CPU tiene 10. Falta 1 DQ. (Módulo SM 1222 DQ 8 Relé).
    * Analógicas: 10 AI. Necesitamos expandir (Módulos SM 1231 AI 8).
2.  **Configuración:** Seleccionar los módulos físicos en TIA Portal (Hardware Catalog) y verificar que no se exceda la cantidad máxima de módulos permitida por el PLC (generalmente 8 módulos de expansión para un S7-1200).

---

### 🧠 Ejercicio 02: ¿Me alcanza con la CPU 1214C?

**Desglose de señales:**

| Elemento | Tipo | Cantidad |
| :--- | :--- | :--- |
| Sensores prox | DI | 4 |
| Fines de carrera | DI | 2 |
| Pulsadores NA | DI | 3 |
| Emergencia NC | DI | 1 |
| **Total DI** | | **10** |
| Lámparas 24V | DQ | 3 |
| Relés | DQ | 2 |
| **Total DQ** | | **5** |
| Sensor Temp (0-10V) | AI | 1 |
| Comando VFD (0-10V) | AQ | 1 |

**Análisis:**
* **DI:** CPU 1214C tiene 14. Tenemos 10. **(Ok)**.
* **DQ:** CPU 1214C tiene 10. Tenemos 5. **(Ok)**.
* **Analogía:** La CPU 1214C estándar no tiene entradas/salidas analógicas integradas.
    * **Conclusión:** **Sí, necesitas agregar módulos adicionales**.
    * **Solución:** Debes agregar una **Signal Board (SB 1231 AI)** para la temperatura y un módulo de expansión **SM 1232 (AQ)** para el variador de frecuencia.
