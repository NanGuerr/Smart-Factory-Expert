#  El Lenguaje de Programación LD - Ladder Diagram 

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

```

```text
Archivo Resumen_PLC_Simbologia_Ladder.md generado exitosamente.

```text
    Variable
   --| |--

```

### 🔒 Contacto Normalmente Cerrado (NC)

* **Definición:** Permite el paso libre de la corriente de forma predeterminada mientras la variable booleana asociada permanezca en un estado lógico de `0` (FALSO).
* **Comportamiento:** Cuando la variable cambia su estado a `1` (VERDADERO), el contacto "conmuta" abriéndose, lo que interrumpe de inmediato el paso de la corriente en esa sección del peldaño.
* **Representación esquemática:**
```text
  Variable
 --|/|--

```



### 🟢 Bobina Común (Salida Directa)

* **Definición:** Representa la acción de activación. Se energiza cuando el circuito de contactos a su izquierda completa un camino cerrado continuo.
* **Efecto:** Al energizarse, escribe un `1` lógico en la variable asociada. Si esta variable está vinculada a una salida digital física (por ejemplo, `%Q0.0`), el PLC aplicará voltaje físico en el borne correspondiente para activar un actuador (como una lámpara o un relé).
* **Representación esquemática:**
```text
  Variable
 --( )--

```



### 🔴 Bobina Negada

* **Definición:** Funciona de manera inversa a la bobina común. Permanece energizada (escribiendo un `1` lógico) siempre y cuando **NO** reciba corriente desde el circuito de contactos de su lado izquierdo.
* **Efecto:** Si la lógica anterior del peldaño se vuelve verdadera y le suministra energía, la bobina negada conmuta a cero (`0`), cortando la alimentación de la variable o salida digital asignada.
* **Representación esquemática:**
```text
  Variable
 --(/)--

```



---

## 🎛️ 3. Combinaciones Lógicas Fundamentales

La disposición de los contactos en serie o en paralelo dentro de una *Network* permite estructurar las operaciones de álgebra de Boole básicas:

### 🤝 Combinación AND (Lógica de Serie)

Se logra colocando dos o más contactos de forma consecutiva en la misma línea. Es necesario que **TODOS** los contactos conmuten simultáneamente para permitir el paso de la corriente y energizar la bobina final.

* **Esquema:**
```text
 Boton_1   Boton_2     Lampara
---| |-------| |--------( )

```


* **Tabla de Verdad:**
| Botón 1 | Botón 2 | Lámpara |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |



### 🛣️ Combinación OR (Lógica en Paralelo)

Se configura ramificando o bifurcando las líneas de los contactos en caminos independientes que vuelven a unirse antes de la bobina. Para activar la salida, basta con que **AL MENOS UNO** de los contactos en paralelo conmute y complete un camino de corriente.

* **Esquema:**
```text
   Boton_1
+---| |---+   Lampara
|         |----( )
+---| |---+
   Boton_2

```


* **Tabla de Verdad:**
| Botón 1 | Botón 2 | Lámpara |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 1 |



### 🔄 Combinación XOR (O Exclusiva)

Esta configuración asegura la activación de la salida siempre y cuando uno de los dos componentes esté activo, **pero nunca ambos al mismo tiempo**. Se implementa cruzando contactos abiertos y cerrados en paralelo.

* **Esquema:**
  
```text
   Boton_1   Boton_2
+---| |-------|/|---+   Lampara
|                   |----( )
+---|/|-------| |---+
   Boton_1   Boton_2

```

**Tabla de Verdad:**
| Botón 1 | Botón 2 | Lámpara |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

