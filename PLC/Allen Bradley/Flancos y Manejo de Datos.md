# 🔢 Comparaciones, Flancos y Manejo de Datos

En la **Clase 5**, el curso avanza hacia instrucciones que permiten procesar datos numéricos y detectar cambios de estado instantáneos, lo cual es vital para el control de procesos y la gestión de alarmas 🚨.

---

### 1. Instrucciones de Comparación ⚖️
Permiten que el PLC tome decisiones basadas en valores numéricos (como el acumulado de un timer, contador o señal analógica).

* **EQU (Equal):** Comprueba si dos valores son iguales 👥.
* **NEQ (Not Equal):** Comprueba si dos valores son diferentes 🚫.
* **LES (Less Than) / LEQ (Less Than or Equal):** Comprobar si un valor es menor o menor o igual que otro ⬇️.
* **GRT (Greater Than) / GEQ (Greater Than or Equal):** Comprobar si un valor es mayor o mayor o igual ⬆️.
* **LIM (Limit Test):** Una de las más potentes; verifica si un valor se encuentra dentro o fuera de un rango definido por un límite inferior y uno superior 📏.

---

### 2. Instrucciones de Transición (One Shots) ⚡
Cruciales para detectar el "flanco" de una señal (el momento exacto del cambio). Evitan ejecuciones repetidas mientras una entrada permanece activa.

* **ONS (One Shot):** Se coloca en medio de un renglón. Permite el flujo lógico por un solo *scan* cuando la condición precedente cambia de falso a verdadero ⏱️.
* **OSR (One Shot Rising) y OSF (One Shot Falling):** Instrucciones de salida que detectan el flanco de subida (0 a 1) o de bajada (1 a 0) respectivamente 📈📉.
* **Uso común:** Disparar cálculos matemáticos, iniciar pesajes o incrementar contadores sin rebotes 🛠️.

---

### 3. Profundización en Temporizadores y Contadores 🔄
Se revisan aplicaciones complejas integrando los conceptos previos:

* **Encadenamiento:** Uso del bit **.DN** de un temporizador para activar otro en cascada ⛓️.
* **Reset de Contadores:** Uso correcto de la instrucción **RES** vinculada a comparadores para reiniciar procesos automáticamente al alcanzar la meta de producción 🔁.

---

### 4. Manejo de Tipos de Datos en Comparación 📊
El video enfatiza la importancia de la compatibilidad entre datos:

* **SINT, INT, DINT:** Enteros de distinto tamaño (8, 16 y 32 bits) 🔢.
* **REAL:** Números de punto flotante (con decimales), esenciales para sensores de temperatura o presión 🌡️.

---

### 5. Aplicación Práctica: Control de Rango 🎚️
Ejemplo de uso de la instrucción **LIM** para activar una alarma si un tanque supera el 90% de su capacidad o baja del 10%, integrando señales analógicas simuladas 🏗️.

---

### 6. Buenas Prácticas de Programación 📑
* **Documentación:** Importancia de describir los símbolos de comparación para facilitar el entendimiento a otros ingenieros ✍️.
* **Orden Lógico:** Colocar las comparaciones al inicio de los renglones para optimizar el tiempo de ejecución (*scan time*) ⚡.

---

### 💡 Conclusión
Esta clase cierra el bloque de **"Lógica Básica"** y prepara el terreno para las instrucciones matemáticas y de movimiento de datos posteriores 🏗️.
