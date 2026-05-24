
# 🎛️ El Lazo PID – Configuración (PID-0106)

Este módulo aborda la base matemática del algoritmo PID y su implementación práctica en TIA Portal utilizando el objeto tecnológico **PID_Compact**. Se demuestra cómo simular y configurar un lazo cerrado completo sin necesidad de hardware real mediante el uso de la serie S7-1500 y PLC-SIM. 🏭💻📐

---

### 🧮 La Ecuación Matemática del PID

El controlador calcula de forma continua el error instantáneo $e(t) = SP - PV(t)$ para calcular la acción de control ($Out(t)$) sumando el efecto de tres componentes esenciales:


$$\text{Out}_(t) = K_p (\frac{e_(t) + \int_{0}^{t} e(\T) d\T}{K_i} \ + K_d \frac{de_(t)}{dt}$$)


*(Nota: En algunas variantes, las constantes integrales y derivativas se expresan en función del tiempo de integración.

1. **📊 Acción Proporcional ($K_p$):** Multiplica el error actual por una ganancia. Si el error es grande, la respuesta es grande. Su función principal es aportar la fuerza inicial para acercar la variable al objetivo, aunque por sí sola suele dejar un error en estado estacionario (offset).
2. **⏳ Acción Integral ($K_i / T_i$):** Examina el historial del error acumulado en el tiempo (la integral). Su propósito crítico en la industria es eliminar por completo el error en estado estacionario, forzando al sistema a llegar exactamente al Set Point.
3. **🔮 Acción Derivativa ($K_d / T_d$):** Analiza la velocidad con la que cambia el error (la derivada). Actúa como un "freno predictivo" que anticipa el comportamiento futuro del sistema para reducir las oscilaciones y amortiguar el *overshoot*.

---

### 🔌 Interfaz del Bloque `PID_Compact` (Patas del Bloque)

El bloque `PID_Compact` se añade obligatoriamente en un bloque de interrupción cíclica (como el OB30) para asegurar un tiempo de muestreo constante. Sus conexiones principales son:

#### 📥 Entradas (Inputs)

* **`Setpoint`:** El valor de consigna al que se desea llevar el proceso (ej. 50.0 °C).
* **`Input`:** La Variable de Proceso (**PV**) en formato de ingeniería o coma flotante (`Real`), proveniente habitualmente de un bloque de simulación de planta o un sensor ya escalado (ej. 23.5 °C).
* **`Input_PER`:** La entrada analógica analógica directa del hardware (`Int`), es decir, el valor bruto que lee la tarjeta (de 0 a 27648). Si se usa esta pata, el bloque escala automáticamente internamente.
* **`ManualEnable`:** Entrada booleana. Al activarse (`ON`), pasa el controlador a **Modo Manual**, permitiendo al operador fijar la salida directamente.
* **`ManualValue`:** El valor de salida que adoptará el PID si el `ManualEnable` está activo.
* **`Reset`:** Reinicia el controlador, poniendo a cero la parte integral acumulada y limpiando errores del bloque.

#### 📤 Salidas (Outputs)

* **`Output`:** La salida de control calculada en formato flotante (`Real`), típicamente escalada de 0.0 a 100.0%. Es la que se conecta al modelo de la planta o actuador.
* **`Output_PER`:** La salida analógica en formato bruto (`Int`, de 0 a 27648) para comandar directamente una tarjeta analógica física hacia una válvula o variador.
* **`State`:** Entero que indica el modo de operación actual del PID (0=Inactivo, 1=Optimización inicial, 2=Optimización fina, 3=Modo automático, 4=Modo manual).
* **`Error`:** Código hexadecimal o ID de error que indica si el bloque ha fallado (por ejemplo, por una división por cero o una variable fuera de límites).

#### 🔄 Modo Automático (ManualEnable = OFF)

Cuando la pata `ManualEnable` se encuentra apagada o en `False`, el bloque opera bajo el **Modo Automático**. En este estado, el algoritmo PID toma el control absoluto de la salida, calculando de forma autónoma la señal necesaria para corregir el error del proceso.

---

### ⚙️ Ventana de Configuración del Objeto Tecnológico

Al hacer clic en el icono de configuración (la caja de herramientas) del `PID_Compact`, TIA Portal abre un asistente con las siguientes pestañas críticas de parametrización:

* **📈 Configuración de Entradas y Salidas:** Permite definir si se va a trabajar con `Input` o `Input_PER`, y si la salida será continua (`Output`), analógica (`Output_PER`) o por pulsos PWM (`Output_PWM`).
* **📐 Escala de Valor Real:** Configura los límites físicos de la variable de proceso en ingeniería (ej. mínimo 0.0°C - máximo 150.0°C) para asociarlos correctamente a los 27648 puntos de la entrada analógica.
* **🛑 Límites del Valor Real y de Salida:** Establece umbrales de seguridad. Por ejemplo, evitar que la salida del PID caiga por debajo de 0% o suba más de 100%, o disparar alarmas si la PV supera un valor peligroso.
* **🖥️ Monitorización:** Permite visualizar en tiempo real mediante gráficas (*Trending*) la respuesta del Set Point, la Variable de Proceso y la Salida del PID de manera simultánea para analizar la estabilidad del lazo.

