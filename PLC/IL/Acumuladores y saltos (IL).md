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
```

## 📌 Conceptos Clave: Etiquetas (Labels)

Para poder realizar un salto de programa, primero es obligatorio identificar el destino de llegada mediante una **Etiqueta (Label)**.

* **Metodología:** Se escribe el nombre de la etiqueta deseada seguido de dos puntos (`:`) justo antes de la instrucción `LD` que da inicio a esa nueva sección o etapa.
* **Ejemplo de sintaxis:** `Etapa3C: LD VarA`

---

## ⚡ Clasificación de los Saltos de Programa

Los saltos en el lenguaje IL se clasifican principalmente en dos categorías según dependan o no del estado del acumulador:

### 🌐 1. Saltos No Condicionales (Incondicionales)
Se ejecutan de forma obligatoria siempre que el programa llega a la instrucción, sin importar el valor o estado lógico en el que se encuentre el acumulador.

* **Operador:** **JMP** (Jump), seguido del nombre de la etiqueta de destino.
* **Comportamiento:** Al llegar a esta línea, el PLC interrumpe la lectura secuencial y se desplaza inmediatamente a la etiqueta indicada, ignorando las líneas de código intermedias.

---

### 🚦 2. Saltos Condicionales
Este tipo de saltos solo se concreta si se cumple una condición específica basada en el estado lógico booleano (`True` o `False`) que posea el acumulador en ese preciso instante.

Se utilizan los siguientes operadores con modificadores:

* **JMPC:** El salto se realiza **sí, y solo sí**, el resultado actual dentro del acumulador es **Verdadero (True / 1)**. Si es falso, el PLC ignora el salto y continúa con la línea inmediatamente inferior.
* **JMPCN:** El salto se realiza **sí, y solo sí**, el resultado actual dentro del acumulador es **Falso (False / 0)**. Si es verdadero, el PLC no salta y sigue ejecutando de forma secuencial.

---

## 🏢 Aplicación en la Estructuración del Programa

El uso estratégico de los saltos (tanto condicionales como incondicionales) permite segmentar un programa complejo en múltiples bloques lógicos independientes (por ejemplo: `Etapa 1`, `Etapa 2A`, `Etapa 2B`, `Etapa 3A`, etc.). 

Esto permite que, en función de las selecciones del operario o de las condiciones de seguridad de la máquina, el PLC cambie por completo su comportamiento dinámico en tiempo de ejecución, optimizando el tiempo de ciclo de scan al omitir bloques de código que no se necesitan en un momento dado.

---
