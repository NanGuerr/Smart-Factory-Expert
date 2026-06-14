# ⚙️ Automatización PLC: `Sistema de llenado`

Este archivo contiene la especificación lógica del programa de control PLC extraído del archivo XML Sistema de llenado. El programa gestiona una secuencia de operaciones (probablemente para un sistema de bombeo o llenado) utilizando lógica Ladder.

---

## 📥 Entradas (Sensores y Comandos)
| Variable | Tipo | Descripción |
| :--- | :--- | :--- |
| `FC_CERRADA` | `BOOL` | Final de carrera (Válvula/Puerta cerrada) |
| `FC_ABIERTA` | `BOOL` | Final de carrera (Válvula/Puerta abierta) |
| `FC_BYPASS` | `BOOL` | Sensor de derivación o condición auxiliar |
| `Apertura` | `BOOL` | Comando de inicio de apertura |
| `Pausa` | `BOOL` | Comando de pausa en la operación |
| `Cierre` | `BOOL` | Comando de cierre/reset del sistema |

---

## 📤 Salidas (Actuadores)
| Variable | Tipo | Descripción |
| :--- | :--- | :--- |
| `Q_BOMBA` | `BOOL` | Activación de la bomba |
| `Q_VALV_CIERRE`| `BOOL` | Válvula de cierre |

---

## 🔄 Estados de la Secuencia (`PASO_1` - `PASO_6`)
El programa utiliza una máquina de estados para gestionar la lógica de control.

* **PASO_1:** Inicio del ciclo de apertura (activado tras 5s de condición inicial).
* **PASO_2:** Transición lógica intermedia (dependiente de `FC_BYPASS`).
* **PASO_3:** Estado de bloqueo (controlado por temporizador `Temp_Bloqueo` de 15s).
* **PASO_4:** Estado de Rearranque (controlado por temporizador `Temp_Rearranque` de 3s).
* **PASO_5:** Operación activa.
* **PASO_6:** Estado final/reset.

---

## ⏳ Temporizadores (TON - Timer On Delay)
| Instancia | Tiempo | Función |
| :--- | :--- | :--- |
| `Temp_Apertura` | `T#5s` | Retardo para activar `PASO_1` |
| `Temp_Bloqueo` | `T#15s` | Temporización de seguridad para `PASO_3` |
| `Temp_Rearranque`| `T#3s` | Temporización para `PASO_4` |

---

## 🧱 Resumen de la Lógica (Ladder)
1. **Inicio de Ciclo:** El sistema evalúa `FC_CERRADA` y `Apertura`. Si se mantienen, el temporizador `Temp_Apertura` (5s) permite activar `PASO_1`.
2. **Control de Bomba:** `Q_BOMBA` es gestionada por múltiples condiciones (`PASO_1`, `PASO_2`, `PASO_5`). Se activa (Set) en `PASO_1` y `PASO_5` (bajo ciertas condiciones de sensores), y se resetea (Reset) en situaciones de `Cierre` o paso a `PASO_6`.
3. **Seguridad y Pausa:** Se incluyen contactos para `Pausa` y `FC_BYPASS` que permiten alterar el flujo de la secuencia o detener la bomba mediante lógica `Set/Reset`.
4. **Reset General:** La variable `Cierre` actúa como un comando de emergencia o reinicio que resetea `Q_BOMBA`, `Q_VALV_CIERRE` y los pasos `PASO_1` y `PASO_2`.

---
*Nota: Este archivo fue generado automáticamente a partir de la estructura del código PLCopen XML Sistema de llenado.*
