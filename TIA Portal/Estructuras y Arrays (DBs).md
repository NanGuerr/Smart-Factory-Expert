# 🗄️ Guía: Estructuras y Arrays (DBs)

Esta guía explica cómo organizar datos de forma avanzada usando estructuras y listas en Bloques de Datos (DB).

---

## 🧩 1. Estructuras (Struct)
Una **Struct** permite agrupar variables de diferentes tipos de datos bajo un solo nombre simbólico.

* **Uso:** Crear objetos lógicos. Por ejemplo, en lugar de tener `Motor1_Start`, `Motor1_Stop`, `Motor1_Vel`, creas una estructura `Motor1` que contiene las tres variables.
* **Copiar y Pegar:** Puedes copiar una fila completa (o un grupo de filas) que forme una `Struct` y pegarla en otro DB. TIA Portal mantendrá las jerarquías y nombres, lo cual es increíblemente útil para replicar lógica.

---

## 📋 2. Arrays (Matrices)
Un **Array** es una colección de elementos **del mismo tipo de dato**.

* **Creación:** En el campo `Data Type` de una variable en el DB, escribe: `Array[0..9] of Real`. Esto creará una lista de 10 números reales indexados del 0 al 9.
* **Funcionalidad:**
    * **Acceso indexado:** Puedes acceder a los datos usando una variable como índice, por ejemplo: `MiArray[i]`, donde `i` puede cambiar mediante un bucle.
    * **Eficiencia:** Ideal para *Data Logging*, historiales, colas de impresión o buffers de sensores.

---

## 🛠️ Ejemplo Práctico: DB de Control
Imagina un DB llamado `DB_Control_Maq` con la siguiente estructura:

| Nombre | Tipo de Datos | Descripción |
| :--- | :--- | :--- |
| **Config_Motor** | **Struct** | Agrupación de datos del motor |
| - `Start` | Bool | Comando de arranque |
| - `Velocidad` | Real | Setpoint de velocidad |
| **Historico_Temp** | **Array[0..3] of Real** | Listado de las últimas 4 mediciones |

---

## ⚙️ Modificación de Propiedades y Alcance
Dentro del editor del DB, puedes modificar las propiedades de cada variable en las columnas laterales:

1.  **Valor de arranque (Start Value):** El valor inicial al encender la CPU.
2.  **Retain:** Si marcas esta casilla, el valor se mantiene aunque el PLC pierda energía.
3.  **Accesible desde HMI:** Si no marcas esto, el panel no podrá leer/escribir la variable (por seguridad o privacidad de datos).
4.  **Escribible desde HMI:** Permite que el operario cambie valores (Setpoints) desde la pantalla.

### ⚠️ ¿Cómo modificar la estructura de forma segura?
Si cambias un `Struct` o un `Array` (añadiendo elementos en medio):
1.  **Toma una Instantánea (Snapshot):** En el menú superior del DB, usa el icono de la cámara para guardar los valores actuales que están en el PLC.
2.  **Modifica:** Realiza los cambios necesarios en el DB.
3.  **Copia a valores de arranque:** Haz clic en el icono de "Copiar valores de instantánea a valores de arranque" (el icono con una flecha hacia abajo).
4.  **Descarga:** Descarga el DB al PLC. Esto asegura que no pierdas la configuración actual de tu máquina.
