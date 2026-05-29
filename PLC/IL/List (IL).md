# 📝 El Lenguaje Instruction List (IL)

---

## ⚙️ Metodología del Lenguaje IL

El lenguaje IL consiste en una secuencia estructurada de instrucciones escritas de forma puramente textual. Su lógica se procesa de manera secuencial línea por línea.

### 🧱 Estructura de una Línea de Código
Cada instrucción comienza en una nueva línea y se compone de la siguiente estructura básica:
* **Operador:** Define la acción o función matemática/lógica a realizar.
* **Modificador (Opcional):** Altera el comportamiento del operador (por ejemplo, añadiendo una negación `N`).
* **Operando:** El objeto sobre el cual actúa el operador (puede ser una variable, un valor constante o una instancia de función).

> **Ejemplo de sintaxis:**
> `LDN I1.2`  *(Carga la entrada I1.2 de forma negada)*
> `ST Q0.0`   *(Almacena el resultado en la salida Q0.0)*

⚠️ **Nota de Seguridad:** Debido a la libertad que posee este lenguaje para realizar saltos entre distintas líneas de código, se debe tener especial cuidado al programar, ya que es altamente susceptible a errores en tiempo de ejecución o a la creación de bucles (loops) infinitos que bloqueen el procesador.

---

## 🔄 Comparativa: Ladder Diagram (LD) vs. Instruction List (IL)

A continuación se muestra la equivalencia directa entre los circuitos gráficos en Ladder y las instrucciones de texto en IL:

| Tipo de Circuito (LD) | Representación Gráfica | Código en Lista de Instrucciones (IL) |
| :--- | :---: | :--- |
| **Contacto Directo** | `—[ ]—` | `LD A`<br>`ST X` |
| **Contacto Negado** | `—[/]—` | `LDN A`<br>`ST X` |
| **Conexión en Serie (AND)** | `—[ ]—[ ]—` | `LD A`<br>`AND B`<br>`ST X` |
| **Conexión en Serie con Negación** | `—[ ]—[/]—` | `LD A`<br>`ANDN B`<br>`ST X` |
| **Conexión en Paralelo (OR)** | `—[ ]—`<br>`—[ ]—` | `LD A`<br>`OR B`<br>`ST X` |
| **Circuitos Combinados Complejos** | Agrupaciones de ramas | Se utilizan operadores de bloque como `ANB` (AND Block) u `ORB` (OR Block) junto con paréntesis para priorizar ecuaciones complejas. |

---
