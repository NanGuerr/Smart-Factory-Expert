# Sistema de Control de Llenado de Tanque 💧

Sistema automatizado para el llenado y gestión de un tanque de almacenamiento de agua, basado en la interpretación de los esquemas adjuntos.

## 1. Visión General del Sistema 🏗️
El sistema se ilustra en **llenado de tanque con motor y valvula.png**. Se trata de un tanque de recolección de agua de lluvia con control de nivel mediante sensores:

*   **Sensores (Entradas):**
    *   **S2 (I2):** Sensor de nivel alto (Apagado de entrada de agua de red).
    *   **S3 (I3):** Sensor de nivel medio (Encendido de entrada de agua de red).
    *   **S4 (I4):** Sensor de nivel bajo (Protección contra marcha en seco).
*   **Actuadores (Salidas):**
    *   **Motor (M1/Q1):** Bombea agua hacia un tanque de presión.
    *   **Válvula (K4/Q2):** Controla el llenado desde la red de agua potable.

---

## 2. Análisis de Lógica de Control ⚙️

### 💻 Diagrama de Bloques Funcionales (FBD)
Como se muestra en **llenado de tanque con diagrama de bloques funcionales.png**, el control se divide en dos procesos mediante bloques lógicos:

1.  **Control del Motor (Q1):**
    *   Utiliza una compuerta **AND**.
    *   **Lógica:** El motor se activa solo si S3 (I3) y S4 (I4) están activos, asegurando que hay agua suficiente para no trabajar en seco.
2.  **Control de la Válvula (Q2):**
    *   Utiliza una lógica combinacional con compuertas **OR** y **AND**.
    *   **Función:** Gestiona la histéresis del llenado: permite que la válvula se abra para llenar el tanque cuando el nivel cae, usando la memoria de estado (feedback de Q2) para mantener el llenado hasta alcanzar el nivel deseado (S2).

### 🪜 Diagrama de Escalera (Ladder)
En **llenado de tanque con ladder.png**, la lógica se traduce al lenguaje de contactos eléctricos (LAD):

*   **Rung 1 (Motor):** Implementa la serie de contactos I3 e I4 para activar Q1.
*   **Rung 2, 3 y 4 (Válvula):** Implementa el enclavamiento. Utiliza contactos normalmente cerrados y abiertos para gestionar el ciclo de llenado/apagado basado en los sensores S2, S3 y S4, garantizando que la válvula se mantenga activa incluso después de que el nivel sobrepase S3, hasta llegar a S2.

```text
NETWORK 1: Control de Motor (Bomba)
│    I3            I4
├───[ ]──────────[ ]──────────────────────────────────────────( ) Q1
NETWORK 2: Control de Válvula (Llenado)
│    I3            I2
├───[/]──────────[/]────────┬─────────────────────────────────( ) Q2
│                           │
│    I4            Q2       │
└───[/]──────────[ ]────────┘
```
---

## 3. Procedimientos Operativos 🛠️

1.  **Arranque del sistema:** Al detectar agua (S4 activo), el sistema habilita las funciones de bombeo y llenado.
2.  **Protección:** Si el nivel baja de S4, el motor se apaga automáticamente para evitar daños (protección contra marcha en seco).
3.  **Gestión de Niveles (Llenado):**
    *   Cuando el nivel desciende por debajo de S3, la válvula de la red (K4/Q2) se abre.
    *   El llenado continúa hasta que el agua alcanza el nivel S2, momento en el cual el sistema desactiva la válvula para evitar desbordamientos.

---

### 🧠 Bloques Funcionales (FBD)

En el diagrama de bloques que adjuntaste, el sistema se simplifica visualmente:

1. **Bloque Motor:** Representado por una compuerta **AND** estándar. Las señales `I3` e `I4` entran al bloque, y la salida `Q1` solo es verdadera si ambas entradas son verdaderas.
2. **Bloque Válvula:** Se implementa mediante una estructura de **LATCH** (o flip-flop RS). Las entradas `I3` e `I2` actúan como condiciones de *RESET* (parada), mientras que la lógica combinada de los sensores permite el *SET* (arranque).

Este diseño es fundamental en la industria para garantizar que el motor nunca opere sin agua (protección por nivel bajo) y que el llenado sea autónomo sin intervención constante del operario.

```text
Entrada S3 (I3) ──┐
                  │  AND (&)  ───────►  Motor (M1/Q1)
Entrada S4 (I4) ──┘
             

Válvula (K4/Q2) ──────────────┐          
                              │  ──── OR ───────►    ──────────┐                 
Entrada S2 (I2) ──[NOT]┤──────│                                │ AND (&) ───────► Válvula (K4/Q2)
                              │      Entrada S2 (I2) ──[NOT]┤──┘
Entrada S4 (I4) ──[NOT]┤──────┘
```
