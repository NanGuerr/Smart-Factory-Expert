# 🏭 Control de Reactor Batch 🧪

## 1. Diagrama de Flujo Secuencial (SFC)
El sistema opera mediante un proceso secuencial de cuatro etapas principales, definido en la lógica del Reactor Batch.

| Etapa | Nombre | Descripción / Acciones |
| :--- | :--- | :--- |
| **Etapa 1** | `Etapa1_Espera` | Estado inicial. Espera la señal `xComando_Arranque` para transicionar. |
| **Etapa 2** | `Etapa2_Carga` | Activa `xApertura_Valv_Alim` para cargar el reactor. |
| **Etapa 3** | `Etapa3_Operacion` | Activa `xArranque_Motor_Agit`, `xApertura_Valv_Fluido` y la señal `xEtapa3`. Incluye un temporizador (TON) de 5 segundos. |
| **Etapa 4** | `Etapa4_Descarga` | Activa `xApertura_Valv_Desc` para vaciar el tanque. |

**Transiciones clave:**
* La transición a **Etapa 2** depende de `xComando_Arranque`.
* La transición a **Etapa 3** depende de `xTanque_Lleno`.
* La transición a **Etapa 4** depende de la salida `Q` del temporizador `TON0` (5 segundos).
* La transición de retorno a **Etapa 1** depende de `xTanque_Vacio`.

---

## 2. Configuración de Velocidad (Lógica Ladder) ⚙️
El sistema utiliza instrucciones `MOVE` para establecer una consigna de velocidad (`ConsignaVel`) basada en cinco entradas digitales.

| Entrada | Valor a `ConsignaVel` |
| :--- | :--- |
| **Entrada 1** | 0.0 |
| **Entrada 2** | 10.0 |
| **Entrada 3** | 20.0 |
| **Entrada 4** | 50.0 |
| **Entrada 5** | 100.0 |

---

## 3. Lógica de Sensores: Bomba y Generador 💡
Basado en la tabla de verdad proporcionada, el control de la `Bomba` y el `Gen` (Generador) depende de los estados de los Sensores A, B y C.

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

* **Nota sobre la Bomba:** Se activa (`1`) en todas las condiciones excepto cuando los sensores A y B están ambos activos (`1`) simultáneamente.
* **Nota sobre el Generador:** Se activa (`1`) cuando al menos uno de los sensores B o C está activo, exceptuando la condición inicial donde todos son `0`.
