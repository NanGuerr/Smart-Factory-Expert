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

# 🗺️ Guía Técnica: Lectura e Interpretación de Diagramas P&ID

---

## 📘 Resumen de Análisis
La lectura de diagramas **P&ID** (Piping and Instrumentation Diagram) es la habilidad técnica fundamental para cualquier programador de PLC. Estos diagramas no solo muestran tuberías, sino que representan la "lógica de instrumentación" del proceso, permitiendo al programador identificar qué sensores (entradas) y elementos de control (salidas) debe gestionar.

---

## 🔍 Análisis de los Elementos del P&ID

Los diagramas proporcionados ilustran la estandarización utilizada en la industria (normativa ISA) para la representación de instrumentos:

### 1. Interpretación de los Círculos (Instrumentos)
El círculo representa el dispositivo de control o medición:
* **Ubicación:** * Si el círculo tiene una **línea horizontal** en su interior, el instrumento está instalado en un **Panel de Control** (a la vista del operador).
    * Si el círculo **no tiene línea**, el instrumento está instalado directamente en **Campo** (cerca de la tubería o equipo).
* **Etiquetado:** Cada círculo contiene letras que definen su función. 
    * *Ejemplo:* **FIC** significa **F**low (Flujo), **I**ndicator (Indicador), **C**ontroller (Controlador).

### 2. Tipos de Señales y Conexiones
Las líneas que unen los instrumentos representan cómo se comunica la información:
* **Línea continua (—):** Señal eléctrica (señales 4-20mA, digitales, etc.).
* **Línea con marcas transversales (— // —):** Señal neumática (aire comprimido para actuar válvulas).
* **Línea con círculos (—o—o—):** Señal de bus de datos o comunicación digital (común en protocolos modernos).


---

## 🛠️ Procedimientos para la Automatización (Flujo de Trabajo)

Para traducir un P&ID a un programa de PLC, se sigue un procedimiento técnico riguroso:

### Paso 1: Mapeo de Instrumentos
1. **Identificación de etiquetas (Tags):** Listar cada instrumento presente en el plano (ej. `FT-101`, `FV-101`).
2. **Definición de Función:** Clasificar si es una **Entrada** (Sensor, Transmisor) o una **Salida** (Válvula, Bomba, Motor).

### Paso 2: Determinación del Tipo de Señal
Es crítico conocer el tipo de señal para configurar el PLC:
* **Señales Analógicas:** Lecturas continuas (presión, nivel, caudal). Requieren tarjetas de entrada analógica y escalamiento en el software.
* **Señales Digitales:** Estados discretos (`On/Off`, `Abierto/Cerrado`). Requieren tarjetas de entrada digital (DI) o salida digital (DO).

### Paso 3: Análisis del Bucle de Control
Estudiar cómo interactúan los elementos:
* ¿El controlador (`C`) ajusta la válvula (`FV`) basado en el valor que lee el transmisor (`FT`)? 
* Esto define si se implementará un **Bucle Cerrado (PID)** o una lógica secuencial simple.

---

## 💡 Recomendaciones para el Programador
* **Consistencia:** Mantén siempre el nombre de la variable (Tag) en el PLC idéntico al código del P&ID. Si el plano dice `FT-101`, la variable en el PLC debe ser `FT_101`.
* **Seguridad:** Los P&ID también contienen información de seguridad (como válvulas de alivio o interruptores de emergencia). **Nunca** omitas estas señales en tu lógica de programación.
* **Documentación:** Crea una tabla de E/S (Entradas/Salidas) basada en el P&ID antes de empezar a programar. Esto reduce errores y facilita el mantenimiento futuro.

---
