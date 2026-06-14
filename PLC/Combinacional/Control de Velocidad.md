# 📂 Lógica de Control Industrial

## ⚙️ 1. Control de Velocidad (Lógica Ladder)
El siguiente sistema utiliza instrucciones `MOVE` para asignar valores de consigna de velocidad (`ConsignaVel`) según la entrada digital activada.

| Entrada | Valor a `ConsignaVel` |
| :--- | :--- |
| **Entrada 1** | 0.0 |
| **Entrada 2** | 10.0 |
| **Entrada 3** | 20.0 |
| **Entrada 4** | 50.0 |
| **Entrada 5** | 100.0 |

---

## 🔢 2. Lógica de Sensores (Tabla de Verdad)
Basado en los estados de los sensores A, B y C, el sistema determina el funcionamiento de la **Bomba** y el **Generador (Gen.)**.

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

---

## 🚦 3. Lógica de Semáforo (SFC)
El control del semáforo sigue una secuencia lógica de cuatro etapas, activadas mediante un pulsador inicial.

| Etapa | Acciones / Salidas | Temporizador |
| :--- | :--- | :--- |
| **Etapa 1** | `xLuzRoja`, `xEtapa1` | 7 segundos |
| **Etapa 2** | `xLuzRoja`, `xLuzAmarilla`, `xEtapa2` | 3 segundos |
| **Etapa 3** | `xLuzVerde`, `xEtapa3` | 5 segundos |
| **Etapa 4** | `xLuzAmarilla`, `xEtapa4` | 3 segundos |

* **Disparo inicial:** El proceso comienza al activar la entrada `xPulsador`.
