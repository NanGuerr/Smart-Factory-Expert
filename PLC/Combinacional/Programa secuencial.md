# ⚙️ Código XML a Lenguaje Ladder (LD) 🪜

Diagrama de contactos (Ladder) en formato de arte ASCII. 

El archivo contiene la lógica de una máquina de estados secuencial (`PASO_1` a `PASO_6`) que controla una bomba y una válvula mediante Set `(S)` y Reset `(R)`, incorporando tres temporizadores a la conexión (`TON`).

```text
NETWORK 1: Inicialización con Temporizador de Apertura
│   PASO_1    FC_CERRADA    Apertura           Temp_Apertura
├───[/]──────────[ ]──────────[ ]────────┬──────[ TON ]──────┬──────────(S) PASO_1
│                                        │ IN              Q │
│                                   T#5s─┤ PT             ET │
│                                        └───────────────────┘

NETWORK 2: Arranque de Bomba y Paso 2
│   PASO_1      PASO_2
├───[ ]──────────[/]─────────┬──────────────────────────────────────────(S) Q_BOMBA
│                            │
│                            │  FC_BYPASS
│                            └─────[ ]──────────────────────────────────(S) PASO_2

NETWORK 3: Detención de Bomba y Temporizador de Bloqueo
│   PASO_2      PASO_3
├───[ ]──────────[/]─────────┬──────────────────────────────────────────(R) Q_BOMBA
│                            │
│                            │                 Temp_Bloqueo
│                            └───────────┬──────[ TON ]──────┬──────────(S) PASO_3
│                                        │ IN              Q │
│                                  T#15s─┤ PT             ET │
│                                        └───────────────────┘

NETWORK 4: Rearranque de Bomba
│   PASO_3      PASO_4     Apertura           Temp_Rearranque
├───[ ]──────────[/]──────────[ ]────────┬──────[ TON ]──────┬─────┬────(S) PASO_4
│                                        │ IN              Q │     │
│                                   T#3s─┤ PT             ET │     └────(S) Q_BOMBA
│                                        └───────────────────┘

NETWORK 5: Gestión de Estados de Válvula y Bomba
│   PASO_4      PASO_5
├───[ ]──────────[/]─────────┬───────────────────────────────────
│                            │
│                            │  Apertura
│                            ├─────[ ]──────────────────────────────────(S) Q_BOMBA
│                            │
│                            │   Pausa
│                            ├─────[ ]──────────────────────────────────(R) Q_BOMBA
│                            │
│                            │ FC_ABIERTA
│                            └─────[ ]──────────────────────────────────(S) PASO_5

NETWORK 6: Finalización del Ciclo Activo
│   PASO_5      PASO_6
├───[ ]──────────[/]─────────┬──────────────────────────────────────────(R) Q_BOMBA
│                            │
│                            └──────────────────────────────────────────(S) PASO_6

NETWORK 7: Secuencia de Cierre y Reseteo General
│   Cierre
├───[ ]──────────────────────┬──────────────────────────────────────────(R) Q_BOMBA
│                            │
│                            ├──────────────────────────────────────────(S) Q_VALV_CIERRE
│                            │
│                            ├──────────────────────────────────────────(R) PASO_1
│                            │
│                            ├──────────────────────────────────────────(R) PASO_2
│                            │
│                            ├──────────────────────────────────────────(R) PASO_3
│                            │
│                            ├──────────────────────────────────────────(R) PASO_4
│                            │
│                            ├──────────────────────────────────────────(R) PASO_5
│                            │
│                            └──────────────────────────────────────────(R) PASO_6

NETWORK 8: Parada de Válvula por Fin de Carrera (Flanco Positivo)
│ FC_CERRADA
├───[P]─────────────────────────────────────────────────────────────────(R) Q_VALV_CIERRE
