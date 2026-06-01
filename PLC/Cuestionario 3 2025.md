# 📘 Respuestas: Cuestionario de Programación PLC

A continuación, se presentan las respuestas detalladas sobre los conceptos fundamentales de los controladores lógicos programables (PLC).

---

### 📋 Cuestionario Resuelto

1. **¿Cuántos bits componen cada registro?**
   * **Respuesta:** 8 bits (c). *Cada registro se compone de 8 bits, numerados del 0 al 7.* 💾

2. **¿Cuál de los siguientes lenguajes es del tipo textual?**
   * **Respuesta:** ST - Structured Text (c). *Los otros tres, LD, FBD y SFC, son lenguajes gráficos.* ✍️

3. **¿Cuántos bits ocupa una variable con una W en la dirección? (Ej: %IW2)**
   * **Respuesta:** 16 bits (d). *El prefijo 'W' hace referencia a Word, que equivale a 16 bits.* 📏

4. **Si tengo una variable cuyos valores oscilan entre 0 y 82,000. ¿Qué tipo de datos debo utilizar?**
   * **Respuesta:** UDINT (d). *El rango del INT es hasta 32,767 y el del WORD es hasta 65,535; el UDINT llega hasta más de 4,000 millones, siendo el adecuado.* 🔢

5. **Si tengo una variable con decimales. ¿Qué tipo de datos debo utilizar?**
   * **Respuesta:** REAL (c). *El tipo REAL es el estándar para números con coma flotante.* 📉

6. **¿Dentro de qué área de memoria se almacenan los estados de las variables no retentivas?**
   * **Respuesta:** Memoria de trabajo (b). *Es donde se ejecutan los cálculos y se guardan los estados volátiles.* 🧠

7. **Relación de tipos de POU:**
   * **a - 3 (Programa):** *Corazón de la aplicación, requiere instanciación.* 🧩
   * **b - 1 (Función):** *Salidas únicas, sin memoria.* 🛠️
   * **c - 2 (Bloque de Función):** *Múltiples salidas, posee memoria.* 🏗️

8. **¿Las variables locales son accesibles desde cualquier parte del proyecto?**
   * **Respuesta:** **Falso**. *Las variables locales solo son accesibles dentro del programa en el que fueron declaradas. Las que son accesibles globalmente son las variables globales.* 🔒

9. **Representación de variable tipo INT como salida en el registro 1:**
   * **Respuesta:** %QW1 (c). *Salida (Q), Tipo Word/INT (W), Registro (1).* 📤

10. **Sintaxis para una constante tipo TIME de 3 segundos:**
    * **Respuesta:** T#3s (a) y TIME#3s (d). *Ambas son aceptadas, siendo T#3s la más corta.* ⏳

11. **¿Qué sucede si tenemos dos tareas cíclicas en el proyecto?**
    * **Respuesta:** Las opciones **b y c son correctas**. *El controlador gestiona la ejecución priorizando tareas y permitiendo que una de mayor prioridad interrumpa a otra.* ⚙️

12. **¿Es posible tener dentro de una misma tarea más de un programa instanciado?**
    * **Respuesta:** **Verdadero**. *Es posible y común asociar varios programas a una misma tarea; se ejecutarán en el orden en que estén agrupados.* 🔄

---
