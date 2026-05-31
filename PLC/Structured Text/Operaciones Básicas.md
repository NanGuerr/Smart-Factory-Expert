# 🧮 Operaciones Básicas (ST)

---

## 📘 Resumen 

Detalla las operaciones fundamentales necesarias para manipular datos en el lenguaje de Texto Estructurado (ST), incluyendo asignaciones, comparaciones, lógica booleana y cálculos aritméticos.

---

## 💾 1. Operación de Asignación (`:=`)
Equivalente al bloque `MOVE` en Ladder. Copia el valor de la derecha hacia la variable de la izquierda.
* **Ejemplo:** `A := 10;` o `A := B;`
* *Nota:* Los tipos de datos deben ser coincidentes.

---

## ⚖️ 2. Operadores de Comparación
Evalúan la relación entre dos variables y devuelven siempre un valor booleano (`TRUE` o `FALSE`).

* `=` (Igual)
* `<>` (Distinto)
* `<` (Menor)
* `<=` (Menor o igual)
* `>` (Mayor)
* `>=` (Mayor o igual)
* **Ejemplo:** `B := A < 5;` (Si A es 10, B será `FALSE`).

---

## 🧠 3. Operadores Lógicos (Booleanos)
Permiten realizar operaciones entre componentes lógicos (`TRUE`/`FALSE`).

* **AND / &**: Operación "Y".
* **OR**: Operación "O".
* **XOR**: O exclusivo.
* **NOT**: Negación.
* **Ejemplo:** `C := A OR B;`

---

## 🔢 4. Operaciones Aritméticas

### Básicas
* `+` (Adición)
* `-` (Sustracción)
* `*` (Multiplicación)
* `/` (División)
* **Ejemplo:** `C := A + B;`

### Avanzadas
* `**` (Exponenciación, ej: `B := A**2;`)
* **MOD** (Módulo o resto de la división)
* **MAX(var1, var2)**: Devuelve el valor mayor.
* **MIN(var1, var2)**: Devuelve el valor menor.
* **ABS(var)**: Valor absoluto.
* **LIMIT(VarMin, VarVal, VarMax)**: Limita un valor dentro de un rango definido.

---

## 💡 Recomendaciones de Programación
* **Prioridad:** Utiliza paréntesis `( )` para forzar el orden de resolución en ecuaciones complejas.
* **Tipos de Datos:** Asegúrate siempre de que las variables aritméticas sean numéricas (Int, Real) y las lógicas sean booleanas (Bool) para evitar errores de compilación.

---
