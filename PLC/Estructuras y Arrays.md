# 🗂️ Estructuras y Arrays

Este documento resume la organización inteligente de variables mediante **Estructuras**, **Arrays** y **UDTs** en entornos de automatización.

---

## 🏗️ 1. Estructuras (`STRUCT`)
A medida que un programa de PLC crece o se incorporan múltiples componentes idénticos (como varios motores), la cantidad de variables individuales se vuelve inmanejable y confusa para el programador. 

Las **Estructuras (STRUCT)** permiten agrupar variables de diferentes tipos de datos bajo un único nombre simbólico.

### ⚙️ Caso de Ejemplo: Control de un Motor
Para operar un motor necesitamos:
* `CMD_Arranque` ➡️ **BOOL** (Comando de arranque: 0 apagado, 1 encendido)
* `SP_Vel` ➡️ **INT** (Consigna de velocidad)
* `RD_Vel` ➡️ **INT** (Lectura de velocidad actual)
* `AL_Temp` ➡️ **BOOL** (Alarma por sobretemperatura)

Si tuviéramos 3 motores sin estructuras, tendríamos que escribir `M1_CMD_Arranque`, `M2_CMD_Arranque`, etc. 

🟢 **Con STRUCT lo organizamos de forma limpia:**
* **▼ M1 (STRUCT)**
  * `CMD_Arranque` (BOOL)
  * `SP_Vel` (INT)
  * `RD_Vel` (INT)
  * `AL_Temp` (BOOL)
* **► M2 (STRUCT)**
* **► M3 (STRUCT)**

👉 **¿Cómo se llama a la variable?** Se escribe el nombre de la estructura seguido de un punto y el elemento. 
* 📌 *Ejemplo:* `M3.SP_Vel`

---

## 📊 2. Arreglos (`ARRAY`)
Cuando se necesita repetir el **mismo tipo de datos** consecutivamente o agrupar señales con características similares, se utiliza un **Array** o arreglo.

* 🔢 **Indexación:** Son listas ordenadas e indexadas por un número entero que, por buena práctica, casi siempre comienza en **0**.
* 🔘 **Ejemplo de Aplicación:** Una botonera con 8 comandos de arranque para 8 motores diferentes.

Instead of declaring 8 individual variables, we create a single vector:
* **▼ Arranque** ➡️ `Array [0..7] of BOOL`
  * `Arranque[0]` (BOOL)
  * `Arranque[1]` (BOOL)
  * `Arranque[2]` (BOOL)
  * ...
  * `Arranque[7]` (BOOL)

👉 **¿Cómo se llama a la variable?** Se escribe el nombre del array y el índice numérico correspondiente dentro de corchetes.
* 📌 *Ejemplo:* `Arranque[3]`

---

## 🛠️ 3. Tipos de Datos de Usuario (`UDT`)
Cuando las estructuras definidas se repiten muchas veces en el proyecto, la mejor práctica es crear un **UDT (User Data Type)**.

* 📝 **Definición:** Es una estructura personalizada por el usuario que se declara en un área independiente del software y funciona como un "nuevo tipo de dato" propio (equivalente a crear tu propio `BOOL` o `INT`).
* 🔄 **Reusabilidad:** Una vez creado el UDT `Motor`, puedes declarar variables asignándoles este tipo de dato directamente.

* **▼ M1** ➡️ Tipo de dato: **Motor** (UDT)
  * `CMD_Arranque` (BOOL)
  * `SP_Vel` (INT)
  * `RD_Vel` (INT)
  * `AL_Temp` (BOOL)

👉 **¿Cómo se llama a la variable?** Igual que en las estructuras:
* 📌 *Ejemplo:* `M1.SP_Vel`

---

## 🚀 4. El Súper Combo: Combinar `ARRAY` y `UDT`
La verdadera potencia en la programación de PLCs industriales surge al fusionar ambas herramientas. Podemos declarar un **Array cuyo tipo de datos sea un UDT**.

Imagine que debe controlar **100 motores** idénticos en una planta fabril:
* **▼ M** ➡️ `Array [0..99] of Motor` *(Donde "Motor" es nuestro UDT)*
  * **▼ M[0]**
    * `CMD_Arranque` (BOOL)
    * `SP_Vel` (INT)
    * `RD_Vel` (INT)
    * `AL_Temp` (BOOL)
  * ► `M[1]`
  * ► `M[2]`
  * ...
  * ► `M[99]`

🌟 **Ventaja:** Con una sola línea de declaración se generan cientos de variables perfectamente ordenadas, reduciendo drásticamente el tiempo de preparación y facilitando la lectura del código.
