# 📜 Normativas – IEC 61131 

Este documento resume el estándar internacional **IEC 61131**, el cual unifica y homogeneiza el desarrollo de controladores lógicos programables (PLCs).

---

## 🏛️ 1. ¿Qué es el Estándar IEC 61131?
Es un conjunto de normas internacionales orientadas a **homogeneizar el desarrollo con PLCs** y todos sus periféricos asociados. 

🔄 **Importancia Industrial:** A pesar de que muchas marcas del mercado utilizan software propietario y entornos específicos, la adopción de esta norma facilita enormemente:
* El reemplazo rápido de dispositivos de diferentes fabricantes.
* La interconexión y comunicación robusta entre sistemas de automatización.

---

## 📅 2. Estructura de la Norma
El estándar internacional se divide formalmente en **7 partes esenciales**:

1. ℹ️ **Información general:** Conceptos básicos y definiciones.
2. 🔬 **Especificaciones y ensayos de equipo:** Requerimientos mecánicos, eléctricos y pruebas físicas del hardware.
3. 💻 **Lenguajes de programación:** Definición de la sintaxis y semántica de las herramientas de software.
4. 📖 **Guías de usuario:** Recomendaciones para la selección, instalación y mantenimiento seguro.
5. 📡 **Comunicaciones:** Modelos y perfiles de conectividad de los controladores con otros dispositivos.
6. 🎛️ **Control difuso o fuzzy:** Integración de lógica difusa para sistemas de control avanzado.
7. 🚀 **Guías de programación:** Prácticas y pautas eficientes de desarrollo de software para el usuario final.

---

## ⚙️ 3. IEC 61131-3: Lenguajes de Programación
La parte 3 es una de las más relevantes para los automatizadores, ya que unifica los métodos de codificación. El estándar comprende exactamente **5 lenguajes de programación**, divididos en textuales y gráficos:

### ✍️ Lenguajes Textuales (2)
* 📑 **Texto Estructurado (ST / Structured Text):** Lenguaje de alto nivel con una sintaxis similar a *Pascal* o *C*, ideal para cálculos matemáticos complejos, bucles y procesamiento algorítmico de datos.
* 📋 **Lista de Instrucciones (IL / Instruction List):** Lenguaje de bajo nivel similar al código *Assembly* (Ensamblador), muy rápido en su ejecución pero menos intuitivo para proyectos grandes.

### 🎨 Lenguajes Gráficos (3)
* 🪜 **Diagrama de Contactos o Ladder (LD):** Basado en la lógica de relés y esquemas eléctricos tradicionales con bobinas y contactos. Es el lenguaje más extendido e intuitivo para mantenimiento.
* 📦 **Diagrama de Bloques de Funciones (FBD / Function Block Diagram):** Representación mediante bloques lógicos interconectados, similar a los diagramas de compuertas lógicas analógicas y electrónicas.
* 🗺️ **Bloques de Función Secuenciales (SFC / Sequential Function Chart):** Derivado de las redes de *Petri*, organiza la arquitectura del programa en etapas secuenciales, transiciones condicionales y acciones específicas. Ideal para describir procesos por pasos.

---

## ⏱️ Gestión de Tareas
Una tarea es un componente que gestiona cuándo se ejecuta la lógica (POUs). Los programas **siempre** deben estar asociados a tareas.

### 🔄 Ciclo de ejecución básico
1.  **Lectura:** Captura el estado de las entradas.
2.  **Ejecución:** Corre el programa asociado.
3.  **Actualización:** Envía las señales a las salidas.

### 📋 Tipos de Tareas
*   **IDLE:** Tarea de prioridad más baja. Se ejecuta cuando no hay otras tareas pendientes.
*   **CÍCLICAS:** Se ejecutan periódicamente según un intervalo de tiempo. Se les puede asignar prioridad (0-15).
*   **EVENTOS:** Llamadas automáticamente por el sistema operativo ante un disparador.

### ⚙️ Reglas de funcionamiento
*   El controlador ejecuta solo **una tarea a la vez**.
*   Una tarea puede **interrumpir** a otra si tiene mayor prioridad.
*   El orden de ejecución de los programas dentro de una tarea sigue el orden en que fueron agrupados.
