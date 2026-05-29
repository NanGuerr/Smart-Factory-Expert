# 🔌 Sensores y Actuadores

Este documento resume de manera clara y estructurada las **Señales Estándares en la Industria**, **Sensores Digitales**, **Sensores Analógicos** y las técnicas de **Adaptación de Señales** para el control industrial.

---

## ⚡ 1. Señales Estándares en la Industria

Para lograr una alta compatibilidad entre dispositivos de diferentes fabricantes, la automatización industrial se rige bajo señales normalizadas.

### 🔘 Señales Digitales (Binarias)
Poseen únicamente dos estados lógicos discretos (`1` o `0`, `ON`/`OFF`, `TRUE`/`FALSE`).
* **📥 Entradas al PLC:** El estándar industrial por excelencia utiliza **24 VCC** (Voltaje de Corriente Continua). Es un requisito crítico que tanto el PLC como el sensor compartan la misma referencia de tensión (**GND o masa**).
* **📤 Salidas del PLC:** Pueden entregarse mediante dos tecnologías comunes:
  * Transistor / Fuente interna a **24 VCC**.
  * **Contacto seco de relé:** Funciona como un interruptor aislado, permitiendo conmutar voltajes independientes, tanto en corriente alterna (CA) como continua (CC). Las tensiones más habituales en la industria son **24V, 48V, 110V y 220V**.

### 📈 Señales Analógicas
Representan magnitudes físicas continuas y variables en el tiempo. Se dividen en dos categorías:
* **📐 Rangos de Voltaje:** `0..10 V`, `±10 V`, `±5 V`.
* **🔋 Rangos de Corriente:** `0..20 mA`, `4..20 mA`, `±20 mA`.

#### 🆚 Ventajas de las Señales de Corriente frente a las de Voltaje:
1. 🛡️ **Inmunidad al ruido:** Son mucho más resistentes a las interferencias electromagnéticas externas generadas por motores o líneas de potencia.
2. 📍 **Estabilidad en la distancia:** Al ser un lazo cerrado, la corriente es idéntica en cualquier punto del circuito, eliminando pérdidas por caída de tensión en cables largos.
3. 🦺 **Seguridad Humana:** El rango máximo (20 mA) se encuentra por debajo del umbral de riesgo eléctrico nocivo para el ser humano (30 mA).

#### 🎯 Beneficios Exclusivos del Lazo de 4..20 mA:
* 🪓 **Detección de cortes:** Al tener un "cero vivo" de 4 mA, si el cable se rompe o desconecta, el valor cae a 0 mA, permitiendo al PLC diagnosticar la falla inmediatamente.
* 📡 **Protocolo HART:** Permite superponer una señal digital sobre la línea analógica para realizar tareas de parametrización, calibración y diagnóstico avanzado del instrumento en tiempo real (siempre que el hardware sea compatible).

---

## 🛑 2. Sensores Digitales (Ejemplos de Campo)

Dispositivos que conmutan su estado para informar eventos discretos en el proceso:
* 🔘 **Elementos de Mando:** Pulsadores, interruptores manuales y llaves conmutadoras multiposición (ej. llave conmutadora de 4 posiciones).
* 🕵️‍♂️ **Sensores de Proximidad Inductivos:** Detectan la presencia de objetos metálicos sin necesidad de contacto físico.
* 🎛️ **Interruptores de Proceso:** * 🗜️ **Presostatos / Vacuostatos:** Conmutan al alcanzar un límite de presión o vacío.
  * 🌡️ **Termostatos:** Actúan según umbrales de temperatura.
  * 🌊 **Nivostatos:** Indican niveles críticos de líquidos o sólidos (lleno/vacío).

---

## 📊 3. Sensores Analógicos y Conexiones

Miden variables de manera escalar y requieren un circuito de acondicionamiento continuo. Dependiendo de su topología eléctrica y alimentación, se clasifican en:
* ⚡ **Sensores de Voltaje:** Transmiten variaciones de diferencia de potencial directo hacia la tarjeta de entrada analógica del PLC.
* 🔄 **Sensores de Corriente de 2 Hilos:** El mismo par de cables transporta simultáneamente la alimentación eléctrica al sensor y la señal de medida analógica (lazo de corriente).
* 🔲 **Sensores de Corriente de 4 Hilos:** Cuentan con un par de cables independientes destinados en exclusiva a la alimentación del instrumento (ej. 220 VCA o 24 VCC) y otro par independiente para emitir la señal analógica aislada.

---

## 🎛️ 4. Adaptación y Conversión de Señales

En muchas ocasiones, las características eléctricas del sensor de campo no coinciden de forma nativa con los módulos de entrada del PLC. Se emplean los siguientes métodos de adaptación:
* 🔄 **Adaptación de 4 Hilos a 2 Hilos:** Configuración mediante la inserción de fuentes externas y lazos en serie para unificar el canal de datos y alimentación.
* 🔌 **Conversión de Corriente a Voltaje:** Si dispones de un lazo de corriente (`4..20 mA`) pero el PLC solo acepta voltaje (`0..10 V`), se puede adaptar fácilmente colocando una resistencia de precisión en paralelo en los bornes de entrada del PLC para transformar el flujo de corriente en una caída de tensión medible.

---
