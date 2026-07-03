# 🏭 Especificación Funcional: Control de Turbina

## 📋 1. Tabla de Variables PLC (Entradas y Salidas)

A continuación, se declaran las variables necesarias para la tabla de variables del PLC, asignando nombres significativos y comentarios técnicos basados en la descripción del sistema.

### 🟢 Entradas Digitales (DI)

| Nombre de Variable | Tipo | Descripción / Comentario |
| --- | --- | --- |
| `Emergencia_R` | Bool | Parada de emergencia tipo hongo (NC) ubicada en el tablero de comando remoto/panel. |
| `Emergencia_L` | Bool | Parada de emergencia tipo hongo (NC) ubicada a pie de máquina (Local). |
| `Selectora_LR` | Bool | Selectora de predisposición de control (0 = Local, 1 = Panel HMI). |
| `Arranque_L` | Bool | Botón NA a pie de máquina para iniciar secuencia de arranque. |
| `Parada_L` | Bool | Botón NA a pie de máquina para iniciar parada controlada. |
| `Sensor_Q1` | Bool | Sensor de llama para verificar encendido del quemador tangencial 1. |
| `Sensor_Q2` | Bool | Sensor de llama para verificar encendido del quemador tangencial 2. |
| `Valvula_Prin` | Bool | Sensor de fin de carrera de válvula principal manual (1 = cuando está cerrada). |
| `Frenos_Aplicados` | Bool | Fin de carrera que confirma si las pastillas de freno están aplicadas. |

### 🔴 Salidas Digitales (DQ)

| Nombre de Variable | Tipo | Descripción / Comentario |
| --- | --- | --- |
| `CDM_Motor` | Bool | Comando para arranque del motor auxiliar de arrastre. |
| `CDM_Junta` | Bool | Comando para accionamiento de la junta neumática que acopla el motor. |
| `CDM_Chispero1` | Bool | Comando para accionamiento del chispero 1. |
| `CDM_Chispero2` | Bool | Comando para accionamiento del chispero 2. |
| `CDM_Frenos` | Bool | Comando de pistón neumático para aplicar las pastillas de frenos. |
| `CDM_Escape` | Bool | Comando de válvula de 2 vías para escape/expulsión de gas en emergencia. |
| `CDM_Emergencia` | Bool | Comando para encender el chispero en la chimenea de emergencia. |
| `CDM_Manual` | Bool | Señal de comando de modo (0 = Fijo/Manual, 1 = Automático) para la válvula. |

### 🎛️ Entradas Analógicas (AI) - *Sin Escalar*

| Nombre de Variable | Tipo | Descripción / Comentario |
| --- | --- | --- |
| `Sens_Velocidad` | Int/Word | Sensor de velocidad genérico mediante conteo rápido. |
| `Sens_Temperatura` | Int/Word | Sensor de temperatura OMRON 653-ES1C-A40. |
| `Sens_Presion` | Int/Word | Sensor de presión salida compresor TELEMECANIQUE XMLP006GC21F. |

### 📈 Salidas Analógicas (AQ)

| Nombre de Variable | Tipo | Descripción / Comentario |
| --- | --- | --- |
| `SP_Velocidad` | Int/Word | Señal de consigna de velocidad automática para el controlador. |
| `SP_Manual` | Int/Word | Señal de consigna manual para el controlador. |

---

## ⚙️ 2. Configuración de Parámetros en Módulos de Hardware

Para integrar correctamente los dispositivos de campo, los módulos en TIA Portal deben configurarse desde la vista de dispositivos con los siguientes parámetros:

* **Módulo de Entradas Analógicas (AI):**

**Tipo de medición:** Seleccionar `Intensidad (Transductor de medida de 4 hilos)`.
**Rango de medición:** Seleccionar `4 a 20 mA`. Esto servirá, por ejemplo, para mapear la velocidad de 0 a 6000 RPM.

* **Módulo de Salidas Analógicas (AQ):**
**Tipo de salida:** Seleccionar `Intensidad`.
**Rango de salida:** Seleccionar `4 a 20 mA`.

* *Nota:* Asegúrate de que las direcciones lógicas `%IW` y `%QW` de estas tarjetas coincidan con las mapeadas en la Tabla de Variables de tu PLC.

---

## 🗂️ 3. Estructura de Bloques de Programa

El programa se organizará modularmente utilizando la siguiente arquitectura de bloques:

### 📜 Bloques de Función (FC)

* **`FC1` (Secuencia):** Contendrá toda la lógica de control de la máquina de estados. Gestionará los pasos de arranque, desde el acople del motor hasta la habilitación del control automático a 4600 rpm , y las rutinas de parada controlada.

* **`FC2` (Seguridad):** Se ejecutará cíclicamente para evaluar las condiciones de parada de emergencia: botón accionado, sobrevelocidad (> 5500 rpm), alta presión (> 5.5 bar o baja presión sostenida), y sobretemperatura (> 350°C).


### 💾 Bloques de Datos (DB)

Se creará un Global Data Block llamado **`DB_Sistemas`** para almacenar el estado general e información estructurada:

* **Estructura `HMI`:**

* `CMD_Arranque` (Bool): Recibe la orden de arranque desde el panel a 350m de distancia.
* `CMD_Parada` (Bool): Recibe la orden de parada controlada desde el panel HMI.

* **Estructura `Lecturas`:**
  
* `Velocidad` (Real): Almacenará el valor ya escalado en RPM.
* `Temperatura` (Real): Almacenará el valor ya escalado en grados Celsius.
* `Presion` (Real): Almacenará el valor ya escalado en bar.

---

## 🔄 4. Tratamiento Analógico y Control de Secuencia

* **Librerías de Escalado:** Utilizaremos los bloques de librería preexistentes `Escalado_AI` (F3) y `Escalado_AQ` (F4). Estos deben arrastrarse al entorno de programación (ej. dentro de un bloque Main u otro FC de escalado) para leer los canales físicos (ej. `Sens_Velocidad`) y escribir el resultado flotante directamente en la estructura `DB_Sistemas.Lecturas`.

* **Variable de Secuencia:** Para organizar los estados del programa dentro del `FC1`, se declarará un arreglo para administrar los pasos actuales de la máquina (por ejemplo, Paso 1: motor auxiliar , Paso 2: chisperos y válvulas al 10%, etc.).

* **Declaración:** Array `[1..6] of Bool`. Cada índice en estado TRUE representará la etapa activa de la secuencia.
