# 📋 Diagramación y Planificación de un Proyecto de Automatización

El éxito en la implementación de un sistema de control con PLC comienza mucho antes de escribir la primera línea de código. Se basa en una identificación exhaustiva de los requerimientos y una planificación ordenada. 🏗️

## 🔍 Paso 1: Lectura e Interpretación del P&ID
El **P&ID (Piping & Instrumentation Diagram)** es nuestra hoja de ruta, basada en la norma **ISA S5.1**. 🗺️
* **¿Qué nos muestra?**: Conexiones entre tuberías, instrumentos, válvulas, sensores (temperatura, nivel, presión) y actuadores (bombas).
* **Utilidad**: Permite visualizar la relación lógica y física de todos los componentes del sistema de control.

## ⚙️ Paso 2: Dimensionamiento de Entradas y Salidas (E/S)
Una vez entendido el proceso, debemos cuantificar qué señales necesitamos para controlar el sistema. 📊
* **Análisis**: Definir cuántas señales son necesarias y de qué tipo (Digitales o Analógicas).
* **Identificación**: Clasificar cada instrumento según:
    * Nombre del instrumento.
    * Ubicación física.
    * Parámetro a medir o controlar.

## 🛠️ Paso 3: Selección del PLC
No todos los controladores son iguales. Al elegir el "cerebro" del proyecto, debemos evaluar: 🧠
* **Tamaño y complejidad** del proceso.
* **Cantidad y tipo de E/S** (digitales, analógicas, comunicaciones).
* **Entorno** donde operará (industrial, exterior, temperatura, etc.).
* **Presupuesto** del cliente.
* **Disponibilidad** y **Soporte técnico** local.

## 📝 Paso 4: Armado de la Tabla de E/S (I/O Table)
Este es el paso final de la planificación. Consiste en documentar cada variable en una tabla para organizar el direccionamiento en el software de programación. 🗄️

| Nombre | Tipo de datos | Dirección | Descripción |
| :--- | :--- | :--- | :--- |
| **B1_AL** | Bool | %I0.0 | Alarma B1 |
| **B1_AB** | Bool | %I0.1 | Válvula B1 ABIERTA |
| **B2_Q** | Bool | %Q0.5 | Señal de arranque B2 |
| **CAUDAL** | Real | %ID2 | Caudalímetro |

