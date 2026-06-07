# 🏭 Comunicación Industrial (PLC & VFD) 🚀

## 🌐 1. Configuración de Red IP para Programación
**Escenario:** Tenemos un PLC con la dirección IP `192.168.0.10` y máscara `255.255.255.0`.

**Pregunta:** ¿Qué dirección sería la mejor elección para darle a mi PC de programación y así poder estar en la misma red que el PLC habilitando la comunicación? 💻🔌

- ❌ 192.168.0.10 (Conflicto de IP)
- ❌ 192.168.0.300 (Fuera de rango)
- ❌ 255.255.255.0 (Es una máscara, no una IP)
- ❌ 197.200.10.10 (Red diferente)
- ❌ 192.168.0.1
- ✅ **192.168.0.237** (Respuesta Correcta)
- ❌ 10.1.0.10 (Red diferente)

---

## 📑 2. Mapeo de Áreas de Memoria y Códigos de Función (FC) Modbus
A continuación, se detalla el código de función utilizado para leer datos en cada área: 📑🔢

| Área de Memoria | Rango de Direcciones | Código de Función (FC) |
| :--- | :--- | :--- |
| **Coils** (Bobinas) 🟢 | 1 - 10000 | **FC 01** |
| **Discrete Inputs** (Entradas) 📥 | 10001 - 20000 | **FC 02** |
| **Input Registers** (Registros de Entrada) 📊 | 30001 - 40000 | **FC 04** |
| **Holding Registers** (Registros de Retención) 💾 | 40001+ | **FC 03** |

---

## ⚡ 3. Caso Práctico: Variador de Frecuencia (VFD) Siemens SINAMICS V20
El objetivo es mostrar la velocidad en **RPM** del equipo mediante un script de Python. El equipo en cuestión es el siguiente: cache.industry.siemens.com. 🐍⚙️

**Datos relevantes para la comunicación (Manual pág. 133):**

- 📂 **Registro Modbus:** 40**025**
- 📉 **Límite inferior de la medición:** -16250
- 📈 **Límite superior de la medición:** 16250
- 🔍 **FC que debo usar para lectura:** FC 0**3**
- 📏 **Offset (respecto a 40001):** **24**
- 🔢 **Cantidad de registros a leer:** **1**

---
_Documento generado para fines de capacitación técnica en automatización industrial._ 🛠️🤖
