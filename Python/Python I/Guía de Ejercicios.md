# 📋 Fundamentos de Python para Ingeniería

---

## 🏗️ PY1-0309 – Variables

### 1. Registro de peso de pieza industrial ⚖️
Una empresa necesita registrar el peso de una pieza antes de su procesamiento.
* **Pistas:** `input()`, `print()`
* **Ejemplo:**
    * Ingrese el peso de la pieza en kg: `24.7`
    * *Resultado:* La pieza pesa 24.7 kg

### 2. Ficha técnica de una máquina ⚙️
Guardá en variables el nombre de una máquina, su tiempo de uso diario y consumo energético.
* **Pistas:** variables, f-string `print(f"texto {variable}")`
* **Ejemplo:**
    * Máquina: Compresor A
    * Horas de uso: 6
    * Consumo energético: 45.8
    * *Resumen:* La máquina Compresor A operó 6 horas y consumió 45.8 kWh

### 3. Presión de entrada y salida de una bomba 🔄
Solicitá la presión de entrada y de salida de una bomba hidráulica.
* **Pistas:** `input()`, variables
* **Ejemplo:**
    * Presión de entrada: 85 psi
    * Presión de salida: 120 psi

---

## 🗂️ PY1-0310 – Tipos de Datos

### 1. Identificación de sensor 📡
Creá variables para representar el nombre de un sensor, su lectura actual (`float`) y si está activo (`bool`).
* **Pistas:** `type()`, `str`, `float`, `bool`
* **Ejemplo:** Sensor: T-1000 | Lectura: 82.5 | Estado: True

### 2. Conversión de lecturas desde consola 🔡➡️🔢
El usuario ingresa una lectura como texto. Convertila a número flotante y mostrá el tipo de dato.
* **Pistas:** `input()`, `float()`, `type()`
* **Ejemplo:** * Lectura ingresada: '78.95'
    * Tipo de dato: `<class 'float'>`

### 3. Cantidad de fallas en lote 📉
Pedí al usuario cuántas fallas detectó en un lote (entero) y sumale 5 por posibles errores no detectados.
* **Pistas:** `int()`, `+`
* **Ejemplo:**
    * Fallas reportadas: 12
    * Total estimado: 17

---

## ➕ PY1-0311 – Operadores Aritméticos

### 1. Cálculo de caudal en tubería 🌊
Cálculo basado en área ($m^2$) y velocidad ($m/s$). **Caudal = Área * Velocidad**.
* **Pistas:** `*`, `float()`
* **Ejemplo:** Área: 0.25 | Velocidad: 3.5 | Caudal: 0.875 $m^3/s$

### 2. Ley de Ohm ⚡
Calculá la corriente eléctrica. **Corriente = Voltaje / Resistencia**.
* **Pistas:** `/`, `float()`
* **Ejemplo:** Voltaje: 120 | Resistencia: 30 | Corriente: 4.0 A

### 3. Producción total del día 🏭
Una máquina produce X piezas por hora. ¿Cuántas hará en 8 horas?
* **Pistas:** `*`, `int()`
* **Ejemplo:** Producción por hora: 120 | Total diario: 960 piezas

---

## ⚖️ PY1-0312 – Comparación

### 1. Verificación de sobrepeso ⚠️
Si el peso de una pieza supera los 50 kg, debe ser revisada.
* **Pistas:** `>`
* **Ejemplo:** Peso: 52 kg | ¿Revisión necesaria? **True**

### 2. Comparar temperaturas entre hornos 🔥
Ingresá la temperatura de dos hornos industriales y mostrá cuál es mayor.
* **Pistas:** `>`
* **Ejemplo:** Horno 1: 670 °C | Horno 2: 695 °C | ¿H1 > H2? **False**

### 3. Chequeo de presión en rango seguro ✅
Una bomba debe trabajar entre 30 y 90 psi.
* **Pistas:** `>=`, `<=`, `and`
* **Ejemplo:** Presión: 45 psi | Estado: **True**

---

## 🧠 PY1-0313 – Operadores Lógicos

### 1. Sensor activo y lectura crítica 🚨
Si `S_Activo` es True y `S_lectura` > 70, `S_Alerta` es True.
* **Pistas:** `and`, `True`
* **Ejemplo:** Activo: True | Lectura: 82 | Alerta: **True**

### 2. Temperatura fuera de zona segura 🌡️
Detectá si la temperatura es menor a 10 o mayor a 80.
* **Pistas:** `or`, `<`, `>`
* **Ejemplo:** Temperatura: 8 | ¿Fuera de rango? **True**

### 3. Comprobación de funcionamiento 🛠️
Mostrá si al menos uno entre una bomba o un compresor está encendido.
* **Pistas:** `or`, `bool`
* **Ejemplo:** Bomba: False | Compresor: True | Sistema operativo: **True**

---

## 📥 PY1-0314 – Entrada y Salida de Datos

### 1. Registro de turno de operario 👤
Pedí nombre y turno. Mostrá un mensaje de bienvenida.
* **Pistas:** `input()`, `print()`
* **Ejemplo:** "Bienvenida, Julia. Estás en el turno Noche."

### 2. Área de plancha metálica 📏
Pedí el largo y el ancho de una plancha y calculá su área.
* **Pistas:** `float()`, `*`
* **Ejemplo:** Largo: 2.5 | Ancho: 1.2 | Área: 3.0 $m^2$

### 3. Evaluación combinada presión y volumen 🧪
Si (presión > 100) Y (volumen < 50), el resultado es True.
* **Pistas:** `and`, `float()`
* **Ejemplo:** Presión: 110 | Volumen: 45 | Resultado: **True**
