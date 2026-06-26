# 📘 Gestión de I/O, Direccionamiento y Variables en PLCs

Esta guía resume los conceptos esenciales para la configuración y gestión de datos en un PLC (basado en estándares de TIA Portal).

---

## 🔌 1. Entradas, Salidas y Marcas (Memoria)

Los PLCs interactúan con el mundo físico a través de señales eléctricas convertidas en datos lógicos:

* **📥 Entradas (I - Inputs):** Reciben señales de sensores, pulsadores o interruptores. Se conectan a los **bornes físicos** del módulo de entrada.
* **📤 Salidas (Q - Outputs):** Envían señales a actuadores como relés, contactores, luces piloto o válvulas. Se conectan a los **bornes físicos** del módulo de salida.
* **🧠 Marcas (M - Flags/Memory):** Son bits de memoria interna. No existen físicamente en los bornes; sirven para procesar lógica, almacenar estados intermedios y controlar secuencias.

---

## 🔢 2. Direccionamiento: Bytes y Bits

El direccionamiento identifica dónde se encuentra cada variable. Se basa en una estructura de **Byte.Bit** (Ejemplo: `I0.1`).

* **Bit (0 o 1):** Es la unidad mínima (la variable lógica).
* **Byte (8 bits):** Agrupa 8 bits consecutivos (Ejemplo: `IB0` contiene `I0.0` a `I0.7`).
* **Estructura lógica:**
    * **I0.0:** Entrada, Byte 0, Bit 0.
    * **Q0.5:** Salida, Byte 0, Bit 5.
    * **M10.2:** Marca, Byte 10, Bit 2.

---

## 📋 3. Organización y Documentación

Para mantener un proyecto ordenado, usamos herramientas de mapeo:

* **Tabla de Variables (PLC Tags):** Es el "diccionario" donde asignamos nombres simbólicos (ej. `Boton_Parada`) a direcciones físicas (ej. `I0.0`). Esto facilita la lectura del código.
* **Plano de Ocupación:** Es el documento o vista de hardware que muestra qué dispositivo está conectado a qué borne físico. Es vital para el cableado y mantenimiento.

---

## 🌐 4. Alcance de las Variables (Scope)

No todas las variables son iguales; su "alcance" define dónde pueden ser leídas o escritas:

* **🌍 Variables Globales (Global):**
    * Definidas en la Tabla de Variables o DBs Globales.
    * **Accesibles desde cualquier bloque** del programa (OB, FC, FB).
    * Ideales para E/S físicas y datos de comunicación entre bloques.

* **🏠 Variables Locales (Local/Static/Input/Output en FB):**
    * Definidas dentro de la interfaz de un bloque específico (FC o FB).
    * Solo el bloque puede "ver" estas variables.
    * Útiles para encapsular lógica y evitar que otros bloques interfieran con los datos internos de una función.

* **⏱️ Variables Temporales (TEMP):**
    * Se declaran en la interfaz del bloque como `Temp`.
    * **No retienen su valor** de un ciclo de scan a otro.
    * Se inicializan (o contienen basura) al llamar al bloque y se pierden al terminar. Son perfectas para cálculos intermedios rápidos.

---

## 💡 Tips de Uso
1. **Digital I/O:** Recuerda que las entradas/salidas digitales solo entienden 0 o 1 (ON/OFF). Para señales analógicas (sensores de presión, temperatura), se usan direcciones diferentes (PIW/PQW o palabras).
2. **Buenas Prácticas:** Usa siempre nombres simbólicos en la tabla de variables. Nunca programes usando direcciones absolutas (ej. `I0.0`) directamente en el código; si el cableado cambia, el código se romperá. Cambiando la dirección en la **Tabla de Variables**, el programa completo se actualiza automáticamente.

# Direccionamiento y Gestión de Variables en TIA Portal
---

## 📍 1. Direccionamiento Físico vs. Simbólico

En TIA Portal, es fundamental entender cómo el software identifica los datos:

* **Direccionamiento Físico (Absoluto):** Hace referencia directa a la dirección de memoria o borne del PLC (ej. `%I0.0`, `%Q0.5`, `%M10.2`). 
    * *Ventaja:* Útil para depuración rápida.
    * *Desventaja:* Si cambias el cableado, debes buscar y reemplazar cada instancia en tu código.
* **Direccionamiento Simbólico:** Asigna un nombre (Tag) a la dirección física (ej. `Boton_Start`, `Motor_Principal`).
    * *Ventaja:* Es la **mejor práctica**. Si necesitas cambiar la dirección, solo lo haces una vez en la *Tabla de Variables* y TIA Portal actualiza automáticamente todo el proyecto.

---

## ✏️ 2. Tabla de Variables (PLC Tags)

La tabla de variables es el "diccionario" de tu proyecto.

* **Editar y Sobrescribir:**
    * Abre **"PLC Tags"** en el árbol del proyecto.
    * Puedes añadir nuevas variables escribiendo el nombre, seleccionando el tipo de dato (`BOOL`, `INT`, `REAL`, etc.) y asignando la dirección.
    * Si sobrescribes una dirección existente, TIA Portal te avisará si hay conflictos de solapamiento de direcciones.
    * **Tip:** Puedes exportar/importar esta tabla a Excel, editarla masivamente y volver a importarla para ahorrar tiempo.

---

## 🌳 3. Árbol de Proyectos (Project Tree)

El árbol de proyectos es el mapa central de tu sistema. Se organiza en nodos principales:

* **Dispositivos (Device Configuration):** Donde configuras el hardware (CPU, módulos, redes).
* **PLC Tags:** Lugar donde resides tus tablas de variables globales.
* **Program Blocks (Bloques de programa):** Donde vive tu lógica (`OB1`, `FC`, `FB`).
* **Online & Diagnostics:** Acceso para ver estados, buffer de errores y conexión online.

---

## 📥 4. ¿Cómo llamar variables en TIA Portal?

Existen tres formas principales de invocar una variable en tu código:

1. **Auto-completado (La más común):** Mientras escribes en un bloque (Network), empieza a teclear el nombre de la variable (ej. `Mot...`). TIA Portal desplegará una lista de sugerencias. Selecciona la correcta con `Enter`.
2. **Drag & Drop:** Abre la tabla de variables o el árbol de proyectos en una ventana dividida. Selecciona la variable deseada y arrástrala directamente al segmento (Network) donde la necesites.
3. **Selección directa:** Al insertar una instrucción (como un contacto o bobina), haz clic en el icono de **"..." (tres puntos)** junto a la caja de dirección. Se abrirá una ventana de selección donde puedes navegar por las tablas de variables existentes.

---

## 💡 Consejos de Experto
* **Uso de nombres claros:** Evita nombres como `Tag_1`. Usa `Sensor_Presion_Tanque_Alto` para que cualquier persona que lea tu código entienda qué hace la variable.
* **Consistencia:** Mantén la tabla de variables limpia. Elimina variables que no uses para evitar confusiones y errores de compilación.
