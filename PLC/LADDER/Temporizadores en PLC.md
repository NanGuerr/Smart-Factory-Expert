# ⏲️ Temporizadores

Basado en el código XML (estándar PLCopen) el programa corresponde a un entorno de **Diagrama Ladder (LD)** que utiliza un bloque de función de **Temporizador a la Conexión (TON)**.

A diferencia de las compuertas lógicas básicas, los temporizadores en Ladder suelen representarse como bloques (cajas) insertados directamente en la línea de control (escalón o *rung*).

Aquí tienes la representación gráfica en diagrama Ladder basada en tu código:

### 🔌 Temporizador a la Conexión

```text
NETWORK 1: Temporización de Señal (TON)
Al activarse el contacto xEntrada, el temporizador comienza a contar. Tras 4 segundos, la salida
se activa.

                 +------- TON0 -------+
    xEntrada     |        TON         |       xSalida
|------[ ]-------| IN               Q |---------( )-------|
|                |                    |                   |
|     t#4s ------| PT              ET |---(tTiempoAcum.)  |
|                +--------------------+                   |

```

---

### 💡 Análisis de los componentes del bloque:

1. **`xEntrada` (Contacto a `IN`):** Es la condición de arranque. Cuando este contacto se cierra (pasa a 1 lógico), el temporizador `TON0` comienza su conteo. Si la entrada se apaga antes de completar el tiempo, el temporizador se reinicia a cero.

2. **`t#4s` (Preselección `PT`):** Es el tiempo programado (*Preset Time*). Según tu código XML, este valor está fijo en **4 segundos**.

3. **`xSalida` (Bobina desde `Q`):** Es la salida principal del temporizador. Esta bobina solo se encenderá (Set) cuando la señal de `IN` se haya mantenido activa de forma ininterrumpida durante los 4 segundos completos.

4. **`tTiempoAcumulado` (Salida `ET`):** Es el tiempo transcurrido (*Elapsed Time*). Esta variable va mostrando en tiempo real cuánto tiempo lleva contando el temporizador (de 0s a 4s). Es muy útil para mostrar el progreso en pantallas HMI (Interfaces Hombre-Máquina).



### ⚙️ Ejemplo de uso

```text
NETWORK 1: Arranque de Bomba con Retardo y Enclavamiento
Al activar la entrada 'xMarcha', el temporizador TON0 comienza a contar. Tras 3 segundos, su salida (Q)
se activa. Esta señal pasa por el contacto cerrado 'xParada' y enciende la bobina 'xBomba'.
Una vez encendida, el contacto paralelo de 'xBomba' la mantiene autoenclavada aunque se suelte la marcha.

                 +------- TON0 -------+
    xMarcha      |        TON         |      xParada
|-----[ ]--------| IN               Q |---+----[/]----------( ) xBomba --|
|                |                    |   |                              |
|     t#3s ------| PT              ET |--(tTiempoTranscurrido)           |
|                +--------------------+   |                              |
|   xBomba                                |                              |
|-----[ ]---------------------------------+                              |

─────────────────────────────────────────────────────────────────────────────────────────

NETWORK 2: Temporización de Alarma de Falla (Función Set)
Si el contacto 'xFalla' se cierra y se mantiene así durante 4 segundos, el temporizador TON1 emite una señal
que activa la bobina Set (S) de 'xAlertaFalla', dejándola encendida permanentemente hasta que sea reseteada.

                 +------- TON1 -------+
    xFalla       |        TON         |     
|-----[ ]--------| IN               Q |---------------------(S) xAlertaFalla -|
|                |                    |                                       |
|     t#4s ------| PT              ET |---                                    |
|                +--------------------+                                       |

```

---

### 💡 Análisis de los componentes del bloque:

* **Bloque `TON0` (Network 1):** Actúa como una protección o confirmación de arranque. Evita que la bomba arranque por un toque accidental del botón `xMarcha`; el operador debe mantener presionado el botón por 3 segundos continuos (`t#3s`). La variable `tTiempoTranscurrido` va leyendo este avance.

* **Autoenclavamiento (`xBomba` paralelo a `TON0`):** Una vez que la bomba arranca, la energía fluye por debajo a través del contacto `[ ] xBomba`. Esto permite que el operador suelte el botón `xMarcha` (apagando el temporizador) sin que la bomba se detenga.

* **Contacto `[/] xParada`:** Es el botón de detención. Al ser normalmente cerrado en la lógica, permite el paso de corriente. Cuando se presiona (se abre), corta la energía a la bobina `xBomba`, botando el enclavamiento.

* **Bloque `TON1` y Bobina Set `(S)` (Network 2):** Es un filtro de falsas alarmas. La falla debe estar presente 4 segundos seguidos (`t#4s`) para ser considerada real. Al cumplirse el tiempo, la bobina de retención `(S)` asegura que la alerta sonora o visual (`xAlertaFalla`) quede memorizada, incluso si la señal original de la falla desaparece rápido.

  Basado en el código XML (estándar PLCopen) que has proporcionado, he analizado la lógica y la he traducido a un **Diagrama Ladder (Lenguaje de Contactos)**.

Este programa contiene dos redes principales: una para el arranque retardado de una bomba con su respectivo autoenclavamiento, y otra para generar una alarma de falla si un problema persiste por cierto tiempo.

Aquí tienes la representación gráfica en diagrama Ladder:

### ⚙️ Otro Ejemplo de uso

```text
NETWORK 1: Arranque de Bomba con Retardo y Enclavamiento
Al activar la entrada 'xMarcha', el temporizador TON0 comienza a contar. Tras 3 segundos, su salida (Q)
se activa. Esta señal pasa por el contacto cerrado 'xParada' y enciende la bobina 'xBomba'. Una vez
encendida, el contacto paralelo de 'xBomba' la mantiene autoenclavada aunque se suelte la marcha.

                 +------- TON0 -------+
    xMarcha      |        TON         |      xParada
|-----[ ]--------| IN               Q |---+----[/]----------( ) xBomba --|
|                |                    |   |                              |
|     t#3s ------| PT              ET |--(tTiempoTranscurrido)           |
|                +--------------------+   |                              |
|   xBomba                                |                              |
|-----[ ]---------------------------------+                              |

─────────────────────────────────────────────────────────────────────────────────────────

NETWORK 2: Temporización de Alarma de Falla (Función Set)
Si el contacto 'xFalla' se cierra y se mantiene así durante 4 segundos, el temporizador TON1 emite una señal
que activa la bobina Set (S) de 'xAlertaFalla', dejándola encendida permanentemente hasta que sea reseteada.

                 +------- TON1 -------+
    xFalla       |        TON         |     
|-----[ ]--------| IN               Q |---------------------(S) xAlertaFalla -|
|                |                    |                                       |
|     t#4s ------| PT              ET |---                                    |
|                +--------------------+                                       |

```

---

### 💡 Análisis de los componentes del bloque:

* **Bloque `TON0` (Network 1):** Actúa como una protección o confirmación de arranque. Evita que la bomba arranque por un toque accidental del botón `xMarcha`; el operador debe mantener presionado el botón por 3 segundos continuos (`t#3s`). La variable `tTiempoTranscurrido` va leyendo el avance en tiempo real.

* **Autoenclavamiento (`xBomba` paralelo a `TON0`):** Una vez que la bomba arranca, la energía fluye por la rama inferior a través del contacto `[ ] xBomba`. Esto permite que el operador suelte el botón `xMarcha` (lo que apaga el temporizador) sin que la bomba se detenga.

* **Contacto `[/] xParada`:** Es el botón de detención. Al ser normalmente cerrado en la lógica, permite el paso de corriente por defecto. Cuando se presiona (se abre), corta la energía a la bobina `xBomba`, botando el enclavamiento.

* **Bloque `TON1` y Bobina Set `(S)` (Network 2):** Es un filtro de falsas alarmas. La falla debe estar presente 4 segundos seguidos (`t#4s`) para ser considerada real. Al cumplirse el tiempo, la bobina de retención `(S)` asegura que la alerta sonora o visual (`xAlertaFalla`) quede memorizada, incluso si la señal original de la falla desaparece rápidamente.
