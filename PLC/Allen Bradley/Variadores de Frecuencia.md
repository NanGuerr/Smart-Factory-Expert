# 📈 Clase 8: Control Analógico y Variadores de Frecuencia (VFD)

La **Clase 8** es una de las más importantes para aplicaciones de control de procesos, ya que abandona el mundo binario (encendido/apagado) para entrar en el control de variables continuas y el manejo de motores mediante variadores de frecuencia (**VFD**) 🚀.

---

### 1. Concepto de Señal Analógica 🌡️
El video explica cómo el PLC interpreta el mundo físico:

* **Señales de entrada:** Sensores que entregan rangos de **4-20 mA** o **0-10 VDC** (presión, temperatura, nivel) 📡.
* **Resolución y Cuantización:** Conversión de la señal física en un número entero que el procesador entienda (ej. de 0 a 32767 unidades o "counts") 🔢.

---

### 2. Escalamiento de Señales 📏
Conversión de "unidades crudas" (*counts*) a unidades de ingeniería (**PSI, °C, RPM**).

* **Instrucción SCL (Scale):** Común en RSLogix 500; en Studio 5000 se suele usar bloques de función (**FBD**) o la ecuación de la recta ($y = mx + b$) 📐.
* **SCP (Scale with Parameters):** Add-On Instruction que facilita definir límites inferiores/superiores y su correspondencia real 🎯.

---

### 3. Control de VFD (Variadores de Frecuencia) ⚙️
Interfaz entre el PLC y un variador (como el **PowerFlex** de Allen Bradley):

**A. Control por Señales Digitales:**
* Salidas digitales para **Start/Stop** y sentido de giro (**Forward/Reverse**) 🔄.
* Configuración de velocidades fijas (pasos de frecuencia) ⏱️.

**B. Control por Señales Analógicas:**
* Salida Analógica del PLC conectada a la referencia del VFD 🔌.
* Variación de frecuencia (**0-60 Hz**) enviando una señal proporcional de **4-20 mA** 📉.

---

### 4. Configuración del Módulo Analógico en Studio 5000 🛠️
Paso a paso para añadir módulos al **I/O Configuration**:

* **Selección del tipo de señal:** Voltaje vs. Corriente ⚡.
* **Filtros:** Configuración para evitar el ruido eléctrico en la señal 🧹.
* **Alarmas integradas:** Configuración de rangos "High-High" o "Low-Low" directamente en el módulo 🚨.

---

### 5. Monitoreo y Diagnóstico 🕵️‍♂️
* **Estatus del Canal:** Detección de fallas como cables rotos (señal < 4mA) ❌.
* **Pruebas de Lazo:** Verificación de que el valor en Studio 5000 coincide con la lectura de un multímetro 🧪.

---

### 6. Aplicación Práctica: Control de Velocidad 🏎️
Ejemplo de escalamiento de un potenciómetro para controlar la velocidad de un motor en tiempo real, observando el cambio de registros en el controlador 📈.

---

### 💡 Concepto Clave de la Clase
El dominio de las señales analógicas permite pasar de una "lógica de contactos" a una **estrategia de control**, permitiendo que las máquinas se adapten suavemente a los cambios del proceso en lugar de operar solo con golpes de encendido y apagado 🌊.
