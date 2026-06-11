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

# Escalar Sensor Lineal 📉

La lógica del archivo **"Escalar sensor lineal.xml"** que has proporcionado, he analizado su contenido, el cual realiza una operación matemática para convertir un valor de entrada crudo de un sensor a una escala de temperatura, y luego evalúa si esa temperatura supera un límite para activar una alerta.

### Análisis de la Lógica del Programa

El programa sigue dos secuencias principales en su bloque de función `Main`:

1. **Escalamiento de Señal:** Toma la variable `iSensorTemperatura` (de tipo `ULINT`), la multiplica por 200 y la divide por 32767 para obtener un valor entero de temperatura en `iTemperatura`. Esto es típico de la conversión de señales analógicas (por ejemplo, de un convertidor A/D de 15 bits a una escala de 0-200 grados).
2. **Lógica de Alerta:** Utiliza un bloque comparador `GT` (Greater Than) que verifica si `iTemperatura` es mayor a 80. Si esta condición se cumple, se activa la salida `xAlertaSobretemperatura`.

---

### Gráfico ejemplo de contador 🔄

Diagrama Ladder que representa cómo funcionaría esa lógica de control de motor y alarma:

```text
NETWORK 1: Activación de Alarma de Mantenimiento
Cuando el Motor (Q3) está encendido, habilita el temporizador (B003). 
Si el motor opera continuamente por el tiempo configurado, la salida Q4 se activa.

    Motor(Q3)          +------- B003 -------+
|-----[ ]--------------| EN              Q  |-------( ) Alarma_Mant(Q4)
|                      |                    |
|                      | PT          (ET)   |
|                      +--------------------+
|
|   Mant(I1)
|-----[ ]-------------------------------------------( R ) Alarma_Mant(Q4)

```

### Explicación del diagrama:

* **[ EN ] (Enable):** Al recibir la señal de `Motor(Q3)`, el temporizador `B003` comienza a acumular tiempo.
* **Temporización:** Una vez que el tiempo predefinido se cumple, la salida del bloque `B003` (la bobina `Q4`) se energiza, indicando que es necesario realizar el mantenimiento.
* **[ R ] (Reset):** El botón `I1` (Botón Mantenimiento) actúa como un reinicio para la alarma. Al presionarlo, se fuerza la bobina de la alarma a su estado original (apagado/0), permitiendo reiniciar el conteo tras haber realizado las labores de mantenimiento.
