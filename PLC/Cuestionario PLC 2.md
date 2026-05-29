# 📝 Cuestionario de Programación de PLCs

Este documento recopila las preguntas de la evaluación con sus respectivas respuestas correctas, organizadas de forma visual para facilitar el repaso técnico.

---

## ⚡ 1. Instrumentación y Sensores

### 🔌 ¿Cuáles son las ventajas de los sensores de corriente frente a los de tensión?

* **Opciones disponibles:**
  * [ ] Son más económicos
  * [ ] Son más pequeños
  * [ ] Tienen mayor inmunidad al ruido electromagnético
  * [ ] Es más fácil conseguirlos
  * [ ] Son eléctricamente estables

* **🟢 Respuesta Correcta:**
  * **Tienen mayor inmunidad al ruido electromagnético** 🛡️
  * **Son eléctricamente estables** ⚖️

---

## 🧠 2. Arquitectura de Controladores (PLCs)

### 💾 ¿Cuáles son las características de la memoria de trabajo?

* **Opciones disponibles:**
  * [ ] Lectura / Escritura
  * [ ] Sólo lectura
  * [ ] Sólo escritura con el equipo de programación
  * [ ] Volátil
  * [ ] 
* **🟢 Respuesta Correcta:**
  * **Lectura / Escritura** 🔄
  * **Volátil** 💨

### 🔢 ¿Cuántos bits componen cada registro?
* **Opciones disponibles:**
  * [ ] 2
  * [ ] 4
  * [ ] 8
  * [ ] 16
  * [ ] 10

* **🟢 Respuesta Correcta:** **8** 🧱 *(Equivale a 1 Byte)*.

---

## 💻 3. Lenguajes de Programación (Norma IEC 61131-3)

### 🔤 ¿Cuáles de los siguientes lenguajes de programación son lenguajes textuales?

* **Opciones disponibles:**
  * [ ] Ladder (Esquema de contactos)
  * [ ] Lista de Instrucciones (IL)
  * [ ] Diagrama de Bloques de Funciones (FBD)
  * [ ] Bloques de Función Secuenciales (SFC)
  * [ ] Texto Estructurado (ST)

* **🟢 Respuesta Correcta:**
  * **Lista de Instrucciones** 📋
  * **Texto Estructurado** ✍️
 
---

## 📊 4. Direccionamiento y Tipos de Datos

### 🏷️ ¿Cuántos bits ocupa una variable con una "W" en la dirección? (Ej: `%IW2`)
* **Opciones disponibles:**
  * [ ] 1
  * [ ] 2
  * [ ] 8
  * [ ] 16
  * [ ] 32

* **🟢 Respuesta Correcta:** **16** 🪙 *(La "W" indica una variable de tipo **Word**, compuesta por 2 Bytes o 16 bits)*.

### 📈 Si tengo una variable cuyos valores irán entre 0 y 82,000. ¿Qué tipo de datos debo utilizar para declararla?

* **Opciones disponibles:**
  * [ ] BYTE (0 a 255)
  * [ ] WORD (0 a 65,535)
  * [ ] INT (-32,768 a 32,767)
  * [ ] UDINT (0 a 4,294,967,295)
  * [ ] BOOL (0 o 1)

* **🟢 Respuesta Correcta:** **UDINT** 🔢 *(Unsigned Double Integer, ideal para enteros grandes sin signo)*.

### 📐 Si tengo una variable cuyos valores tendrán decimales. ¿Qué tipo de datos debo utilizar para declararla?

  * [ ] BOOL
  * [ ] WORD
  * [ ] REAL
  * [ ] INT
  * [ ] TIME

* **🟢 Respuesta Correcta:** **REAL** 🧮 *(Representa números de punto flotante/decimales)*.

---

## 🗃️ 5. Estructuras de Datos Complejas

### 🌡️ En un programa, puedo ver que una variable aparece como `Temperatura[3]`. ¿A cuál de estos grupos pertenece esta variable?

* **Opciones disponibles:**
  * [ ] Estructura
  * [ ] UDT (User Defined Type)
  * [ ] Array

* **🟢 Respuesta Correcta:** **Array** 📦 *(Matriz o arreglo indexado que contiene elementos del mismo tipo de datos)*.
