# 🛠️ Diagnóstico Eficiente: Toggle vs. Cross Reference

Estas herramientas separan a un programador básico de uno que sabe realizar un diagnóstico eficiente en planta. Permiten manipular el sistema en condiciones controladas y localizar errores con precisión quirúrgica 🚀.

---

### 1. El "Toggle Bit": Funcionamiento y Seguridad ⚡
El **Toggle Bit (Ctrl + T)** cambia el estado de un bit de 0 a 1 o de 1 a 0 directamente en la memoria del controlador. A diferencia del "Force", no bloquea el bit; solo cambia su valor en el instante de la pulsación.

#### 🔄 Cómo funciona en el ciclo de escaneo (Scan Cycle)
El PLC ejecuta su lógica miles de veces por segundo. Si haces Toggle sobre un bit escrito por una instrucción (como una bobina **OTE**):
1. Pulsas **Ctrl + T** y el bit cambia en la RAM del PLC 🧠.
2. Al microsegundo, el PLC ejecuta el renglón de lógica correspondiente.
3. Si la lógica es falsa, reescribe un 0 sobre tu cambio ✍️.
* **Resultado:** El bit parpadea tan rápido que parece que "no funcionó".

#### 🛡️ Procedimiento Seguro
* **Bits de control/usuario:** Úsalo en bits que no dependan de entradas físicas o bobinas OTE (ej. bits de "Permisivo" o "Habilitación") 🔓.
* **Verifica Referencias Cruzadas:** Asegúrate de que no haya una instrucción destructiva activa antes de proceder 🚫.
* **Impacto en Actuadores:** ¡Cuidado! Nunca hagas Toggle en bits que activen movimientos físicos (motores, pistones) sin despejar el área 🏗️.
* **Uso de "One Shots":** Evita que el bit se quede "pegado" en 1 si el proceso requiere un flanco de subida 📈.

---

### 2. Filtrado de Referencias Cruzadas (Cross References) 🔍
En proyectos grandes, filtrar por tipo de instrucción es la forma más rápida de encontrar quién está "dañando" una lógica.

#### 📑 Pasos para filtrar
1. Selecciona el tag y presiona **Ctrl + E**.
2. Haz clic en el icono del **embudo (Filter)** en la barra de herramientas 🚩.

#### filter Tipos de Filtros Críticos:
* **Destructive (Escribir):** Filtro más usado (Marcar como **"Yes"**). Muestra solo instrucciones que modifican el valor (**OTE, OTL, MOV**). Ideal para saber por qué un bit se apaga solo 🕵️.
* **Instruction:** Filtra por instrucciones específicas como **JSR** o **TON** ⏱️.
* **Routine/Program:** Limita la búsqueda a una rutina específica si sospechas que el error está en un área determinada de la planta 📍.

---

### 💡 Comparativa: Toggle vs. Force

| Característica | Toggle Bit (Ctrl+T) 🔄 | I/O Forcing 🔒 |
| :--- | :--- | :--- |
| **Persistencia** | No. La lógica puede sobrescribirlo. | Sí. Bloquea el valor sobre la lógica. |
| **Uso común** | Pruebas rápidas de bits internos. | Pruebas de hardware o puentes. |
| **Riesgo** | Bajo/Medio (puede no tener efecto). | Alto (anula protecciones). |
| **Indicación Visual**| Ninguna en el hardware. | LED "FORCES" parpadeando. |

---
