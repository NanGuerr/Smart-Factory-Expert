# 📘 Guía de Ejercicios Ladder – Práctica Industrial

> **Aclaración General:** Para resolver los siguientes ejercicios deberán crear todas las variables necesarias respetando la nomenclatura Siemens. No es obligatorio hacer todos los ejercicios, ¡pero se los recomiendo para que puedan practicar mucho!

---

## 🔌 1) Contactos NA / NC y Combinaciones Lógicas

### 1️⃣ Arranque con condición de seguridad

* **Lógica:** Se implementa un circuito de enclavamiento (autoretención). El motor arranca si el botón de marcha (`I0.0`) está pulsado, no hay sobrecarga (`I0.2` normalmente cerrado para que conduzca cuando esté en 0) y la puerta de seguridad está cerrada (`I0.3` normalmente abierto). La realimentación del propio `Q0.0` mantiene la marcha. El botón de parada (`I0.1` en NC) corta toda la línea.
* **Segmento Ladder:**
```text
--[ I0.0 ]----[ /I0.2 ]----[ I0.3 ]----+----[ /I0.1 ]----( Q0.0 )--
|                                      |
+----[ Q0.0 ]--------------------------+

```



### 2️⃣ Sistema de doble confirmación

* **Lógica:** Se requiere una conexión en serie estricta de ambos pulsadores de las manos para activar la prensa. Si cualquiera de los dos se abre, la salida se apaga inmediatamente.
* **Segmento Ladder:**
```text
--[ I0.4 ]----[ I0.5 ]-----------------------------------( Q0.1 )--

```



### 3️⃣ Modos de operación excluyentes

* **Lógica:** Evaluamos primero que los selectores no estén ambos activos simultáneamente mediante una compuerta lógica o contactos cruzados para la marca de modo válido.
* **Segmento Ladder:**
```text
--[ I0.6 ]----[ /I0.7 ]----------------------------------( M0.1 )-- (Modo Manual válido)
--[ I0.7 ]----[ /I0.6 ]----------------------------------( M0.3 )-- (Modo Auto válido)
--[ M0.1 ] or [ M0.3 ] --[ Selector activo ]------------( Q0.2 )--

```



### 4️⃣ Control de bomba

* **Lógica:** Se requiere un temporizador con retardo a la conexión (`TON`) de 5 segundos activado por el botón de marcha (`I1.0`). Si transcurren los 5 segundos sin interrupción y no hay alarma (`M0.2`), se habilita la marcha con retención.
* **Segmento Ladder:**
```text
--[ I1.0 ]----[ /M0.2 ]-----------------------------------[ TON (IN) ] (PT = 5s)
--[ Timer.Q ]----[ /I1.1 ]----[ /M0.2 ]--------------------+--( Q0.3 )--
|                                                         |
+----[ Q0.3 ]---------------------------------------------+

```



---

## ⚡ 2) Detectores de Flanco

### 1️⃣ Conteo de piezas por sensor

* **Lógica:** Detectar el flanco positivo del sensor óptico (`I1.5`) para generar un pulso de un ciclo que incremente en 1 la variable de conteo (`MD1`) utilizando la función `ADD`.
* **Segmento Ladder:**
```text
--[ P ] (I1.5)-------------------------------------------( M10.0 )--
--[ M10.0 ]---------------------------------------------|[ ADD ]--
                                                         IN1: MD1
                                                         IN2: 1
                                                         OUT: MD1

```



### 2️⃣ Generación de evento único

* **Lógica:** Detectar el flanco negativo (`N`) de la presencia de la caja (`I2.0`) al retirarse de la zona de despacho. Esto dispara un temporizador `TON` de 5 segundos que mantiene activo el pistón (`Q0.6`).
* **Segmento Ladder:**
```text
--[ N ] (I2.0)-------------------------------------------( M1.3 )--
--[ M1.3 ] or [ Q0.6 ]----[ /Timer.Q ]-------------------( Q0.6 )--
--[ Q0.6 ]-----------------------------------------------[ TON ] (PT = 5s)

```



### 3️⃣ Control de acceso

* **Lógica:** Detectar el flanco positivo de la validación de tarjeta (`I2.1`) para activar brevemente la habilitación de acceso (`Q0.7`), asegurando que sea un único pulso por pasada.
* **Segmento Ladder:**
```text
--[ P ] (I2.1)-------------------------------------------( M1.4 )--
--[ M1.4 ]-----------------------------------------------( Q0.7 )--

```



### 4️⃣ Un solo pulsador (Difícil - Tipo Flip-Flop / Toggle)

* **Lógica:** Cada vez que se presiona el botón (`I1.2`), se detecta su flanco positivo (`M100.0`). Cada flanco detectado cambia el estado lógico de la salida de la cinta (`Q0.4`) invirtiéndola respecto al estado anterior.
* **Segmento Ladder:**
```text
--[ P ] (I1.2)-------------------------------------------( M100.0 )--
--[ M100.0 ]---------------------------------------------|[ XOR / NOT Lógica de inversión de Q0.4 ]--

```



---

## 📊 3) Comparadores

### 1️⃣ Control de temperatura

* **Lógica:** Comparar la variable real `MD20` mediante bloques de comparación `>=`.
* **Segmento Ladder:**
```text
--[ >= ] (MD20 >= 40.0)----------------------------------( Q1.0 )-- (Ventilador)
--[ >= ] (MD20 >= 60.0)----------------------------------( Q1.1 )-- (Alarma)

```



### 2️⃣ Ventana de operación

* **Lógica:** Utilizar un bloque de rango o doble comparación para verificar que `MD24` esté entre 5.0 y 20.0 bar.
* **Segmento Ladder:**
```text
--[ >= (MD24 >= 5.0) ]----[ <= (MD24 <= 20.0) ]----------( Q1.2 )--

```



### 3️⃣ Control de nivel de tanque

* **Lógica:** Comparar nivel actual `MD28` con umbrales mínimo y máximo para setear/resear la bomba.
* **Segmento Ladder:**
```text
--[ < (MD28 <= NivelMin) ]-------------------------------( S ) Q1.3 --
--[ > (MD28 >= NivelMax) ]-------------------------------( R ) Q1.3 --

```



### 4️⃣ Supervisión de velocidad

* **Lógica:** Calcular la diferencia absoluta entre `VelocidadReal` (`MD32`) y `Nominal` (`MD36`) y compararla con el margen porcentual permitido.

### 5️⃣ Comparación entre líneas

* **Lógica:** Restar o comparar directamente si `ProduccionLinea1 - ProduccionLinea2 >= 20`.
* **Segmento Ladder:**
```text
--[ >= ] ((MD40 - MD44) >= 20)------------------------( Q1.5 )--

```



---

## ⏱️ 4) Temporizadores

* 🔥 **Retardo en arranque auxiliar:** Contacto de `HornoActivo` (`I2.2`) directo a la entrada de un bloque `TON` (10s), cuya salida activa `Extractor` (`Q1.6`).
* 🛑 **Retardo en parada:** Al abrir `BotonParadaCinta` (`I2.3`), un `TOF` de 5 segundos mantiene energizada la `CintaActiva` (`Q1.7`).
* 🚰 **Válvula temporizada:** Al activarse `OrdenLlenado` (`I2.4`), un bloque `TON` de 3 segundos energiza `ValvulaLlenado` (`Q2.0`) y se autoreetea al cumplirse el tiempo.
* ⏱️ **Pulsación prolongada:** Un `TON` configurado a 5s que evalúa el estado sostenido de `BotonArranqueProlongado` (`I2.5`) para activar `BombaArranque` (`Q2.1`).
* 🚨 **Señal intermitente:** Combinar un temporizador cíclico o tren de pulsos activado mientras `AlarmaActiva` (`I2.6`) esté en nivel alto para destellar la `Baliza` (`Q2.2`).

---

## 🔢 5) Contadores

> **Nota:** En PLC Siemens, el bloque contador ya contabiliza sobre flanco, por lo que no es necesario generar el flanco manualmente para su funcionamiento básico.

* 📦 **Lote de producción:** Usar un bloque `CTU` (Contador ascendente). Entrada de flanco conectada a `SensorConteo` (`I2.7`), valor preseleccionado (`PV`) en 20. La salida del contador activa `LoteCompleto` (`Q2.3`).
* 🏗️ **Control de pallet:** Similar al anterior con `SensorCaja` (`I3.0`) hasta completar la capacidad del pallet (`Q2.4`).
* 📈 **Control de stock:** Usar un bloque `CTUD` (Contador Ascendente/Descendente). `IngresoMaterial` (`I3.3`) incrementa, `EgresoMaterial` (`I3.4`) decrementa, con límite máximo de 20.

---

## 📐 6) Operaciones Aritméticas

* 📊 **Escalado analógico:** Para llevar `IW64` (0–27648) a porcentaje (`MD50`), aplicar la fórmula matemática en bloques: `(IW64 * 100.0) / 27648.0`.
* 🌡️ **Promedio de sensores:** Sumar `MD54 + MD58 + MD62` y dividir el resultado total entre `3.0`, guardando en `PromedioTemp` (`MD66`).
* ⚙️ **Producción horaria:** Multiplicar `CiclosHora` (`MD70`) por `PiezasPorCiclo` (`MW74`) utilizando una función `MUL` para obtener `ProduccionTotal` (`MD76`).
* ⏳ **Tiempo restante:** Utilizar divisiones sucesivas entre 3600 (para obtener `Horas` de `TiempoTotal`) y operaciones módulo `% 3600` divididas entre 60 para los `Minutos`, dejando el resto como `Segundos`.

---

## 🏭 7) Factory I/O (Filling Tank)

**Lógica de Solución:**

1. 🔒 Crear marcas o memorias de control para evitar que el llenado y el vaciado ocurran al mismo tiempo (enclavamiento mutuo).
2. 👆 Detectar el flanco positivo del botón de llenado (para exigir soltar y volver a presionar tal como pide la consigna).
3. ⏲️ Activar la válvula de carga y utilizar un temporizador `TON` calculado en función del caudal lineal de la regleta visual (por ejemplo, si tarda 10 segundos en llegar a 50 litros, configurar el `TON` a 10s por cada comando de llenado).
4. 🔄 Realizar la misma lógica simétrica para el botón de vaciado con su respectivo tiempo proporcional a los 20 litros requeridos.
