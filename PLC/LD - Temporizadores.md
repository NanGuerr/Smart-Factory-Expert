# 🛠️ Curso Introductorio de PLC: El Lenguaje Ladder Diagram (LD)

## ⏱️ Sección Destacada: Temporizadores

### ¿Qué son los Temporizadores?

Son elementos de programación fundamentales que permiten:

* ⏳ Retrasar una señal.
* ⏸️ Mantener una señal activa.
* 🔄 Sincronizar una señal con el resto del programa.

Además, su gran versatilidad permite realizar combinaciones entre ellos para diseñar funciones personalizadas a la medida de cualquier aplicación industrial.

### 🧩 Características Comunes de la Instancia

Al insertar cualquier tipo de temporizador en el programa, comparte la misma estructura de bloque y variables:

* **Instancia:** Se le debe asignar un nombre o identificador único que **no debe repetirse** en todo el programa.
* **IN (Entrada de señal):** Variable de tipo Booleano (`Bool`).
* **Q (Salida de señal):** Variable de tipo Booleano (`Bool`).
* **PT (Preset Time):** Tiempo preestablecido de configuración (`Time`).
* **ET (Elapsed Time):** Tiempo transcurrido durante la cuenta (`Time`).

---

## 🔄 Tipos de Temporizadores Disponibles

El lenguaje LD clasifica los temporizadores en tres tipos principales según su comportamiento dinámico:

| Tipo | Descripción | Función Principal |
| --- | --- | --- |
| **TON** | Retardo a la conexión 🟢 | Demora el encendido de la salida `Q` tras activarse la entrada `IN`. |
| **TOF** | Retardo a la desconexión 🔴 | Mantiene la salida `Q` activa durante un tiempo tras apagarse la entrada `IN`. |
| **TP** | Pulso ⚡ | Genera un pulso en la salida `Q` con una duración exacta igual a `PT`, sin importar los cambios en `IN`. |

