# 🧠 Acumuladores en Instruction List (IL)

Este documento profundiza en el funcionamiento del **Acumulador**, el componente central y más importante para la ejecución de la lógica en el lenguaje de bajo nivel Lista de Instrucciones (IL).

---

## 💾 ¿Qué es el Acumulador?

La Lista de Instrucciones (IL) es un lenguaje de programación totalmente **orientado a un acumulador**. 

* **Definición:** El acumulador es una pequeña memoria caché interna oculta dentro del procesador o memoria de trabajo del PLC.
* **Propósito:** Sirve como zona de paso temporal donde se "cargan" los estados de las entradas, salidas físicas o variables de memoria.
* **Versatilidad:** Puede almacenar tanto valores digitales (Booleanos: `0` o `1`) como valores numéricos analógicos (Enteros o Reales).

### ⚠️ Regla de Oro en IL
Toda secuencia lógica o cálculo matemático en IL debe comenzar obligatoriamente con la instrucción **LD** (Load). Cada vez que se invoca un comando `LD`, el valor anterior que residía en el acumulador es **sobreescrito por completo**, por lo que se debe planificar la secuencia de código con sumo cuidado.

---

## 📊 Caso Práctico y Análisis de Ejecución

Para comprender cómo muta el acumulador ciclo a ciclo, analizamos el procesamiento de la siguiente línea de código combinada (analógica y digital):

### 📝 Código en Lista de Instrucciones (IL)
```il
LD      VarA
LE      VarB
AND     VarC
ST      Res
