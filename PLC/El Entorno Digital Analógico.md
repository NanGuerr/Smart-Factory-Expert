# 🎛️ El Mundo Analógico vs. El Entorno Digital 

Este documento resume de forma concisa y estructurada las propiedades de las **Señales Digitales y Analógicas**, los procesos de conversión mediante **ADC** y **DAC**, y la estrategia de conmutación **PWM**.

---

## 🔘 1. Señales Digitales (Discretas)

* **Definición:** Una señal digital (o binaria) es aquella que posee exclusivamente **dos estados lógicos** (`1` o `0`, `ON`/`OFF`, `TRUE`/`FALSE`).
* **Voltajes habituales:** En el hardware industrial, el estado alto `1` suele traducirse en un voltaje continuo positivo (**24 VCC o 5 VCC**), mientras que el estado bajo `0` equivale a **0 VCC**.
* **Propósito en el PLC:** Se emplean para determinar estados de elementos binarios como pulsadores, switches, fines de carrera y relés. Además, constituyen el lenguaje base interno con el que los microprocesadores traducen y manipulan cualquier dato del entorno exterior.

---

## 📈 2. Señales Analógicas (Continuas)

* **Definición:** Es una señal continua en el tiempo que puede adoptar **infinitos valores** entre dos puntos determinados (similar al comportamiento de una perilla giratoria).
* **Variables típicas:** Utilizadas para cuantificar magnitudes físicas variables como la presión, la temperatura, el caudal o el nivel.
* **Escalas industriales normalizadas:** Para que el PLC interprete estas magnitudes, se adaptan linealmente a rangos físicos de tensión o corriente:
  * 📐 **Voltaje:** `0..10 V`, `±10 V`, `±5 V`
  * 🔋 **Corriente:** `0..20 mA`, `4..20 mA`, `±20 mA`

---

## 🔄 3. Conversión de Señales Analógicas a Digitales (ADC)

Para operar con datos analógicos, los procesadores requieren de un circuito **ADC** (*Analog-to-Digital Converter*). El ciclo consta de las siguientes fases secuenciales:

1. 📥 **Adquisición:** Se releva la señal analógica directamente desde el borne de entrada física del PLC.
2. ⏱️ **Muestreo:** Se toma un valor instantáneo de la señal cada cierto intervalo de tiempo fijo.
3. 📐 **Cuantización:** Se analiza la muestra y se le asigna un valor discreto en función de la resolución del convertidor.
4. 🔢 **Codificación:** Se convierte el valor ponderado en una secuencia binaria puramente digital.
5. 💾 **Almacenamiento:** El valor binario final se resguarda dentro de un registro en la memoria de trabajo del PLC, identificado con una dirección específica.

🔬 **Tipos de circuitos ADC más utilizados:**
* Flash
* Sigma-Delta (Σ-Δ)
* Simple / Doble Rampa
* Aproximaciones Sucesivas

---

## 🔌 4. Conversión de Señales Digitales a Analógicas (DAC)

Cuando el PLC requiere gobernar un actuador analógico (ej. regular la apertura de una válvula proporcional), debe traducir sus variables lógicas en señales físicas. El proceso inverso se realiza mediante un circuito **DAC** (*Digital-to-Analog Converter*):

1. 🏷️ **Direccionamiento:** Se identifica la dirección del borne físico de salida analógica asignado.
2. 🔠 **Decodificación:** Se lee el valor numérico en binario almacenado en el registro de memoria.
3. 📏 **Cuantización:** Se determina el nivel correspondiente de tensión o corriente de salida en función de la resolución.
4. ⚡ **Conversión:** Se energiza el hardware convertidor para inyectar la señal eléctrica a la salida.
5. 🧼 **Filtrado:** Se acondiciona eléctricamente la salida para eliminar el efecto de "escalonamiento" propio de la señal discreta.

⚙️ **Tipos de circuitos DAC más comunes (Redes de resistencias de precisión):**
* Resistencias Ponderadas
* Red R-2R

---

## 🌊 5. Modulación por Ancho de Pulso (PWM)

Existe un método alternativo y económico para enviar comandos de comportamiento analógico (como regular la intensidad de una lámpara o la velocidad de un motor) sin necesidad de contar con una tarjeta de salidas analógicas dedicadas: la **Modulación por Ancho de Pulso (PWM)**.

* ⏱️ **Funcionamiento:** Se define un tiempo de ciclo fijo y muy corto llamado **Período**. En base al valor analógico deseado (escalado de 0% a 100%), la salida digital se mantiene encendida (`ON`) un porcentaje proporcional de ese período.
* 🔋 **Ciclo de Trabajo (*Duty Cycle*):** Es el tiempo relativo en que la señal digital permanece en nivel alto durante un período. 
  * *Ejemplo:* Si el valor deseado es del 60% en un período de 10 ms, la salida digital se enciende durante 6 ms y se apaga los 4 ms restantes del ciclo.
* ⚠️ **Restricción de Hardware:** Al implicar una conmutación a frecuencias muy elevadas, **no se deben utilizar salidas a relé**, ya que el desgaste mecánico las destruiría rápidamente. Se exige el uso de salidas digitales de estado sólido (**Transistor**).

---
