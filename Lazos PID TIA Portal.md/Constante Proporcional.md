# 📊 La Constante Proporcional - $K_p$ (PID-0107 - 0108)

Este módulo profundiza de forma práctica y experimental en la **Acción Proporcional ($K_p$)**, analizando cómo se comporta un lazo de control cuando aislamos este parámetro y cuáles son sus ventajas y limitaciones físicas en un proceso industrial. 🏭📐📈

---

### 🧮 Aislamiento Matemático del Control Proporcional (Modo P)

Para estudiar el efecto único de la ganancia proporcional, el controlador se configura para anular las acciones integral y derivativa. Matemáticamente en TIA Portal:

* Se anula la parte **Integral** haciendo que el tiempo integral ($T_i$) tienda a **Infinito** ($K_i \to \infty$), provocando que su división se vuelva cero.
* Se anula la parte **Derivativa** asignándole a la constante un valor de **Cero** ($K_d = 0$).

Al limpiar la ecuación general, obtenemos la fórmula del **Controlador P Puro**:

$$\text{Out}(t) = K_p \cdot e(t)$$

*(Donde la salida del controlador es directamente proporcional al error actual $e_{(t)} = SP - PV$).*

---

### 📈 El Efecto de la $K_p$ en la Variable de Proceso

El valor que le asignemos a la constante $K_p$ modifica drásticamente la agresividad con la que el PLC responderá ante un error:

* **⚡ Pendiente de Respuesta:** Un aumento en el valor de $K_p$ incrementa la "pendiente" o la velocidad con la que la Variable de Proceso (**PV**) sube para alcanzar el Set Point. A mayor $K_p$, el actuador (ej. una válvula o un variador) se abrirá con mucha más fuerza e inclinación inicial.
* **🔄 El Riesgo de Oscilación:** Si el valor de $K_p$ se incrementa demasiado (ganancia excesiva), el controlador se vuelve sobre-reactivo. La planta responderá de forma tan violenta que superará el Set Point (*overshoot*), luego intentará corregir frenando bruscamente, provocando que la variable empiece a **oscilar continuamente** sin poder estabilizarse, lo que puede dañar los componentes físicos del proceso.

---

### ❌ El Problema del Error Estacionario (Offset)

Una de las grandes revelaciones de este módulo es que **un controlador proporcional puro NUNCA puede alcanzar exactamente el valor de la consigna o Set Point**.

* **¿Por qué ocurre?** A medida que la Variable de Proceso (**PV**) se acerca al Set Point, el error ($e$) se vuelve cada vez más pequeño. Como la salida depende de multiplicar $K_p \cdot e$, si el error es casi cero, la salida del PLC hacia el actuador también se vuelve casi cero (la válvula se cierra o el motor se detiene).
* **El resultado:** El sistema encuentra un punto de equilibrio antes de llegar a la meta, generando un **error estacionario permanente** (también llamado *Offset*).

---

### 🛠️ ¿Cómo se corrige este error?

Para eliminar este desfase y lograr que la variable llegue exactamente al Set Point sin inducir oscilaciones salvajes, es obligatorio activar y aumentar los valores de las demás constantes del bloque `PID_Compact`:

1. **La Acción Integral ($K_i / T_i$):** Se encarga de ir sumando ese pequeño error estacionario a lo largo del tiempo hasta generar la fuerza necesaria para extinguir el error por completo.
2. **La Acción Derivativa ($K_d / T_d$):** Permitirá amortiguar el efecto de velocidad inducido por la $K_p$, reduciendo el sobreimpulso cuando las constantes trabajen en conjunto.

# 💻 Demostración Práctica (PID-0108)

Este módulo es una sesión 100% práctica dentro de TIA Portal. En ella se valida experimentalmente el comportamiento de un controlador Proporcional Puro (Modo P) utilizando herramientas de diagnóstico avanzadas del entorno de Siemens para observar la oscilación y el error estacionario. 📉🕹️⚙️

---

### 🛠️ Herramientas de TIA Portal Utilizadas en la Práctica

Para manipular el proceso y observar el comportamiento de la planta simulada sin un PLC físico, el instructor se apoya en dos herramientas clave de diagnóstico:

1. **📋 Tablas de Observación y Forzado Permanente (Watch and Force Tables):** 
   * Se utilizan para inyectar valores directamente en la memoria del PLC simulado. 
   * Desde aquí se modifica de manera manual y dinámica el **Set Point (Consigna)** y se fuerzan las variables de entorno para ver cómo reacciona el lazo cerrado frente a cambios bruscos del tipo "escalón".

2. **📈 Objeto Tecnológico PID_Compact (Ventana de Monitorización):**
   * Es la pantalla gráfica (*Trending*) donde se lanzan las curvas en tiempo real. 
   * Permite visualizar de forma simultánea tres curvas críticas en diferentes colores: la línea recta del **Set Point (SP)**, la curva de la **Variable de Proceso (PV)** y los movimientos de la **Salida del PID (Output)**.

---

### 🧪 Desarrollo del Experimento en el Video

El ejercicio práctico se divide en dos fases bien definidas, manteniendo siempre las constantes integral ($K_i$) y derivativa ($K_d$) desactivadas o en valores neutros (sin alterar el experimento):

#### 🏁 Fase 1: Simulación de un valor de $K_p$ exagerado (Inestabilidad)
* **Acción:** Se introduce un Set Point determinado y se configura en el asistente del `PID_Compact` una constante proporcional ($K_p$) extremadamente alta/exagerada.
* **Resultado en la gráfica:** Se observa cómo la curva de la Variable de Proceso (**PV**) sube con una pendiente vertical violentísima, superando por mucho el Set Point. Inmediatamente, la salida del PID intenta corregir de forma agresiva y el sistema entra en una **oscilación permanente y descontrolada** en forma de onda senoidal, demostrando que un exceso de ganancia vuelve al sistema completamente inestable.

#### 📉 Fase 2: Reducción de $K_p$ y visualización del Error Estacionario (*Offset*)
* **Acción:** Mientras el sistema oscila, el instructor reduce progresivamente el valor de la $K_p$ a niveles moderados para calmar el lazo.
* **Resultado en la gráfica:** La oscilación salvaje desaparece y la curva del proceso se estabiliza en una línea horizontal pacífica. Sin embargo, en la gráfica se evidencia perfectamente el **error estacionario**: la línea de la **PV** se queda "congelada" unos centímetros por debajo de la línea del **Set Point**, demostrando de forma empírica que el control P puro es incapaz de extinguir la diferencia final por sí solo.

---

### 📝 Nota de Laboratorio

💡 Esta práctica demuestra por qué la ventana de monitorización del `PID_Compact` es la herramienta favorita de los programadores. Te permite diagnosticar la salud de tu lazo de control de un solo vistazo: si ves ondas repetitivas (Fase 1), sabes que tu $K_p$ está demasiado alta; si ves una línea estable pero que no llega a la meta (Fase 2), sabes que te urge activar la constante integral. 🚀
