# 🧠 Variables Físicas vs. Variables Internas, Memoria y Datos


Este documento contiene el resumen del mapa y comportamiento de las **Áreas de Memoria**, los **Registros de Trabajo**, y la diferencia fundamental entre **Entradas, Salidas y Marcas**.

---

## 🗂️ 1. Áreas de Memoria del PLC
El PLC organiza su información y su programa dividiéndose en tres grandes arquitecturas de almacenamiento:

* **📦 Memoria de Carga:** * **Función:** Es el lugar donde se transfiere el programa de control del PLC y los estados predeterminados iniciales.
  * **Características:** Es de **Sólo Lectura** y de carácter **No volátil** (la información permanece al desenergizar el equipo). Solo puede ser modificada a través del software y el equipo de programación.
* **⚙️ Memoria de Trabajo:** * **Función:** Zona de alta velocidad donde verdaderamente se ejecuta la lógica del proceso. Al arrancar (boot), el procesador clona el código de la memoria de carga hacia aquí. Almacena todos los cálculos intermedios, estados y valores activos de las variables.
  * **Características:** Es de **Lectura/Escritura** y de carácter **Volátil** (pierde los datos si se corta la alimentación).
* **🔋 Memoria Remanente:** * **Función:** Una sección pequeña y segura diseñada para almacenar configuraciones críticas, recetas, contadores o parámetros de calibración que **no deben perderse** ante fallos de energía o reinicios del equipo.
  * **Características:** Es de **Lectura/Escritura** y de carácter **No volátil**.

---

## 🔢 2. Memoria de Trabajo y Registros
Dentro de la memoria de trabajo, la información no está dispersa; se empaqueta en celdas lógicas llamadas **Registros**.

* 🧩 **Estructura:** Cada registro numérico (comenzando siempre desde el **0**) está compuesto exactamente por **8 bits** (Numerados del bit `0` al bit `7`).
* 📋 **Mapeo:** A medida que creamos y declaramos variables en nuestro programa, el software reserva dinámicamente los espacios requeridos en estos registros. Para interactuar con una variable, el procesador apunta directamente a su **dirección física o lógica**.

---

## 🔄 3. El Triángulo de Registros: Entradas, Salidas y Marcas
Los datos relevados por el entorno y las decisiones tomadas por el PLC se dividen de manera aislada e independiente en tres tablas de registros independientes (comienzan desde el 0 y **no se superponen**, permitiendo tener la misma dirección relativa pero en tablas distintas):

### 📥 Entradas (`I / E`)
* **Naturaleza:** Vinculadas directamente a la periferia física de hardware.
* **Mapeo:** Representan directamente el estado eléctrico de los bornes físicos de entrada. Aquí se graban las lecturas de los **pulsadores, interruptores y sensores** cableados.

### 📤 Salidas (`O / Q / A`)
* **Naturaleza:** Vinculadas directamente a la periferia física de hardware.
* **Mapeo:** Corresponden con los bornes de salida del PLC. Cuando el programa escribe un valor (*TRUE* o 1) en un bit de esta tabla, se energiza el borne físico para comandar **contactores, electroválvulas, lámparas o motores**.

### 🏷️ Marcas (`M`)
* **Naturaleza:** Memorias de uso **estrictamente interno** del procesador.
* **Mapeo:** No tienen ninguna conexión con los bornes físicos del PLC. Son pizarras virtuales fundamentales para que el programador almacene **estados intermedios**, banderas lógicas (flags) o resultados de operaciones secuenciales.

---

# ⚙️ Programación de PLC: Variables, Memoria y Datos

Esta guía resume los conceptos fundamentales sobre cómo se gestiona la información dentro de un PLC.

---

## 💾 El Área de Memoria del PLC
El cerebro del PLC necesita almacenar programas, cálculos y estados. Esta área se divide según su función y persistencia:

*   **⚡ Memoria de Carga:** Donde reside el programa y estados iniciales. Es **no volátil** y de sólo lectura.
*   **🧠 Memoria de Trabajo:** Donde se ejecuta el programa. Es **volátil**; al arrancar, el procesador copia el programa desde la memoria de carga.
*   **⏳ Memoria Remanente:** **No volátil** y de lectura/escritura. Permite conservar valores de variables incluso tras un reinicio, ideal para procesos críticos.

---

## 🗄️ Los Registros
Las variables se organizan en secciones llamadas **registros** dentro de la memoria de trabajo.

*   Cada registro tiene **8 bits** (numerados del 0 al 7).
*   Existen áreas específicas según el origen de los datos:
    *   **📥 Entradas (I/E):** Datos de la periferia (sensores, botones).
    *   **📤 Salidas (O/Q/A):** Accionamientos hacia dispositivos físicos.
    *   **内部 Marcas (M):** Uso interno, ideales para estados intermedios sin vínculo directo con la periferia.

---

## 📊 Tipos de Datos Elementales
Los datos en el PLC se definen según el uso y el tamaño necesario.

| Tipo de Dato | 🛠️ Descripción | 📐 Tamaño | 🔢 Rango/Valores |
| :--- | :--- | :--- | :--- |
| **BOOL** | Lógico | 1 bit | TRUE / FALSE |
| **BYTE** | Cadena de bits | 8 bits | 0 a 255 |
| **WORD** | Cadena de bits | 16 bits | 0 a 65,535 |
| **INT / UINT** | Enteros | 16 bits | -32,768 a 32,767 (INT) |
| **DWORD** | Cadena de bits | 32 bits | 0 a 4,294,967,295 |
| **DINT / UDINT** | Enteros dobles | 32 bits | ±2,147,483,647 |
| **REAL / FLOAT** | Decimales | 32 bits | Valores con decimales |
| **TIME** | Duración | 32 bits | T#... |

---

## 🔠 Uso de Constantes
Para valores fijos, utilizamos constantes con prefijos específicos:
*   **Enteros:** `Int#12456`
*   **Reales:** `Real#1.6e3`
*   **Word:** `Word#16#2F3E`
*   **Bool:** `Bool#1` o `True`
*   **Time:** `Time#1.64s`
*   **String:** `String# 'Pause?'`
