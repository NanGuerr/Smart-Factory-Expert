# 🧮 Operaciones Aritméticas y Transferencia

---
## 🔁 Operación de Transferencia: El Bloque MOVE

El bloque **MOVE** es una de las instrucciones más utilizadas en la programación de PLC. Su función principal es **copiar** el contenido de una variable o un valor constante directamente en otra variable de destino.

### 🧱 Estructura del Bloque MOVE

* **EN (Enable):** Entrada condicional de tipo Booleano (`Bool`). El bloque solo ejecuta la transferencia de datos cuando esta entrada recibe un flanco o señal activa (Verdadero).
* **IN:** El dato de origen que se desea copiar. Puede ser una constante numérica (ej. `100`, `50`) o una variable de memoria.
* **ENO (Enable Output):** Salida booleana que se activa para confirmar que la transferencia se realizó de manera exitosa.
* **OUT1:** La variable de destino donde se almacena el valor copiado desde `IN`.

---

## ➕ Operaciones Aritméticas Básicas

Los PLCs cuentan con bloques matemáticos predefinidos para realizar cálculos con números enteros o de punto flotante. Al igual que el bloque MOVE, estas funciones operan bajo el control de la entrada de habilitación **EN**.

### 🧩 Bloques Matemáticos Disponibles

* **ADD (Suma):** ➕ Realiza la adición de los valores presentes en sus entradas (ej. `IN1 + IN2`) y deposita el resultado en la variable conectada a la salida `OUT`.
* **SUB (Resta):** ➖ Resta el valor de la segunda entrada al de la primera (ej. `IN1 - IN2`) y guarda el resultado en `OUT`.
* **MUL (Multiplicación):** ✖️ Multiplica los valores de entrada (ej. `IN1 * IN2`) y entrega el producto en `OUT`.
* **DIV (División):** ➗ Divide el primer valor entre el segundo (ej. `IN1 / IN2`) y almacena el cociente en la salida `OUT`.

### 📝 Estructura General de los Bloques Aritméticos

* **EN:** Entrada de habilitación (`Bool`). Si está activa, se realiza la operación matemática.
* **IN1 / IN2:** Valores numéricos de entrada sobre los cuales se aplicará la operación.
* **ENO:** Salida de habilitación (`Bool`) que indica que la operación se procesó correctamente.
* **OUT:** Variable de destino donde se escribe el resultado numérico final.

---

# 📑 Resumen y Análisis: Shift / Rotate

El documento técnico detallado en **rotar y desplazar.png** explica el uso de funciones de desplazamiento de bits en controladores lógicos programables (PLC), una herramienta esencial cuando se requiere modificar los bits de una variable analógica de forma individual.

---

## 📝 Transcripción del Texto

> **Shift / Rotate**
> A veces, por una razón u otra puede llegar a ser necesario modificar los bits de una variable en forma individual.
> Para ello, existen unas funciones que permiten intercambiar o mover los bits dentro de una variable analógica.
> **Desplazar** mueve los bits de la variable que esté en la entrada IN, en un número entero igual al valor de N. Los valores que "desbordan" de la variable **se eliminan**, y los espacios blancos se rellenan con ceros.
> **Por ejemplo:**
> *(Se muestra un bloque SHL con entrada `VariableA`, parámetro `N = 3` y salida `VariableB`)*.

---

## ⚙️ Bloques Tecnológicos Identificados

La imagen presenta las dos funciones principales de desplazamiento (Shift):

* **SHL (Desplazar Izquierda / SHift Left):** Bloque que mueve los bits hacia la izquierda.
* **SHR (Desplazar Derecha / SHift Right):** Bloque que mueve los bits hacia la derecha.

### 🧩 Estructura Común de los Bloques:

* **EN (Enable):** Entrada de habilitación booleana.
* **IN:** Entrada de datos (variable analógica original).
* **N:** Cantidad de posiciones o bits a desplazar (número entero).
* **ENO (Enable Output):** Salida de habilitación booleana.
* **OUT:** Variable analógica resultante con los bits modificados.

---

## 📊 Análisis del Ejemplo Práctico (SHL con N = 3)

La ilustración gráfica de **rotar y desplazar.png** demuestra de manera muy clara qué ocurre internamente a nivel de bits cuando se ejecuta un desplazamiento a la izquierda por tres posiciones ($x3$):

1. **Estado Inicial (`VariableA`):** El registro analógico contiene la secuencia binaria de 8 bits: `1 0 1 0 1 1 1 0`.
2. **Desplazamiento y Desborde:** Al aplicar un desplazamiento de 3 posiciones hacia la izquierda, los tres bits más significativos de la izquierda (`1`, `0`, `1`) "desbordan" los límites del registro y **se eliminan automáticamente**.
3. **Relleno de Espacios Vacíos:** Los bits restantes (`0 1 1 1 0`) se mueven tres posiciones hacia la izquierda, dejando tres lugares vacíos en la parte derecha del registro (los bits menos significativos).
4. **Resultado Final (`VariableB`):** Estos espacios vacíos del final se rellenan con ceros (`0 0 0`), generando la nueva secuencia binaria resultante: `0 1 1 1 0 0 0 0`.

