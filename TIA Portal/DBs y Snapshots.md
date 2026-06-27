# ⚙️ Variables, DBs y Snapshots 

Esta guía cubre la personalización de variables, la optimización de la visualización y el manejo seguro de Bloques de Datos (DBs).

---

## 🏷️ 1. Adaptación de Variables (PLC Tags)

En la tabla de **PLC Tags**, puedes configurar tus variables con total flexibilidad:

* **Nombre:** Haz clic sobre el nombre actual y escribe el nuevo nombre (usa nombres descriptivos como `Motor_Principal_Status`).
* **Tipo de Datos:** Cambia el tipo desplegando el menú (ej. de `BOOL` a `INT`) en la columna "Data type".
* **Dirección (Físicas/Marcas):** En la columna "Address", modifica la dirección (ej. `%I0.0` a `%I0.1` o `%M10.0` a `%M10.1`). *Nota: Si la dirección ya está en uso, TIA Portal te avisará de un solapamiento.*
* **Comentarios:** Es **vital** utilizar la columna "Comment" para describir la función de la variable. Esto ahorra horas de depuración en el futuro.

### 👁️ Visualización de Comentarios
Para ver la información completa de tus variables mientras programas (muy útil en los bloques):
1. Ve al menú superior **Ver (View)**.
2. Selecciona **Mostrar con (Show with)**.
3. Haz clic en **Información de la variable (Variable information)**.
4. Selecciona **Mostrar información de la variable**.
*Esto hará que aparezcan comentarios y detalles adicionales debajo de cada tag en tu código KOP/FBD.*

---

## 💾 2. Propiedades Exclusivas en Bloques de Datos (DB)

Al trabajar dentro de un DB, cada variable tiene propiedades especiales que puedes ajustar en la columna de propiedades:

* **Valor de arranque (Start Value):** El valor que toma la variable al arrancar el PLC o al cargar el bloque.
* **Remanencia (Retain):** Activa esta opción para que el valor de la variable se **mantenga** después de una caída de tensión (power cycle).
* **Valor de observación (Monitor Value):** Es el valor actual en tiempo real cuando estás conectado online.
* **Accesibilidad HMI/SCADA:**
    * **Accesible desde HMI:** Debe estar marcada para que un panel operador pueda leer la variable.
    * **Escribible desde HMI:** Permite que el panel modifique el valor (ej. setpoints).

---

## ⚠️ 3. Modificación Segura de DBs y Snapshots

Modificar la estructura de un DB (añadir o cambiar variables) es una operación delicada porque implica una descarga de bloque que puede reiniciar los valores de tus variables.

### El flujo seguro para no perder datos:

1. **Tomar Instantánea (Snapshot):** - Con el PLC en línea (Online), abre el DB.
   - Haz clic en el botón **"Tomar instantánea de los valores actuales"** (icono de cámara/flechas).
   - Esto guarda los valores que el proceso tiene en este instante exacto.

2. **Copiar a Valores de Arranque:**
   - Una vez tomada la instantánea, haz clic en **"Copiar valores de instantánea a valores de arranque"**.
   - Ahora, los valores que tenías "online" se han convertido en los valores por defecto (offline).

3. **Modificación del DB:**
   - Detén el proceso (STOP del PLC) si es necesario por seguridad.
   - Realiza los cambios en la estructura del DB (añadir variables, cambiar tipos).
   - Compila el bloque.

4. **Descarga:**
   - Descarga el DB al PLC. Al haber copiado los valores a "Valores de arranque", el PLC iniciará con los datos de proceso que tenías antes de la modificación.

*⚠️ **Aviso:** Nunca realices cambios estructurales en un DB (como añadir una variable en medio de una estructura) en un proceso crítico sin detener la máquina, ya que los desplazamientos de memoria pueden causar comportamientos inesperados si no se gestionan correctamente.*
