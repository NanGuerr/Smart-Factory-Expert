# 📑 PL0-0324 - Guía de Ejercicios Resueltos: LADDER (V1)

---

## 📘 Resumen de la Guía
Este documento recopila las soluciones lógicas y criterios de diseño en **Diagrama de Contactos (Ladder Diagram)** para resolver problemas comunes de automatización y control de procesos en PLCs. Cubre desde operaciones lógicas combinacionales binarias hasta manipulación de registros lógicos y aritméticos.

---

## 🔌 1. Manejo Básico de Bits

### 🟢 Ejercicio 1.1: Encendido en Paralelo
* **Requerimiento:** Encender las salidas `Q1.0` y `Q2.0` al presionar el botón `I2.0`.
* **Lógica Ladder:** Un contacto Normalmente Abierto (NO) referenciado a `I2.0` se conecta en un ramal paralelo directo hacia dos bobinas de salida: `Q1.0` y `Q2.0`.

### 🔴 Ejercicio 1.2: Lógica Inversa (Contacto Cerrado)
* **Requerimiento:** Mantener `Q5.0` encendida mientras `I5.1` esté sin actuar. Cuando `I5.1` se actúe, `Q5.0` debe apagarse.
* **Lógica Ladder:** Se utiliza un contacto Normalmente Cerrado (NC) de la entrada `I5.1` en serie con la bobina `Q5.0`. Mientras la entrada permanezca en nivel lógico bajo (`0`), el camino retiene continuidad hacia la salida.

### 🔀 Ejercicio 1.3: Combinatoria de Contactos
* **Requerimiento:** Encender `Q3.2` cuando estén activas las entradas `I1.1` e `I2.1` (NO), pero `I3.4` no esté presente (NC).
* **Lógica Ladder:** Se realiza una compuerta lógica AND cableando en serie dos contactos Normalmente Abiertos (`I1.1` e `I2.1`) y un contacto Normalmente Cerrado (`I3.4`) para energizar la bobina de salida `Q3.2`.

---

## ⏱️ 2. Temporizadores, Detectores de Flanco y Set / Reset

### 🔒 Ejercicio 2.1: Enclavamiento Biestable (Set / Reset)
* **Requerimiento:** Al presionar el botón `I2.3`, `Q2.3` debe encenderse y mantenerse retenida al soltar el pulsador. Con el botón `I3.5`, `Q2.3` debe apagarse.
* **Lógica Ladder:** Se implementa una instrucción **SET** para la variable `Q2.3` asociada al contacto NO de la entrada `I2.3`, y una instrucción **RESET** para `Q2.3` controlada por el contacto NO de `I3.5`. El reset suele priorizarse por seguridad.

### ⏱️ Ejercicio 2.2: Temporizador de Pulso Único (TP) con Flanco
* **Requerimiento:** Al activar `I3.6` y mantenerlo presionado, se enciende `Q5.2` por 5 segundos y se apaga de forma automática. No debe reencenderse hasta soltar y volver a presionar.
* **Lógica Ladder:** La entrada `I3.6` se conecta a un bloque detector de flanco ascendente (`P_TRIG`). El pulso de salida del flanco se asocia a la entrada `IN` de un temporizador de pulso (**TP**) configurado con un tiempo preestablecido `PT := T#5s`. La salida `Q` del temporizador comanda la bobina `Q5.2`.

### 📈 Ejercicio 2.3: Temporización al Flanco de Bajada
* **Requerimiento:** Al presionar y *luego soltar* `I5.3`, la salida `Q9.2` debe encenderse por 5 segundos.
* **Lógica Ladder:** Se emplea un bloque de detección de flanco descendente (`N_TRIG`) condicionado por la variable de entrada `I5.3`. Su salida activa la entrada `IN` de un temporizador **TP** con un parámetro `PT := T#5s`, mandando la señal hacia `Q9.2`.

### 🚀 Ejercicio Desafío: Alternador Bifuncional (Un Solo Botón)
* **Requerimiento:** Encender y apagar una bomba (`%Q0.3`) utilizando un único pulsador físico cableado en `%I0.5`.
* **Lógica Ladder:**
    1. La entrada `%I0.5` se evalúa mediante un flanco ascendente (`P_TRIG`) para obtener un disparo de un solo ciclo de scan por pulsación.
    2. El disparo del flanco alimenta dos líneas paralelas interbloqueadas: una línea conecta un contacto NC de la propia bomba `%Q0.3` a una bobina **SET** de `%Q0.3`; la otra línea conecta un contacto NO de la bomba `%Q0.3` a una bobina **RESET** de `%Q0.3`. De esta manera, cambia de estado con cada pulso.

---

## 🔄 3. Bloques Comparadores

### 📊 Ejercicio 3.1: Control e Histéresis de Presión
* **Requerimiento:** Medir presión en `%MD30` ("PRES") con rango normal de 1 a 7 bar. Si sale del rango por 10 segundos o más, encender alerta `%Q3.0`. Caso contrario, activar `%M5.5` ("PRES_OK").
* **Lógica Ladder:**
    * Se emplean comparadores lógicos: Menor que (`LT < 1.0`) y Mayor que (`GT > 7.0`) evaluando el registro `%MD30`.
    * Las salidas de ambos comparadores se asocian en paralelo (compuerta lógica OR) y se conectan a la entrada `IN` de un temporizador con retardo a la conexión (**TON**) con `PT := T#10s`. Al cumplirse el tiempo en falla, se energiza el bit `%Q3.0`.
    * La marca `%M5.5` ("PRES_OK") se activa colocando un contacto inversamente cerrado (NC) de la alarma `%Q3.0` (o negando la condición instantánea de los comparadores).

### 🛑 Ejercicio 3.2: Protección de Sobrevelocidad en Ventilador
* **Requerimiento:** Arrancar con `%I0.2` y parar con `%I0.3` un ventilador `%Q0.3`. Si el sensor escalado de velocidad `%MD4` ("VEL_VENT") supera las 250 rpm, apagar de inmediato.
* **Lógica Ladder:** El circuito tradicional de arranque/parada por memoria (Set/Reset) se complementa implementando un bloque comparador Mayor que (`GT > 250.0`) sobre la variable `%MD4`. La salida de este bloque comparador se vincula en paralelo con la entrada física de parada `%I0.3` directo al renglón de **RESET** de la salida `%Q0.3`.

---

## 🔢 4. Bloques Contadores

### 📈 Ejercicio 4.1: Capacidad de Carga en Montacargas
* **Requerimiento:** Contar 10 cajas detectadas mediante el sensor de fin de carrera `%I0.7` ("FC_CAJA") para encender la marca `%M4.2` ("MONT_LLENO"). El reinicio se realiza con `%I1.2` ("MONT_VACIO").
* **Lógica Ladder:** Se utiliza un bloque contador ascendente (**CTU**). El sensor `%I0.7` alimenta la entrada de conteo `CU`, el botón `%I1.2` se conecta a la entrada de restauración `R`, y el valor se define en `PV := 10`. Cuando el valor actual `CV` alcanza las 10 unidades, la salida del bloque activa la bobina `%M4.2`.

### 🤝 Ejercicio 4.2: Conteo de Acciones Simultáneas
* **Requerimiento:** Encender la salida `%Q0.3` tras presionar 5 veces al mismo tiempo los botones `%I0.3` y `%I0.7`.
* **Lógica Ladder:** Se asocian en serie los contactos NO de `%I0.3` e `%I0.7` dirigidos a un detector de flanco de subida (`P_TRIG`). La salida filtrada de este flanco se cablea a la entrada `CU` de un contador **CTU** configurado con un límite `PV := 5`. La salida del bloque contador enciende la bobina `%Q0.3`.

---

## 🔀 5. Transferencia de Datos

### ⚙️ Ejercicio 5.1: Selector de Consigna Digitalizada
* **Requerimiento:** Mover valores numéricos constantes de velocidad (0.0, 20.0, 40.0, 80.0, 150.0) a la variable real `%MD4` ("CONSIGNA_VEL") mediante el uso exclusivo de 5 marcas booleanas (`V1` a `V5`).
* **Lógica Ladder:** Se estructuran 5 renglones independientes con bloques de transferencia **MOVE**:
    * Un contacto NO de `V1` activa un bloque `MOVE` con `IN := 0.0` y `OUT1 := %MD4`.
    * Un contacto NO de `V2` activa un bloque `MOVE` con `IN := 20.0` y `OUT1 := %MD4`.
    * *(Se replica la estructura sucesivamente para `V3`, `V4` y `V5` con sus respectivos valores flotantes)*.

---

## 🧮 6. Operaciones Aritméticas

### ✖️ Ejercicio 6.1: Optimización de Polinomio de Factor Común
* **Requerimiento:** Ejecutar la ecuación matemática:
  $VAR\_RESULTADO = (VAR1 \times X) + (VAR2 \times X) + (VAR3 \times X) + (VAR4 \times X) + (VAR5 \times X)$
* **Análisis Aritmético:** Por regla distributiva, se reduce el costo de procesamiento agrupando la operación:
  $VAR\_RESULTADO = (VAR1 + VAR2 + VAR3 + VAR4 + VAR5) \times X$
* **Lógica Ladder:**
    1. Se inserta un bloque de suma **ADD** con pines añadidos para calcular de forma simultánea `VAR1 + VAR2 + VAR3 + VAR4 + VAR5`, guardando el resultado en una variable interna de almacenamiento temporal (ej. `%MD100` o `Aux_Suma`).
    2. En el escalón inmediato inferior, un bloque de multiplicación **MUL** toma como entradas la variable `Aux_Suma` y la variable `X`, asignando el producto matemático final a la dirección de `VAR_RESULTADO`.

### ➗ Ejercicio 6.2: Intercepción de Fallo de División por Cero
* **Requerimiento:** Si el divisor `VarB` de un bloque `DIV` proveniente de un HMI se establece en 0, bloquear la ecuación y hacer sonar una alarma `%Q0.1` ("Al_Sonora") durante 5 segundos.
* **Lógica Ladder:**
    * Antes de ejecutar el bloque operativo `DIV`, se interpone un bloque de comparación de igualdad (**EQ**) para comprobar si `VarB == 0.0`.
    * Si la condición es verdadera (el divisor es cero), se bloquea la habilitación de la entrada `EN` del bloque de división para evitar que el microprocesador del PLC caiga en un fallo crítico de ejecución de hardware.
    * Al mismo tiempo, el bit de salida del comparador activa la entrada `IN` de un temporizador tipo pulso (**TP**) parametrizado en `PT := T#5s`, cuya salida física enciende de manera controlada la bobina `%Q0.1`.

---
