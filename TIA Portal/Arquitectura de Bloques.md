# 🧩 Arquitectura de Bloques en TIA Portal

Esta guía detalla la estructura lógica, configuración y jerarquía de los bloques de programación en TIA Portal, esenciales para diseñar sistemas robustos y eficientes.

---

## 🏗️ 1. Tipos de Bloques de Programación

En TIA Portal, el programa se organiza en bloques con propósitos específicos:

* **OB (Organization Blocks):** Son la interfaz entre el Sistema Operativo (SO) y el programa del usuario. Controlan la ejecución cíclica y responden a eventos/interrupciones.
* **FC (Functions - Funciones):** Bloques de código **sin memoria propia**. No guardan datos entre llamadas. Ideales para cálculos matemáticos o lógica que no requiere persistencia.
* **FB (Function Blocks - Bloques de función):** Bloques de código **con memoria propia**. Requieren un "bloque de datos de instancia" (DB) para almacenar sus valores. Mantienen estados internos (ej. tiempos acumulados, pasos de una secuencia).
* **DB (Data Blocks - Bloques de datos):** Bloques utilizados exclusivamente para **almacenar datos**. Pueden ser globales (accesibles por todos) o de instancia (pertenecientes a un FB específico).

---

## 📂 2. Clasificación de Bloques de Organización (OBs)

Los OBs se clasifican según el evento que los dispara:

### 🔄 Ejecución Cíclica y Arranque
* **Main [OB1]:** El bloque principal. Ejecuta el ciclo de programa continuamente.
* **Startup [OB100]:** Se ejecuta una sola vez al pasar el PLC de STOP a RUN. Ideal para inicializar valores.

### ⏱️ Interrupciones de Tiempo
* **Cyclic Interrupt (OB30-OB38):** Interrumpe el ciclo principal en intervalos de tiempo fijos (ej. cada 10ms). Crucial para control PID.
* **Time Delay Interrupt (OB20-OB23):** Ejecuta un bloque después de un tiempo definido tras dispararse.
* **Time of Day (OB10-OB17):** Se ejecuta a una hora específica (ej. 8:00 AM).

### ⚡ Interrupciones de Hardware y Diagnóstico
* **Hardware Interrupt (OB40-OB47):** Disparado por un evento físico en una entrada digital (ej. sensor rápido).
* **Diagnostic Error Interrupt (OB82):** Se dispara si un módulo detecta un error de hardware o fallo de cableado.
* **Pull/Plug of Modules (OB83):** Detecta cuando se inserta o extrae un módulo.
* **Rack/Station Failure (OB86):** Detecta pérdida de comunicación con periferia descentralizada.
* **Time Error Interrupt (OB80):** Se dispara si el ciclo de escaneo excede el tiempo máximo permitido (Watchdog).

### ⚙️ Motion Control (MC)
* **MC-Servo, MC-PreServo, MC-PostServo:** Bloques de alta prioridad dedicados a la gestión de ejes de movimiento y control de lazos cerrados.
* **MC-Interpolator:** Gestiona la interpolación de trayectorias en sistemas multicorte o ejes complejos.

---

## ⚙️ 3. Configuración del Bloque
Al crear un bloque, accedes a sus **propiedades**:

1. **Lenguaje:** Puedes elegir entre **LAD** (KOP), **FBD** (FUP), **SCL** (Texto estructurado) o **STL** (AWL). SCL es ideal para cálculos complejos, LAD/FBD para lógica booleana visual.
2. **Número:** Puedes dejar que TIA Portal asigne el número automáticamente o asignarlo manualmente (útil para organizar tus librerías).
3. **Tiempo de ciclo (Watchdog):** En la configuración de la CPU, defines cuánto puede tardar el ciclo completo antes de que el PLC vaya a error.

---

## 🏗️ 4. Uso, Segmentos y Jerarquía

### ¿Cómo se usan?
Los bloques se "llaman" desde el **Main [OB1]** o desde otros bloques (FC/FB). Esto crea un **árbol de llamadas**.

### Segmentos
Los bloques se dividen en **Segmentos** (Network).
* **Función:** Organizar visualmente la lógica. Puedes poner comentarios por segmento, lo que facilita el mantenimiento y la lectura (se recomienda 1 lógica por segmento).

### Grados de Prioridad
El PLC tiene un sistema de prioridades para la ejecución:
1. **Prioridad Alta:** Interrupciones de Hardware y Errores (OB8x, OB4x, OB3x). *Interrumpen al OB1.*
2. **Prioridad Media:** Tareas de comunicación y tiempo.
3. **Prioridad Baja:** El ciclo principal de programa (OB1).

*⚠️ **Nota importante:** Si una interrupción tarda demasiado, puede bloquear la ejecución del OB1 y causar un error de "Cycle Time Exceeded". ¡Mantén tus bloques de interrupción breves!*
