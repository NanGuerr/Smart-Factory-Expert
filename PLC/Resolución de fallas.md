# Resolución de fallas en sistemas industriales 💢

El diagnóstico y la resolución de fallas en sistemas de automatización industrial es una habilidad crítica. Basado en el documento proporcionado sobre **Diagnóstico e Identificación de Fallas Comunes**, aquí presento una guía estructurada para abordar estos problemas, organizada por tipo de falla para facilitar tu aprendizaje:

---

### 1. PLC en Estado STOP 🛑

Cuando el PLC entra en este modo, detiene la ejecución del programa y coloca las salidas en una condición segura.

* **¿Cómo identificarlo?**: El LED de estado en el panel frontal indica "STOP". Frecuentemente, esta condición viene acompañada de un indicador de falla adicional.
* **Causas comunes**:
* **Errores de software**: Fallas internas en la lógica, como una operación de división por cero.
* **Hardware faltante**: Ausencia de una tarjeta de memoria obligatoria.
* **Problemas de periféricos**: Módulos de periferia incorrectos o fallas graves en la comunicación con los mismos.
* **Intervención externa**: Accionamiento accidental de la palanca de stop o envío de un comando de parada desde el software.



### 2. Fallas de Comunicación 📡

Representan la pérdida de enlace entre el PLC y otros componentes del sistema (HMI, SCADA o módulos remotos).

* **Síntomas**:
* En **HMI/SCADA**: Variables congeladas o indicadores de error (##### o !!!!!!).
* En **periferia**: Encendido de LEDs de error de bus (como "BF" o *Bus Fail* en equipos Siemens).


* **Causas típicas**:
* Configuraciones incorrectas: Direcciones IP, nodos o esclavos mal asignados.
* Daño físico: Cables seccionados o conexiones invertidas.
* Parámetros: Velocidad de comunicación (*baud rate*) incompatible.
* Alimentación: Falta de energía en el bus de campo.



### 3. Falla de Lectura en Canales Analógicos 📊

Ocurre cuando el valor capturado por el PLC no refleja la realidad física del proceso.

* **Síntomas**: Valores fuera de rango (ej. un sensor de 0-15 bar reportando 29 bar) o señales estáticas.
* **Causas técnicas**:
* Desajuste de la señal (ej. configurar entrada para corriente 4-20mA cuando el sensor envía tensión 0-10V).
* Problemas de conexión: Sensores cableados al revés o lazo abierto (cable cortado).
* Incompatibilidad de hardware: Confusión entre sensores de 2 hilos y entradas de 4 hilos.



### 4. Ruido en Entradas (Analógicas o Digitales) ⚡

El ruido eléctrico degrada la señal, provocando inestabilidad o activaciones fantasma.

* **Factores de riesgo**:
* Proximidad a motores, generadores o variadores de frecuencia sin apantallamiento.
* Tendido de cables de señal junto a cables de potencia.
* Falta de una referencia a tierra sólida o uso de cable no blindado.


### 5. Errores Esporádicos o Aleatorios 👻

Son los más complejos debido a que ocurren en milisegundos y son difíciles de observar visualmente.

* **Estrategias de diagnóstico**:
* **Función "Trace"**: Similar a un osciloscopio, permite graficar en tiempo real el comportamiento de las variables y almacenar un registro cuando la falla ocurre.
* **Marcas de detección**: Asignar una marca (*flag*) a la señal sospechosa. Aunque la señal dure un instante, la marca quedará enclavada, indicando que ocurrió la activación.
* **Filtrado por tiempo (TON)**: Implementar temporizadores que obliguen a que una señal sea estable durante un tiempo predeterminado antes de que el PLC ejecute una acción, evitando que activaciones espurias o ruido disparen paradas de motor no deseadas.


