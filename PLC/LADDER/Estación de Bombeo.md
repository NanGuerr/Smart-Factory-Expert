# 🏭 Proyecto de Automatización de Estación de Bombeo

---

## 📋 1. Descripción General del Proceso

El proyecto consiste en el control de **2 bombas de agua** que pueden ser operadas de forma Local (Pozo) o Remota (Sala de Control). El sistema cuenta con estrictas medidas de seguridad e interbloqueos para proteger la integridad mecánica de los equipos y las tuberías.

### 🚦 Reglas de Operación y Seguridad:
* **Modos de Operación:** Seleccionables mediante una llave de 3 posiciones (Pozo, Sala o Desconectado).
* **Exclusión Mutua:** Solo puede funcionar una bomba a la vez; operan de manera alternada.
* **Interbloqueo por Válvulas:** Es imperativo que la válvula de salida esté abierta antes de arrancar. **No se puede arrancar la bomba si la válvula está cerrada**.
* **Protección por Sobrecaudal:** Si el transmisor de flujo (FIT-100) registra más de **6.0 lt/s**, el sistema debe detener automáticamente las bombas y disparar una alarma.
* **Fallas Locales:** Cada bomba tiene un sensor de falla propio que también detiene el equipo y emite una alerta.

---

## 🔌 2. Mapeo de Entradas y Salidas (I/O)

En base a la transcripción de las imágenes y la estructura interna del archivo `plc.xml`, el PLC requiere la siguiente asignación de variables (Tagging).

### 📥 Entradas (Inputs)
| Variable | Tipo | Dirección | Descripción |
| :--- | :--- | :--- | :--- |
| `B1_AL` / `B2_AL` | Bool | `%I0.0` / `%I0.3` | Alarma local de Bomba 1 y Bomba 2 |
| `B1_AB` / `B2_AB` | Bool | `%I0.1` / `%I0.4` | Válvulas B1 y B2 - Posición ABIERTA |
| `B1_CE` / `B2_CE` | Bool | `%I0.2` / `%I0.5` | Válvulas B1 y B2 - Posición CERRADA |
| `SEL_SALA` / `SEL_POZO` | Bool | `%I0.6` / `%I1.1` | Selectoras de modo de control (Sala / Pozo) |
| `CDO_AR_SALA` / `CDO_AR_POZO` | Bool | `%I0.7` / `%I1.2` | Comandos de Arranque (Sala / Pozo) |
| `CDO_PAR_SALA` / `CDO_PAR_POZO`| Bool | `%I1.0` / `%I1.3` | Comandos de Parada (Sala / Pozo) |
| `CAUDAL` | Real | `%ID2` | Lectura analógica del Caudalímetro |

### 📤 Salidas (Outputs)
| Variable | Tipo | Dirección | Descripción |
| :--- | :--- | :--- | :--- |
| `B1_Q` / `B2_Q` | Bool | `%Q0.2` / `%Q0.5` | Señal física de arranque a contactores (B1/B2) |
| `B1_ST_SALA` / `B2_ST_SALA` | Bool | `%Q0.0` / `%Q0.3` | Indicadores luminosos de marcha en SALA |
| `B1_ST_POZO` / `B2_ST_POZO` | Bool | `%Q0.1` / `%Q0.4` | Indicadores luminosos de marcha en POZO |
| `FALLA_SALA` / `FALLA_POZO` | Bool | `%Q0.6` / `%Q0.7` | Bocinas/Balizas de aviso de falla general |

---

## 🏗️ 3. Diagramas de Bloques Funcionales

Para traducir este problema a programación, el sistema se divide en tres bloques lógicos principales que interactúan entre sí.

### Bloque A: Lógica de Selección y Mando
Este bloque decide de dónde provienen las órdenes basándose en las selectoras.

```text
[Selector SALA] ----+
                    |---> (AND Lógico) ---> [Comando Válido]
[Botón Arranque] ---+                            |
                                                 v
                                       HACIA BLOQUE DE MOTOR

```

### Bloque B: Interbloqueos y Seguridad (Safety Chain)

Toda orden de arranque pasa por este filtro. Si una condición no se cumple, se corta la señal a la bobina del motor (`B1_Q` o `B2_Q`).

```text
[Comando Válido] ----------------------------------------------+
                                                               |
[Sensor Válvula CERRADA] ---(Invertido / NOT)------------------|
                                                               |---> [BOBINA MOTOR Q]
[Alarma Local Motor] ------(Invertido / NOT)-------------------|
                                                               |
[Caudalímetro CAUDAL] ---> [Bloque >= 6.0] --(Invertido)-------+

```

### Bloque C: Gestión de Alarmas

Cualquier falla dispara las alarmas generales en ambas estaciones.

```text
[Alarma Local B1] ---------+
                           |
[Alarma Local B2] ---------+---> (OR Lógico) ---> [Salida FALLA SALA]
                           |                 ---> [Salida FALLA POZO]
[Bloque Caudal >= 6.0] ----+

```

---

## 🧠 4. Análisis del Código `plc.xml` (Ladder)

Al revisar el archivo XML adjunto, se observa que la lógica está estructurada exactamente bajo estos principios mediante programación combinacional:

1. **Bobinas de Set/Reset:** El arranque de las bombas (`B1_Q` y `B2_Q`) utiliza enclavamientos (Set/Reset) operados por los pulsadores, siempre condicionados por el estado del selector (`SEL_SALA` o `SEL_POZO`).
2. **Bloque GE (Greater or Equal):** Se utiliza el bloque matemático de comparación `>=` configurado con la constante `6.0` y la entrada analógica `CAUDAL`. La salida de este bloque va directamente en paralelo a las bobinas de Reset de ambas bombas para garantizar la detención inmediata.


3. **Prevención de Válvula Cerrada:** Los contactos `B1_CE` y `B2_CE` (Normalmente Cerrados) están en serie con las bobinas de arranque. Si el sensor detecta que la válvula está cerrada (cambia a estado `1`), el contacto se abre e impide que la energía llegue a la bobina de Set.

El archivo contiene un esquema típico de alternancia y control para un sistema de dos bombas con bloques de comparación analógica. Lo he dividido según los comentarios (`Indicaciones`) internos del mismo programa.


```text

// Indicaciones Bomba 1 Línea 1: Condiciones de Arranque (Set)

│  CDO_AR_POZO   SEL_POZO         B2_Q      B1_AB     B1_CE  AUX_ARRANQUE     B1_Q
├───[ ]───────────[ ]──────┬──────[/]───────[ ]───────[/]───────[/]──────┬────(S)──
│                          │                                             │
│  CDO_AR_SALA   SEL_SALA  │                                             │AUX_ARRANQUE
├───[ ]───────────[ ]──────┘                                             └────(S)──

// Línea 2: Condiciones de Parada (Reset)

│ CDO_PAR_POZO   SEL_POZO                                                 B1_Q
├───[ ]───────────[ ]──────┬──────────────────────────────────────────────────(R)──
│                          │
│ CDO_PAR_SALA   SEL_SALA  │
├───[ ]───────────[ ]──────┤
│                          │
│     B1_AL                │
├───[ ]────────────────────┤
│                          │
│              ┌─────────┐ │
│              │   GE    │ │
│    CAUDAL ───┤ IN1  OUT├─┘
│              │         │
│       6.0 ───┤ IN2     │
│              └─────────┘

// Línea 3: Estado de la Bomba 1

│     B1_Q                                                                 B1_ST_POZO
├───[ ]──────────────────────────────────────────────────────────────────┬────( )──
│                                                                        │
│                                                                        │ B1_ST_SALA
│                                                                        └────( )──

// Indicaciones Bomba 2 Línea 4: Condiciones de Arranque (Set)

│  CDO_AR_POZO   SEL_POZO         B1_Q      B2_AB     B2_CE  AUX_ARRANQUE     B2_Q
├───[ ]───────────[ ]──────┬──────[/]───────[ ]───────[/]───────[ ]──────┬────(S)──
│                          │                                             │
│  CDO_AR_SALA   SEL_SALA  │                                             │AUX_ARRANQUE
├───[ ]───────────[ ]──────┘                                             └────(R)──

// Línea 5: Condiciones de Parada (Reset)

│ CDO_PAR_POZO   SEL_POZO                                                 B2_Q
├───[ ]───────────[ ]──────┬──────────────────────────────────────────────────(R)──
│                          │
│ CDO_PAR_SALA   SEL_SALA  │
├───[ ]───────────[ ]──────┤
│                          │
│     B2_AL                │
├───[ ]────────────────────┤
│                          │
│              ┌─────────┐ │
│              │   GE    │ │
│    CAUDAL ───┤ IN1  OUT├─┘
│              │         │
│       6.0 ───┤ IN2     │
│              └─────────┘

// Línea 6: Estado de la Bomba 2

│     B2_Q                                                                 B2_ST_POZO
├───[ ]──────────────────────────────────────────────────────────────────┬────( )──
│                                                                        │
│                                                                        │ B2_ST_SALA
│                                                                        └────( )──

// Indicaciones de Alarma (Línea 7: Falla en el Pozo)

│     B1_AL                                                               FALLA_POZO
├───[ ]────────────────────┬──────────────────────────────────────────────────( )──
│                          │
│     B2_AL                │
├───[ ]────────────────────┤
│                          │
│              ┌─────────┐ │
│              │   GE    │ │
│    CAUDAL ───┤ IN1  OUT├─┘
│              │         │
│       6.0 ───┤ IN2     │
│              └─────────┘

// Línea 8: Falla en la Sala

│     B1_AL                                                               FALLA_SALA
├───[ ]────────────────────┬──────────────────────────────────────────────────( )──
│                          │
│     B2_AL                │
├───[ ]────────────────────┤
│                          │
│              ┌─────────┐ │
│              │   GE    │ │
│    CAUDAL ───┤ IN1  OUT├─┘
│              │         │
│       6.0 ───┤ IN2     │
│              └─────────┘

```

---

**Documento Técnico de Análisis** 
