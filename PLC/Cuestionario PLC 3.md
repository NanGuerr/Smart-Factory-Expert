# 📝 Cuestionario Técnico: Programación en Lenguaje LADDER y Bloques Lógicos

---

## 🔌 Pregunta 1: Análisis de Continuidad Eléctrica
### ¿Qué estado deben tener los botones A y B, para que la lámpara C se encienda? 💡

```text
    "A"                  "B"                 "C"
   %I0.1                %I1.0               %Q0.0
────┤   ├───────────────┤ / ├─────────── ────( )────
────┤ / ├───────────────┤   ├─────────── ────( )────

```

* ⚪ `A = 1; B = 1`
* ⚫ **`A = 1; B = 0` (Respuesta Correcta)**
* ⚪ `A = 0; B = 1`
* ⚪ `A = 0; B = 0`

---

## ⏱️ Pregunta 2: Comportamiento de Señales y Temporizadores
### Si dejo pulsado el botón A, cuánto tiempo se mantendrá encendida la salida C? 🔄

```text
    "A"                                     "C"
   %I0.1                                    %Q0.0
────┤ P ├────────────────────────────────────( )────

```

* ⚪ `Un ciclo de programa`
* ⚪ `2 segundos`
* ⚫ **`Se mantendrá hasta que se deje de pulsar el botón` (Respuesta Correcta)**
* ⚪ `Se mantendrá hasta que no se resetee con una instrucción -(R)`

---

## ⏱️ Pregunta 3: Comportamiento de Señales y Temporizadores
### Si dejo pulsado el botón A, cuánto tiempo se mantendrá encendida la salida C? 🔄

```text
    "A"                                      "C"
   %I0.1                                    %Q0.0
────┤ N ├────────────────────────────────────( )────

```

* ⚪ `Un ciclo de programa`
* ⚪ `Se mantiene encendida mientras tenga pulsado el botón`
* ⚫ **`No se enciende` (Respuesta Correcta)**
* ⚪ `Se mantendrá hasta que no se resetee con una instrucción -(R)`

---

## 🧮 Pregunta 4: Ecuaciones Matemáticas en Bloques
### ¿A qué ecuación puede describir las operaciones que están realizando estos bloques encadenados? 📐

│              ┌─────────┐                               ┌─────────┐                               ┌─────────┐
│              │   ADD   │                               │   MUL   │                               │   DIV   │
├──────────────┤ EN   ENO├───────────────────────────────┤ EN   ENO├───────────────────────────────┤ EN   ENO├──
│  ┌───────┐   │         │    ┌──────┐       ┌──────┐    │         │    ┌──────┐       ┌──────┐    │         │   ┌─────────┐
│  │NumeroA├───┤ IN1  OUT├────┤ AuxA │       │ AuxA ├────┤ IN1  OUT├────┤ AuxB │       │ AuxB ├────┤ IN1  OUT├───┤Resultado│
│  └───────┘   │         │    └──────┘       └──────┘    │         │    └──────┘       └──────┘    │         │   └─────────┘
│  ┌───────┐   │         │                   ┌──────┐    │         │                   ┌───────┐   │         │
│  │NumeroB├───┤ IN2     │                   │ 5.0  ├────┤ IN2     │                   │NumeroC├───┤ IN2     │
│  └───────┘   └─────────┘                   └──────┘    └─────────┘                   └───────┘   └─────────┘

* ⚪ `Resultado = (NumeroC / 5) * NumeroA + NumeroB`
* ⚪ `Resultado = NumeroA / Numero C * 5 + NumeroB / NumeroC`
* ⚫ **`Resultado = (NumeroA + Numero B) * 5 / Numero C` (Respuesta Correcta)**

---

## ⚙️ Pregunta 5: Prioridad de Ejecución y Consignas
### ¿Cuál será la consigna final de velocidad si se activan las entradas 1, 3 y 5 simultáneamente? 🏁

* ⚪ `0`
* ⚫ **`100` (Respuesta Correcta)**
* ⚪ `120`
* ⚪ `20`

---
**Documento Técnico de Evaluación** 🙌 _- INGELEARN_
