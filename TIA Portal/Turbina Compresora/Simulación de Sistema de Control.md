# 💻 Guía de Simulación Integral - Sistema de Control

Este documento detalla el procedimiento para configurar, integrar y verificar la simulación completa del sistema de control de la turbina utilizando TIA Portal.

## 🎛️ 1. Lógica de Comando: Local vs. HMI
Para garantizar la seguridad y la correcta operación, hemos implementado una selectora que prioriza los mandos:
* **Modo Local (Selectora = 0):** Se priorizan los comandos físicos del tablero local (contacto normalmente cerrado).
* **Modo Panel/HMI (Selectora = 1):** Se priorizan los comandos provenientes del panel HMI.
* *Nota:* Esta lógica se aplica tanto al arranque como a la parada controlada, añadiendo el contacto de la selectora en serie con los comandos correspondientes.

## ⚙️ 2. Preparación del Entorno de Simulación
Para realizar la simulación integral, seguimos estos pasos:
1. **Librería de la Turbina:** Extraer los archivos comprimidos.
2. **Importación a TIA Portal:**
   * Abrir "Librerías" -> "Plantillas Maestras".
   * Arrastrar **Lazo Control** a *Objetos Tecnológicos*.
   * Arrastrar **Modelo Planta** y **Turbina** a *Bloques de Programa*.
3. **Interrupción Cíclica:** Agregar un bloque OB de interrupción cíclica, arrastrar el bloque de funciones de la Turbina dentro y asignar un nombre de instancia.

## 🔗 3. Configuración del Bloque de Simulación
Configuramos las entradas/salidas del bloque de simulación:
* **Conexiones Digitales:** Motor auxiliar, Junta Neumática, Frenos, Sensores de quemadores (Q1/Q2), Modo Control (Manual/Auto).
* **Conexiones Analógicas:** * Setpoint manual/automático -> Salidas analógicas.
    * Salidas del bloque -> Entradas analógicas (Velocidad, Presión).
* **DB Lazo:** Arrastrar el objeto "Lazo Control" desde *Objetos Tecnológicos*.

## 🏗️ 4. Integración en el Main (OB1)
Para que los escalados funcionen correctamente:
* Cortar los segmentos de escalado del `OB1` principal.
* Pegarlos debajo de la simulación.
* Verificar que todos los bloques (incluyendo el bloque de seguridad) estén correctamente llamados en el `OB1`.

## 🧪 5. Ejecución de la Simulación
1. **Guardar y Compilar:** Iniciar la simulación (`PLCSim`).
2. **Forzado de Señales:** Abrir "Tabla Sim" y forzar las entradas digitales (I 0.0 en adelante).
3. **Observación:** Abrir el editor de secuencia e iniciar la observación.
4. **Puesta en Servicio:** Acceder al "Lazo Control" y abrir la ventana de puesta en servicio para monitorear el comportamiento gráfico.

## 🚀 6. Validación de la Operación
* **Arranque:** Activar Paradas de Emergencia (1) y Válvula Principal. Iniciar secuencia.
* **Secuencia:** Verificar el acople de junta (1 seg) -> arranque motor -> aceleración.
* **Transiciones:** * 478 RPM: Activar Sensores Q1/Q2.
    * 2750 RPM: Desacople de junta y apagado de motor.
* **Régimen:** El sistema pasa a modo automático y regula a la consigna definida.
* **Parada Controlada:** Presionar el botón de parada. La válvula regula al 10% (10s) -> 0%. A las 2500 RPM se aplican frenos. A < 1 RPM se resetea la secuencia, quedando lista para un nuevo ciclo.
