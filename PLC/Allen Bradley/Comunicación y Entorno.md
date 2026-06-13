# 🔌 Comunicación y Entorno de Studio 5000 💻

Esta clase es fundamental porque explica cómo establecer la comunicación entre la computadora y el controlador, además de realizar un recorrido por la interfaz principal del software de programación 🌐.

---

### 1. RSLinx Classic: El puente de comunicación 🌉
RSLinx Classic es el servidor de comunicaciones indispensable. Sin este software, Studio 5000 no puede "ver" al PLC.

* **RSWho:** Ventana para navegar por las redes configuradas y verificar dispositivos activos 🕵️.
* **Configuración de Drivers:** Proceso para añadir nuevos drivers (EtherNet/IP o Virtual Backplane para simulaciones) 🔌.
* **Identificación de dispositivos:** Reconocimiento de iconos de PLC, módulos de E/S y otros componentes en la red 💡.

---

### 2. Creación de un Proyecto en Studio 5000 ✨
Flujo de trabajo inicial para comenzar un programa desde cero:

* **Selección del controlador:** Elegir el modelo exacto (ej. CompactLogix 5370 o ControlLogix 5580) 📑.
* **Definición de la versión (Firmware):** La importancia de que la versión del software coincida con la del hardware o simulador ⚙️.
* **Configuración del Chasis/Slot:** Indicar la posición física exacta del procesador 📍.

---

### 3. Navegación en Logix Designer (La Interfaz) 🖥️
Recorrido por las áreas principales del software:

* **Controller Organizer (Panel Izquierdo):** El árbol jerárquico del proyecto 🌳.
* **Controller Tags:** Donde se crean las variables globales 🌎.
* **Tasks / Programs / Routines:** La jerarquía de ejecución del código ⏳.
* **I/O Configuration:** Donde se agregan y configuran los módulos físicos de entradas y salidas 📥📤.
* **Área de Trabajo:** Donde se escribe la lógica (principalmente en lenguaje Ladder) 🪜.
* **Barra de Estado Online:** Muestra modos (Offline, Online, Run, Program) y estados de falla 🚨.

---

### 4. Organización de la Lógica (Tareas y Rutinas) 🏗️
Estructura lógica para mantener un código ordenado:

* **Main Task:** Tarea principal que se ejecuta cíclicamente 🔄.
* **Main Routine:** Rutina de entrada donde el PLC comienza la lectura 🚀.
* **Subrutinas:** Uso de la instrucción **JSR** (Jump to Subroutine) para segmentar el programa 🧩.

---

### 5. Controller Tags vs. Program Tags 🏷️
Una distinción técnica crucial:

* **Controller Tags (Globales):** Variables visibles para todo el proyecto y otros dispositivos como HMIs 📡.
* **Program Tags (Locales):** Variables que solo existen dentro de un programa específico, evitando conflictos de nombres 🔒.

---

### 6. Procedimiento "Who Active" 🔍
Establecer el vínculo final entre el software y el hardware:

* **Who Active:** Herramienta dentro de Studio 5000 para buscar el PLC a través del driver de RSLinx 📡.
* **Download:** Enviar el programa de la PC al PLC ⬇️.
* **Upload:** Traer el programa del PLC a la PC ⬆️.
* **Go Online:** Conectarse para monitorear en tiempo real sin modificar el programa residente ⚡.

---

### 💡 Conclusión
Este módulo es el paso previo a la escritura de código, asegurando que el entorno de desarrollo esté correctamente vinculado al hardware 🛠️.
