# 📊 Almacenamiento de Datos en Arrays (ST)

---

## 📘 Resumen 

Explica cómo utilizar **Arrays** (arreglos o vectores) en lenguaje Texto Estructurado (ST). Los arrays son estructuras de datos que permiten almacenar múltiples valores del mismo tipo bajo un solo nombre, facilitando operaciones complejas como promedios históricos, registros de datos (datalogging) y monitoreo de sensores.

---

## 🏗️ ¿Qué es un Array?
Un array es una colección ordenada de elementos. En lugar de crear diez variables separadas para diez mediciones de temperatura (`Temp0`, `Temp1`, ..., `Temp9`), definimos un solo array `Temp[0..9]`.

* **Índice:** Es la posición del valor dentro del array (comienza usualmente en `0`).
* **Ventaja:** Permite manipular grandes volúmenes de datos mediante bucles (`FOR`).

---

## 🧠 Lógica de Almacenamiento (Desplazamiento)
Para mantener un historial (por ejemplo, las últimas 10 mediciones), cada vez que llega un nuevo dato, debemos "mover" los valores existentes para hacer espacio al nuevo.

### 🔄 Algoritmo de desplazamiento:
1. El valor de la posición `[8]` pasa a `[9]`.
2. El valor de la posición `[7]` pasa a `[8]`.
3. ... y así sucesivamente hasta el `[0]`.
4. El nuevo dato se escribe en la posición `[0]`.

```st
(* Desplazamiento de mediciones *)
FOR i := 0 TO 8 BY 1 DO
    Temp[9-i] := Temp[8-i];
END_FOR;

(* Inserción del nuevo dato *)
Temp[0] := LecTemp;

```

---

## 🧮 Cálculo de Promedios con Bucles

Una vez almacenados los datos, recorrer el array para calcular el promedio es muy eficiente usando un bucle `FOR`.

```st
(* Cálculo del promedio de las últimas 10 mediciones *)
PromTemp := 0;

FOR j := 0 TO 9 BY 1 DO
    PromTemp := PromTemp + Temp[j];
END_FOR;

PromTemp := PromTemp / 10;

```

---

## 💡 Recomendaciones de Programación

* **Límites:** Asegúrate siempre de que el índice del array (`i` o `j`) nunca exceda los límites definidos (ej. `0` a `9`), de lo contrario, el PLC generará un error de desbordamiento.
* **Eficiencia:** El uso de bucles para recorrer arrays es una de las características más potentes de ST frente a Ladder, ya que reduce drásticamente la cantidad de líneas de código necesarias para tareas repetitivas.
* **Documentación:** Comenta siempre qué representa el array y qué unidad de medida almacena.

---
