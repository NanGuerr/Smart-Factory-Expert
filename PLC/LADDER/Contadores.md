# 4 ejemplos basados en la lógica de control 🎛️

### 1. Contador de Marcha/Parada (Contador de ciclos)

Este gráfico representa cómo un contador (CTU) incrementa su valor cada vez que ocurre un pulso de marcha y se reinicia mediante una entrada.

```text
    xPulso (I)      +------- CTU0 ------+
|------[ ]----------| CU             Q  |----( ) xConteoFinalizado
|                   |                   |
|   xReset (I) -----| R                 |
|                   |                   |
|   INT#10 ---------| PV                |
|                   +-------------------+

```

---

### 2. Generador de Pulso y Temporizador

Basado en tu archivo "Contador y generador de pulso.xml", aquí se utiliza un temporizador `TON` para generar un retardo antes de activar una salida.

```text
                     +------- TON0 -------+
    xEntrada         |        TON         |
|------[ ]-----------| IN               Q |----( ) xSalida
|                    |                    |
|    t#10s ----------| PT              ET |----(iMinutos)
|                    +--------------------+

```

---

### 3. Contador de Paletizado

Este código está diseñado para contar una cantidad específica de productos o cajas antes de activar el proceso.

```text
    xSensor          +------- CTU_Palet --+
|------[ ]-----------| CU             Q  |----( ) xProcesoPaletizado
|                    |                   |
|   xReset_Fin ------| R                 |
|                    |                   |
|    INT#50 ---------| PV                |
|                    +-------------------+

```

---

### 4. Lógica de Alarma de Mantenimiento (Tu ejemplo solicitado)

Esta estructura es la que mencionaste en tu consulta original, combinando el estado de un motor, un temporizador para medir tiempo de uso y un botón de reseteo.

```text
    Motor(Q3)        +------- B003 -------+
|------[ ]-----------| EN             Q   |----( ) Alarma_Mant(Q4)
|                    |                    |
|   Mant(I1) --------| R                  |
|                    +--------------------+

```

---

### Notas técnicas para tu implementación:

* **[ EN ] (Enable):** En tu ejemplo, esta entrada habilita el conteo del temporizador. Si el motor se apaga, el tiempo acumulado (según el tipo de bloque) podría detenerse o reiniciarse.
* **[ R ] (Reset):** Es fundamental para las alarmas de mantenimiento; al presionar `I1`, fuerzas el valor del temporizador `B003` a 0, apagando la alarma `Q4` hasta que el motor cumpla nuevamente el tiempo preestablecido.
* **Variables:** Asegúrate en tu software (como LOGO! Soft Comfort) de asignar las direcciones físicas correctas (`Q3`, `Q4`, `I1`) tal como aparecen en los archivos XML adjuntos.
