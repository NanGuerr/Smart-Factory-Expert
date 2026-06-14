# ⚙️ Cuestionario de Lógica Digital y Sistemas 🏗️

### 1. Tabla de Verdad: Control de Motor 🕹️
**Problema:** Una llave (selecciona sentido), un pulsador (enciende el motor). Dos salidas (giro horario/antihorario).
* Reglas:
    * El motor solo enciende con el pulsador.
    * La llave selecciona el sentido.
    * **NUNCA** se encienden ambas salidas a la vez.


a. 
| Pulsador | Llave | Horario | Antihorario |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 |

b.
| Pulsador | Llave | Horario | Antihorario |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

c.
| Pulsador | Llave | Horario | Antihorario |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |

d.
| Pulsador | Llave | Horario | Antihorario |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |

* **Resultado:** La opción correcta es la **B** ✅

| Pulsador | Llave | Horario | Antihorario |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
---

### 2. Sistema Antiincendios: Simplificación Lógica 🚒
**Problema:** Sistema con bomba de agua y generador auxiliar. Se requiere simplificar las condiciones lógicas obtenidas de un documento extenso de requerimientos mediante un Mapa de Karnaugh.

| Sensor A | Sensor B | Sensor C | Bomba | Gen. |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 | 1 |

---

a. 

Mapa de Karnaugh: Salida "Bomba" 💧

| C \ AB | 00 | 01 | 11 | 10 |
| :---: | :---: | :---: | :---: | :---: |
| **0** | 0 | 1 | 0 | 1 |
| **1** | 1 | 1 | 0 | 1 |

Mapa de Karnaugh: Salida "Gen." (Generador) ⚡

| C \ AB | 00 | 01 | 11 | 10 |
| :---: | :---: | :---: | :---: | :---: |
| **0** | 0 | 1 | 1 | 0 |
| **1** | 1 | 1 | 1 | 1 |

b.

Mapa de Karnaugh: Salida "Bomba" 💧

| C \ AB | 00 | 01 | 11 | 10 |
| :---: | :---: | :---: | :---: | :---: |
| **0** | 1 | 1 | 0 | 1 |
| **1** | 1 | 1 | 0 | 1 |

Mapa de Karnaugh: Salida "Gen." (Generador) ⚡

| C \ AB | 00 | 01 | 11 | 10 |
| :---: | :---: | :---: | :---: | :---: |
| **0** | 0 | 1 | 1 | 0 |
| **1** | 1 | 1 | 0 | 1 |

c. 

Mapa de Karnaugh: Salida "Bomba" 💧

| C \ AB | 00 | 01 | 11 | 10 |
| :---: | :---: | :---: | :---: | :---: |
| **0** | 1 | 1 | 0 | 1 |
| **1** | 1 | 1 | 0 | 1 |

Mapa de Karnaugh: Salida "Gen." (Generador) ⚡

| C \ AB | 00 | 01 | 11 | 10 |
| :---: | :---: | :---: | :---: | :---: |
| **0** | 0 | 1 | 1 | 0 |
| **1** | 1 | 1 | 1 | 1 |

* **Resultado:** El Mapa de Karnaugh correcto es la **C** ✅

Mapa de Karnaugh: Salida "Bomba" 💧

| C \ AB | 00 | 01 | 11 | 10 |
| :---: | :---: | :---: | :---: | :---: |
| **0** | 1 | 1 | 0 | 1 |
| **1** | 1 | 1 | 0 | 1 |

Mapa de Karnaugh: Salida "Gen." (Generador) ⚡

| C \ AB | 00 | 01 | 11 | 10 |
| :---: | :---: | :---: | :---: | :---: |
| **0** | 0 | 1 | 1 | 0 |
| **1** | 1 | 1 | 1 | 1 |
