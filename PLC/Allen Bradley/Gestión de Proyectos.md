# 🏗️ Estructura, Documentación y Gestión de Proyectos

Esta **Clase 6** es fundamental para pasar de programas simples a proyectos profesionales organizados, escalables y seguros. Se enfoca en cómo estructurar el código y cómo gestionar la información fuera del software 🚀.

---

### 1. Control de Flujo del Programa 🔄
El video explica cómo gestionar la ejecución del código para que sea más eficiente y ordenado, utilizando principalmente la segmentación por rutinas.

* **Instrucción JSR (Jump to Subroutine):** Es la pieza clave 🔑. Se utiliza en la *Main Routine* para llamar a otras rutinas (ej. `Rutina_Manual`, `Rutina_Automatico`, `Rutina_Alarmas`). Si una rutina no es llamada por un JSR, el PLC simplemente no ejecutará ese código 🚫.
* **SBR (Subroutine) y RET (Return):** Permiten pasar parámetros entre rutinas. El uso de entradas y salidas en subrutinas facilita la creación de bloques de código reutilizables 🧩.
* **Manejo de Tareas (Tasks):** * **Continuous Task:** Se ejecuta siempre en bucle 🔁.
    * **Periodic Tasks:** Se ejecutan cada cierto tiempo exacto, ideal para lazos **PID** ⏱️.

---

### 2. Exportación e Importación de Comentarios y Tags 📊
Una parte vital de la ingeniería es la documentación masiva:

* **Herramienta de Exportación:** Cómo exportar todos los Tags y sus descripciones a un archivo formato **CSV** 📂.
* **Edición en Excel:** Ventaja de usar Excel para escribir cientos de comentarios o renombrar variables rápidamente para luego reimportarlos 📑.
* **Documentación del Proyecto:** Importancia de que cada entrada y salida física tenga su comentario para facilitar el mantenimiento preventivo y correctivo 🛠️.

---

### 3. Respaldos y Gestión de Archivos (Backups) 💾
Mejores prácticas para no perder el trabajo y mantener un historial de cambios:

* **Archivos .ACD:** Formato estándar de Studio 5000. Contiene el código, la configuración de hardware y los comentarios 📁.
* **Formatos L5K y L5X:** Formatos basados en texto (**XML**) útiles para importar/exportar partes específicas o abrir archivos en distintas versiones de software 📝.
* **Uso del "Save As" y Compresión:** Recomendaciones sobre cómo nombrar archivos (incluyendo fecha y versión) y generar respaldos con configuración de red 🤐.

---

### 4. Comparación de Programas (Compare Tool) 🔍
El video introduce la herramienta **Logix Designer Compare Tool**, que permite abrir dos versiones de un mismo programa para ver exactamente qué peldaños (*rungs*) o tags fueron modificados ⚖️.

---

### 💡 Conceptos Técnicos Destacados
* **Scan Time:** El exceso de JSR o una mala organización del flujo puede afectar el tiempo de ciclo del PLC ⚡.
* **Offline vs Online:** Importancia de realizar respaldos antes de realizar una modificación "en caliente" (**Online Edit**) por seguridad 🛡️.

---
Esta clase cierra el ciclo de **"Manejo del Software"**, dándote las herramientas para manejar proyectos de gran envergadura sin perder el control de la estructura o la documentación 🏗️.
