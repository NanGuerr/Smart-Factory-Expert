# 🖥️ El Lenguaje Texto Estructurado (ST)

---

## 📘 Resumen 

Itroduce el lenguaje **Texto Estructurado (ST)**, un lenguaje de programación de **alto nivel** definido por la norma IEC 61131-3. A diferencia de los lenguajes gráficos o de bajo nivel, el ST es altamente legible para los humanos, pareciéndose a lenguajes de programación como C o Pascal.

---

## 🏗️ Metodología y Características
El lenguaje ST se basa en sentencias que rigen el flujo de trabajo del PLC. 

* **Ejecución:** Se procesa de forma secuencial, línea a línea, de arriba hacia abajo. Al llegar al final, el programa se reinicia automáticamente desde el principio (ciclo de scan).
* **Sintaxis:** Posee reglas estrictas (similares a la ortografía) para escribir comandos, facilitando la abstracción del código.

### 🧱 Componentes del Lenguaje
En el lenguaje ST encontramos los siguientes elementos:
* **Sentencias:** Comandos que definen acciones.
* **Funciones:** Bloques de lógica predefinida.
* **Operadores:** Elementos matemáticos o lógicos (`+`, `-`, `*`, `/`, etc.).
* **Variables:** Espacios de memoria que almacenan datos.
* **Constantes:** Valores fijos durante la ejecución.

---

## 💡 Organización y Legibilidad
Para mantener el código ordenado y comprensible, el lenguaje permite herramientas de estructuración:

* **Espacios y Tabulaciones:** Aunque no son estrictamente necesarios para la ejecución, el uso de sangrías (indentación) es fundamental para distinguir qué comandos pertenecen a qué bloques (por ejemplo, dentro de un `IF` o un `FOR`).
* **Comentarios:** Es vital para la documentación del software. Se utilizan los símbolos:
    * `(*` para abrir un comentario.
    * `*)` para cerrar un comentario.
* **Paréntesis `( )`:** Se utilizan para encapsular parámetros dentro de funciones o para forzar la **prioridad en operaciones matemáticas** complejas.

---

## 🔄 Ejemplo de Estructura de Control (ST)
El siguiente ejemplo muestra cómo se visualiza un contador y un bucle de recorrido en este lenguaje:

```st
(* El contador se resetea a los 60 segundos *)
Contador_Segundos(CU := CLOCK_PULSE_15, RESET := Contador_Segundos.Q, PV := 60);

Indice := Contador_Segundos.CV;

IF Contador_Segundos.Q = true THEN
    (* Recorro el array en busca del valor máximo *)
    AuxTempMaxima := 0;
    
    FOR Indice := 0 TO 59 BY 1 DO
        IF (AuxArray[Indice] > AuxTempMaxima) THEN
            AuxTempMaxima := AuxArray[Indice];
        END_IF;
    END_FOR;
    
    TempMaxima := AuxTempMaxima;
END_IF;

```
