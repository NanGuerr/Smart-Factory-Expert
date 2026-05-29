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
