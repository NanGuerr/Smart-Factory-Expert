# 🚰 Tanque de agua industrial

El diagrama de bloques funcionales (FBD) estructurado para el control del tanque de agua industrial, asumiendo el comportamiento estándar de los sensores de nivel, dan un "1" lógico cuando el agua los cubre y un "0" cuando están en seco. Además,con interbloqueos de seguridad para que el tanque no intente llenarse y vaciarse al mismo tiempo.

### ⚙️ Diagramas de Bloques Funcionales (FBD) - Llenado de Tanque

```text
NETWORK 1: Control de la Válvula de Llenado (Q1)
El tanque comienza a llenarse si el nivel cae por debajo del sensor inferior. Se detiene al tocar el sensor superior
o si ocurre una emergencia. Se incluye interbloqueo con Q2.

Sensor Inferior (I1) ─[NOT]─┐
                            ├──►[  &  ] (B001) ──►[ S ]
Válvula Descarga (Q2) ─[NOT]┘                     [ RS ] (B002) ─────► Válvula Llenado (Q1)
                                               ┌──►[ R ]
Sensor Superior (I2) ───────┐                  │
                            ├──►[ >=1 ] (B003) ┘
Alarma Emergencia (Q3) ─────┘

─────────────────────────────────────────────────────────────────────────────────────────

NETWORK 2: Control de la Válvula de Descarga (Q2)
La descarga se activa mediante un comando externo (ej. un operador o un proceso). Se detiene automáticamente
cuando el tanque se vacía (sensor inferior en seco) o si hay emergencia.

Comando Descarga (I3) ──────┐
                            ├──►[  &  ] (B004) ──►[ S ]
Válvula Llenado (Q1) ─[NOT]─┘                     [ RS ] (B005) ─────► Válvula Descarga (Q2)
                                               ┌──►[ R ]
Sensor Inferior (I1) ─[NOT]─┐                  │
                            ├──►[ >=1 ] (B006) ┘
Alarma Emergencia (Q3) ─────┘

─────────────────────────────────────────────────────────────────────────────────────────

NETWORK 3: Temporizador de Emergencia y Alarma (Q3)
Si la válvula de llenado permanece encendida más tiempo del normal (ej. tubería rota o sensor superior dañado),
un temporizador activa una alarma y bloquea el sistema.

Válvula Llenado (Q1) ──────────►[ TON ] (B007) ──►[ S ]
                                                  [ RS ] (B008) ─────► Alarma / Corte (Q3)
Reset de Alarma (I4) ──────────────────────────►[ R ]

```

---

### 💡 Análisis del Funcionamiento Lógico

* **Válvula de Llenado (Q1 - Network 1):**
* **Encendido (Set):** Utilizamos un bloque `NOT` en el Sensor Inferior (`I1`). Cuando el agua baja y el sensor queda en seco (0 lógico), el `NOT` lo convierte en un 1. Si la válvula de descarga está apagada (segundo `NOT`), la compuerta `AND` (`B001`) envía la señal para abrir la válvula de llenado.
* **Apagado (Reset):** La válvula de llenado se cerrará en cuanto el agua alcance el Sensor Superior (`I2`) **O** si se activa la Alarma de Emergencia (`Q3`), gracias a la compuerta `OR` (`B003`).


* **Válvula de Descarga (Q2 - Network 2):**
* Tiene un interbloqueo en la compuerta `AND` (`B004`) para asegurar que **nunca** se pueda abrir si el tanque se está llenando (`Q1`).
* Se cerrará automáticamente (Reset) en el momento en que el tanque se quede vacío (cuando el Sensor Inferior `I1` marque 0, invertido por el `NOT` a 1) para evitar que entren burbujas de aire a las tuberías del proceso.


* **Temporizador de Emergencia (Q3 - Network 3):**
* El bloque de retardo a la conexión (`TON B007`) empieza a contar segundos/minutos en el instante en que `Q1` se abre.
* Si el tanque se llena normalmente y `Q1` se apaga a tiempo, el temporizador se reinicia a cero.
* Si el temporizador llega a su límite (por ejemplo, porque el agua se está fugando o el sensor superior se atascó), emite un pulso que "Setea" el bloque `RS` (`B008`), activando la salida `Q3`. Esta salida actúa cortando inmediatamente las bombas (revisar los Reset de Network 1 y 2) y requiere que un operador pulse el botón de Reset (`I4`) tras solucionar la avería.
