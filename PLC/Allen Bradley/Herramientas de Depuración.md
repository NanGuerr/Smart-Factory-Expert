# 🛠️ Commissioning, Diagnóstico y Herramientas de Depuración

La **Clase 7** es fundamental para las etapas de "puesta en marcha" (*commissioning*) y diagnóstico de fallas (*troubleshooting*). Se enseñan herramientas que ahorran horas de búsqueda manual y permiten manipular el sistema en condiciones controladas 🚀.

A continuación, el resumen detallado:

---

### 1. Importación Masiva de Comentarios y Descripciones 📊
Se profundiza en el flujo de trabajo entre **Excel** y **Studio 5000**.

* **Procedimiento:** A través del menú `Tools > Import > Tags and Logic Comments`, se pueden cargar archivos **.CSV** 📂.
* **Utilidad:** Ideal para proyectos con cientos de entradas y salidas (I/O). Se editan en una hoja de cálculo y se importan de golpe, asegurando que la documentación coincida con los planos eléctricos 📑.

---

### 2. Referencias Cruzadas (Cross-References) 🔍
Es la herramienta de navegación más potente para un programador.

* **Función:** Permite ver instantáneamente todos los lugares donde se usa un **Tag** específico en todo el proyecto (Ladder, bloques de función, etc.) 📍.
* **Uso práctico:** Clic derecho sobre un tag > `Go to Cross Reference` (o **Ctrl + E**). Muestra si el tag se está "leyendo" o "escribiendo" (Destructivo: Yes/No) 📝.
* **Depuración:** Vital para encontrar por qué una salida no se activa o quién está sobreescribiendo un valor por error 🕵️‍♂️.

---

### 3. Forzado de Señales (I/O Forcing) ⚠️
Obliga a una entrada o salida a tomar un valor (0 o 1) ignorando el estado físico y la lógica del programa.

* **Forzado de Entradas:** Simula un sensor activo para probar la lógica sin activarlo físicamente 🚨.
* **Forzado de Salidas:** Activa un actuador (motor, válvula) directamente desde el software ⚙️.
* **Seguridad:** El indicador **"FORCES"** en Studio 5000 se pone en amarillo y el LED del PLC parpadea 🟡.
* **Diferencia Crítica:** 
    * **Toggle Bit:** Cambia el valor en memoria, pero la lógica puede revertirlo en el siguiente *scan* 🔄.
    * **Force:** Mantiene el valor fijo por encima de cualquier condición 🔒.

---

### 4. Monitoreo y Edición de Valores 🖥️
* **Monitor Tags:** Permite observar variables en tiempo real y cambiar valores de temporizadores (**Preset**) o contadores sin entrar al código ⏱️.
* **Watch Window:** Ventanas personalizadas para agrupar solo los tags de interés de una máquina específica, evitando navegar por miles de variables 🗂️.

---

### 5. Herramienta de Búsqueda (Find) 🔎
* **Búsqueda Avanzada (Ctrl + F):** Uso de filtros para localizar instrucciones, nombres de rutinas o comentarios de peldaño (**Rung Comments**) en proyectos extensos 📑.

---

### 🛑 Nota de Seguridad
**Nunca dejes "Forces" activos** en un PLC de producción al terminar una intervención. Esto anula las protecciones de seguridad lógicas y puede causar accidentes graves si el sistema no se comporta como se espera 🛡️.
