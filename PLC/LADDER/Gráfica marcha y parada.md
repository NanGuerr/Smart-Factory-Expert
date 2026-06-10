
# 📈 Representación gráfica 2 Bombas:

Basado en el código XML (PLCopen) la lógica y la he traducido a un **Diagrama Ladder (Lenguaje de Contactos)**.

El código que compartiste corresponde a un circuito clásico y muy útil en la industria: **Un sistema de alternancia de dos bombas con un solo botón de marcha**. Cada vez que presionas "Marcha", arranca una bomba diferente, distribuyendo el desgaste entre ambas.


```text
NETWORK 1: Marcha/Parada Bomba 1
El interbloqueo inicial (xBomba2) asegura que no funcionen ambas a la vez. Si la Memoria 1 (xM1) está
desactivada, al pulsar xMarcha arranca la Bomba 1 y se auto-enclava.

     xBomba2       xM1        xMarcha                  xParada
|------[/]----+----[/]----------[ ]----+-----------------[/]----------( ) xBomba1 --|
|             |                        |                                            |
|             +----[ ] xBomba1 --------+                                            |


NETWORK 2: Alternancia (Set M1)
Una vez que la Bomba 1 arranca, activa la Memoria 1 (Set). Esto "prepara" el sistema para que la próxima vez
sea el turno de la Bomba 2.

     xBomba1                                                               
|------[ ]------------------------------------------------------------(S) xM1 ------|
|                                                                                   |


NETWORK 3: Marcha/Parada Bomba 2
Similar a la red 1. Si la Bomba 1 está apagada y la Memoria 1 (xM1) ESTÁ activada, al pulsar xMarcha le toca
arrancar a la Bomba 2, auto-enclavándose.

     xBomba1       xM1        xMarcha                  xParada
|------[/]----+----[ ]----------[ ]----+-----------------[/]----------( ) xBomba2 --|
|             |                        |                                            |
|             +----[ ] xBomba2 --------+                                            |


NETWORK 4: Alternancia (Reset M1)
Cuando la Bomba 2 arranca, resetea (apaga) la Memoria 1. De esta forma, el ciclo se reinicia y la próxima vez
le tocará de nuevo a la Bomba 1.

     xBomba2
|------[ ]------------------------------------------------------------(R) xM1 ------|
|                                                                                   |

```

### 💡 Análisis de los componentes:

1. **Contactos `[/] xBomba2` y `[/] xBomba1` al inicio:** Son **interbloqueos de seguridad**. Garantizan que si la Bomba 2 está encendida, la corriente no pueda pasar hacia la bobina de la Bomba 1 bajo ninguna circunstancia (y viceversa).

2. **Contactos `[/] xM1` y `[ ] xM1`:** Actúan como un **conmutador (Flip-Flop)**. La memoria `xM1` decide a quién le toca trabajar. Si `xM1` es `0`, el camino se abre para la Bomba 1. Si `xM1` es `1`, el camino se abre para la Bomba 2.

3. **Ramas en paralelo `[ ] xBomba1` y `[ ] xBomba2`:** Son los **enclavamientos (Latch)**. Permiten que puedas soltar el botón de `xMarcha` (que es un pulsador momentáneo) y la bomba siga funcionando hasta que alguien presione el pulsador de `xParada`.
