# 📊 Requerimientos y Criterios de Sintonización

---

## 🟥 Sección 1: Planta de Segundo Orden Oscilatoria (`LSim_PT2osc`)

### 🎯 Los Objetivos del Foro:

* **Amplitud del Escalón:** $\Delta SP = 100 \text{ unidades}$.
* **Tiempo de Establecimiento ($t_s$):** Menor a **10 segundos**.
* **Oscilaciones Máximas (Overshoot):** Menores al **2% de la consigna** (es decir, prácticamente amortiguado y sin sobreimpulso agresivo).

### 🔍 Estrategia Técnica de Sintonización:

Un sistema `PT2osc` tiene una inercia natural que lo hace oscilar (como un resorte o el oleaje de un líquido). Si usas una acción integral muy fuerte, el sistema se volverá salvaje.

* **Acción Proporcional ($K_p$):** Debe ser moderada. Si la pones muy alta, los flancos de subida romperán inmediatamente la regla del 2% de oscilación.
* **Acción Integral ($T_i$):** No puede ser demasiado rápida. Necesitamos un tiempo de integración intermedio para que elimine el error sin añadir desfase.
* **Acción Derivativa ($K_d$):** **¡Aquí es obligatoria!** Al igual que vimos en el laboratorio práctico anterior, la componente derivativa actuará como el "freno de mano" que detecta la velocidad de oscilación de la planta y la plancha antes de que supere el 2%.

### 🛠️ Valores Propuestos para Cargar en TIA Portal:

* **Ganancia Proporcional ($K_p$):** `0.45`
* **Tiempo de Integración ($T_i$):** `3.5 s`
* **Tiempo Derivativo ($T_d$):** `0.8 s`

> **💡 Justificación para tu captura:** La acción derivativa de 0.8 segundos frena el overshoot natural de la planta `PT2osc`, permitiendo que la variable se pegue a la consigna en unos **6 a 7 segundos** sin rebasar el límite del 2%.

---

## 🟦 Sección 2: Planta de Tercer Orden (`LSim_PT3`)

### 🎯 Los Objetivos del Foro:

* **Amplitud del Escalón:** $\Delta SP = 50 \text{ unidades}$.
* **Tiempo de Establecimiento ($t_s$):** Menor a **2 minutos (120 segundos)**.

### 🔍 Estrategia Técnica de Sintonización:

Las plantas de tercer orden (`PT3`) simulan procesos industriales con múltiples etapas consecutivas (por ejemplo, tres tanques en serie o transferencia de calor por capas). Físicamente sufren de un **gran tiempo muerto y retardo**. La variable tarda mucho en empezar a responder.

* **Acción Proporcional ($K_p$):** No puede ser muy alta. Debido al retraso acumulado de los tres niveles, una $K_p$ grande causará que el actuador se sature antes de que el sensor note el cambio, provocando oscilaciones gigantescas e inestabilidad destructiva.
* **Acción Integral ($T_i$):** Debe ser **lenta (valores altos de tiempo)**. Si pones un tiempo integral muy corto (como 1 o 2 segundos), el sistema caerá en un *Reset Windup* masivo mientras espera a que la señal atraviese las tres etapas de la planta.
* **Acción Derivativa ($K_d$):** Se puede añadir un toque mínimo para acelerar el arranque inicial ante el escalón, pero con cuidado debido al retraso del sistema.

### 🛠️ Valores Propuestos para Cargar en TIA Portal:

* **Ganancia Proporcional ($K_p$):** `0.8`
* **Tiempo de Integración ($T_i$):** `25.0 s`
* **Tiempo Derivativo ($T_d$):** `1.5 s`

> **💡 Justificación para tu captura:** Como el requerimiento nos da un margen generoso de **2 minutos**, priorizamos la estabilidad absoluta. Un tiempo integral de 20 a 25 segundos evita que el controlador se desespere por el retraso de la planta, logrando un asentamiento suave y seguro sobre el Setpoint en aproximadamente **45 a 60 segundos**.

---

# 📸 Checklist para tus Capturas de Pantalla en el Foro

Cuando abras la ventana de **Medición** del `PID_Compact` para tomar tus evidencias, asegúrate de cumplir con lo que pide el instructor:

1. **Modo Online:** El PLC o PLCSIM debe estar en Run, y el lazo PID en **Modo Automático** (revisa que la línea verde de monitorización esté activa).
2. **Uso de Cursores:** Haz clic en la gráfica para activar los **dos cursores verticales** (las líneas de medición de tiempo). Pon el *Cursor 1* exactamente en el flanco donde cambiaste la consigna, y el *Cursor 2* en el punto donde la señal verde ya se estabilizó de forma permanente dentro de los parámetros. La casilla de diferencia de tiempo ($\Delta t$) demostrará visualmente que cumpliste los <10 segundos (para la PT2) y los <2 minutos (para la PT3).
3. **Cuadro de Parámetros PID:** Asegúrate de que en la parte inferior o lateral de la captura se alcancen a ver los valores numéricos de $K_p$, $T_i$ y $T_d$ que utilizaste.
