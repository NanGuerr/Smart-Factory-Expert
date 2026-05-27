# Resumen de Automatización Industrial

## 🌡️ 10 Sensores Analógicos
1.  **Sensores de temperatura:** Miden el calor mediante sondas como RTD o termopares.
2.  **Sensores de presión:** Monitorean la presión en fluidos o gases.
3.  **Sensores de nivel:** Determinan la cantidad de material en tanques.
4.  **Sensores de caudal (Caudalímetros):** Miden el flujo de fluidos en tuberías.
5.  **Sensores de distancia:** Calculan la cercanía de objetos mediante láser o ultrasonido.
6.  **Sensores de luz (LDR / Fotocélulas):** Miden la intensidad lumínica ambiental.
7.  **Sensores de velocidad (Tacómetros):** Miden las RPM de ejes rotativos.
8.  **Sensores de humedad:** Detectan la cantidad de vapor de agua en el aire o materiales.
9.  **Sensores de fuerza (o carga):** Miden peso o tensión mediante galgas extensiométricas.
10. **Sensores de pH:** Miden el nivel de acidez o alcalinidad en soluciones.

## 🤖 10 Sensores Digitales
1.  **Sensores de proximidad inductivos:** Detectan objetos metálicos sin contacto.
2.  **Sensores de proximidad capacitivos:** Detectan materiales metálicos y no metálicos.
3.  **Sensores de proximidad fotoeléctricos (Barrera):** Detectan objetos al interrumpir un haz de luz.
4.  **Sensores de proximidad fotoeléctricos (Reflexivos):** Detectan el reflejo de luz sobre un objeto.
5.  **Finales de carrera (Limit Switches):** Detectan el contacto físico de una parte móvil.
6.  **Sensores de efecto Hall (Digitales):** Detectan campos magnéticos.
7.  **Sensores ultrasónicos (Modo ON/OFF):** Detectan la presencia a una distancia fija.
8.  **Pulsadores y selectores:** Actuadores manuales para enviar señales de control.
9.  **Termostatos (Bimetálicos):** Interruptores que actúan ante un límite de temperatura.
10. **Presostatos:** Interruptores que activan al alcanzar una presión determinada.

## 🧠 Conceptos Fundamentales

### ⚡ Conformación de un Motor de CC
Un motor de CC está compuesto por un **estator** (carcasa fija que genera un campo magnético mediante imanes o bobinas) y un **rotor** que gira al convertirse en un imán temporal cuando la corriente lo atraviesa. Este sistema se completa con el conjunto de **colector y escobillas**, las cuales permiten el paso de la electricidad hacia el rotor mediante contacto físico durante su rotación, transmitiendo así la fuerza mecánica.

### 🔄 Diferencia entre Lazo Abierto y Cerrado
La diferencia principal radica en la realimentación. En un sistema de **lazo abierto**, el controlador envía una orden y no supervisa el resultado, operando de manera "ciega" (como una tostadora que calienta por tiempo fijo sin saber si el pan se quemó). En cambio, en un sistema de **lazo cerrado**, el proceso cuenta con sensores que miden constantemente la salida para compararla con el objetivo deseado, permitiendo que el sistema se autoajuste automáticamente.

### 📊 Diferencia entre Sensor Analógico y Digital
La diferencia fundamental es la capacidad de detalle: el **sensor analógico** funciona como un "cuentista" que entrega valores continuos y detallados (como medir exactamente 25.4 °C en lugar de solo identificar si hace calor), mientras que el **sensor digital** es binario, operando únicamente con dos estados posibles, "Sí" o "No" (encendido/apagado o 1/0), lo que lo hace ideal para detectar presencias.

### 💻 Tipos de PLC y Marcas Reconocidas
Los PLC se clasifican principalmente en **compactos** (CPU, entradas y salidas integradas en una pieza) y **modulares** (permiten expandir la capacidad añadiendo módulos independientes en un rack). Las marcas más reconocidas a nivel mundial son:
* **Siemens** (Alemania)
* **Rockwell Automation / Allen-Bradley** (EE. UU.)
* **Schneider Electric** (Francia)
* **Mitsubishi Electric** (Japón)
* **Omron** (Japón)
