# 📊 Guía de Diagnóstico con Buffer y Traces

Esta guía técnica cubre las herramientas fundamentales para la resolución de problemas de alto nivel en PLCs Siemens: el Buffer de Diagnóstico y la función de Traces (Traza).

---

## 🗄️ 1. Buffer de Diagnóstico (Diagnostic Buffer)

Es el "libro de bitácora" o historial de eventos del PLC. Registra cronológicamente todos los sucesos relevantes del sistema.

### Funcionalidad
* **Listado de errores:** Muestra fallos de hardware, errores de programa, cambios de estado (RUN/STOP), y eventos de comunicación.
* **Diagnóstico:** Cada entrada incluye un código de error, fecha, hora exacta y, a menudo, el bloque de organización (OB) que causó el evento.
* **Acceso:** Se accede haciendo doble clic en **"Online & Diagnostics"** sobre el PLC en el árbol del proyecto, y seleccionando "Diagnostic buffer".

---

## 📈 2. Traces (Traza): El Osciloscopio del PLC

La función "Trace" permite grabar el comportamiento de las variables del PLC con una resolución temporal muy alta (incluso ciclo a ciclo). Es ideal para detectar errores esporádicos o problemas de temporización que el monitoreo visual normal no puede captar.

### Componentes de una Configuración de Trace:

#### A. Configuración de Señales
Es la selección de las variables (Tags) que deseas registrar.
* Se pueden elegir tanto variables de memoria (M), como entradas (I), salidas (Q) o variables dentro de bloques de datos (DBs).

#### B. Muestreo (Sampling)
Define la frecuencia con la que el PLC registra el valor de la variable.
* **Ciclo:** Puedes elegir registrar en cada ciclo de Scan del PLC o en un intervalo de tiempo específico.
* **Recurso:** Ten en cuenta que un muestreo muy rápido consume más memoria del PLC y tiempo de ciclo.

#### C. Disparador (Trigger)
Es la "condición de inicio" para comenzar a grabar los datos.
* **Tipos de Disparador:**
    * **Disparador inmediato:** Comienza a grabar tan pronto como se descarga el trace.
    * **Flanco de subida/bajada:** La grabación inicia cuando una señal pasa de 0 a 1 o viceversa.
    * **Nivel:** Inicia cuando la señal alcanza un valor lógico o umbral determinado.
* **Medición del disparador:** Permite ajustar cuánto tiempo antes y después del evento (trigger) deseas ver en la gráfica.

---

## 🛠️ Procedimiento para crear un Trace

1. **Configuración:** En el árbol del proyecto, ve a "Traces" y agrega una nueva configuración.
2. **Selección:** Arrastra las señales que deseas monitorear a la ventana de configuración.
3. **Trigger:** Configura las condiciones de disparo (ej. Iniciar cuando la entrada `I0.0` sea `TRUE`).
4. **Descarga:** Debes descargar la configuración del Trace al PLC.
5. **Activación:** Haz clic en "Start recording".
6. **Análisis:** Una vez capturado el evento, el TIA Portal mostrará gráficas de tiempo. Puedes usar los cursores para realizar **mediciones de tiempo** entre dos puntos específicos de la señal (útil para calcular tiempos de respuesta).

---

## ⚠️ Consejos de experto
* **No ignores el Buffer:** Si el PLC se va a STOP, el buffer de diagnóstico es el primer lugar donde debes buscar la causa (ej. un error de acceso a memoria o tiempo de ciclo excedido).
* **Eficiencia en Traces:** Si necesitas registrar datos por un periodo muy largo, usa **"Long-term trace"** (si tu CPU lo soporta) para no saturar la memoria interna del PLC.
