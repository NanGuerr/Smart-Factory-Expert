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
|--[Botón]-----(Salida)---  (La salida se apaga al soltar el botón)

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

**Pregunta:** Según el enunciado del control de cinta (Arranque con 3s, Parada, Falla), ¿Es correcto el código simple?

* [x] **No** (Respuesta correcta: El enunciado requiere lógica compleja de temporización y contadores de falla que excede un simple rung).

---

### 14. Procesamiento de Sensores 📊

**Pregunta:** El cliente me solicita obtener el promedio de las mediciones de un sensor en un minuto. ¿Qué me conviene utilizar?

* [x] **Array** (Respuesta correcta)

