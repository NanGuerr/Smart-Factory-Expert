# 🏗️ Lógica Start/Stop en PLC

La lógica "Start/Stop" es la base fundamental de toda la lógica de control industrial (PLC) 🏭.

El esquema simple `---| |-------|/|--------( )` funciona como una compuerta lógica **AND**, pero para que se comporte como un control de "Start/Stop" industrial (donde presionas un botón momentáneo y el equipo se queda encendido), le falta un elemento crucial: el **enclavamiento** (también llamado "sel-in" o "retención") 💡.

A continuación, explico cómo debe configurarse realmente y por qué funciona así.

## ⚙️ El Circuito de Enclavamiento (Start/Stop)

Para que el sistema tenga "memoria" y no se apague al soltar el botón de inicio, debemos colocar un contacto auxiliar de la salida en paralelo al botón de *Start*.

### Estructura del Diagrama
```text
START (NO)            STOP (NC)
---| |-------+----------|/|--------( OUT )
             |
---| |-------|
OUT (NO)
(LATCH)

```

## 🛠️ ¿Cómo funciona cada componente?

* **Botón de STOP (Contacto NC - Normalmente Cerrado) 🛑:**
* Es el elemento de seguridad. Al ser NC, la electricidad pasa a través de él de forma natural (el estado lógico es "1" o "verdadero").
* Si el cable se corta o se presiona el botón, el circuito se abre y corta la energía inmediatamente.


* **Botón de START (Contacto NO - Normalmente Abierto) 🟢:**
* Es el interruptor de inicio. Espera a que el operario presione el botón para cerrar el circuito.


* **Contacto LATCH (Salida en paralelo) 🔒:**
* Este es el "seguro". Cuando la salida (`OUT`) se activa, este contacto paralelo también se cierra. Esto permite que la corriente siga fluyendo por esta rama, aunque sueltes el botón de *Start*.



## 🔄 Secuencia de Operación

1. **Estado Reposo (Apagado) 💤:** El botón de *Stop* permite el paso de corriente, pero el de *Start* está abierto, por lo que la bobina de salida (`OUT`) no recibe energía.
2. **Encendido (Presionando Start) ⚡:** Al presionar el botón de *Start*, la corriente fluye hacia la bobina (`OUT`). En ese instante, el contacto paralelo (`OUT`) se cierra.
3. **Enclavamiento (Soltando Start) ⛓️:** Al soltar el botón de *Start*, el circuito se abre en la parte superior, **pero** la corriente sigue pasando por la línea paralela que cerró el contacto `OUT`. El equipo se mantiene encendido.
4. **Apagado ⏹️:** Para detener el proceso, presionas el botón de *Stop*. Esto rompe el circuito principal, desenergiza la bobina (`OUT`), y al apagarse la bobina, el contacto de enclavamiento se abre nuevamente, dejando el sistema listo para un nuevo ciclo.

---

**Nota de Seguridad 🛡️:** Este diseño es vital en la industria porque, ante un corte de energía, el sistema no se reinicia solo cuando vuelve la luz (requiere que el operario presione *Start* de nuevo), garantizando la seguridad de los trabajadores.
