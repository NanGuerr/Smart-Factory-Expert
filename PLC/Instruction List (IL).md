# 🛠️ Instrucciones Básicas en Instruction List (IL)

Esta sección se centra en la **Simbología Básica y las Instrucciones Elementales** del lenguaje de programación Lista de Instrucciones (IL). Aquí se estudian los operadores indispensables para realizar cargas en memoria, operaciones lógicas combinacionales, agrupamientos complejos mediante paréntesis y funciones de comparación analógica.

---

## 📋 Clasificación de Instrucciones Básicas

### 📥 1. Cargar Acumulador (Load) y Almacenamiento (Store)
Estas instrucciones gestionan el movimiento inicial y el destino de los bits dentro del registro del acumulador del PLC:

* **LD (Load):** Carga el valor del operando directamente en el acumulador (equivalente a un contacto normalmente abierto `—[ ]—`).
* **LDN (Load Not):** Carga el valor de forma invertida o negada (equivalente a un contacto normalmente cerrado `—[/]—`).
* **LDR (Load Rising):** Carga basándose en un detector de flanco ascendente (contacto de flanco de subida `—[P]—`).
* **LDF (Load Falling):** Carga basándose en un detector de flanco descendente (contacto de flanco de bajada `—[N]—`).
* **ST (Store):** Almacena el resultado actual del acumulador en la variable asignada (bobina simple `—( )—`).
* **STN (Store Not):** Almacena el resultado del acumulador de forma invertida (bobina negada `—(/)—`).
* **S (Set):** Enclava permanentemente la variable en verdadero si el acumulador es `1` (bobina de Set `—(S)—`).
* **R (Reset):** Desenclava permanentemente la variable a falso si el acumulador es `1` (bobina de Reset `—(R)—`).

---

### 🔀 2. Operaciones Lógicas Combinacionales (AND / OR)
Permiten encadenar condiciones lógicas en serie o en paralelo con el valor que ya se encuentra en el acumulador:

* **AND / ANDN:** Realizan la operación lógica "Y" con el operando de forma directa o negada (conexión en serie).
* **ANDR / ANDF:** Aplican la operación "Y" condicionada a un flanco de subida o de bajada del operando.
* **OR / ORN:** Realizan la operación lógica "O" con el operando de forma directa o negada (conexión en paralelo).
* **ORR / ORF:** Aplican la operación "O" condicionada a un flanco de subida o de bajada del operando.

---

### 🧩 3. El Uso de Paréntesis `()`
Los paréntesis se emplean para agrupar, anidar instrucciones y estructurar combinaciones lógicas complejas que alteran la prioridad de ejecución secuencial.

* **Sintaxis:** La apertura del paréntesis se añade como un **modificador** pegado directamente al operador principal (por ejemplo: `AND(` u `OR(`), mientras que el cierre del paréntesis `)` se escribe en una línea de código completamente independiente.

> **Ejemplo de aplicación:**

```text

LD      M1.0                   │       M1.0             I1.3                 Q2.1
AND(    I1.3   ------------>   ├───────┤ ├───────┬───────┤ ├───────┐─────────( )──
ORN     I1.4     LADDER        │                 │      I1.4       │
)                              │                 └───────┤\├───────┘
ST      Q2.1

```

### 📊 4. Bloques Comparadores Analógicos
Se utilizan para evaluar variables numéricas (enteras o reales). El resultado de la comparación pasa al acumulador como un valor booleano (`0` o `1`):

* **GT (Greater Than):** Mayor que (`>`).
* **GE (Greater or Equal):** Mayor o igual que (`>=`).
* **EQ (Equal):** Igual a (`==`).
* **LE (Less or Equal):** Menor o igual que (`<=`).
* **LT (Less Than):** Menor que (`<`).
* **NE (Not Equal):** Distinto o diferente de (`<>`).

---
