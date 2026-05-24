# 📝 La constante derivativa

$$\text{Out}_{(t)} = K_p \left( e_{(t)} + \frac{\int_{0}^{t} e(T) \ dT}{K_i} + K_d \frac{de_{(t)}}{dt} \right)$$

Para comprobar qué es lo que hace la constante derivativa, evaluemos primero *qué es lo que representa*, físicamente, este término.
$$\frac{de_{(t)}}{dt}$$

La **derivada del error** representa simplemente una **proyección** de cómo será el error a futuro. En otras palabras, una recta tangente a un punto determinado en la curva del error.

Si el sistema comprueba que **a futuro**, si el error no se corrige lo suficientemente rápido, hará un ajuste en la salida.
A su vez, si la **consigna** cambia de golpe, le dará un **impulso inicial a la salida** para corregir lo más rápido posible.
Si en cambio, se detecta que el error está disminuyendo **demasiado rápido**, y la inercia del sistema hará que se "pase de largo", la componente derivativa es capaz de corregir **de antemano** la salida para evitar ésta situación.
Esto, permite usar valores más altos de componentes integral y proporcional, haciendo que el sistema se estabilice en un muy corto tiempo.

**Aspectos a tener en consideración:**
* Cuanto más grande sea el valor de la constante derivativa ($K_d$), **mayor será el valor de la acción derivativa**.
* La componente derivativa es **muy sensible**. Si uno se excede en la cantidad de acción derivativa, hará que el sistema entre en oscilación.
* **No usar acción iniciativa** *(Fe de errata de la lámina: se refiere a acción derivativa)* (o reducirla al mínimo) para sistemas que son **demasiado cambiantes**, o con sensores que tengan demasiado ruido en la medición.

---

# 🔮 Análisis Técnico: La Constante Derivativa – $K_d$ (PID-0111)

Este módulo aborda la última componente del lazo PID: la **Acción Derivativa ($K_d$)**. A diferencia de la Proporcional (que mira el presente) y la Integral (que mira el pasado), la acción derivativa tiene un carácter **predictivo**, reaccionando a la velocidad con la que cambia el error.

---

### 🧮 1. Significado Matemático y Físico: La Velocidad del Error

El término derivativo en la ecuación se expresa como:

$$\frac{de_{(t)}}{dt}$$

* **📉 ¿Qué representa gráficamente?:** Representa la **pendiente de la recta tangente** a la curva del error en un instante específico. En física, la derivada de una posición es la velocidad; en control, la derivada del error es la **velocidad con la que el error se está agrandando o achicando**.
* **👁️ Proyección a futuro:** Al calcular la pendiente, el algoritmo traza una proyección matemática. No sabe con certeza el futuro, pero asume que si la curva mantiene esa velocidad, el error se comportará de una manera determinada en los próximos milisegundos y actúa basándose en esa predicción.

---

### 🏎️ 2. Análisis Dinámico: ¿Cómo altera el comportamiento del PLC?

La acción derivativa ejerce dos efectos opuestos y sumamente útiles dependiendo de la situación del proceso (representado en la gráfica por la línea azul clara de control PID completo frente a la línea discontinua morada de control P puro):

* **🚀 El Impulso Inicial (Acelerador):** Cuando el Setpoint (línea roja) cambia drásticamente del tipo escalón, el error se dispara de forma instantánea. Como la velocidad de cambio del error es infinita en ese microsegundo, la derivada genera un **pico o pulso masivo de salida** hacia el actuador. Esto hace que el sistema reaccione con una velocidad extrema, logrando que la Variable de Proceso (PV) suba casi de forma vertical (línea azul).
* **🛑 El Freno Predictivo (Amortiguador):** Conforme la PV se acerca rápidamente al Setpoint, el error se está reduciendo a gran velocidad. La acción derivativa detecta que el error disminuye "demasiado rápido" y calcula que, por culpa de la inercia física de la planta, el valor **se pasará de largo (overshoot)**. Para evitarlo, la componente derivativa actúa al revés: **resta energía a la salida, frenando el proceso de antemano**.

**💡 Beneficio Global:** Al tener un "freno de mano" tan eficiente, el programador puede permitirse configurar una $K_p$ más agresiva y una $K_i$ más rápida. El resultado final es un sistema que alcanza la meta en un tiempo récord y se estabiliza de inmediato sin oscilaciones.

---

### ⚠️ 3. Reglas Críticas de Configuración en TIA Portal

* **🔄 Relación Directa (A diferencia de la Integral):** Aquí la constante $K_d$ está multiplicando directamente en el numerador. Por lo tanto, **a mayor valor numérico asignado a la $K_d$, mayor será el impacto** de la acción derivativa en la salida.
* **⚡ El Peligro del Ruido Eléctrico (Sistemas con Filtros):** La derivada odia el ruido. Si un sensor de temperatura o presión tiene fluctuaciones rápidas debido a interferencias eléctricas (pequeños picos y valles), la derivada interpretará esas variaciones milimétricas como "errores cambiando a velocidad extrema". Esto provocará que la salida del PID empiece a dar golpes violentos e impredecibles, haciendo colapsar al sistema o destruyendo mecánicamente el actuador (válvulas o motores).
* **❌ ¿Cuándo NO usarla?:** No se debe activar en sistemas con lecturas inestables o demasiado cambiantes, a menos que se aplique primero un filtro paso bajo digital a la entrada del `Input` para suavizar la señal analógica.

¡Excelente descripción del comportamiento práctico! Has tocado un punto clave del laboratorio: esas oscilaciones "cuadradas" o bruscas que suben y bajan como flancos digitales ocurren cuando un sistema tiene una combinación inestable (típicamente por una acción integral que satura o una proporcional muy agresiva). Al meter la componente derivativa, su naturaleza matemática actúa sobre la velocidad de cambio, "planchando" la gráfica y estabilizando esas transiciones abruptas.

Como no tengo acceso directo para iniciar sesión en tu cuenta de IngeLearn y reproducir el video, he estructurado toda tu descripción técnica en un resumen de laboratorio impecable en formato Markdown (`.md`) con emojis, listo para tus apuntes de TIA Portal:

---

# 💻 Resumen: Constante Derivativa – Demostración Práctica (PID-0112)

Este módulo práctico en TIA Portal demuestra en tiempo real cómo la **Acción Derivativa ($K_d$)** altera drásticamente la dinámica de la señal de salida, actuando directamente sobre la velocidad del error para mitigar el sobreimpulso (*overshoot*) y amortiguar oscilaciones críticas. 📉🕹️⚡

---

### 🧪 Desarrollo del Experimento en el Video

La práctica expone el contraste inmediato en la gráfica de monitorización del objeto tecnológico `PID_Compact` antes y después de activar el parámetro derivativo:

#### ⏹️ Paso 1: El Estado Inicial sin Derivativa (Oscilación en "Flancos")

* **El Problema:** Antes de aplicar la constante derivativa, el lazo de control (operando solo en modo PI) se encuentra en un punto crítico de inestabilidad debido a parámetros exagerados.
* **Comportamiento en la Gráfica:** La Variable de Proceso (**PV**) no dibuja una curva suave; en su lugar, se muestra en **oscilaciones abruptas con formas que parecen cuadros**, subiendo y bajando violentamente como si fueran los flancos de subida y bajada de una señal digital. Esto sucede porque el actuador pasa de estar totalmente abierto a totalmente cerrado de golpe, sin amortiguación. El *overshoot* (sobreimpulso) es masivo en cada ciclo.

#### 🔮 Paso 2: Introducción de la Constante Derivativa ($K_d$)

* **La Acción:** El instructor activa y empieza a modificar el valor de la constante derivativa ($K_d$) en el asistente de configuración.
* **El Efecto Matemático:** Al ser la derivada del error en el tiempo ($\frac{de}{dt}$), el bloque detecta la velocidad extrema con la que la variable sube y baja en esos flancos digitales.
* **Resultado en la Gráfica:** De forma inmediata, la componente derivativa empieza a restar o sumar amplitudes a la salida según sea necesario:
* **Al aumentar los valores de $K_d$:** La acción derivativa inyecta un efecto de "freno predictivo" que **disminuye drásticamente las amplitudes de las ondas y reduce el *overshoot***. Esas transiciones cuadradas y bruscas se suavizan, transformándose en una curva amortiguada que se estabiliza rápidamente sobre el Setpoint.
* **Al restar o bajar demasiado los valores de $K_d$:** El sistema pierde su amortiguación y los flancos bruscos u oscilaciones tienden a regresar.

---

### 📌 Conclusiones Críticas del Laboratorio

> 💡 **La regla de oro de la $K_d$ en TIA Portal:** La acción derivativa estabiliza lo que la proporcional e integral descontrolan. Si tu gráfica muestra picos violentos o cambios en forma de flancos debido a la inercia del sistema, la $K_d$ es la encargada de leer esa velocidad de cambio para anticiparse al desastre, recortar el sobreimpulso y clavar la variable de proceso exactamente en la consigna.

```text
Efecto visual del ajuste de Kd:
   - Kd = 0 (Inestable)  -->  Oscilaciones cuadradas (Flancos digitales / Overshoot alto).
   - Kd Óptima           -->  Curva suavizada, amortiguación rápida y estabilidad en el SP.
   - Kd Excesiva         -->  Reintroducción de oscilaciones rápidas por ruido matemático.

```
