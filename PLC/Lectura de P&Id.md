# 🏗️ Diagramación y Lectura de P&Id

---

## 📘 Resumen 

Se enfoca en la metodología profesional para abordar un proyecto de automatización. El paso crucial antes de escribir una sola línea de código es la **planificación y el análisis técnico** de los requisitos del proceso.

---

## 📋 1. Metodología de Diagramación
Para controlar un sistema de forma eficiente, el programador debe realizar un levantamiento detallado de la infraestructura:

* **Inspección de Documentación:** Revisión exhaustiva de planos, esquemas eléctricos y diagramas de instrumentación (P&ID).
* **Identificación de Componentes:** Mapeo de todos los elementos físicos involucrados (válvulas, sensores, motores, indicadores).
* **Inspección de Terreno:** En sistemas de renovación (retrofitting), es vital verificar el estado actual del cableado y los componentes existentes.

---

## 🛠️ 2. Desglose del Problema
Un proyecto bien desglosado se divide principalmente en:

* **Entradas (Inputs):** Sensores de presión, caudalímetros, selectoras, paradas de emergencia, interruptores de límite.
* **Salidas (Outputs):** Señales de arranque de motores, válvulas solenoide, indicadores luminosos de estado, alarmas sonoras.

> **Ejemplo de Mapeo de Variables (Tagging):**
> | Nombre | Tipo de datos | Descripción |
> | :--- | :--- | :--- |
> | `B1_AL` | Bool | Alarma Bomba 1 |
> | `B1_AB` | Bool | Válvula B1 - ABIERTA |
> | `B1_Q`  | Bool | Señal de arranque B1 |
> | `B2_ST_SALA` | Bool | Indicador estado B2 - Sala |

---

## ⚙️ 3. Tipos de Programación en PLC
El módulo destaca dos enfoques principales según la naturaleza de la aplicación:

1. **Programación Cíclica / Combinacional:** Ideal para procesos donde las salidas dependen directamente del estado actual de las entradas (lógica de estados).
2. **Programación Secuencial:** Utilizada para procesos que siguen un orden de pasos definido (Etapa 1 → Etapa 2 → Etapa 3), común en máquinas de transferencia o llenado automático.

---

## 💡 Consejos para el Programador
* **Documentación:** Mantener una tabla de variables actualizada es la mejor herramienta para evitar errores de dirección o duplicidad de señales.
* **Modularidad:** Dividir el código en bloques funcionales (ej. un bloque para el control de la Bomba 1, otro para la Bomba 2) hace que el programa sea más fácil de depurar y mantener.
* **Seguridad ante todo:** Identificar siempre las señales de emergencia y los estados seguros antes de implementar cualquier secuencia automática.

---

### 1. Elementos Principales (Componentes)

* **Transmisor de Flujo (FT-101):** Ubicado en la línea principal de tubería. Es el encargado de medir el caudal del fluido que pasa por ella.
* **Controlador de Flujo (FIC-101):** Representado por el círculo central, es el "cerebro" que recibe la señal del transmisor, la compara con el valor deseado (setpoint) y envía la orden de corrección.
* **Válvula de Control (FV-101):** Ubicada en la tubería, es el elemento final de control que se abre o cierra para regular el paso del fluido basándose en la orden del controlador.

### 2. Señalización y Conexiones

* **Línea Continua (— — —):** La conexión entre el Transmisor (FT-101) y el Controlador (FIC-101) es una **señal eléctrica**.
* **Línea con Trazo y Puntos (— · — · —):** La conexión entre el Controlador (FIC-101) y la Válvula de Control (FV-101) indica una **señal neumática** (común en válvulas accionadas por aire).

### 3. Texto en el Diagrama

* **"Flow Process"**: Título superior que indica que el diagrama describe un proceso de control de flujo.
* **"Control Room"**: Indica que el controlador (FIC-101) está montado en el panel de control o sala de control, ya que el círculo no tiene una línea horizontal en su interior.
* **"Field"**: Indica que los elementos (FT y FV) están instalados directamente en el área de proceso ("en campo").

---

Este tipo de diagrama es fundamental para que los ingenieros y técnicos comprendan cómo se automatiza el flujo de un líquido o gas dentro de una planta industrial, asegurando que la medición y la regulación funcionen en un bucle cerrado.

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



---

**Documento Técnico de Análisis** 
