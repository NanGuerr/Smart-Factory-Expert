# ⚙️ Funciones (FC) en TIA Portal

Las **FCs** son bloques de código ideales para tareas que se repiten con diferentes datos, como cálculos matemáticos, conversiones o lógica combinacional.

* **Uso:** Se utilizan para modularizar el programa. Si tienes una lógica compleja (como un filtro de señal o un cálculo) que usas en 10 partes distintas de la máquina, escribes una sola FC y la llamas 10 veces, ahorrando espacio y errores.
* **No tienen memoria:** Al terminar su ejecución, los datos locales (TEMP) se pierden.
* **Interfaz:** Tienen parámetros de entrada (Input), salida (Output), entrada/salida (InOut) y variables temporales (Temp).

---

## 📝 Ejemplo: Cálculo de Promedio (4 Valores REAL)

Para este ejercicio, configuraremos una FC llamada `FC_CalcularPromedio`.

### 1. Interfaz de la FC (Tabla de variables del bloque)

| Nombre | Tipo | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `In_Valor1` | Input | REAL | Primer valor |
| `In_Valor2` | Input | REAL | Segundo valor |
| `In_Valor3` | Input | REAL | Tercer valor |
| `In_Valor4` | Input | REAL | Cuarto valor |
| `Out_Promedio` | Output | REAL | Resultado final |
| `Temp_Suma` | Temp | REAL | Variable interna para la suma |

### 2. Lógica en KOP (Ladder)

**Segmento 1: Suma de los 4 valores**
*(Usamos la instrucción `ADD` para sumar los 4 valores y guardarlos en la variable temporal `Temp_Suma`)*

```text
      "ADD_R" (Suma Real)
      +-------+
In1 --| EN    |
      |       |
In2 --|       |
      |       |--- [Temp_Suma]
In3 --|       |
      |       |
In4 --|       |
      +-------+

```

**Segmento 2: División para el promedio**
*(Dividimos la suma acumulada por 4.0 para obtener el promedio)*

```text
      "DIV_R" (División Real)
      +-------+
Temp_Suma --| EN    |
      |       |
4.0   --|       |--- [Out_Promedio]
      |       |
      +-------+

```

# ⚙️ Guía de Funciones (FC) en TIA Portal

Las **Funciones (FC)** son bloques de programación sin memoria propia, ideales para modularizar lógica reutilizable.

---

## 🛠️ ¿Qué son las FCs?
Una función es un bloque de código que ejecuta una tarea específica y devuelve un resultado. A diferencia de los FBs, no requieren un bloque de datos (DB) de instancia porque no guardan estados internos entre ciclos de escaneo.

### 📌 Uso y Funcionalidad
* **Modularización:** Divide un programa grande en piezas pequeñas y legibles.
* **Reutilización:** Escribe la lógica una vez y úsala en múltiples lugares.
* **Limpieza:** Facilita el mantenimiento; si debes corregir un cálculo, solo lo haces en la FC y se actualiza en todo el proyecto.

---

## 📊 Ejemplo: FC para Calcular Promedio (REAL)

A continuación, la estructura para realizar el promedio de 4 señales analógicas (tipo REAL) utilizando lenguaje **KOP (Ladder)**.

### 📋 Interfaz (Variables)
| Parámetro | Dirección/Tipo | Tipo de Dato |
| :--- | :--- | :--- |
| `In_Valor1` | Input | REAL |
| `In_Valor2` | Input | REAL |
| `In_Valor3` | Input | REAL |
| `In_Valor4` | Input | REAL |
| `Out_Promedio` | Output | REAL |
| `Temp_Suma` | Temp | REAL |

---

### 💻 Lógica en KOP (Ladder)

#### **Segmento 1: Sumatoria**
Se utiliza la instrucción `ADD_R` (Suma de reales).
* Conectas los 4 parámetros de entrada (`In_Valor1` a `In_Valor4`) a las entradas de la caja de suma.
* El resultado se almacena en la variable temporal `Temp_Suma`.

#### **Segmento 2: Promedio**
Se utiliza la instrucción `DIV_R` (División de reales).
* Entrada 1: `Temp_Suma`.
* Entrada 2: Constante `4.0` (valor fijo).
* Salida: `Out_Promedio`.

---

## 💡 Consejos de implementación
1. **Variables Temporales (Temp):** Siempre usa variables `TEMP` para cálculos intermedios (como la suma) dentro de la FC. Esto asegura que la memoria se gestione correctamente y no ocupes espacio en bloques de datos globales.
2. **Tipo de dato REAL:** Recuerda siempre usar las instrucciones de punto flotante (`ADD_R`, `DIV_R`). Si intentas usar instrucciones de enteros (`ADD_I`), el PLC dará error de compilación o resultados incorrectos al tratar decimales.
3. **Escalabilidad:** Si necesitas hacer promedio de 8 valores en lugar de 4, simplemente añade más entradas a la instrucción `ADD_R` y cambia el divisor a `8.0`.


### Puntos clave que incluí en el documento:

* **Diferenciación:** Por qué usar variables `TEMP` es vital en las FCs para mantener un código limpio y eficiente.
* **Instrucciones específicas:** Enfatizo el uso de `ADD_R` y `DIV_R`, ya que en TIA Portal es un error muy común intentar sumar valores reales con bloques de enteros.
* **Estructura:** La división en dos segmentos (Suma y División) que solicitaste para garantizar un flujo de datos ordenado.

