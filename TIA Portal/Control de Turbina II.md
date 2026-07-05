# Representación técnica ⚙️ 

Para representar la lógica de control de tu turbina compresora siguiendo el formato de diagramas de contactos (LADDER) se ha estructurado la secuencia de arranque y operación basada en los pasos descritos previamente en Programación de Control de Turbina.

```text

NETWORK 1: Activación de Paso 1 (Arranque)
│   Arranque_L    Velocidad < 0.5   Valvula_Prin
├───[ ]──────────────[ ]──────────────[ ]────────┬──────────────────────(S) PASO_1
│                                                │
│                                                └──────────────────────(S) CDM_Junta

NETWORK 2: Temporización y Acople de Motor (Paso 2)
│   PASO_1      PASO_2    Delay_Acople
├───[ ]──────────[/]─────────┬──────[ TON ]──────┬──────────(S) CDM_Motor
│                            │ IN            Q   │
│                       T#1s─┤ PT           ET   │
│                            └───────────────────┘
│
│   Velocidad > 478
│────[ ]────────────────────────────────────────────────────────────────(S) PASO_2

NETWORK 3: Habilitación de Chisperos y Apertura 10% (Paso 3)
│   PASO_2      PASO_3    Delay_Chispero
├───[ ]──────────[/]─────────┬──────[ TON ]──────┬──────────(S) CDM_Chispero1
│                            │ IN            Q   │       └──(S) CDM_Chispero2
│                       T#2s─┤ PT           ET   │
│                            └───────────────────┘
│
│   PASO_2      Delay_Chispero.Q
├───[ ]──────────────[ ]────────────────────────────────────────────────(MOVE 10 -> Consigna_Manual)
│
│   Sensor_Q1   Sensor_Q2
├───[ ]──────────────[ ]────────────────────────────────────────────────(S) PASO_3

NETWORK 4: Aceleración a 25% y Paso 4
│   PASO_3      PASO_4
├───[ ]──────────[/]─────────┬──────────────────────────────────────────(MOVE 25 -> Consigna_Manual)
│                            │
│   Velocidad > 2750         │
│────[ ]─────────────────────┴──────────────────────────────────────────(S) PASO_4

NETWORK 5: Desacople de Motor y Paso 5
│   PASO_4      PASO_5
├───[ ]──────────[/]─────────┬──────────────────────────────────────────(R) CDM_Junta
│                            │
│                            │      Delay_Apagado
│                            ├──────[ TON ]──────┬──────────────────────(R) CDM_Motor
│                            │ IN            Q   │
│                       T#5s─┤ PT           ET   │
│                            └───────────────────┘
│
│   Motor_Apagado (Delay_Apagado.Q)
│────[ ]────────────────────────────────────────────────────────────────(S) PASO_5

NETWORK 6: Modo Automático y Finalización (Paso 6)
│   PASO_5      PASO_6
├───[ ]──────────[/]─────────┬──────────────────────────────────────────(MOVE 1 -> Modo_Auto)
│                            │                                       └──(MOVE 4600 -> Consigna_Auto)
│                            │                                       └──(MOVE 0 -> Consigna_Manual)
│                            │
│   Velocidad >= 4600        │
│────[ ]─────────────────────┴──────────────────────────────────────────(S) PASO_6

NETWORK 7: Reset de Chisperos
│   PASO_3
├───[ ]─────────────────────────────────────────────────────────────────(R) CDM_Chispero1
│                                                                    └──(R) CDM_Chispero2

NETWORK 8: Parada de Emergencia (General)
│   Emergencia_R  OR  Emergencia_L
├───[ ]──────────────[/]───────────┬────────────────────────────────────(R) PASO_1..PASO_6
│                                  │                                 └──(R) CDM_Motor
│                                  │                                 └──(R) CDM_Chispero1..2
│                                  └────────────────────────────────────(S) CDM_Escape

```
