# 📋 Análisis de TIA Portal

### 1. Estructura de Datos Global `Lazo TIA Portal`

* **Transcripción:** Muestra un Bloque de Datos Global (DB6) llamado `"Proceso"`. Contiene variables de tipo estático (`Static`) como: `Consigna` (Real), `Temperatura` (Real), `Actuador` (Real), `Consigna Manual` (Real), `Reset PID` (Bool), `Reset MP` (Bool), `EN_Man PID` (Bool) y `calcParams` (Bool).
* **Análisis:** Este DB actúa como la "interfaz de memoria" compartida del proyecto. Centraliza los datos para que las pantallas HMI, las tablas de observación o los diferentes bloques del programa lean y escriban en un solo punto ordenado.

### 2. Instanciación del Controlador (`Lazo TIA Portal1.jpg`)

* **Transcripción:** Dentro del bloque de interrupción cíclica `Cyclic interrupt [OB30]`, en el Segmento 1, se ha instanciado el bloque tecnológico **`PID_Compact`** (asociado al DB de instancia `%DB4 "PID_Compact_4"`).
* Conexiones visibles: `"Proceso".Consigna` mapeado a `Setpoint`, `"Proceso".Temperatura` a `Input`, `"Proceso".EN_Man PID` a `ManualEnable`, `"Proceso".Consigna Manual` a `ManualValue` y `"Proceso".Reset PID` a `Reset`. La pata `Output` escribe directamente sobre `"Proceso".Actuador`.


* **Análisis:** Aquí se observa la configuración en modo automático/manual controlada por software. La salida calculada (`Output`) no va a una tarjeta física real, sino que se almacena en la variable `"Proceso".Actuador` para alimentar el simulador.

### 3. El Modelo de Planta Simulada (`Lazo TIA Portal2.jpg`)

* **Transcripción:** En el Segmento 2 del mismo `OB30`, se encuentra el bloque de simulación de primer orden **`*LSim_PT1`** (asociado al `%DB5 "LSim_PT1_DB"`).
* Conexiones visibles: `"Proceso".calcParams` conectado a `calcParam`, `"Proceso".Actuador` conectado a la entrada `input`, constante `2.5` en el tiempo de rezago `tmLag1`, constante `3.5` en la ganancia `gain`, constante `0.1` (100 ms) en el tiempo de ciclo `cycle`. Límites de salida en `350.0` (`maxOut`) y `0.0` (`minOut`). El resultado se asigna a `"Proceso".Temperatura` mediante el pin `output`.


* **Análisis:** **Este es el cierre del lazo cerrado virtual.** La salida del PID alimenta la entrada de la planta (`LSim_PT1`), y la salida de la planta (`output`) realimenta inmediatamente la pata `Input` del PID en el segmento anterior a través de la variable `Temperatura`. El ciclo se repite con precisión matemática exacta cada 100 ms (`cycle := 0.1`).

### 4. Menú de Parámetros Avanzados (`Lazo TIA Portal3.jpg`)

* **Transcripción:** Muestra la pestaña de configuración interna del objeto tecnológico `PID_Compact_4`. En la sección de *Ajustes avanzados > Parámetros PID*, se observa: Ganancia proporcional = `1.0`, Tiempo de integración = `20.0 s`, Tiempo derivativo = `0.0 s` (desactivado), Coeficiente retardo derivativo = `0.2`, y Tiempo de muestreo del algoritmo PID = `1.0 s`.
* **Análisis:** Ventana de sintonización manual. Al tener el tiempo derivativo en `0.0 s`, el sistema está operando estrictamente como un controlador **PI**. El tiempo de muestreo del algoritmo se ha fijado en 1 segundo.

### 5. Monitorización y Optimización en Tiempo Real (`Lazo TIA Portal4.jpg`)

* **Transcripción:** Panel de diagnóstico dividido. A la izquierda, el bloque PID corriendo; a la derecha, la ventana de medición y optimización. La gráfica muestra el comportamiento dinámico con límites del eje Y de 0 a 350 °C. En la parte inferior, se lee el estado actual del regulador: *"Activado - Modo automático"*, con un Setpoint de `120.0`, un Input de `138.198` y un Output de `39.23%`.
* **Análisis:** En la gráfica se aprecia un cambio escalón en el Setpoint (línea marrón/roja) y cómo la Variable de Proceso (línea verde) responde con un comportamiento PT1 amortiguado. Hacia el final de la gráfica, se observa una perturbación brusca seguida de oscilaciones que el PID intenta corregir de forma automática variando su porcentaje de salida (línea naranja/roja de escalones).

---

# 🎛️ Resumen: Integración en TIA Portal (PID-0113)

Este módulo práctico consolida toda la teoría del curso, enseñando cómo integrar el objeto tecnológico `PID_Compact` con las plantillas maestras de simulación de procesos de Siemens (`LSim`) dentro de un bloque de organización cíclico, permitiendo probar, diagnosticar y sintonizar un lazo cerrado completo mediante software. 🏭💻📈

---

### 🏛️ La Arquitectura del Lazo Cerrado Virtual

Para construir un entorno de pruebas idéntico a un proceso industrial real sin disponer de componentes físicos, el instructor plantea una estructura dividida en tres capas dentro de TIA Portal:

```
[ DB6 "Proceso" ] <---> [ OB30: PID_Compact ] ---> (Actuador) ---> [ OB30: LSim_PT1 ] ---> (Temperatura) ---> [ Vuelve al PID ]

```

1. **💾 Bloque de Datos Centralizado (DB6):** Almacena las variables globales del lazo. Esto evita el uso de marcas físicas de memoria (`M`) y permite mapear de forma limpia las entradas y salidas de los bloques simulados.
2. **🔄 Bloque de Organización de Interrupción Cíclica (OB30):** Aloja tanto al controlador como a la planta. Garantiza que los cálculos de ambos bloques se ejecuten en intervalos de tiempo fijos y estrictos (en este caso, parametrizado a **100 ms**), asegurando la precisión de las ecuaciones diferenciales e integrales.

---

### 🔌 Conexión Cruzada de Bloques (Paso a Paso Técnico)

El secreto de la simulación radica en cómo se entrelazan las "patas" o pines del `PID_Compact` con las del bloque de planta `LSim_PT1`:

* **Acción de Control:** La pata `Output` del PID calcula el porcentaje de energía necesario (0-100%) y lo guarda en la variable `"Proceso".Actuador`. Esta variable se conecta directamente en la pata `input` de la planta `LSim_PT1`.
* **Respuesta de la Planta:** El bloque `LSim_PT1` procesa esa señal aplicando la ganancia estática asignada ($K = 3.5$) y la constante de tiempo ($\tau = 2.5\text{ s}$). El resultado simulado sale por su pin `output` hacia la variable `"Proceso".Temperatura`.
* **Realimentación (Feedback):** La variable `"Proceso".Temperatura` se inyecta de vuelta en la pata `Input` del bloque `PID_Compact`, completando el lazo cerrado de control.

---

### 📈 Diagnóstico y Puesta en Servicio (*Commissioning*)

Una vez que el programa está corriendo en el PLC virtual (PLC-SIM), el asistente de monitorización del `PID_Compact` se convierte en la estación de control del ingeniero:

* **📊 Vista de Parámetros:** Permite al operador cambiar en caliente las ganancias ($K_p$, $T_i$, $T_d$) para evaluar inmediatamente cómo cambia la estabilidad del sistema.
* **📉 Curvas de Tendencia (*Trending*):** Grafica en tiempo real la interacción entre los cambios de consigna impuestos por el usuario y la reacción de la planta. Permite evaluar visualmente el comportamiento frente a perturbaciones externas (como caídas repentinas de temperatura) y verificar la velocidad con la que el algoritmo PI devuelve el proceso hacia el Setpoint establecido.

---

💡 **Conclusión de las notas:** Este método de integración es el estándar profesional para validar estrategias de control antes de cargarlas en un PLC real en planta. Permite equivocar los parámetros de sintonización y generar inestabilidades o saturaciones en un entorno seguro y controlado por software. Puedes guardar este resumen final directamente en tus apuntes `.md`.
