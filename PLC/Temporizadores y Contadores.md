# ⏱️ Sección Destacada: Temporizadores

### ¿Qué son los Temporizadores?

Son elementos de programación fundamentales que permiten:

* ⏳ Retrasar una señal.
* ⏸️ Mantener una señal activa.
* 🔄 Sincronizar una señal con el resto del programa.

Además, su gran versatilidad permite realizar combinaciones entre ellos para diseñar funciones personalizadas a la medida de cualquier aplicación industrial.

### 🧩 Características Comunes de la Instancia

Al insertar cualquier tipo de temporizador en el programa, comparte la misma estructura de bloque y variables:

* **Instancia:** Se le debe asignar un nombre o identificador único que **no debe repetirse** en todo el programa.
* **IN (Entrada de señal):** Variable de tipo Booleano (`Bool`).
* **Q (Salida de señal):** Variable de tipo Booleano (`Bool`).
* **PT (Preset Time):** Tiempo preestablecido de configuración (`Time`).
* **ET (Elapsed Time):** Tiempo transcurrido durante la cuenta (`Time`).

---

## 🔄 Tipos de Temporizadores Disponibles

El lenguaje LD clasifica los temporizadores en tres tipos principales según su comportamiento dinámico:

| Tipo | Descripción | Función Principal |
| --- | --- | --- |
| **TON** | Retardo a la conexión 🟢 | Demora el encendido de la salida `Q` tras activarse la entrada `IN`. |
| **TOF** | Retardo a la desconexión 🔴 | Mantiene la salida `Q` activa durante un tiempo tras apagarse la entrada `IN`. |
| **TP** | Pulso ⚡ | Genera un pulso en la salida `Q` con una duración exacta igual a `PT`, sin importar los cambios en `IN`. |


---

## 🧮 ¿Qué son los Contadores?

Los contadores son bloques de función que permiten registrar cuántas veces ocurre un evento o transición en el programa. Son ampliamente utilizados en procesos industriales, como el conteo de productos en una cinta transportadora o el control de ciclos de una máquina.

Existen tres tipos principales de contadores:

1. **CTU** (Contador Ascendente / Count Up) 📈
2. **CTD** (Contador Descendente / Count Down) 📉
3. **CTUD** (Contador Ascendente/Descendente / Count Up/Down) 🔄

---

## 🧱 Características y Estructura del Bloque

Al igual que los temporizadores, cada contador requiere una **Instancia única** (un nombre o identificador que no debe repetirse en todo el programa) para almacenar sus variables internas.

### 📥 Entradas del Bloque (Inputs)

* **CU (Count Up):** Entrada booleana para el conteo ascendente. Suma `1` al valor actual con cada flanco de subida (falso a verdadero).
* **CD (Count Down):** Entrada booleana para el conteo descendente. Resta `1` al valor actual con cada flanco de subida.
* **R (Reset):** Entrada booleana que pone el valor de conteo actual (`CV`) directamente en `0` (prioritaria en CTU y CTUD).
* **LD (Load):** Entrada booleana que carga el valor establecido en `PV` directamente dentro del valor actual (`CV`) (utilizada en CTD y CTUD).
* **PV (Preset Value):** Valor preestablecido o meta de conteo (de tipo entero).

### 📤 Salidas del Bloque (Outputs)

* **Q / QU:** Salida booleana de conteo ascendente. Se activa (verdadero) cuando el valor actual (`CV`) es mayor o igual al valor preestablecido (`PV`).
* **QD:** Salida booleana de conteo descendente. Se activa (verdadero) cuando el valor actual (`CV`) es menor o igual a `0`.
* **CV (Counter Value):** Valor actual del conteo (de tipo entero).

---

## ⚙️ Tipos de Contadores y su Funcionamiento

| Tipo | Ícono | Descripción Dinámica |
| --- | --- | --- |
| **CTU** | 📈 | **Contador Ascendente:** Incrementa `CV` con cada pulso en `CU`. Si `CV ≥ PV`, la salida `Q` se enciende. El pin `R` reinicia `CV` a `0`. |
| **CTD** | 📉 | **Contador Descendente:** Decrementa `CV` con cada pulso en `CD`. Si `CV ≤ 0`, la salida `Q` se enciende. El pin `LD` carga el valor de `PV` en `CV`. |
| **CTUD** | 🔄 | **Contador Mixto:** Combina ambas funciones. Posee entradas `CU` y `CD`, y salidas independientes `QU` (para el límite superior) y `QD` (para el límite inferior). |



