# 🪜 Lógica de Programación Ladder y Operaciones de Control

En esta **Clase 4**, el curso pasa de la configuración del entorno a la acción: la escritura de lógica en **Ladder Diagram (LD)**. Es una sesión fundamental para entender cómo el PLC toma decisiones basadas en estados binarios y variables de tiempo ⚡.

A continuación, el resumen de los puntos clave:

---

### 1. Instrucciones de Bit (Lógica Booleana) 🔢
Son los ladrillos básicos de cualquier programa en Allen Bradley. Se explica el concepto de **"continuidad lógica"**:

* **XIC (Examine if Closed - `] [`):** Actúa como un contacto normalmente abierto. Deja pasar la "corriente" lógica si el tag asociado es 1 (True) ✅.
* **XIO (Examine if Open - `]/[`):** Actúa como un contacto normalmente cerrado. Deja pasar la lógica si el tag asociado es 0 (False) ❌.
* **OTE (Output Energize - `( )`):** Es la bobina básica. Si hay continuidad en el peldaño (rung), el tag se pone en 1. Si se pierde la continuidad, vuelve a 0 💡.

---

### 2. Retentividad: OTL y OTU (Latch/Unlatch) 🔒
A diferencia de la OTE, estas instrucciones se usan en pareja para mantener un estado:

* **OTL (Output Latch - `(L)`):** Una vez que se activa, el tag permanece en 1 aunque la condición de entrada desaparezca 📌.
* **OTU (Output Unlatch - `(U)`):** Es la única forma de resetear un tag activado por un OTL para volverlo a 0 🔓.
* *Nota técnica:* Útiles para memorias de estado, pero requieren precaución para evitar condiciones de carrera ⚠️.

---

### 3. Temporizadores (Timers) ⏱️
Se analiza la estructura de datos tipo **TIMER**, que consta de tres valores principales (**PRE**, **ACC**, y bits de estado):

* **TON (Timer On Delay):** Retardo a la conexión. Empieza a contar cuando el renglón es verdadero ⏳.
* **TOF (Timer Off Delay):** Retardo a la desconexión. Mantiene la salida activa un tiempo después de que la entrada se apaga ⌛.
* **RTO (Retentive Timer On):** Similar al TON, pero no pierde el tiempo acumulado si el renglón se vuelve falso (requiere instrucción **RES**) 💾.

**Bits de estado del Timer:**
* **.EN (Enable):** El temporizador está energizado.
* **.TT (Timer Timing):** El temporizador está contando.
* **.DN (Done):** El tiempo acumulado llegó al valor preestablecido (Preset) 🏁.

---

### 4. Contadores (Counters) 🔢
Uso de la estructura **COUNTER** para eventos físicos o lógicos:

* **CTU (Count Up):** Incrementa el valor acumulado (.ACC) en cada flanco positivo ⬆️.
* **CTD (Count Down):** Decrementa el valor acumulado ⬇️.
* **RES (Reset):** Instrucción necesaria para llevar el contador de vuelta a cero 🔄.

---

### 5. Creación de Tags "al vuelo" 🚀
Optimización del flujo de trabajo:

* **Atajo Ctrl + W:** Para crear un tag inmediatamente después de escribir su nombre ⌨️.
* **Tipos de datos:** **BOOL** (bits), **DINT** (enteros) y estructuras complejas (**TIMER/COUNTER**) 📊.

---

### 6. Ediciones Online (Online Edits) ⚡
Modificar el código sin detener el proceso industrial:

* **Letras de edición:** `[I]` (Insert), `[D]` (Delete) y `[R]` (Replace) 📝.
* **Ciclo de edición:** *Start Pending Edits* -> *Accept* -> *Test* -> *Assemble* 🔄.

---

### 💡 Tip de Ingeniería
En Allen Bradley, el tiempo se expresa en **milisegundos**. Si quieres programar **5 segundos**, el valor de **PRE** debe ser **5000** 📏.
