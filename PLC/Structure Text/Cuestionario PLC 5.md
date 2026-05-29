# 📝 Cuestionario de Evaluación: Texto Estructurado (ST)

---

## 🔁 Pregunta 1: Análisis de bucles FOR
### ¿Cuántas veces se repetirá la operación dentro del FOR?
*FOR Cnt := 1 TO 9 BY 1 DO*

* ⚫ **`9 veces` (Respuesta Correcta)**
* ⚪ `1 vez`
* ⚪ `10 veces`
* ⚪ `20 veces`

> **💡 Explicación:** El bucle `FOR` se ejecuta desde el índice 1 hasta el 9 inclusive, lo que resulta en un total de 9 iteraciones.

---

## ❌ Pregunta 2: Diagnóstico de errores de sintaxis
### ¿Qué es lo que está fallando en la sección del programa?

* ⚫ **`Falta un punto y coma en una de las sentencias.` (Respuesta Correcta)**
* ⚪ `Tabulación errónea`
* ⚪ `AuxTempMaxima se llama al final sólo con minúsculas`
* ⚪ `Hay demasiado espacio blanco entre sentencias`

> **💡 Explicación:** En ST, cada línea de asignación debe finalizar con un punto y coma (`;`). La falta de este carácter impide que el compilador procese correctamente la instrucción antes del `END_IF`.

---

## 💬 Pregunta 3: Documentación del código
### ¿Qué símbolos se utilizan para realizar comentarios?

* ⚪ `//`
* ⚪ `**`
* ⚫ **`(* *)` (Respuesta Correcta)**

> **💡 Explicación:** Según la norma IEC 61131-3, los comentarios en Texto Estructurado se encierran entre `(*` para abrir y `*)` para cerrar.

---

## 🧮 Pregunta 4: Operaciones matemáticas y MOD
### ¿Cuál es el resultado de la operación `C := (A ** B) MOD 30;` si A = 10 y B = 2?

* ⚪ `25`
* ⚪ `100`
* ⚪ `2`
* ⚫ **`10` (Respuesta Correcta)**

> **💡 Explicación:** Primero, $10^2 = 100$. Luego, al dividir 100 entre 30, obtenemos un cociente de 3 y un residuo (MOD) de 10.

---

## 📈 Pregunta 5: Acumulación de variables
### ¿Cuál es el resultado de la operación `Cuenta := Cuenta + 3;` luego de 5 iteraciones? (Iniciando en 0)

* ⚪ `5`
* ⚪ `3`
* ⚪ `0`
* ⚫ **`15` (Respuesta Correcta)**

> **💡 Explicación:** La operación suma 3 unidades a la variable en cada iteración. Tras 5 pasos, el acumulado es $3 \times 5 = 15$.

---
**Documento Técnico de Evaluación** 
