# 📊 Tipos de Datos

Esta guía resume los tipos de datos fundamentales utilizados en la programación de PLCs Siemens bajo el entorno TIA Portal, basándose en la configuración estándar de registros.

---

## 💡 Tipos de Datos Definidos

### 1. BOOL / BIT 🟢
Representan variables de dos estados (TRUE/FALSE). Son la base de la lógica digital.
* **Uso:** Señales de sensores, interruptores, activación de relés.
* **Tamaño:** 1 bit.
* **Ejemplo:** `%Q0.1` (Salida 0.1).

### 2. BYTE 📦
Agrupa 8 bits consecutivos. Permite manipular datos de entrada/salida en paquetes de 8.
* **Uso:** Lectura de bloques de entradas digitales o envío de señales de control agrupadas.
* **Rango:** 0 a 255.
* **Ejemplo:** `%IB1` (Byte de entrada 1).

### 3. WORD 🔡
Bloque de 16 bits. Se utiliza para representar valores hexadecimales o de control.
* **Uso:** Gestión de datos de comunicación o configuración de registros.
* **Rango:** 0 a 0xFFFF (hexadecimal).
* **Ejemplo:** `%MW2` (Marca Word 2).

### 4. INT / UINT (Integer / Unsigned Integer) 🔢
Valores enteros de 16 bits.
* **INT:** Permite valores negativos (-32,768 a 32,767).
* **UINT:** Solo positivos (0 a 65,535).
* **Uso:** Contadores, posiciones de encoder simples.
* **Ejemplo:** `%QW0` (Salida Word 0).

### 5. DINT / UDINT (Double Integer) 🏗️
Valores enteros de 32 bits para mayor rango.
* **DINT:** -2,147,483,648 a 2,147,483,647.
* **UDINT:** 0 a 4,294,967,295.
* **Uso:** Contadores de alta precisión, cálculos grandes.
* **Ejemplo:** `%QD1` (Salida DINT 1).

### 6. REAL / FLOAT 📈
Números con decimales utilizando norma IEEE 754.
* **Uso:** Medidas analógicas (temperatura, presión, nivel).
* **Tamaño:** 32 bits.
* **Ejemplo:** `%MD2` (Marca DINT/Real 2).

### 7. TIME ⏱️
Variables de tiempo. Utilizan el prefijo `T#`.
* **Uso:** Temporizadores, control de ciclos de proceso.
* **Tamaño:** 32 bits.
* **Ejemplo:** `T#5s`, `T#2m30s`, `%MD0`.

---

## 📋 Cuadro Comparativo de Direccionamiento

| Tipo de Dato | Tamaño (Bits) | Ejemplo Direccionamiento | Rango Típico |
| :--- | :---: | :--- | :--- |
| **BOOL** | 1 | `%Q0.1` | TRUE / FALSE |
| **BYTE** | 8 | `%IB1` | 0 a 255 |
| **WORD** | 16 | `%MW2` | 0 a 0xFFFF |
| **INT** | 16 | `%QW0` | -32,768 a 32,767 |
| **UINT** | 16 | `%QW0` | 0 a 65,535 |
| **DINT** | 32 | `%QD1` | ±2.14 x 10^9 |
| **REAL** | 32 | `%MD2` | Decimales |
| **TIME** | 32 | `%MD0` | T#... |

*Nota: La sintaxis de direccionamiento `%R[Tabla][Tamaño][Número]` varía según el tipo de registro (R = I, Q, M) 
