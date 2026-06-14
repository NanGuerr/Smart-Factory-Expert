# 📋 Técnica de Automatización

Este documento resume la lógica de control, la tabla de verdad de los sensores y el diagrama SFC proporcionado.

## ⚙️ 1. Control de Velocidad (Lógica Ladder)
La lógica utiliza bloques `MOVE` para asignar valores específicos de consigna de velocidad (`ConsignaVel`) según la entrada digital activa.

| Entrada | Valor (ConsignaVel) |
| :--- | :--- |
| Entrada 1 | 0.0 |
| Entrada 2 | 10.0 |
| Entrada 3 | 20.0 |
| Entrada 4 | 50.0 |
| Entrada 5 | 100.0 |

## 🧪 2. Lógica de Control de Sensores (Tabla de Verdad)
El estado operativo de la `Bomba` y el `Gen.` (Generador) está determinado por la combinación lógica de las entradas de los sensores A, B y C.

| Sensor A | Sensor B | Sensor C | Bomba | Gen. |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 | 1 |

## 🔄 3. Secuencia de Control (SFC)
El diagrama de funciones secuenciales (SFC) define el flujo del proceso industrial, gestionando la transición entre diferentes estados.

* **Estructura**: El proceso está organizado en una secuencia que abarca desde la `Etapa1` hasta la `Etapa7`.
* **Temporización**: Se utilizan temporizadores (`TON`) para gestionar los tiempos de proceso, incluyendo `Temp Apertura`, `Temp Bloqueo` y `Temp Rearranque`.
* **Condiciones de Transición**: El flujo depende de variables de estado y sensores como `xFC_ABIERTA`, `xFC_BYPASS`, `xApertura`, `xPause` y `xCierre`.
* **Acciones**: Se implementan comandos de `Set` (S) y `Reset` (R) para controlar actuadores específicos como `xQ_BOMBA` y `xQ_VALV_CIERRE`.
