# 🏭 Programación Combinacional

## 🧠 ¿Qué es la Programación Combinacional?
En este tipo de programación, el estado de las salidas depende directa y exclusivamente del estado actual de las entradas. 

* **Cero memoria:** La principal característica es que no se almacena en ninguna memoria el estado anterior de entradas o salidas.
* **Reacción inmediata:** En cuanto una entrada cambia, la salida se actualiza de inmediato, obteniendo siempre el mismo resultado para la misma combinación.
* **Señales:** Por lo general, se trabaja con señales booleanas.
* **Simplicidad:** Se pueden plantear y resolver fácilmente con papel y lápiz antes de pasarlos al PLC.

---

## 🔣 Simbología Lógica Fundamental
Para plantear las ecuaciones que resolverán el automatismo, se utiliza la siguiente notación:

* ➕ **Símbolo `+`:** Representa una operación lógica **OR**.
* ⏺️ **Símbolo `.`:** Representa una operación lógica **AND**.
* 🔢 **Valores `0` y `1`:** El `0` representa una señal Falsa (FALSE) y el `1` una señal Verdadera (TRUE).
* ❌ **Símbolo `X`:** Representa un valor indeterminado o *"Don't Care"* (no importa si es `0` o `1`).
* 🗜️ **Paréntesis `( )`:** Se usan para priorizar o agrupar operaciones.
* ➖ **Barra Superior ($\overline{A}$):** Indica que la variable o la operación matemática debajo de ella está **negada** (NOT).

---

## 📊 Tablas de Verdad
Son herramientas que permiten comprobar en qué estado deben estar las salidas en función de las combinaciones de las entradas. 

### 🛠️ Pasos para crear una Tabla de Verdad:
1. **Definir columnas:** Colocar todas las variables de entrada y luego las de salida.
2. **Calcular filas:** Se agregan filas utilizando la fórmula $2^N$, donde $N$ es el número de entradas del sistema.
3. **Llenar combinaciones:** Se rellenan las columnas de entradas con todas las combinaciones binarias posibles.
4. **Establecer salidas:** Se completa la columna de salida según los requerimientos lógicos del problema.

> 💧 **Ejemplo práctico del curso:** Un sistema con tres tanques (S1, S2, S3) que debe activar una alarma (AL) única y exclusivamente cuando hay exactamente **dos tanques llenos**. Si hay un solo tanque, los tres, o ninguno lleno, la alarma no suena.

---

## 🗺️ Simplificación: Mapas de Karnaugh
El mapa de Karnaugh es una estrategia visual muy útil, derivada de la tabla de verdad, para simplificar enormemente las ecuaciones booleanas de un sistema.

### 🧩 Reglas de Agrupación:
* **Potencias de 2:** Los `1`s se agrupan encerrándolos en círculos que formen rectángulos o cuadrados de 2, 4, 8 o 16 términos.
* **Eficiencia:** El objetivo es no dejar ningún `1` afuera usando la menor cantidad de figuras posibles.
* **Intersección:** Un mismo `1` puede pertenecer a varios grupos a la vez.
* **Comodines:** Las `X` ("Don't Care") pueden incluirse en un grupo para hacerlo más grande y simplificar más la ecuación, o dejarse por fuera si no aportan beneficio.
* **Simplificación Lógica:** Al agrupar, se eliminan las variables que resultan "ambiguas" (es decir, aquellas que dentro del mismo grupo valen `0` y `1` simultáneamente).
