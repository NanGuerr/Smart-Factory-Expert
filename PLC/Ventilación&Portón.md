# Sistema de Ventilación

Basado en la consigna del sistema de ventilación, se tiene la representación de la lógica en **Diagrama de Bloques Funcionales (FBD)**.

El sistema implementa un **temporizador de retardo a la conexión (TON)**: cuando se activa el interruptor o sensor `I1`, el sistema espera el tiempo configurado antes de encender el ventilador `Q1`.

### 🏗️ Diagramas de Bloques Funcionales (FBD)

#### NETWORK 1: Temporización de Arranque

El bloque `TON` recibe la señal de entrada y, una vez cumplido el tiempo programado, envía una señal de activación.

```text
Entrada (I1) ─────┐
                  │  TON (Retardo) ───────► Salida_T (M1)
Tiempo (PT) ──────┘

```

#### NETWORK 2: Control del Ventilador (Q1)

La señal del temporizador (o marca interna `M1`) es la que finalmente habilita la salida del ventilador.

```text
Salida_T (M1) ────────────────────────────► Ventilador (Q1)

```

---

### 💡 Análisis de los Bloques

* **Bloque `TON` (Timer On-Delay):** Es el corazón de este sistema. Su función es crear una "demora". Esto es muy útil en sistemas de ventilación para evitar arranques repentinos debido a interferencias eléctricas o para permitir que otros sistemas (como sensores de gas o temperatura) se estabilicen antes de encender el ventilador.
* **Salida `Q1` (Ventilador):** Es la bobina física o relé que acciona el motor del ventilador. En este diseño, depende exclusivamente del temporizador.

Si deseas que el ventilador se pueda apagar o encender de forma manual además del automático, el diagrama necesitaría una compuerta `OR` adicional para integrar la señal de un pulsador manual con la señal del temporizador.
```text

Entrada ON (I1) ──────────────────────┐
                                      │                                    ────┐ ───[NOT]┤ (B002)
                                      │ Reset RS (B001) ──── Extrator (Q1)     │
Entrada OFF (I2)────┐                 │                                        │
                    │──── OR (B009)───┘                                    ────┘ ───────── (B005)
[NOT]┤ (B008)───────│ 
                    │
Salida (Q3)         │
     ───────────────┘

             ───────┐         ─────┐
                    │ Salida (Q1)  │ ─── AND & (B002) ────── Ventilador (Q2) ─── (B003)
Entrada (I3)        │         ─────┘
                    │ ── [NOT]┤ ──────┐ 
                    │                 │ ── AND & (B005) ─── TON (B006)
            ────────┘ ── Salida (Q1) ─┘                         │ 
                                                                │ ───OR (B007) ───┐ RS (B008)── (Q3)── (B009)
                                                                │                 │
Entrada (I4) ───────┐               ───┐                        │                 │
                    │──── AND & (B003) │ ─────►  TON (B004)─────┘            Entrada OFF (I2)
Salida (Q2) ────────┘               ───┘


```


# Sistema Final de Carrera (Portón)


```text
Entrada S3 (I3) ──┐
                  │  AND (&)  ───────►  Motor (M1/Q1)
Entrada S4 (I4) ──┘
             

Válvula (K4/Q2) ──────────────┐          
                              │  ──── OR ───────►    ──────────┐                 
Entrada S2 (I2) ──[NOT]┤──────│                                │ AND (&) ───────► Válvula (K4/Q2)
                              │      Entrada S2 (I2) ──[NOT]┤──┘
Entrada S4 (I4) ──[NOT]┤──────┘

Entrada (I1) ─────┐
                  │  TON (Retardo) ───────► Salida_T (M1)
Tiempo (PT) ──────┘

```
