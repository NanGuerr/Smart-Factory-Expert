# ⚙️ Programación y Secuencia de Control de Turbina

Este documento detalla la lógica de control implementada para la automatización de la turbina.

## 🎛️ 1. Escalado de Entradas Analógicas
* Comenzaremos a darle forma a nuestro programa.
* Antes de comenzar la secuencia, lo primero que tendremos que hacer es escalar nuestras entradas analógicas para poder recibir un valor que podamos interpretar.
* Para ello, en el primer segmento del OB1, pondremos el escalado de entradas analógicas.
* Simplemente insertaremos nuestro escalado que ya hemos hecho antes, y como primer sensor tendremos el sensor de presión.
* El máximo del sensor según su hoja de datos era 6, y el mínimo es 0.
* El máximo del canal analógico es 27648 y el mínimo del canal es 0.
* El valor escalado dijimos que lo guardaríamos en el DB sistema, lecturas, presión.
* Para el resto de los sensores, tendremos que hacer lo mismo.

## ⚙️ 2. Escalado de Salidas Analógicas y Consignas
* Luego, lo que tendremos que hacer es llamar a nuestra secuencia, y después de ella, tendremos que hacer el escalado de las salidas analógicas.
* Aquí tenemos dos; lo que tenemos que hacer es crear primero la consigna.
* Para ello iremos a DB sistema y crearemos una nueva estructura que sea consigna.
* Si recordamos, tenemos la consigna manual de la válvula y la consigna automática de velocidad, ambos son valores reales.
* En el caso de la válvula, la consigna manual va de 0 a 100%, y la consigna de velocidad automática podía ir de 0 a 6000 RPM.
* Sabiendo esto, agregaremos ambos escaladores.
* Pondremos en comando de entrada las consignas creadas recién en el DB sistema: la consigna manual de válvula (máximo 100%, mínimo 0) con salida directa a la salida analógica.
* En el otro caso, la consigna automática de velocidad puede ir de 0 a 6000, y la salida irá al setpoint de velocidad a nuestra salida analógica real.
* Con estos dos valores, controlaremos nuestra secuencia.

## 🚀 3. Lógica de la Secuencia de Arranque (Paso 1)
* Ahora sí podemos acceder a nuestro bloque secuencia y comenzar a programarlo propiamente dicho.
* Para comenzar la secuencia, tenemos tres condiciones que cumplir.
* La primera es que se presione el botón de arranque, ya sea desde el panel HMI o desde el tablero local.
* En este caso elegiremos la señal que proviene del tablero local y luego veremos cómo elegir entre las dos.
* La segunda condición es que la velocidad esté cercana a 0, por lo que consultaremos utilizando un comparador menor, habilitando la rama si nuestra lectura de velocidad es menor a 0.5.
* A esa velocidad es relativamente seguro que la junta y el motor se acoplen.
* Luego, deberemos consultar si la válvula principal está abierta o cerrada.
* Buscaremos la señal de válvula principal y, en los comentarios, veremos que en 1 la válvula principal de gas está abierta; por lo tanto, un contacto NA está bien.
* Cuando la válvula principal se abre, el contacto se pone en 1 y permite el paso de la corriente.
* Cuando se dan las tres condiciones en simultáneo, habilitaremos el paso 1 poniéndolo en SET (DB sistema, paso 1).
* Esto nos indicará que el arranque ha comenzado y podremos empezar a realizar las acciones.

## 🔗 4. Acople del Motor y Autosustentación (Paso 2)
* Una vez que el paso 1 está cumplido, debemos bloquearlo; por más que se presione el botón de arranque, no se volverá a habilitar hasta que el arranque actual esté completamente terminado.
* Por un tema lógico, lo que haremos será acoplar la junta primero y luego, después de un tiempo, acoplar el motor para darle tiempo a la junta a que se acople bien al eje.
* Para ello podemos agregar un temporizador TON en este ramal llamado delay acople y le daremos de tiempo 1 segundo.
* Una vez que se han accionado la junta y el motor, tendremos que esperar a que la velocidad aumente hasta 478 RPM, que es la velocidad de autosustentación.
* Abriremos una nueva rama y consultaremos si nuestra lectura de velocidad es mayor a 478 RPM.
* De ser así, vamos a dar por cumplido este paso y habilitaremos el paso siguiente (DB sistema, paso 2).
* Una vez que este paso se cumple, nuevamente tendremos que bloquear este ramal para que no vuelva a ejecutarse.

## 🔥 5. Encendido de Chisperos y Apertura de Válvula (Paso 3)
* Una vez que se supera la velocidad de autosustentación, lo que tendremos que hacer es habilitar ambos chisperos.
* Dos segundos después de eso, tendremos que abrir la válvula en un porcentaje fijo del 10%.
* Agregaremos un TON (delay chisperos) de 2 segundos.
* Luego de esos 2 segundos, debemos poner nuestro comando manual/automático en 0 usando la función MOVE y escribiremos un valor de 10 en nuestro comando de apertura manual.
* Para poder dar este paso por cumplido, tienen que estar activos ambos sensores de llama.
* Una vez que esos sensores se ponen en 1, damos por cumplido este paso 3 y evitamos que se ejecute nuevamente.

## 📈 6. Aceleración y Desacople del Motor (Paso 4 y 5)
* A partir de que el paso 3 se cumple, lo que tendremos que hacer es abrir la válvula al 25% haciendo una transferencia de 25 a nuestra consigna de válvula.
* Una vez hecho eso, la condición de transición es que la velocidad supere las 2750 RPM.
* Pondremos un comparador de mayor y consultaremos si nuestra lectura de velocidad es mayor a 2750 RPM.
* En caso de que sea cierto, daremos por cumplido este paso y habilitaremos el siguiente.
* Una vez superada la velocidad de 2750, lo primero que tendremos que hacer es quitar el acople del motor y luego de 5 segundos apagarlo.
* Pondremos una bobina de RESET para el acople y un temporizador; luego de 5 segundos, apagaremos el motor con su comando en 0.
* Una vez que el motor está apagado, daremos por cumplido el paso 5.

## 🤖 7. Modo Automático y Revisiones Finales (Paso 6)
* Habilitaremos el modo automático seteando nuestro comando de modo manual/automático a 1.
* Tendremos que mover un valor de 4600 a la consigna automática de velocidad y por seguridad, mover un 0 a nuestra consigna manual de válvula.
* Al momento de que nuestro sistema alcance nuestra velocidad nominal de 4600 RPM, daremos por cumplido este paso 6.
* Una vez completada la secuencia, haremos una pequeña revisión para comprobar que todos los pasos estén correctamente dispuestos y que no haya problemas en la ejecución.
* Una cosa que tendremos que agregar es en algún momento apagar los chisperos, lo cual podemos hacer luego de que se hayan detectado los dos sensores en el paso 3, reseteando ambos chisperos.
* En la siguiente sección, veremos cómo se hace la parada de emergencia, la parada controlada y las condiciones de seguridad que nos permitirán arrancar la máquina.
