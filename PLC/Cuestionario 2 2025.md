# Cuestionario sobre Controladores y PLC 🤖⚙️

Este documento contiene un resumen detallado sobre conceptos fundamentales de controladores lógicos programables (PLC), instrumentación y automatización.

---

### 1. ¿A qué se le denomina controlador? 🧠
**Respuesta:** Hardware central utilizado para controlar un proceso o tarea en particular.

### 2. ¿Cuántos controladores puede haber como máximo en un sistema de control? 🔢
**Respuesta:** No hay límite.

### 3. ¿Cuáles son las ventajas de utilizar un PLC como controlador? ✅
* Resistencia al ruido electromagnético 🛡️
* Tiempo medio entre fallas definido ⏳
* Modularización y montaje simple 🧩
* Requiere personal calificado para su montaje y operación 👨‍🔧

### 4. ¿Qué prefijos se utilizan para denominar a las entradas? 📥
**Respuesta:** I, E.

### 5. ¿Qué función cumple el Watchdog de un PLC? 🐕
**Respuesta:** Monitorear el estado del equipo y reiniciar/dar aviso en caso de que el PLC no responda.

### 6. ¿A qué módulo del PLC se debe cablear un presostato? 🏗️
**Respuesta:** Entrada Digital.

### 7. ¿A qué módulo del PLC debo cablear la consigna de posición para una válvula regulable? 🚰
**Respuesta:** Salida Analógica.

### 8. ¿Cuáles de las siguientes señales analógicas son las más conocidas? 〰️
**Respuesta:** 0..10v, 4..20mA.

### 9. ¿Qué ventaja presenta una entrada analógica de mayor resolución? 🔍
**Respuesta:** Mayor precisión en la medición.

---

### 10. Cálculo de PWM (Ciclo 8ms, 25% Duty Cycle) ⏱️
**Respuesta:** 2ms estará encendida la salida.

### 11. Ventajas de los sensores de corriente frente a los de tensión ⚡
* Tienen mayor inmunidad frente al ruido electromagnético.
* Son eléctricamente estables.

### 12. Características de la memoria de trabajo 💾
* Lectura / Escritura.
* Volátil.

### 13. Resolución de módulos (Phoenix Contact) 🖥️
* **IB IL AI 4/I/4-20-ECO:** 12 bits.
* **AXL F AI8 1F:** 16 bits.

### 14. Ciclo de trabajo de un PLC 🔄
1.  Lectura de las entradas.
2.  Ejecución del programa.
3.  Actualización de las salidas.

### 15-16. Áreas de memoria de un PLC 🗄️
* **Memoria de Carga:** No volátil, solo lectura. Se carga el programa y estados iniciales.
* **Memoria de Trabajo:** Volátil, lectura/escritura. Donde se ejecuta el programa.
* **Memoria Remanente:** No volátil, lectura/escritura. Almacena estados ante reinicios.

### 17. ¿Señal de presión/temperatura exclusivamente analógica? ❌
**Respuesta:** False (pueden ser digitales dependiendo del sensor).

### 18. Conversión Decimal a Binario (540) 🔢
**Respuesta:** 0000 0010 0001 1100.

### 19. Conversión Decimal a Hexadecimal (273) 🔢
**Respuesta:** 111.

### 20. Pasos de un ADC en un PLC 🔀
1. Adquisición -> 2. Muestreo -> 3. Cuantización -> 4. Codificación -> 5. Almacenamiento.

---

### 21-23. Entradas Digitales (Sinking/Sourcing) 🔌
* **Entrada Sinking:** Requiere sensor PNP (Sourcing).
* **Entrada Sourcing:** Interruptor pasivo (no importa el tipo).
* **Sinking:** La corriente entra.

### 24. Salida a relé ✅
* Opera cargas CC o CA.
* Soporta corrientes mayores.
* Acción lenta.
* Sufre desgaste.

### 25. Módulo de salidas NPN 📉
**Respuesta:** Sinking, el módulo recibe la corriente.

### 26. Señal 4-20 mA ✅
* Requiere abrir circuito para medir.
* No afectada por largas distancias.
* Alta inmunidad a ruidos.
* Detecta rotura de cable.

### 27. Resistencia equivalente (Cálculo) 🧮
**Respuesta:** 0,17 Ω.

### 28-29. Definición de sensores 2 y 4 hilos 📡
* **2 hilos:** El lazo de señal es también de alimentación.
* **4 hilos:** Requiere fuente externa, lazo de señal independiente.
