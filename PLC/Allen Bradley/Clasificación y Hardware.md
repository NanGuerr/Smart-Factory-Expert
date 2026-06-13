# 🛠️ Clasificación y Hardware de Rockwell Automation

La **Clase 2** del curso de **IngeLearn** se centra en clasificar y detallar el hardware de **Rockwell Automation**, permitiendo entender qué controlador elegir según la complejidad del proyecto 🚀.

---

### 1. El Ecosistema "Logix" 🌐
El concepto fundamental es la **Arquitectura Logix**. A diferencia de otras marcas, Allen Bradley busca que el modelo de programación y la base de datos de etiquetas (**tags**) sean consistentes, ya sea en controladores pequeños o de gran escala 🔄.

---

### 2. Clasificación por Tamaño y Capacidad ⚖️
Las familias se dividen en tres grandes grupos:

#### **Micro Controladores (Familia Micro800) 🧱**
* **Modelos:** Micro810, 820, 830, 850 y 870.
* **Uso:** Máquinas pequeñas y aplicaciones de bajo costo 📉.
* **Software:** Se programan con **Connected Components Workbench (CCW)**, no con Studio 5000 💻.
* **Nota técnica:** Son controladores tipo "brick" (bloque compacto) con E/S integradas; modelos superiores permiten expansión ➕.

#### **Controladores Pequeños (CompactLogix) ⚙️**
* **Modelos:** Series 5370 (L1, L2, L3) y la moderna 5380.
* **Uso:** Máquinas de rango medio y control de movimiento (**Motion Control**) sencillo 🏃.
* **Características:** No requieren chasis físico; módulos ensamblados lateralmente. Incluyen puerto **EtherNet/IP** integrado 🔌.

#### **Controladores Grandes (ControlLogix) 🏛️**
* **Modelos:** Series 5570 y 5580.
* **Uso:** Procesos masivos, plantas completas y alta disponibilidad o **redundancia** 🔄.
* **Arquitectura:** Basados en **chasis (rack)**. El procesador, fuente y comunicación son independientes y distribuibles 🧩.

---

### 3. Controladores de Seguridad (GuardLogix) 🚨
Línea identificable por su **color rojo**. Son versiones de CompactLogix o ControlLogix con coprocesadores de seguridad integrados, diseñados para cumplir normativas **SIL** (Safety Integrity Level) 🛡️.

---

### 4. Sistemas Legados (Legacy) 💾
Equipos presentes en fábricas pero no recomendados para proyectos nuevos:
* **SLC 500 y PLC-5:** Antecesores de la era Logix 🏛️.
* **MicroLogix (1000, 1100, 1200, 1400, 1500):** Programados con **RSLogix 500**. El **MicroLogix 1400** destaca por su puerto Ethernet y robustez 💪.

---

### 5. Criterios de Selección de Hardware 📋
Factores clave antes de especificar un PLC:
* **Cantidad de I/O:** Entradas y salidas digitales/analógicas necesarias 📥📤.
* **Memoria:** Complejidad del algoritmo y almacenamiento de datos 🧠.
* **Comunicación:** Cantidad de dispositivos conectados (variadores, HMIs) 📡.
* **Movimiento:** Necesidad de servomotores sincronizados 🔄.

---

### 💡 Conclusión
Este video es esencial para dejar de ver los PLCs como "cajas negras" y entenderlos como herramientas específicas para problemas de distinta escala 📏.
