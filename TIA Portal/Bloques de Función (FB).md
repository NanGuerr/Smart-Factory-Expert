# 🧩 Bloques de Función (FB) en TIA Portal

Esta guía explica la arquitectura de los **FBs** y cómo utilizarlos para crear un filtro de promedio móvil con memoria de estados.

---

## 🏗️ 1. Definición y Características de los FB
Los **Bloques de Función (FB)** son bloques de código con memoria propia. A diferencia de las **FCs**, los FBs requieren un **DB de Instancia** para funcionar.

### ✅ Diferencias Clave: FC vs FB
* **FC (Función):** No tiene memoria. Al terminar de ejecutarse, sus variables temporales se borran. Ideal para cálculos puros o lógica combinacional.
* **FB (Bloque de Función):** Tiene memoria. Usa un DB de instancia para guardar variables `Static`. Ideal para lógica secuencial, controladores PID o cualquier proceso que necesite "recordar" el pasado.

---

## 📊 Ejemplo: FB "Filtrado" (Promedio Móvil)

Este FB calcula el promedio de la medición actual y los últimos 3 registros, actualizándose cada segundo.

### 📋 Interfaz del FB (`FB_Filtrado`)

| Nombre | Tipo | Tipo de dato | Descripción |
| :--- | :--- | :--- | :--- |
| `medicion` | Input | REAL | Valor actual del sensor |
| `valor_filtrado` | Output | REAL | Promedio calculado |
| `sumatoria` | Temp | REAL | Variable interna de cálculo |
| `divisor` | Constant | REAL | Valor fijo = 4.0 |
| `medicionT-1` | Static | REAL | Valor hace 1s |
| `medicionT-2` | Static | REAL | Valor hace 2s |
| `medicionT-3` | Static | REAL | Valor hace 3s |
| `auxDF` | Static | BOOL | Memoria del Detector de Flanco |

---

## 💻 Lógica de Implementación (KOP / Ladder)

### **Segmento 1: Temporización (1Hz)**
* Instrucción: `R_TRIG` (Detector de flanco).
* Entrada: Señal de `Clock_1Hz` (Byte de marcas de sistema).
* Memoria: `auxDF` (Static).
* *Función:* Habilitar la ejecución de los siguientes segmentos solo cuando el flanco es positivo.

### **Segmento 2: Cálculo del Promedio**
* Instrucción `ADD_R`: Suma `medicion` + `medicionT-1` + `medicionT-2` + `medicionT-3`.
* Resultado: Almacenar en `sumatoria` (Temp).
* Instrucción `DIV_R`: Divide `sumatoria` / `divisor` (4.0).
* Resultado final: Guardar en `valor_filtrado` (Output).

### **Segmento 3: Actualización de Memoria (Orden descendente)**
* *Nota: Se debe realizar en este orden para no perder los datos antes de tiempo.*
* `MOVE`: `medicionT-2` -> `medicionT-3`
* `MOVE`: `medicionT-1` -> `medicionT-2`
* `MOVE`: `medicion` -> `medicionT-1`

---
## 💡 Consejos de uso
1. **DB de Instancia:** Al arrastrar este FB al OB1, TIA Portal te pedirá crear un DB (ej. `DB_Filtrado_Instancia`). No olvides asignarlo.
2. **Orden de los MOVE:** Es crítico ejecutar el movimiento de datos (`MOVE`) **después** del cálculo del promedio (Segmento 2) para asegurar que el cálculo use los datos previos y no los nuevos.

Para ayudarte a dominar los **Bloques de Función (FB)**, he preparado esta guía detallada. Los FBs son la piedra angular para crear programas modulares y reutilizables en TIA Portal, especialmente cuando necesitas "memoria" dentro de tu lógica.

### 🧠 Bloques de Función (FB) en TIA Portal

Los **FBs (Function Blocks)** son bloques de código que poseen **memoria propia**. Cada vez que llamas a un FB, este utiliza un **Bloque de Datos de Instancia (DB de instancia)** para almacenar sus valores internos, lo que le permite "recordar" estados entre un ciclo de ejecución y otro.

#### ⚙️ Características principales

* **DB de Instancia:** Cada llamada al FB requiere un DB. Este bloque guarda los valores de las variables estáticas, entradas y salidas.
* **Persistencia:** A diferencia de las funciones simples (FC), los datos en un FB permanecen guardados mientras el PLC esté encendido (o si la DB es retentiva).
* **Modularidad:** Ideal para controlar máquinas complejas donde necesitas instancias repetitivas (ej. 10 motores idénticos).

#### 🆚 Diferencias: FC vs FB

| Característica | FC (Función) | FB (Bloque de Función) |
| --- | --- | --- |
| **Memoria** | No tiene memoria propia. | Tiene memoria (usando DB de instancia). |
| **DB de Instancia** | No requiere. | Sí requiere. |
| **Uso** | Cálculos matemáticos, lógica combinacional simple. | Secuencias, temporizadores, contadores, control de procesos. |
| **Persistencia** | Los datos se pierden al finalizar. | Los datos se guardan en el DB. |

---

### 📝 Ejemplo: FB Filtrado (Promedio Móvil)

Este bloque promediará la medición actual y las 3 anteriores.

* **Nombre del bloque:** `FB_Filtrado`
* **Interfaz:**
* `medicion`: Input (Real)
* `valor_filtrado`: Output (Real)
* `sumatoria`: Temp (Real)
* `divisor`: Constante (Real = 4.0)
* `medicionT-1`, `medicionT-2`, `medicionT-3`: Static (Real)
* `auxDF`: Static (Bool) - Para detector de flanco.



#### 🏗️ Estructura de Segmentos

* **Segmento 1: Detección de Flanco (Clock 1Hz)**
* Usamos una instrucción `R_TRIG` (Detector de flanco) vinculada a `auxDF` y a un `Clock_1Hz`.
* *Objetivo:* Ejecutar la lógica de promedio y actualización solo una vez por segundo.


* **Segmento 2: Cálculo del Promedio (Lógica)**
* `sumatoria := medicion + medicionT-1 + medicionT-2 + medicionT-3`
* `valor_filtrado := sumatoria / divisor`


* **Segmento 3: Desplazamiento de Datos (Shifting)**
* Usamos instrucciones `MOVE` para actualizar el historial.
* `MOVE(medicionT-2) -> medicionT-3`
* `MOVE(medicionT-1) -> medicionT-2`
* `MOVE(medicion)    -> medicionT-1`
