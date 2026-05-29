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

