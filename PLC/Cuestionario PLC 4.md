# 📝 Cuestionario de Evaluación: Programación en Lista de Instrucciones (IL)

---

## 💡 Pregunta 1: Análisis de Operación Lógica
### Con la operación: 

```il
LD A
AND B
ANDN C
ST Lampara
```

```text
A         B         C       Lampara
——[ ]———————[ ]———————[/]————————( )——
```

**¿Qué estados deben tener las señales A, B y C para que la lámpara se encienda?**

* ⚪ `A = 0; B = 0; C = 1`
* ⚪ `A = 0; B = 1; C = 1`
* ⚫ **`A = 1; B = 1; C = 0` (Respuesta Correcta)**
* ⚪ `A = 1; B = 0; C = 1`

> - Contacto A (Normalmente Abierto): Necesita un 1 para cerrarse.
> - Contacto B (Normalmente Abierto): Necesita un 1 para cerrarse.
> - Contacto C (Normalmente Cerrado): Necesita un 0 para permanecer cerrado y dejar pasar la corriente.

---

## ⚡ Pregunta 2: Modificadores en IL
### ¿Qué especifica el modificador R?

* ⚪ `Falla`
* ⚪ `Bobina de Reset`
* ⚫ **`Detector de flanco positivo` (Respuesta Correcta)**
* ⚪ `Operación oR`

> (Nota: No debe confundirse el modificador R acoplado a una instrucción lógica con la instrucción R escrita de manera aislada en una línea, la cual sí actúa como la función de desenclavamiento o Bobina de Reset). La letra R (Rising): Le indica al PLC el momento exacto de la transición, es decir, cuando la señal cambia de Falso (0) a Verdadero (1). Este pulso especial dura únicamente un ciclo de programa (scan). 

---

## 🔀 Pregunta 3: Control de Flujo
### ¿Qué hace la operación JMPCN?

* ⚫ **`Salto condicional sólo si falso` (Respuesta Correcta)**
* ⚪ `Salto condicional sólo si verdadero`
* ⚪ `Salto incondicional`
* ⚪ `Ninguna de las anteriores`

> - JMP (Jump): Indica al procesador del PLC que debe realizar un salto en la secuencia de ejecución del programa hacia una etiqueta (Label) determinada.
> - C (Conditional): Especifica que el salto no es obligatorio, sino que está condicionado al valor lógico que se encuentre guardado en ese preciso instante en el acumulador.
> - N (Not): Invierte el sentido de la condición básica.

---

## 🧠 Pregunta 4: Evaluación de Acumulador
### Con la operación:
`LD A`
`GE B`
`ANDN C`
`ST Resultado`

**¿Cuál es el resultado del acumulador si A=10, B=5 y C=false?**

* ⚪ `10`
* ⚪ `5`
* ⚪ `False`
* ⚫ **`True` (Respuesta Correcta)**

---
**Documento Técnico de Evaluación** 🙌 _- INGELEARN_
