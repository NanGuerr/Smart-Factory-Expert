# 📑 Guía de Ejercicios Resueltos: Lenguaje LADDER (V1)

---

## 📘 Resumen de la Guía

Este documento técnico contiene la resolución conceptual y el análisis de la guía de trabajos prácticos **PL0-0324**, enfocada en el diseño de lógica de control industrial mediante **Diagrama de Contactos (Ladder Diagram - LD)**. Abarca desde el manejo básico de bits hasta funciones avanzadas como temporización, conteo, comparación y aritmética en controladores lógicos programables (PLC).

---

## 🔌 1. Manejo Básico de Bits

### 🟢 Ejercicio 1.1: Activación Simultánea

* **Requerimiento:** Encender las salidas `Q1.0` y `Q2.0` al presionar el botón `I2.0`.
* **Lógica en Ladder:** Un contacto normalmente abierto (NO) asociado a `I2.0` alimenta en paralelo dos bobinas de salida independientes, `Q1.0` y `Q2.0`.

### 🔴 Ejercicio 1.2: Lógica Inversa (NC)

* **Requerimiento:** Mantener `Q5.0` encendida mientras `I5.1` esté sin actuar. Al activarse `I5.1`, `Q5.0` debe apagarse.
* **Lógica en Ladder:** Se utiliza un único contacto normalmente cerrado (NC) asignado a `I5.1` conectado de forma directa a la bobina `Q5.0`. Al abrirse el contacto físico, la bobina se desenergiza.

### 🔀 Ejercicio 1.3: Combinatoria de Contactos

* **Requerimiento:** Encender `Q3.2` cuando estén presentes `I1.1` e `I2.1` (NO), pero `I3.4` esté ausente (NC).
* **Lógica en Ladder:** Conexión en serie (función lógica AND) de dos contactos normalmente abiertos (`I1.1` e `I2.1`) junto con un contacto normalmente cerrado (`I3.4`), rematando en la bobina `Q3.2`.

---

## ⏱️ 2. Temporizadores, Detectores de Flanco y Set/Reset

### 🔒 Ejercicio 2.1: Enclavamiento Clásico (Set/Reset)

* **Requerimiento:** Encender `Q2.3` con el pulso `I2.3` (retener al soltar). Apagar con el botón `I3.5`.
* **Lógica en Ladder:** Se implementa mediante una instrucción de memoria **SET** para `Q2.3` comandada por `I2.3`, y una instrucción **RESET** para `Q2.3` comandada por `I3.5`. El reset posee prioridad de parada ante accionamientos simultáneos.

### ⏱️ Ejercicio 2.2: Temporizador por Pulso Único (TP)

* **Requerimiento:** Al activar `I3.6`, encender `Q5.2` por 5 segundos exactos. Exigir flanco (no repetir si se mantiene presionado).
* **Lógica en Ladder:** La señal `I3.6` ingresa a un detector de flanco ascendente (`P_TRIG`). La salida de este flanco se conecta a la entrada `IN` de un temporizador tipo pulso (**TP**) configurado con `PT := T#5s`. La salida `Q` del bloque temporizador maneja a `Q5.2`.

### 📈 Ejercicio 2.3: Temporización al Flanco de Bajada

* **Requerimiento:** Al presionar y *luego soltar* `I5.3`, activar `Q9.2` durante 5 segundos.
* **Lógica en Ladder:** Se coloca un detector de flanco descendente (`N_TRIG`) asociado a la entrada `I5.3`. Su salida dispara la entrada `IN` de un bloque temporizador **TP** con un parámetro `PT := T#5s`. La salida del bloque gobierna la bobina `Q9.2`.

### 🚀 Ejercicio Desafío: Control de Bomba Monofuncional (Flip-Flop)

* **Requerimiento:** Encender y apagar una bomba (`%Q0.3`) utilizando un único botón pulsador (`%I0.5`).
* **Lógica en Ladder:** 1. El pulsador `%I0.5` pasa por un detector de flanco de subida (`P_TRIG`) para capturar un solo pulso por pulsación.
2. Este pulso se multiplica mediante compuertas lógicas (contactos): si la bomba `%Q0.3` está apagada (contacto NC), el pulso activa una marca interna de encendido. Si la bomba ya está encendida (contacto NO), el pulso activa una marca interna de apagado.
3. Estas marcas ejecutan las funciones de **SET** y **RESET** sobre la salida de la bomba `%Q0.3` de forma cruzada, invirtiendo su estado con cada pulsación.

---

## 🔄 3. Bloques Comparadores

### 📊 Ejercicio 3.1: Control de Presión Fuera de Rango (Alarma Diferida)

* **Requerimiento:** Monitorear la presión en `%MD30` ("PRES"). Rango normal: 1 a 7 bar. Si sale del rango por más de 10 segundos, activar alerta `%Q3.0`. Si todo está correcto, activar `%M5.5` ("PRES_OK").
* **Lógica en Ladder:**
* Se utilizan dos bloques de comparación: Menor que (`< 1`) y Mayor que (`> 7`) conectados en paralelo (función lógica OR) para determinar la condición de "Falla de Presión".
* La salida de esta anomalía activa la entrada `IN` de un temporizador con retardo a la conexión (**TON**) configurado con `PT := T#10s`. Al cumplirse el tiempo, la salida `Q` enciende de forma sostenida la alerta `%Q3.0`.
* En paralelo, un contacto cerrado de la alerta `%Q3.0` (o la negación de la condición de falla inmediata) energiza la marca de estado óptimo `%M5.5`.



### 🛑 Ejercicio 3.2: Enclavamiento de Ventilador con Disparo por Velocidad

* **Requerimiento:** Arranque (`%I0.2`) y parada (`%I0.3`) de un ventilador (`%Q0.3`). Si la lectura escalada de velocidad `%MD4` ("VEL_VENT") supera las 250 rpm, detener inmediatamente.
* **Lógica en Ladder:**
* Se utiliza un bloque de comparación Mayor que (`>`) que evalúa si `%MD4` es superior a `250.0`.
* La salida de este comparador se conecta en paralelo con el botón de parada física `%I0.3` para activar la bobina de **RESET** del ventilador `%Q0.3`. El botón de arranque `%I0.2` se conecta de forma directa al renglón de **SET**.



---

## 🔢 4. Bloques Contadores

### 📈 Ejercicio 4.1: Conteo de Cajas en Cinta

* **Requerimiento:** Contar 10 cajas detectadas por el sensor `%I0.7` ("FC_CAJA") para encender la marca `%M4.2` ("MONT_LLENO"). Resetear con la entrada `%I1.2` ("MONT_VACIO").
* **Lógica en Ladder:** Se implementa un bloque contador ascendente (**CTU**). El sensor `%I0.7` se cablea a la entrada de conteo `CU`. La entrada de restauración `R` se asocia directamente a `%I1.2`. El valor de consigna se fija en `PV := 10`. Al completarse la cuenta, la salida `Q` energiza de manera automática la marca `%M4.2`.

### 🤝 Ejercicio 4.2: Coincidencia de Pulsación Simultánea

* **Requerimiento:** Encender la salida `%Q0.3` tras presionar 5 veces de forma simultánea (a la vez) los botones `%I0.3` y `%I0.7`.
* **Lógica en Ladder:** Se añade un bloque lógico AND uniendo los contactos NO de `%I0.3` e `%I0.7`. Esta combinación en serie se conecta a un detector de flanco de subida (`P_TRIG`), garantizando que solo registre un conteo por cada activación simultánea real. La salida del flanco se lleva al pin `CU` de un contador **CTU** configurado con `PV := 5`. La salida `Q` del contador activa directamente la bobina `%Q0.3`.

---

## 🔀 5. Transferencia de Datos (MOVE)

### ⚙️ Ejercicio 5.1: Selector Multi-Velocidad de Consigna

* **Requerimiento:** Cargar valores reales de velocidad en `%MD4` ("CONSIGNA_VEL") mediante la activación de 5 marcas booleanas excluyentes (`V1` a `V5`).
* **Lógica en Ladder:** Se estructuran 5 renglones independientes utilizando el bloque **MOVE**:
* Contacto de `V1` habilita bloque `MOVE` con `IN := 0.0` y `OUT1 := %MD4`.
* Contacto de `V2` habilita bloque `MOVE` con `IN := 20.0` y `OUT1 := %MD4`.
* Contacto de `V3` habilita bloque `MOVE` con `IN := 40.0` y `OUT1 := %MD4`.
* Contacto de `V4` habilita bloque `MOVE` con `IN := 80.0` and `OUT1 := %MD4`.
* Contacto de `V5` habilita bloque `MOVE` con `IN := 150.0` y `OUT1 := %MD4`.



---

## 🧮 6. Operaciones Aritméticas Complejas

### ✖️ Ejercicio 6.1: Optimización de Ecuación Polinómica

* **Requerimiento:** Resolver la ecuación: $VAR\_RESULTADO = (VAR1 \times X) + (VAR2 \times X) + (VAR3 \times X) + (VAR4 \times X) + (VAR5 \times X)$ empleando números de punto flotante (Real).
* **Análisis Algebraico:** Aplicando la propiedad distributiva del factor común, la ecuación se simplifica drásticamente para ahorrar procesamiento en el PLC:

$VAR\_RESULTADO = (VAR1 + VAR2 + VAR3 + VAR4 + VAR5) \times X$

* **Lógica en Ladder:** 1. Se utiliza un bloque de suma **ADD** extendido (añadiendo pines de entrada adicionales) para procesar de una sola vez la adición de `VAR1 + VAR2 + VAR3 + VAR4 + VAR5`, guardando el subtotal en una variable de marca auxiliar `%MD100` (`AUX_SUMA`).
2. En el siguiente renglón, un bloque de multiplicación **MUL** toma la variable `AUX_SUMA` en su entrada `IN1` y la variable `X` en su entrada `IN2`, depositando el producto final directamente en `VAR_RESULTADO`.

### ➗ Ejercicio 6.2: Intercepción y Protección por División por Cero

* **Requerimiento:** Detectar si el divisor de un bloque `DIV` (`VarB`) toma el valor de `0` en un HMI. Si esto ocurre, disparar una alarma sonora `%Q0.1` durante un intervalo de 5 segundos.
* **Lógica en Ladder:**
* Se inserta un bloque de comparación de igualdad (**EQ**) antes de efectuar la división matemática, validando si `VarB == 0.0`.
* La salida verdadera de esta comparación actúa como un enclavamiento de seguridad que bloquea la ejecución del bloque `DIV` (para evitar fallas por excepción de hardware en el procesador del PLC).
* Simultáneamente, este pulso de igualdad activa la entrada `IN` de un temporizador de pulso (**TP**) parametrizado con `PT := T#5s`. La salida `Q` de este temporizador energiza la salida digital física `%Q0.1` (`Al_Sonora`), garantizando que la alarma se mantenga activa durante el tiempo programado.

