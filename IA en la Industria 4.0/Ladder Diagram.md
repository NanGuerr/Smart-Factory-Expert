# 🪜 El Lenguaje de Programación LD - Ladder Diagram

Este documento contiene un resumen completo, estructurado y dedicado exclusivamente a la **Simbología Básica** del lenguaje de contactos o **Ladder (LD)**.

---

## 🔌 1. ¿Qué es el Lenguaje Ladder (LD)?

El lenguaje **Ladder** (o diagrama de contactos) simula la estructura de los esquemas eléctricos tradicionales de control por relés. Es uno de los lenguajes gráficos más populares en la automatización industrial debido a su facilidad de lectura e interpretación.

### 🧱 Estructura de un Programa:
* **Peldaños (Rungs / Networks):** El programa se organiza de forma lineal mediante peldaños lógicos. Puedes agregar tantos peldaños como el proceso requiera.
* **Flujo de corriente simulado:** El lado izquierdo de cada peldaño representa una barra de tensión viva (comúnmente **24 VCC**). La lógica se lee de izquierda a derecha; si existe un camino continuo cerrado por los contactos, la "corriente" fluye hasta activar los elementos del extremo derecho.
* **Componentes:** * **Contactos (Entradas):** Evalúan estados de variables booleanas y condicionales.
  * **Bobinas (Salidas):** Actúan o ejecutan comandos sobre variables físicas o internas basándose en el resultado del peldaño.
  * **Bifurcaciones:** Las líneas de control pueden ramificarse y unirse para realizar operaciones combinacionales complejas.

---

## 🧭 2. Elementos de la Simbología Básica

El lenguaje Ladder se fundamenta en tres bloques elementales de conmutación booleana:

### 🔓 Contacto Normalmente Abierto (NO)
* **Definición:** Bloquea de manera predeterminada el paso de la corriente mientras la variable booleana asociada tenga un estado lógico de `0` (FALSO).
* **Comportamiento:** En cuanto la variable cambia su estado a `1` (VERDADERO), el contacto físicamente "conmuta", cerrándose y permitiendo que la corriente continúe por el peldaño.
* **Representación esquemática:**
