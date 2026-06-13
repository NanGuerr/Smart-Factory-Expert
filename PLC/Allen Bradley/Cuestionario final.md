# PLC Allen Bradley & Studio 5000

Conceptos fundamentales de la arquitectura Logix 5000, tipos de datos y lógica de control.

---

### 🏗️ Arquitectura y Jerarquía del Sistema

**1) Un programa de PLC puede estar constituido por varias tareas.** ✅
*   **Respuesta:** **a) Verdadero**
*   **Explicación:** En Studio 5000, la **Tarea (Task)** es el elemento de mayor jerarquía. Una Tarea contiene uno o varios Programas.

**2) Un programa de PLC solo puede tener rutinas del mismo lenguaje de programación.** 📑
*   **Respuesta:** **b) Falso**
*   **Explicación:** Es posible combinar rutinas de Ladder (LD), Bloques de Función (FBD), Texto Estructurado (ST) y SFC dentro de un mismo programa.

---

### 🏷️ Gestión de Tags (Variables)

**3) Un tag de controlador se puede emplear en múltiples programas.** 🌍
*   **Respuesta:** **a) Verdadero**
*   **Explicación:** Los **Controller Tags** son globales y visibles para todo el proyecto y dispositivos externos (HMI/SCADA).

**4) Un tag de programa se puede emplear en múltiples programas.** 🔒
*   **Respuesta:** **b) Falso**
*   **Explicación:** Los **Program Tags** son locales; solo existen y son visibles dentro del programa donde fueron creados.

**5) Un tag de programa solo puede ser de tipo base.** 🛠️
*   **Respuesta:** **b) Falso**
*   **Explicación:** Pueden ser de tipo **Alias**, **Consumido** o estructuras complejas como Timers y Contadores.

**6) Un tag de tipo alias lo puedo direccionar con una entrada o salida de PLC.** 🔗
*   **Respuesta:** **a) Verdadero**
*   **Explicación:** El **Alias** vincula un nombre descriptivo (ej. `Sensor_Nivel`) directamente a una dirección física de I/O.

---

### 🔢 Tipos de Datos e Instrucciones de Bit

**7) Las instrucciones de XIC, XIO, OTE solo pueden almacenar un tipo de dato BOOL.** 💡
*   **Respuesta:** **a) Verdadero**
*   **Explicación:** Son instrucciones de bit; solo operan con estados binarios (0 o 1).

**8) Para reflejar un valor con decimales lo tengo que almacenar en un tipo de dato DINT.** 📈
*   **Respuesta:** **b) Falso**
*   **Explicación:** Los DINT son enteros de 32 bits. Para decimales se utiliza el tipo de dato **REAL** (punto flotante).

---

### ⏱️ Temporizadores y Movimiento de Datos

**9) Un temporizador con retardo a la conexión lleva por siglas TOF.** ⏳
*   **Respuesta:** **b) Falso**
*   **Explicación:** El retardo a la conexión es **TON** (Timer On Delay). El **TOF** es para retardo a la desconexión.

**10) Si desea indicar una acción pasado un tiempo con un TON ¿Qué bit debería de emplear?** 🏁
*   **Respuesta:** **c) DN**
*   **Explicación:** El bit **.DN (Done)** se activa cuando el acumulado (.ACC) iguala al valor preestablecido (.PRE).

**11) En una instrucción MOV es posible trasladar un INT a un DINT.** 🚚
*   **Respuesta:** **a) Verdadero**
*   **Explicación:** El PLC realiza una conversión automática ya que el valor de 16 bits (INT) cabe sin problemas en uno de 32 bits (DINT).

---

### 📊 Control Analógico

**12) Las entradas y salidas analógicas solo es posible programarlas con la función SCL en una rutina FBD.** 📉
*   **Respuesta:** **b) Falso**
*   **Explicación:** Se pueden programar en Ladder usando instrucciones matemáticas como **CPT** o mediante instrucciones personalizadas (**AOI**).

---

## 📌 Resumen de Estructura Logix (Jerarquía Correcta)

| Nivel | Nombre | Función Principal |
| :--- | :--- | :--- |
| **1° (Top)** 🔝 | **Task** | Gestiona el tiempo y prioridad de ejecución. |
| **2°** 📁 | **Program** | Agrupa funciones lógicas y separa variables locales. |
| **3° (Bottom)** 📝 | **Routine** | Contiene el código final (Ladder, ST, etc.). |

> **⚠️ Nota de Ingeniería:** Es vital respetar esta jerarquía para evitar problemas de **Scan Time**. Las tareas periódicas aseguran que los procesos críticos se ejecuten en el tiempo exacto requerido.
