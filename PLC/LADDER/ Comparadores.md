# 🎛️ Programación LD — Comparadores

Este documento presenta una transcripción detallada, descriptiva y analítica de los procedimientos y bloques funcionales utilizados para validar magnitudes en el lenguaje de contactos (**Ladder Diagram - LD**), basado en el material oficial de **INGELEARN**. 🚀

---

## 📚 1. Contexto del Módulo 3

Dentro del ecosistema del lenguaje Ladder, el procesamiento de señales pasa de lo puramente binario (encendido/apagado) a lo analógico o numérico a través de herramientas de evaluación. 

* 🔌 **01. Simbología Básica:** Elementos digitales de conmutación.
* ⚡ **02. Detectores de Flanco:** Transiciones lógicas rápidas (P y N).
* 🔒 **03. Enclavamientos:** Retención de señales (Set, Reset, bloques SR/RS).
* ⚖️ **04. Comparadores:** El núcleo de este documento (Validación de variables numéricas).
* ⏱️ **05. Temporizadores:** Relojes de eventos temporales (TON, TOF, TP).
* 🔢 **06. Contadores:** Acumuladores de pulsos digitales (CTU, CTD).
* 🧮 **07. Operaciones Aritméticas y Transferencia:** Manipulación matemática de registros de memoria.

---

## ⚖️ 2. ¿Qué son los Comparadores?

Los **Comparadores** son elementos lógicos de programación que evalúan la relación matemática entre dos valores o variables numéricas/analógicas entre sí (habitualmente denominadas como **IN1** e **IN2**). El bloque se activa y permite el flujo eléctrico virtual siempre y cuando la condición interna declarada se cumpla como verdadera (`True`).

### 🔀 Formas de Representación según el Software
Dependiendo del entorno de desarrollo (TIA Portal, EcoStruxure Machine Expert, CODESYS, etc.), los comparadores pueden implementarse bajo dos formatos principales:

1. 🔌 **Como Contactos (Los más utilizados):** Funcionan como un interruptor condicional dentro de la línea de comandos. Si la comparación es verdadera, el contacto se cierra y permite el paso de la señal eléctrica que lo precede hacia los siguientes elementos del segmento.
2. 📦 **Como Bloques de Función:** Son cajas lógicas independientes. Reciben los datos en sus patillas de entrada (`IN1`, `IN2`) y emiten un estado binario puro `1` (verdadero) o `0` (falso) a través de su patilla de salida (`Q`).

---

## 🔍 3. Tipos de Comparadores Básicos

El sistema permite contrastar datos utilizando seis operadores algebraicos fundamentales. A continuación se detallan sus nomenclaturas estándar e interpretaciones:

| Tipo de Comparación | Símbolo Ladder | Sigla Técnica | ⚙️ Procedimiento de Evaluación |
| :--- | :---: | :---: | :--- |
| **Mayor** | `>` | **GT** *(Greater Than)* | Da paso si el valor de `IN1` es estrictamente superior al de `IN2`. |
| **Menor** | `<` | **LT** *(Lesser Than)* | Da paso si el valor de `IN1` es estrictamente inferior al de `IN2`. |
| **Igual** | `==` | **EQ** *(Equal)* | Da paso únicamente si `IN1` e `IN2` tienen el mismo valor exacto. |
| **Mayor o Igual** | `>=` | **GE** *(Greater or Equal)* | Da paso si `IN1` supera o iguala numéricamente a `IN2`. |
| **Menor o Igual** | `<=` | **LE** *(Lesser or Equal)* | Da paso si `IN1` es menor o igual numéricamente a `IN2`. |
| **Distinto / Diferente** | `<>` | **NE** *(Not Equal)* | Da paso en cualquier escenario, excepto cuando ambos valores son iguales. |

---

## 🛠️ 4. Procedimientos de Implementación y Ejemplos Prácticos

### 🗺️ A. Configuración de Variables en TIA Portal
En softwares industriales avanzados, el bloque comparador requiere que el programador defina explícitamente el **tipo de datos** de las variables de entrada en la parte superior del bloque (por ejemplo, `INT`, `DINT`, `REAL`) para evitar conflictos de desbordamiento de memoria.

#### Ejemplo de Segmento Ladder (Control de Temperatura):
Imagine un sistema de refrigeración industrial donde se debe activar una alarma si la temperatura de un tanque supera los 85°C:

```text
   Variable Analógica    Valor de Consigna
     "Temp_Tanque"          (Constante)
        %IW64                  85
───────┤  >  ├───────────────────────────────────────( )──────
        (INT)                                    "Alarma_Vent"
                                                    %Q0.2

```

* **Análisis del Procedimiento:** El PLC lee continuamente la entrada analógica del sensor (`%IW64`). Mientras el valor sea menor o igual a 85, el bloque permanece abierto. En el instante exacto en que la temperatura sube a 86, la condición **GT (`>`)** se vuelve verdadera, el contacto se cierra virtualmente y la bobina de salida de la alarma `%Q0.2` se enciende.

---

## 📊 5. Tabla de Verdad de Comportamiento Dinámico

Para entender los procedimientos de discriminación lógica de los bloques, observemos cómo reaccionan los diferentes comparadores frente a variaciones de datos fijos:

Si fijamos el valor de comparación **`IN2 = 50`**, la salida de los bloques responderá de la siguiente manera según los cambios en **`IN1`**:

| Valor Actual (`IN1`) | Valor Límite (`IN2`) | Bloque `==` (EQ) | Bloque `>` (GT) | Bloque `>=` (GE) | Bloque `<>` (NE) | Estado de Salida |
| --- | --- | --- | --- | --- | --- | --- |
| **30** | 50 | `0` (Falso) | `0` (Falso) | `0` (Falso) | **`1` (Verdadero)** | Solo el bloque *Distinto* permite el paso. |
| **50** | 50 | **`1` (Verdadero)** | `0` (Falso) | **`1` (Verdadero)** | `0` (Falso) | Se activan los bloques de *Igualdad*. |
| **75** | 50 | `0` (Falso) | **`1` (Verdadero)** | **`1` (Verdadero)** | **`1` (Verdadero)** | Se activan las condiciones de superioridad. |

---

## 🏭 6. Aplicaciones Industriales Típicas

Los bloques de comparación son la base del control de procesos y la toma de decisiones automáticas:

1. 🌊 **Control de Nivel de Tanques:** Detener bombas de llenado si el volumen medido en un sensor ultrasónico es *Mayor o Igual* (`>=`) al límite de seguridad.
2. 📦 **Líneas de Empaque y Conteo:** Activar un brazo desviador o pistón neumático cuando el acumulador de un contador de piezas sea *Igual* (`==`) al tamaño de lote configurado por el operador en la pantalla HMI.
3. 🚨 **Sistemas de Gestión de Alarmas:** Disparar protocolos de parada de emergencia en calderas si los valores de presión analógica resultan *Mayores* (`>`) que los rangos mecánicos nominales permitidos.

