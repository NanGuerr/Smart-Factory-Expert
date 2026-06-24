# 🚦Configuración de Secuencia y Diagnóstico 

Esta guía es una excelente actividad para consolidar el manejo de estados (State Machine) y herramientas de diagnóstico en TIA Portal. Aquí tienes el procedimiento paso a paso para configurar tu lógica y capturar el diagnóstico para la entrega.

---

## ⚙️ 1. Configuración de la Lógica (OB1)

Para evitar errores de escritura cíclica (el problema de la "última bobina"), utiliza un esquema de **Pasos (Steps)** con marcas de memoria (`M`).

### 📋 Estructura recomendada:
* **M10.0**: Paso 1 (Rojo)
* **M10.1**: Paso 2 (Amarillo)
* **M10.2**: Paso 3 (Verde)
* **M10.3**: Paso 4 (Verde + Amarillo)

### 🧩 Lógica sugerida por segmentos:

* **Segmento 1 (Rojo - 10s):**
    * 🔘 Condición: `Start_Button` -> `Set M10.0`.
    * 💡 Acción: Si `M10.0` está activo, `Set Q0.0` (Rojo).
    * ⏱️ Temporizador: `TON` (PT: 10s). Cuando el temporizador termine (`ET >= PT`), ejecuta `Reset M10.0` y `Set M10.1`.

* **Segmento 2 (Amarillo - 3s a 2Hz):**
    * 💡 Acción: Si `M10.1` está activo, utiliza el **Byte de Marcas de Ciclo** del PLC (configurado en el hardware, ej. `M0.5` para 2Hz).
    * ⚡ Lógica: `(M10.1 AND M0.5) -> Set Q0.1` ; `(M10.1 AND NOT M0.5) -> Reset Q0.1`.
    * ⏱️ Temporizador: `TON` (PT: 3s) activado por `M10.1`. Al terminar, `Reset M10.1` y `Set M10.2`.

* **Segmento 3 (Verde - 7s):**
    * 💡 Acción: Si `M10.2` está activo, `Set Q0.2` (Verde).
    * ⏱️ Temporizador: `TON` (PT: 7s) activado por `M10.2`. Al terminar, `Reset M10.2` y `Set M10.3`.

* **Segmento 4 (Verde + Amarillo - 3s):**
    * 💡 Acción: Si `M10.3` está activo, `Set Q0.2` (Verde) y `Set Q0.1` (Amarillo).
    * ⏱️ Temporizador: `TON` (PT: 3s) activado por `M10.3`. Al terminar, `Reset M10.3` (para reiniciar o detener ciclo).

---

## 📈 2. Configuración del Trace

Para la segunda parte de tu entrega, debes mostrar el *Trace* (el osciloscopio virtual) funcionando correctamente:

1. **Crear el Trace:** En el árbol del proyecto, ve a `Traces` > `Add new trace`.
2. **Señales (Signals):** Agrega las salidas físicas (`Q0.0`, `Q0.1`, `Q0.2`) y las marcas de paso (`M10.0`, `M10.1`, etc.).
3. **Configuración de Muestreo:**
    * ⚙️ Selecciona "Recording cycle" -> "Every scan cycle" para máxima resolución.
    * ⏱️ Duración: Configúralo para al menos **25-30 segundos** (suma de tiempos: 10+3+7+3 = 23 segundos).
4. **Disparador (Trigger):**
    * 🎯 Configura el trigger en **Flanco de subida** de la marca `M10.0` (o tu señal de inicio).
    * Esto garantizará que la grabación comience exactamente cuando inicia el ciclo.
5. **Carga y Ejecución:**
    * 📥 Carga la configuración del Trace al PLC.
    * ▶️ Haz clic en "Start recording".
    * 🚀 Inicia tu secuencia en el PLC.
    * ⏹️ Una vez terminada la secuencia, detén el Trace.

---

## ✅ 3. Verificación Final (Tips de cumplimiento)

Antes de tomar la captura final, sigue estos consejos:

* **🔎 Referencia Cruzada:** Haz clic derecho en `Q0.0`, `Q0.1` y `Q0.2` y selecciona *Go to -> Cross-reference*. Asegúrate de que no haya instrucciones de escritura (`=`) en otros segmentos. Solo deben aparecer las instrucciones `S` (Set) y `R` (Reset).
* **⚠️ Comportamiento del Amarillo:** La única forma de manejar el led amarillo en varios lugares (o estados) sin conflictos es **no usar bobinas comunes**. Al usar Set/Reset y exclusión de pasos, evitas que el PLC sobrescriba la salida.
* **📸 Captura:** Organiza tu pantalla dividiendo el TIA Portal: el código (OB1) a la izquierda y el gráfico del Trace (donde se ven los estados ON/OFF de las salidas) a la derecha, para que todo aparezca en una sola imagen.
