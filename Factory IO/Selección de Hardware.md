# ⚙️ Selección de Hardware para PLC Siemens

## 💡 Ejemplo: ¿Cómo seleccionamos el hardware para un proyecto?

En el siguiente ejemplo vamos a configurar un PLC para que sea capaz de manejar entradas y salidas adicionales, más allá de las que tiene el equipo base. 

Vamos a insertar los módulos necesarios para poder manejar: 
*   **20 entradas digitales (DI)** 📥
*   **4 salidas digitales (DQ)** 📤
*   **2 entradas analógicas de 4..20 mA (AI, corriente)** 🌡️

---

## 📝 Ejercicios

### 01 - Análisis de Requerimientos 📟
¿Qué equipo y módulos adicionales elegirían para un proyecto que requiere...?

*   **29 entradas digitales (DI)** 📥
*   **4 salidas digitales a transistor (DQ)** 📤
*   **7 salidas digitales a relé (DQ)** 🔌
*   **10 entradas analógicas de 4..20 mA (AI, corriente)** 📈

---

### 02 - Evaluación de Arquitectura 🏗️
Tengo una arquitectura con los siguientes equipos, y en mi escritorio tengo un **1214C DC/DC/DC** para hacer mi proyecto.

**La pregunta clave es:** ¿Me alcanza con sólo el PLC, o debo agregar módulos adicionales? Si debo agregar, ¿cuáles debo agregar?

#### 📋 Lista de componentes:
1.  **4** sensores de proximidad digitales.
2.  **2** fines de carrera simples, NA.
3.  **3** pulsadores NA.
4.  **1** pulsador de emergencia (NC).
5.  **3** lámparas piloto a 24V, 100mA de corriente.
6.  **2** relés auxiliares con bobina de 24v.
7.  **1** sensor de temperatura, rango 0..10v para -10 a 100°C.
8.  **1** comando de velocidad hacia un variador de frecuencia, para control de una bomba. Rango 0 a 10v.

---

### 🧠 Pista para el Ejercicio 02
Para resolverlo, sigue estos pasos:

1.  **Clasifica:** Determina cuáles de los componentes anteriores son **DI** (Entrada Digital), **DQ** (Salida Digital), **AI** (Entrada Analógica) o **AQ** (Salida Analógica).
2.  **Agrupa:** Organiza los grupos por tipo de señal eléctrica.
3.  **Cuenta:** Suma cuántos hay en cada grupo.
4.  **Verifica:** Compara los resultados contra las capacidades de entradas/salidas físicas que trae un PLC 1214C DC/DC/DC de fábrica. ¿Tienes suficiente espacio o necesitas expansión? 🤔

---
*¡Mucho éxito con tu configuración de hardware!* 🚀
