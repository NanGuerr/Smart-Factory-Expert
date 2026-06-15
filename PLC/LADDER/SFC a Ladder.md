# ⚙️ Programación Secuencial: De SFC a Ladder

La programación mediante **SFC (Sequential Function Chart)** es una herramienta gráfica de alto nivel, ideal para procesos industriales que siguen una secuencia lógica de pasos. 🛤️

## 📝 ¿Qué es SFC?
El SFC permite organizar un proceso complejo en **etapas** y **transiciones**:

* **Etapas (Steps)**: Representan los estados del sistema (ej. "En reposo", "Llenando tanque", "En movimiento"). 🏗️
* **Transiciones**: Son las condiciones lógicas que deben cumplirse para pasar de una etapa a la siguiente (ej. "Sensor de nivel activo", "Tiempo cumplido"). 🚦


## 🔄 Conversión de SFC a Ladder
Aunque el SFC es muy intuitivo, muchos PLCs requieren transformar esta lógica a **Ladder (LD)** para su ejecución. Esta conversión sigue una estructura basada en el "seteo" y "reseteo" de marcas o etapas:

1. **Definición de Etapas**: Cada etapa del SFC se convierte en una variable booleana interna (o marca) en el programa Ladder. ✅
2. **Activación**: Se programa una lógica donde, si la etapa anterior está activa y la transición se cumple, la etapa actual se activa. ⚡
3. **Desactivación**: Una vez que la etapa siguiente se activa, la anterior debe ser desactivada inmediatamente. ⏹️

## 💡 Conceptos Clave en el Montaje Lógico
Para una correcta implementación en Ladder, debemos considerar:

* **Seguridad**: Asegurar siempre un estado de reposo inicial. 🛡️
* **Condiciones de Salida**: Cada etapa debe activar las salidas correspondientes (motores, válvulas, indicadores).
* **Bloques de Código**: El uso de bloques organizados facilita el mantenimiento y la detección de fallas.

## 🧩 Ventajas del Enfoque Secuencial
* **Claridad**: Es mucho más fácil visualizar el flujo del proceso que leer cientos de líneas de lógica booleana. 🔍
* **Escalabilidad**: Agregar un paso nuevo al proceso es tan simple como insertar una nueva etapa y su transición. 📈
* **Diagnóstico**: Si el sistema se detiene, basta con ver qué etapa está activa en el SFC para saber exactamente en qué punto del proceso ocurrió el error. 🚑

### Segmento 1: Etapa Inicial (Etapa 0)

*Esta etapa se activa al inicio o al resetear el sistema.*

* **Rung 1:**
* `[SM0.1 (Primer Ciclo)]` + `[NO B0 (Etapa 0)]` + `[NO B1 (Etapa 1)]` ... -> `(S B0)`
* *Nota: SM0.1 asegura que el sistema comience en la etapa 0.*

### Segmento 2: Transición a Etapa 1

*Si el sistema está en la Etapa 0 y se cumple la condición de inicio (ej. un botón de marcha).*

* **Rung 2:**
* `[NO B0]` + `[NO I0.0 (Marcha)]` -> `(S B1)`
* `[NO B1]` -> `(R B0)`
* *Resultado: Al activarse B1, se resetea automáticamente la etapa anterior B0.*

### Segmento 3: Transición a Etapa 2

*Si el sistema está en la Etapa 1 y se cumple la siguiente condición (ej. sensor de fin de carrera).*

* **Rung 3:**
* `[NO B1]` + `[NO I0.1 (Sensor A)]` -> `(S B2)`
* `[NO B2]` -> `(R B1)`

### Segmento 4: Acciones de Salida

*Las salidas físicas (motores, válvulas) dependen de qué etapa esté activa en ese momento.*

* **Rung 4:**
* `[NO B1]` -> `(Out Q0.0)`  *(Acción de la Etapa 1)*

* **Rung 5:**
* `[NO B2]` -> `(Out Q0.1)`  *(Acción de la Etapa 2)*

---

### Consideraciones técnicas para tu transcripción:

1. **Enclavamiento (Set/Reset):** Es fundamental usar instrucciones de **SET** y **RESET** para las marcas de etapa. Esto asegura que el sistema se mantenga en el estado actual sin necesidad de mantener pulsada una entrada física.
2. **Orden de ejecución:** La lógica de reset debe ir siempre después o de forma independiente a la lógica de seteo para evitar que una etapa se resetee en el mismo ciclo en que se activó.
3. **Seguridad:** Te recomiendo añadir un contacto cerrado en serie con todas las bobinas de `SET` que corresponda a un **Botón de Parada de Emergencia**, para asegurar que el sistema pueda detener la secuencia en cualquier punto.

