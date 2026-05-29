# 📊 Tipos de Variables 

Este documento resume de manera estructurada la clasificación, tamaños, rangos y direccionamiento de los diferentes **Tipos de Variables** utilizados en la programación de PLCs bajo normativas industriales.

---

## 📌 Guía General de Nomenclatura para Direccionamiento
En la estructura de direccionamiento estándar, la sintaxis general responde a:
* **`R`** ➡️ Tabla de Registro: Entrada (**I**), Salida (**Q**), Marca (**M**).
* **`X`** ➡️ Número de registro inicial.
* **`Y`** ➡️ Número de bit específico (usado en variables booleanas).

---

## 🔘 1. Variables Digitales (1 Bit)

### 🛑 BOOL (Booleana)
Representa señales binarias que solo poseen dos estados físicos o lógicos.
* **📐 Tamaño:** 1 bit.
* **📬 Direccionamiento:** `%RX.Y` *(Ejemplo: `%Q0.1`)*
* **🔢 Valores posibles:** `TRUE` / `FALSE` (1 o 0, ON/OFF).

---

## 📦 2. Variables de Tamaño Byte y Word (8 y 16 Bits)

### 🎒 BYTE
Utilizado para pequeñas cadenas de datos o valores numéricos cortos sin signo.
* **📐 Tamaño:** 8 bits (1 registro completo).
* **📬 Direccionamiento:** `%RBX` *(Ejemplo: `%IB1`)*
* **🔢 Valores posibles:** `0` a `255` en decimal (`0x00` a `0xFF` en hexadecimal).

### 📖 WORD
Tipo de dato de palabra común para mapeo de registros de datos o máscaras de bits.
* **📐 Tamaño:** 16 bits (2 registros).
* **📬 Direccionamiento:** `%RWX` *(Ejemplo: `%MW2`)*
* **🔢 Valores posibles:** `0x0000` a `0xFFFF` en hexadecimal.

### 🔢 INT / UINT (Enteros de 16 Bits)
* **📐 Tamaño:** 16 bits (2 registros).
* **📬 Direccionamiento:** `%RWX` *(Ejemplo: `%QW0`)*
* **📉 INT (Signed - Con Signo):** `-32,768` a `32,767`.
* **📈 UINT (Unsigned - Sin Signo):** `0` a `65,535`.

---

## 🚀 3. Variables de Tamaño Doble Palabra (32 Bits)

### 📚 DWORD (Double Word)
Palabra doble para almacenar datos extensos o configuraciones complejas en formato hexadecimal.
* **📐 Tamaño:** 32 bits (4 registros).
* **📬 Direccionamiento:** `%RDX` *(Ejemplo: `%ID3`)*
* **🔢 Valores posibles:** `0x0000 0000` a `0xFFFF FFFF` en hexadecimal.

### 🔢 DINT / UDINT (Enteros de 32 Bits)
Utilizados cuando el rango de conteo o los valores del proceso superan los límites de los 16 bits.
* **📐 Tamaño:** 32 bits (4 registros).
* **📬 Direccionamiento:** `%RDX` *(Ejemplo: `%QD1`)*
* **📉 DINT (Doble Entero con Signo):** `-2,147,483,648` a `2,147,483,647`.
* **📈 UDINT (Doble Entero sin Signo):** `0` a `4,294,967,295`.

### 📈 REAL / FLOAT (Punto Flotante)
Permite la representación exacta de variables analógicas con valores fraccionarios o decimales (presión, temperatura, caudal). Utiliza la norma **IEC 60559 / IEEE 754-2008** basada en cálculo exponencial.
* **📐 Tamaño:** 32 bits (4 registros).
* **📬 Direccionamiento:** `%RDX` *(Ejemplo: `%MD2`)*
* **🔢 Valores posibles:** `-3.402823466E+38` a `3.402823466E+38` *(Ejemplos: `0.2`, `3.14159`, `45.0`)*.

---

## ⏱️ 4. Variables de Tiempo

### ⏳ TIME
Utilizado para configurar temporizadores (retrasos al encendido/apagado, pulsos). Se introduce mediante el prefijo **`T#`** seguido del valor numérico y la unidad de medida.
* **📐 Tamaño:** 32 bits (4 registros).
* **📬 Direccionamiento:** `%RDX` *(Ejemplo: `%MD0`)*
* **🏷️ Unidades admitidas:** `d` (días), `h` (horas), `m` (minutos), `s` (segundos) y `ms` (milisegundos).
* **🔢 Valores posibles:** Desde valores cortos *(Ejemplos: `T#5s`, `T#2m30s`, `T#3h40m`)* hasta un rango máximo de `T#49d17h2m47s295ms`.

---
