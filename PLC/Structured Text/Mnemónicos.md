# ⚙️ Mnemónicos en Texto Estructurado (ST)

---

## 📘 Resumen 

Explora los **mnemónicos y estructuras de control** fundamentales en el lenguaje de Texto Estructurado (ST), permitiendo al programador tomar decisiones lógicas y repetir bloques de código de forma eficiente.

---

## 🚦 1. Estructura Condicional (IF)
El condicional es la herramienta de decisión básica. Permite ejecutar una porción de código solo si se cumple una condición lógica.

* **IF simple:** "Si se cumple la condición, entonces haz esto".
    ```st
    IF (Arranque = TRUE) THEN
        Motor_A := TRUE;
    END_IF;
    ```
* **IF con ELSE:** Permite definir una acción alternativa si la condición inicial no se cumple ("Si no, haz esto otro").
    ```st
    IF (Arranque = TRUE) THEN
        Motor_A := TRUE;
    ELSE
        Motor_A := FALSE;
    END_IF;
    ```

---

## 🔁 2. Estructuras de Repetición (Bucles)
Permiten ejecutar la misma acción múltiples veces sin necesidad de escribir el código repetidamente.

* **Bucle FOR:** Se utiliza cuando sabemos de antemano cuántas veces debe repetirse la acción (basado en un contador).
    ```st
    FOR Contador := Inicio TO Fin BY Paso DO
        Acción;
    END_FOR;
    ```

---

## 🧩 3. Estructura de Selección (CASE)
Cuando una variable puede tomar múltiples valores y cada valor requiere una acción distinta, el `CASE` es la alternativa más limpia y legible frente a múltiples `IF`.

* **Funcionamiento:** Evalúa una variable índice y ejecuta el caso coincidente.
* **Valor por defecto (ELSE):** Ejecuta una acción si el valor no coincide con ninguno de los casos definidos.

    ```st
    CASE Etapa OF
        1: LuzRoja := TRUE;
        2: LuzAmarilla := TRUE;
        3: LuzVerde := TRUE;
    ELSE
        ApagarLuces();
    END_CASE;
    ```

---

## 💡 Recomendaciones de Programación
* **Legibilidad:** Utiliza indentaciones (sangrías) dentro de los `IF`, `FOR` y `CASE` para distinguir fácilmente qué código pertenece a cada bloque.
* **Comentarios:** El uso de `(* comentario *)` es fundamental para documentar la lógica detrás de cada selección o bucle.
* **Manejo de Índices:** Al trabajar con bucles o casos, asegúrate de que las variables índice siempre tengan valores definidos y dentro del rango permitido para evitar errores en tiempo de ejecución.

---

