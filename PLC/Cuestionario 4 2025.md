# Cuestionario 4 Programación de PLCs 🤖⚡

Esta guía contiene ejercicios clave sobre lógica LADDER, estructuras de datos y temporizadores.

---

### 1. Variables en Ladder 💾
**Pregunta:** En un programa puedo ver que una variable aparece como `Temperatura[3]`. ¿A cuál de estos grupos pertenece esta variable?

* [ ] Estructura
* [ ] UDT
* [x] **Array** (Respuesta correcta)

---

### 2. Compuertas Lógicas 🔀
**Pregunta:** ¿Qué estado deben tener los botones A y B para que la lámpara C se encienda?

* [ ] A = 1; B = 1
* [ ] A = 1; B = 0
* [ ] A = 0; B = 1
* [ ] A = 0; B = 0
* [x] **Respuesta correcta:** A = 1; B = 0 o A = 0; B = 1 (Lógica XOR implícita).

---

### 3. Bobinas Simples 🎛️
**Pregunta:** Si dejo pulsado el botón A. ¿Cuánto tiempo se mantendrá encendida la salida C?

* [x] **Se mantendrá hasta que se deje de pulsar el botón** (Respuesta correcta)
* [ ] Un ciclo de programa
* [ ] 2 segundos

---

### 4. Bobinas de Flanco (Negativo) 📉
**Pregunta:** Si dejo pulsado el botón A. ¿Cuánto tiempo se mantendrá encendida la salida C con una instrucción `-(N)-`?

* [x] **Un ciclo de programa** (Respuesta correcta)
* [ ] Se mantiene encendida mientras tenga pulsado el botón
* [ ] No se enciende

---

### 5. Ecuaciones en Bloques 🧮
**Pregunta:** ¿Qué ecuación describe el código con las operaciones de los bloques?

* [x] **Resultado = (NumeroA + NumeroB) * 5 / NumeroC** (Respuesta correcta)

---

### 6. Consigna de Velocidad 🚀
**Pregunta:** ¿Cuál será la consigna final de velocidad si se activan las entradas 1, 3 y 5 simultáneamente?

| Rung | Entrada (Contacto) | Operación | Valor (IN) | Salida (OUT) |
| --- | --- | --- | --- | --- |
| **1** | Entrada1 | MOVE | 0.0 | ConsignaVel |
| **2** | Entrada2 | MOVE | 10.0 | ConsignaVel |
| **3** | Entrada3 | MOVE | 20.0 | ConsignaVel |
| **4** | Entrada4 | MOVE | 50.0 | ConsignaVel |
| **5** | Entrada5 | MOVE | 100.0 | ConsignaVel |

* [x] **100** (Respuesta correcta según lo solicitado)

---

### 7. Contadores 🔢
**Pregunta:** ¿Cuál es la máxima cantidad de cajas que puedo contar (tipo INT)?

* [x] **32767** (Respuesta correcta)

---

### 8. Bobinas en Ladder 🪜
**Pregunta:** Si necesito colocar más de una bobina en un mismo segmento LADDER:

* [x] **Las coloco en PARALELO** (Respuesta correcta)

---

### 9. Compuerta XOR 🚫
**Pregunta:** En la compuerta del tipo XOR, si las entradas están simultáneamente activas, la salida estará encendida.

* [x] **False** (Respuesta correcta)

---

### 10. Enclavamiento (Latch) 🔒
**Pregunta:** ¿Es correcto el siguiente enclavamiento?

* [x] **No** (Respuesta correcta)

**Diagrama explicativo:**

```text
--- INCORRECTO ---
|--[Botón]--+---(Motor)---
|           |
|--[Motor_1]-+ (La salida es diferente Motor a Motor_1)

--- CORRECTO (Enclavamiento) ---
|--[Botón]--+---(Salida)---
|           |
|--[Salida]-+

```

---

### 11. Temporizador TP (Pulso) ⏱️

**Pregunta:** ¿Cuál de las siguientes imágenes corresponde al funcionamiento de un temporizador "TP"?

* [x] **Respuesta correcta: B**

**Diagrama de Flancos (Gráfico explicativo):**

```text
Entrada (IN)  __|‾‾‾‾‾|__________________
                ^
          (Flanco de subida)

Salida (Q)    __|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|_____
                |<---- Tiempo ---->|

```

---

### 12. Tipos de Contadores 📉

**Pregunta:** A continuación se grafican los valores que toma el CV de un contador. ¿A qué tipo de contador corresponde?

* [x] **CTD** (Count Down / Contador descendente - Respuesta correcta)

---

### 13. Lógica de Control de Cinta 🏗️

Según el siguiente enunciado. ¿Es correcto el código?

“Crear un diagrama en LADDER para el control del arranque y parada de una cinta transportadora, la cual es comandada por un motor conectado a una salida digital del PLC. El arranque y parada se realizará a través de un pulsador de marcha y un pulsador de parada (ambos sin enclavamiento, es decir que se presionan y cuando se sueltan vuelven a su posición original). Además, existe una señal de falla que se encuentra cableada a una entrada digital del PLC.

El motor debe arrancar si no hay una falla existente, y luego de 3 segundos de mantener pulsada la marcha. Al soltar la marcha queda encendido. El botón de parada o una falla lo detienen de forma inmediata. Si hay una falla, se enciende un indicador y se bloquea el motor (no puede arrancar). Ese estado de bloqueo se resetea solo si la falla se va, y pulsando el botón de parada 3 veces.

El estado de falla se activa luego de que por lo menos 4 segundos permanezca la falla activa.

Variables de entrada: xMarcha, xParada, xFalla.
Variables de salida: xMotor, xLedFalla.”

**Pregunta:** Según el enunciado del control de cinta (Arranque con 3s, Parada, Falla), ¿Es correcto el código simple?

* [x] **No** (Respuesta correcta: El enunciado requiere lógica compleja de temporización y contadores de falla que excede un simple rung).

---

### 14. Procesamiento de Sensores 📊

**Pregunta:** El cliente me solicita obtener el promedio de las mediciones de un sensor en un minuto. ¿Qué me conviene utilizar?

* [x] **Array** (Respuesta correcta)

