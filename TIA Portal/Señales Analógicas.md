# 📈 Tratamiento de Señales Analógicas

Esta guía detalla cómo gestionar, escalar y configurar señales analógicas (AI y AQ) para una integración profesional.

---

## 🔌 1. Cableado y Direccionamiento
* **Cableado:** Para sensores de 0-10V, conecta el positivo al borne del canal y el negativo a la referencia común (M).
* **Direccionamiento:** Los canales suelen comenzar en la dirección **64** (ej. `%IW64`, `%IW66`).
* **Rango de Trabajo:**
    * **Min:** 0 (0V / 0mA)
    * **Max:** 27648 (10V / 20mA)
    * **Nota:** Valores > 27648 se consideran errores de desbordamiento (Overrange).

---

## 📥 2. Función de Escalamiento AI (Entrada Analógica)
El objetivo es transformar el valor `Raw` (entero) a un valor `Real` (físico).

**Lógica en KOP/SCL:**
1.  **NORM_X:**
    * `MIN`: 0
    * `MAX`: 27648
    * `VALUE`: Canal analógico (ej. `%IW64`)
    * `OUT`: `sensor_normalizado` (Tipo Real, Variable Temporal)
2.  **SCALE_X:**
    * `MIN`: Sensor_Min_Real
    * `MAX`: Sensor_Max_Real
    * `VALUE`: `sensor_normalizado`
    * `OUT`: `valor_escalado_real` (Salida de la función)

---

## 📤 3. Escalamiento de Salidas (AQ) y Signal Boards
Si el PLC no tiene salidas analógicas, debes añadir un **Signal Board** en la vista de dispositivos (Device View) del PLC.

* **Configuración:** Haz clic sobre la Signal Board y configura el modo de salida (Tensión 0-10V o Intensidad 0-20mA).
* **Lógica Invertida (AQ):** Aquí el orden de escalamiento cambia, ya que debemos convertir valor físico a valor entero (Raw).

**Lógica en KOP/SCL:**
1.  **NORM_X:**
    * `MIN`: Comando_Min_Real
    * `MAX`: Comando_Max_Real
    * `VALUE`: `valor_comando_fisico`
    * `OUT`: `valor_normalizado` (Temporal)
2.  **SCALE_X:**
    * `MIN`: 0
    * `MAX`: 27648
    * `VALUE`: `valor_normalizado`
    * `OUT`: `Actuador_QW` (Salida física, Tipo Int)

---

## 💾 4. Parametrización con Bloques de Datos (DB)
Usar un DB para los parámetros es la mejor práctica profesional.

1.  **Crear DB:** Crea un DB llamado `DB_Parametros_Valvula`.
2.  **Estructura:**
    * `Min_Comando` (Real)
    * `Max_Comando` (Real)
    * `Min_Actuador` (Int)
    * `Max_Actuador` (Int)
3.  **Ventaja:** Puedes modificar estos valores **en línea** (Online) mientras la máquina funciona. Si cambias el rango de un sensor o una válvula, no necesitas editar el código ni descargar el proyecto. Solo cambias el valor en el DB y el escalamiento se ajusta instantáneamente.

---

## 💡 Consejos de Experto
* **Seguridad:** Valida siempre que el valor de entrada no supere 27648 antes de escalar para evitar resultados erráticos.
* **Limpieza:** Crea bloques `FC_Escalar_AI` y `FC_Escalar_AQ` reutilizables. Esto mantendrá tu programa principal (OB1) limpio y fácil de leer.
* **Offline vs Online:** La configuración de la Signal Board (Voltaje/Corriente) **requiere una descarga de hardware** al PLC. Planifica esto durante una parada de planta.
