# La constante integral

$$\text{Out}_{(t)} = K_p \left( e_{(t)} + \frac{\int_{0}^{t} e_{(T)} \, dT}{K_i} + K_d \frac{de_{(t)}}{dt} \right)$$
 
Para comprobar qué es lo que hace la constante integral, evaluemos en primer lugar *qué es lo que representa*, físicamente, este término.
 $$\int_{0}^{t} e_{(T)} \, dT$$
 
La **integral del error** representa simplemente **el área bajo la curva del error**. En otras palabras, el área que hay de un segmento entre la **consigna** y el **valor de proceso**.
Si el área es muy grande, ese valor sumará una corrección adicional a la ya existente por la componente proporcional, haciendo que el actuador se mueva un poco más.
**La constante integral**
$$\text{Out}_{(t)} = K_p \left( e_{(t)} + \frac{\int_{0}^{t} e_{(T)} \, dT}{K_i} \right)$$


A medida que el área bajo la curva se va haciendo más pequeña, también lo hace el valor de la acción integral.
**Aspectos a tener en consideración:**
* Cuanto más grande sea el valor de la constante integral ($K_i$), **menor será el valor de la acción integral**. Esto significa que tendrá menos influencia en nuestro sistema de control.
* Valores muy grandes de acción integral, harán que el sistema entre en oscilación.
* **No usar acción integral** (o reducirla al mínimo) para sistemas que son **demasiado lentos**.

---

# La Constante Integral – $K_i$ (PID-0106 / PID-0109)

Este módulo se enfoca en comprender la naturaleza física y matemática de la **Acción Integral**, el componente clave del algoritmo PID encargado de eliminar por completo el error estacionario (*offset*) que la acción proporcional pura no puede corregir. 🏭📐📊

---

### 🧮 Significado Físico: El Área Bajo la Curva del Error

La ecuación del bloque PID (representada en su forma interactiva o de ganancia global en la imagen) establece que el término de la integral es:

$$\int_{0}^{t} e_{(T)} \, dT$$

* **📉 ¿Qué representa gráficamente?:** Físicamente, representa el **área acumulada** que se forma en el espacio comprendido entre la línea del **Setpoint (Consigna)** y la curva del **Valor de Proceso (PV)** a lo largo del tiempo.
* **⚡ Dinámica del área (Corrección Dinámica):**
* **Fase Inicial (Bloque 1 en la gráfica):** Cuando el sistema arranca o cambia el Setpoint, la distancia entre el SP y la PV es notable, generando un área verde rayada muy grande. Esta acumulación masiva le inyecta una *fuerza o corrección adicional* al actuador, obligándolo a abrirse o acelerar más allá de lo que haría la acción proporcional sola.
* **Fase Final (Bloque 2 en la gráfica):** Conforme la PV se acerca a la consigna, el error residual es mínimo y el área que se va sumando es minúscula. Sin embargo, la parte integral **"recuerda"** todo el historial de error pasado y mantiene la salida del actuador abierta en el punto exacto para extinguir el error por completo.

---

### ⚠️ Reglas Críticas de Sintonización (Aspectos a considerar)

El instructor destaca tres reglas de oro que todo programador de TIA Portal debe memorizar al configurar el objeto tecnológico `PID_Compact`:

1. **🔀 Relación Inversa del Parámetro ($K_i$):** Debido a que el parámetro $K_i$ (o el tiempo integral $T_i$) se encuentra en el **denominador** de la ecuación, la relación es inversa: **A mayor valor asignado a la constante $K_i$, menor será el impacto real de la acción integral** en el sistema. Si quieres que la acción integral actúe de manera más agresiva y rápida, debes *reducir* el valor numérico de la constante en el bloque.
2. **🔄 Peligro de Oscilación:**
Si se le permite a la acción integral tener demasiada influencia (asignándole un valor numérico muy pequeño al parámetro $K_i$), el controlador acumulará energía demasiado rápido. Esto causará que la variable de proceso sobrepase bruscamente la consigna (*overshoot*) y el sistema entre en una **fase de oscilación continua**, volviendo inestable la planta.
3. **🛑 Restricción en Sistemas Lentos:**
**No se debe usar la acción integral** (o se debe configurar para que su influencia sea mínima) en procesos que físicamente tengan respuestas extremadamente lentas. En estos sistemas, el error tardará mucho en corregirse de forma natural, lo que provocará que la integral acumule un valor gigantesco en el tiempo (efecto conocido como *Reset Windup* o saturación integral), haciendo que el actuador se sature al 100% y el sistema se vuelva incontrolable al intentar regresar.

---

💡 **Conclusión de las notas:** La acción integral es la medicina que cura el error en estado estacionario de la acción proporcional, pero debe administrarse con cuidado. Su fuerza depende del área bajo la curva del error y su sintonización requiere entender que en la fórmula de Siemens actúa de manera inversamente proporcional. 
