# Ejercicio en **TIA Portal** (lenguaje SCL o Function Block reutilizable)

Necesitamos crear una fórmula matemática de mapeo lineal (también conocida como regla de tres o función de escalado) que convierta nuestro porcentaje de comando ($0.0$ a $100.0\%$) al rango de cuentas del PLC ($0$ a $27648$).

La fórmula matemática para este escalado es:

$$\text{QWXX} = \text{TRUNC} \left( \frac{\text{ValorPorcentaje} \times 27648.0}{100.0} \right)$$

A continuación, te muestro cómo armar un **Bloque de Función (FB)** reutilizable en **SCL** que sirve para cualquier salida analógica de tu proyecto.

---

### 💻 Código en SCL para el Bloque Reutilizable (`FB_EscaladoSalida`)

Puedes crear un nuevo Function Block (FB) y escribir el siguiente código optimizado:

```pascal
FUNCTION_BLOCK FB_EscaladoSalida
TITLE = 'Escalado Genérico para Salidas Analógicas'
VERSION : 0.1

VAR_INPUT
    PorcentajeEntrada : REAL;  // Valor de comando de 0.0 a 100.0 %
END_VAR

VAR_OUTPUT
    SalidaAnalogica : INT;     // Valor entero hacia QWXX (0 a 27648)
END_VAR

VAR
    // Variables temporales o internas si se requieren
    CalculoIntermedio : REAL;
END_VAR

BEGIN
    // 1. Asegurar saturación (Clamping) para evitar desbordamientos por valores erróneos
    IF #PorcentajeEntrada < 0.0 THEN
        #PorcentajeEntrada := 0.0;
ELSIF #PorcentajeEntrada > 100.0 THEN
        #PorcentajeEntrada := 100.0;
    END_IF;

    // 2. Aplicar fórmula de conversión lineal a REAL
    #CalculoIntermedio := (#PorcentajeEntrada * 27648.0) / 100.0;

    // 3. Convertir el resultado REAL a INT y asignarlo a la salida del bloque
    #SalidaAnalogica := REAL_TO_INT(#CalculoIntermedio);

END_FUNCTION_BLOCK

```

---

### ⚙️ ¿Cómo utilizarlo en tu proyecto?

1. **Crear el Bloque:** Agrega un nuevo bloque de tipo **Function Block (FB)** en TIA Portal y asígnale el nombre `FB_EscaladoSalida`.
2. **Asignar el Código:** Pega el código SCL anterior dentro del bloque. Al compilar, se generará automáticamente un **Bloc de Datos de Instancia (DB)** asociado.
3. **Llamarlo en el Programa (OB1 o FC):**
* Cada vez que necesites enviar una señal analógica (por ejemplo, la apertura de una válvula o la velocidad de un variador), llamas a este bloque.
* En la entrada `PorcentajeEntrada` colocas tu variable de control (ej. `MD50` o un valor de receta de $0.0$ a $100.0$).
* En la salida `SalidaAnalogica`, direccionas directamente la palabra de salida física de tu hardware, por ejemplo: **`QW64`** o **`QW96`**.
