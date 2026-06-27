# 💾 Bloques de Datos (DB) en TIA Portal

Los Bloques de Datos (DB - *Data Blocks*) son la estructura fundamental para el almacenamiento de información en los PLC Siemens. A diferencia de los bloques de código (FC/FB), los DBs **no contienen lógica de ejecución**, sino exclusivamente datos.

---

## 🧐 ¿Qué son los Bloques de Datos?
Son áreas de memoria donde se almacenan variables, configuraciones, estados de máquinas, recetas, historiales, etc. Existen dos tipos principales:
* **DB Globales:** Accesibles desde cualquier bloque del programa (OB, FC, FB).
* **DB de Instancia:** Asociados exclusivamente a un Bloque de Función (FB) específico.

---

## 🏗️ Ventajas: DB vs. Marcas (M)

| Característica | Marcas (Flags - M) | Bloques de Datos (DB) |
| :--- | :--- | :--- |
| **Estructura** | Plana y simple. | Jerárquica y compleja (Structs, UDTs). |
| **Capacidad** | Limitada por el área de memoria del sistema. | Muy amplia (prácticamente solo limitada por la CPU). |
| **Organización** | Difícil de gestionar en grandes proyectos. | Altamente organizada y legible. |
| **Retentividad** | Configurable a nivel global. | Configurable por variable individual. |

**¿Por qué usar DBs?** Porque permiten agrupar datos relacionados (ej: *Datos_Motor_1*) en un solo lugar, mejorando la legibilidad y el mantenimiento del código.

---

## 🛠️ Funcionalidades y Uso
* **Recetas:** Almacenar parámetros de producción que cambian según el producto.
* **Historial/Registro:** Guardar estados pasados de una máquina.
* **Interfaz HMI:** Los paneles HMI acceden a los DBs para leer/escribir variables de forma centralizada.
* **Comunicación:** Buffer de intercambio de datos entre PLCs.

---

## 📝 Declaración de Variables en el DB
Dentro de un DB, declaras variables de forma similar a la tabla de variables, pero con mayor flexibilidad:
1. **Nombre:** Identificador simbólico.
2. **Tipo de Dato:** BOOL, INT, REAL, TIME, o incluso estructuras personalizadas (UDTs).
3. **Valor Inicial:** Define con qué valor arranca la variable al cargar el PLC.
4. **Retentividad:** Si activas la casilla "Retain", el dato se mantiene al apagar y encender el PLC.

---

## ⚙️ Creación Automática: DB de Instancia
Esta es una de las funcionalidades más potentes al programar con **Bloques de Función (FB)**:

1. **El Concepto:** Cuando diseñas un FB, defines variables estáticas (`Static`) que "recuerdan" el estado (ej. un contador o un paso de secuencia).
2. **La Instancia:** Al llamar a ese FB en el `OB1` o en otro bloque, el sistema **te obliga** a asignar un DB.
3. **El Proceso Automático:** Al crear la llamada, TIA Portal crea automáticamente un **DB de Instancia** con el mismo nombre o uno asignado. Este DB guarda *exactamente* el valor de las variables `Static`, `Input`, `Output` y `Temp` (si aplica) de esa llamada específica del FB.

* **Ventaja:** Si usas el mismo FB 10 veces para controlar 10 motores diferentes, TIA Portal creará 10 DBs de instancia (uno por motor), permitiendo que cada motor tenga su propio contador, tiempo y estado independiente.
