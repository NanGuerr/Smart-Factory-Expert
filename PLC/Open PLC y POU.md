# 🖥️ Guía de Programación en OpenPLC

Esta guía detalla los pasos fundamentales para configurar, programar y simular proyectos utilizando **OpenPLC Editor**.

---

## 🛠️ Instalación y Primeros Pasos
1.  **Descompresión:** Utiliza un software como WinRar o 7zip para extraer el archivo `.zip` descargado.
2.  **Ejecución:** Localiza el acceso directo `OpenPLC Editor` y haz doble clic para iniciar.
3.  **Creación de Proyecto:**
    *   Ve al menú **Archivo -> Nuevo**.
    *   Crea una carpeta vacía donde desees guardar tu proyecto.
    *   Selecciona dicha carpeta para inicializar el entorno.
4.  **Configuración de POU:** Se abrirá una ventana para definir tu primer **Program Organization Unit (POU)**.
    *   Asigna un nombre.
    *   Selecciona tipo "programa".
    *   Elige el lenguaje de programación (ej. **LD** - Ladder).

---

## 📝 Definición de Variables
El área superior de la interfaz permite declarar variables para evitar el direccionamiento directo de memoria.
*   **Crear:** Presiona el botón `+`.
*   **Configurar:** Define nombre, clase (Local/Global) y tipo de dato (BOOL, DINT, REAL, etc.).
*   **Validación:** Si la declaración es correcta, no aparecerán errores. Si hay fallas (ej. falta `%` en la dirección), el sistema lo indicará con colores.

---

## 💻 Programación y Lógica
Puedes insertar componentes mediante:
*   **Barra de herramientas superior:** Selecciona contacto, bobina, bloques, etc.
*   **Click derecho:** Menú contextual en el área de trabajo central.
*   **Librería (derecha):** Arrastra bloques aritméticos, temporizadores, comparadores, etc.

*Tip: Al hacer doble click en un bloque, puedes acceder a sus **Propiedades** y habilitar el **Control de ejecución** (pines EN/ENO).*

---

## 🚀 Simulación y Depuración
1.  **Iniciar:** Presiona el botón **Start PLC Simulation** en la barra superior.
2.  **Consola:** Si todo está bien, verás "PLC started" en la consola inferior.
3.  **Depuración:**
    *   Haz click en el icono de "instancia de depuración" para visualizar el flujo de energía (cambio de colores en el programa).
    *   **Gráficos:** Presiona el botón del gráfico en la variable deseada para visualizar su comportamiento en tiempo real en la pestaña **Depurador**.
    *   **Forzar Valores:** Haz click derecho en un contacto/variable y selecciona **Force True/False** o utiliza el candado en el depurador para ingresar un valor manual.

---

## 🧩 Conceptos Adicionales: Los POU
La arquitectura IEC 61131-3 utiliza los **POU (Program Organization Units)** para estructurar el código:
*   **Programa:** El corazón de la aplicación; debe ser llamado dentro de una tarea.
*   **Función:** Agrupa acciones repetitivas; tiene múltiples entradas pero **una sola salida** y no posee memoria.
*   **Bloque de funciones:** Similar a la función, pero **posee memoria interna** y permite llamar a otros bloques/funciones.

### 🏷️ Tipos de Variables
*   **Locales:** Accesibles solo dentro del programa donde fueron creadas.
*   **Globales:** Declaradas en la hoja general del proyecto, accesibles desde cualquier programa.
