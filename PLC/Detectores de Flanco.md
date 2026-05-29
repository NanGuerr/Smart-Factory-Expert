# 🎛️ Programación LD y Detectores de Flanco

Este documento presenta una transcripción estructurada, descriptiva y un análisis analítico del material didáctico del **Módulo 3: Curso Introductorio de PLC**, enfocado en la simbología Ladder y el comportamiento dinámico de las señales de conmutación. 🚀

---

## 📚 1. Estructura General del Módulo 3

El lenguaje **LD (Ladder Diagram / Diagrama de Contactos)** basa su lógica en la representación de esquemas eléctricos de relés. Dentro de este módulo, los componentes críticos de control se dividen en:

* 🔌 **01. Simbología Básica:** Contactos normalmente abiertos (NO), normalmente cerrados (NC) y bobinas de salida.
* ⚡ **02. Detectores de Flanco:** Bloques de análisis de transiciones lógicas rápidas (Positivos y Negativos).
* 🔒 **03. Enclavamientos:** Memorias y circuitos de autorretención (*Set / Reset*).
* ⚖️ **04. Comparadores:** Validación de variables analógicas y numéricas ($=, >, <, \geq, \leq$).
* ⏱️ **05. Temporizadores:** Control de tiempos de activación y desactivación (TON, TOF, TP).
* 🔢 **06. Contadores:** Cómputo de eventos digitales (CTU, CTD, CTUD).
* 🧮 **07. Operaciones Aritméticas y Transferencia:** Manipulación matemática de datos de registros de memoria.

---

## ⚡ 2. Análisis Detallado: Detectores de Flanco

Un detector de flanco es un elemento de programación especial en Ladder que evalúa el cambio de estado de una variable booleana (*Trigger*) comparando su valor del ciclo actual con el guardado en una variable de respaldo (*Memoria*). 

> ⏳ **Concepto Clave (Ciclo de Scan):** Cuando el detector cumple su condición de disparo, el contacto lógico en el esquema se "cierra" **durante un único ciclo de programa (Scan)**, volviendo a abrirse de inmediato en el ciclo siguiente.

---

### 🟢 A. Detectores de Flanco Positivo (P)

El detector de flanco positivo (también conocido como flanco de subida) sensa la transición cuando una variable digital pasa de un estado lógico **0 (Falso/Apagado)** a un estado **1 (Verdadero/Encendido)**.

#### 🗺️ Representación en Diagrama Ladder
En el esquema se observa la asignación de direcciones para el bit físico de entrada y la marca de memoria interna necesaria para almacenar el estado anterior:
```text
  "Boton"             "Memoria"           "Lampara"
   %I0.1               %M10.0               %Q0.0
────┤ P ├────────────────────────────────────( )────

```

#### 📊 Tabla de Funcionamiento Dinámico (Paso a Paso)

El ciclo de ejecución demuestra cómo la salida `%Q0.0` se activa únicamente en el instante exacto del cambio (Paso 3):

| Paso | Variable Trigger (`%I0.1`) | Bit de Memoria (`%M10.0`) | Salida Física (`%Q0.0`) | ⚙️ Comportamiento del Sistema |
| --- | --- | --- | --- | --- |
| **1** | 0 | 0 | 0 | Sistema en reposo. Entrada inactiva. |
| **2** | 0 | 0 | 0 | Sin cambios en el estado de la entrada. |
| **3** | **1** | **0** | **1** | **¡Disparo!** La entrada sube a 1. La memoria aún retiene el 0 del ciclo anterior. Se genera el pulso de salida. |
| **4** | 1 | 1 | 0 | La memoria se actualiza a 1. La salida se apaga inmediatamente tras cumplirse el ciclo de scan. |
| **5** | 1 | 1 | 0 | La entrada sigue presionada; no se generan nuevos pulsos. |

---

### 🔴 B. Detectores de Flanco Negativo (N)

El detector de flanco negativo (o flanco de bajada) sensa la transición inversa: detecta el momento exacto en el que una variable digital pasa de un estado lógico **1 (Verdadero/Encendido)** a un estado **0 (Falso/Apagado)**, como al soltar un pulsador.

#### 🗺️ Representación en Diagrama Ladder

```text
  "Boton"             "Memoria"           "Lampara"
   %I0.1               %M10.0               %Q0.0
────┤ N ├────────────────────────────────────( )────

```

#### 📊 Tabla de Funcionamiento Dinámico (Paso a Paso)

La salida `%Q0.0` permanece en reposo durante la pulsación y se dispara únicamente cuando la señal cae (Paso 6):

| Paso | Variable Trigger (`%I0.1`) | Bit de Memoria (`%M10.0`) | Salida Física (`%Q0.0`) | ⚙️ Comportamiento del Sistema |
| --- | --- | --- | --- | --- |
| **1** | 0 | 0 | 0 | Sistema en reposo. |
| **2** | 0 | 0 | 0 | Sin actividad en el captador. |
| **3** | 1 | 0 | 0 | La entrada se activa (pasa a 1), pero el bloque **N** la ignora. |
| **4** | 1 | 1 | 0 | La memoria interna se actualiza a 1 en el siguiente scan. |
| **5** | 1 | 1 | 0 | La entrada se mantiene estable en nivel alto. |
| **6** | **0** | **1** | **1** | **¡Disparo!** La entrada cae a 0, pero la memoria conservaba el 1 previo. Se genera el pulso por un ciclo. |
| **7** | 0 | 0 | 0 | La memoria se limpia a 0. La salida se desactiva. |

---

## 👁️ 3. Cronograma del Pulso (Análisis de Señales)

Geométricamente, el comportamiento de los detectores de flanco dentro del tiempo de ejecución del autómata se puede estructurar de la siguiente manera:

```text
Entrada Digital (%I0.1)
      ┌──────────────────────┐
      │                      │
______│                      └______

Flanco Positivo - P (%Q0.0)
      🔲 Pulse (1 Scan)
______│_____________________________

Flanco Negativo - N (%Q0.0)
                             🔲 Pulse (1 Scan)
_____________________________│______

```

---

## 🛠️ 4. Aplicaciones Prácticas en Automatización Industrial

La utilización de detectores de flancos (`P` y `N`) es indispensable en la programación industrial para:

1. 📥 **Control de Pulsadores Únicos:** Permite alternar el estado de una máquina (Marcha/Paro) utilizando un único botón físico sin sufrir por el tiempo que el operador deja el dedo sobre el contacto.
2. 🧮 **Sistemas de Conteo Completos:** Enviar señales limpias a los bloques contadores (`CTU`) al paso de objetos por un sensor fotoeléctrico, evitando conteos dobles causados por rebotes físicos de la señal.
3. 🚨 **Captura de Alarmas Críticas:** Registrar el instante exacto en el que un sensor de presión o temperatura supera un umbral de falla para congelar los valores analógicos en un registro de diagnóstico histórico.

