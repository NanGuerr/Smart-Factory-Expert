# ⚙️ Sistema de Ventilación

Basado en la consigna del sistema de ventilación, se tiene la representación de la lógica en **Diagrama de Bloques Funcionales (FBD)**.

El sistema implementa un **temporizador de retardo a la conexión (TON)**: cuando se activa el interruptor o sensor `I1`, el sistema espera el tiempo configurado antes de encender el ventilador `Q1`.

### 🏗️ Diagramas de Bloques Funcionales (FBD)

Separándolo en **tres redes lógicas (Networks)** claras mediante diagramas de bloques funcionales (FBD).


```text
NETWORK 1: Control del Extractor (Q1)
Lógica de enclavamiento principal para el extractor con múltiples condiciones de parada.

Entrada ON (I1) ──────────────────────────────────────────────►[ S ]
                                                               [ RS ] (B001) ─────► Extractor (Q1)
Entrada OFF (I2) ──────┐                                       [ R ]
                       │                                         ▲
[NOT] (B008) ──────────┼──────►[ >=1 ] OR (B009) ────────────────┘
                       │
Salida (Q3) ───────────┘

─────────────────────────────────────────────────────────────────────────────────────────

NETWORK 2: Control del Ventilador (Q2)
El ventilador se activa si I3 está presente y el Extractor (Q1) está apagado.

Entrada (I3) ─────────────────────────────────────────────────┐
                                                              ├──►[  &  ] (B002) ──► Ventilador (Q2)
Salida (Q1) ─────────────►[ NOT ]─────────────────────────────┘

─────────────────────────────────────────────────────────────────────────────────────────

NETWORK 3: Gestión de Temporizadores y Alarma/Estado (Q3)
Lógica combinacional con retardos (TON) dependientes de Q1 y Q2 para activar Q3.

Entrada (I3) ──────────┐
                       ├──►[  &  ] (B005) ──►[ TON ] (B006) ──┐
Salida (Q1) ───────────┘                                      │
                                                              ├──►[ >=1 ] (B007) ──►[ S ]
Entrada (I4) ──────────┐                                      │                     [ RS ] (B008) ──► Salida (Q3)
                       ├──►[  &  ] (B003) ──►[ TON ] (B004) ──┘                 ┌──►[ R ]
Salida (Q2) ───────────┘                                                        │
                                                                                │
Entrada OFF (I2) ───────────────────────────────────────────────────────────────┘

```

---

### 💡 Análisis del Funcionamiento Lógico

1. **Extractor (Q1) - *Network 1*:**
* Se enciende (Set) mediante el pulso de `I1`.
* Se apaga (Reset) si ocurre **cualquiera** de estas tres cosas (vía la compuerta OR `B009`):
* Se presiona el botón de parada `I2`.
* Se activa la señal `Q3`.
* La señal invertida del bloque `B008` (es decir, cuando B008 está en 0, envía un 1 lógico que podría mantener el reset, creando un interbloqueo condicional).

2. **Ventilador (Q2) - *Network 2*:**
* Utiliza una compuerta **AND**. Se activa únicamente cuando la `Entrada I3` está activa **Y** el extractor `Q1` está *apagado* (gracias al bloque NOT).

3. **Salida de Control/Estado (Q3) - *Network 3*:**
* Depende de dos temporizadores independientes (`TON`).
* **Ruta 1:** Si `I3` y el extractor `Q1` están activos, comienza a contar el temporizador `B006`.
* **Ruta 2:** Si `I4` y el ventilador `Q2` están activos, comienza a contar el temporizador `B004`.
* Si cualquiera de los dos temporizadores finaliza su conteo, la compuerta **OR** (`B007`) envía un pulso para encender (Set) el enclavamiento `B008`, activando la salida `Q3`.
* Esta salida `Q3` se apaga (Reset) manualmente mediante la `Entrada I2`.

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
