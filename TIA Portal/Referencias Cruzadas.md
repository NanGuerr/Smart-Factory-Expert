# 📊 Referencias Cruzadas y Desafío 

Esta guía explica el uso de las referencias cruzadas en TIA Portal y presenta una estrategia lógica para resolver el desafío de la secuencia de luces utilizando memoria (Set/Reset).

---

## 🔍 1. ¿Qué son las Referencias Cruzadas (Cross-References)?

Las **referencias cruzadas** son una herramienta de diagnóstico en TIA Portal que permite visualizar dónde y cómo se utiliza cada variable (tag) dentro de tu proyecto. 

### 💡 Usos y Funcionalidades
* **Auditoría de Código:** Identificar si una variable se está escribiendo en múltiples lugares (doble asignación).
* **Depuración (Troubleshooting):** Rastrear el origen de un valor o encontrar qué bloque está activando una salida específica.
* **Refactorización:** Saber qué bloques se verán afectados si decides cambiar el nombre o el tipo de dato de una variable.
* **Navegación:** Saltar directamente a la línea de código o bloque donde se usa la variable.

### 🛠️ ¿Cómo hacerlo en TIA Portal?
1. **Acceso rápido:** Haz clic derecho sobre cualquier variable (tag) en el editor de código o en la tabla de variables.
2. **Selección:** Elige la opción **"Go to" (Ir a)** > **"Cross-reference" (Referencias cruzadas)**.
3. **Ventana de resultados:** Se abrirá la tabla de referencias cruzadas en la parte inferior, mostrando:
    * El bloque donde se usa.
    * El segmento (Network).
    * El tipo de acceso (Lectura, Escritura, Acceso de escritura/lectura).
    * El estado (Online/Offline).

---

## 🚦 2. Desafío TP1-0216: Secuencia de Semáforo

El objetivo es crear una secuencia de luces (Rojo, Amarillo, Verde) usando **Set/Reset** para evitar colisiones de lógica.

### 📝 Estrategia de Implementación
Para cumplir con la restricción de **no usar bobinas comunes** (que pueden sobrescribirse por el ciclo de escaneo), utilizaremos una lógica de pasos (State Machine) con **S/R (Set/Reset)**.

#### Configuración sugerida de Tags:
* `%Q0.0`: Rojo
* `%Q0.1`: Amarillo
* `%Q0.2`: Verde
* Marcas de control de pasos: `%M6.0` (Paso 1), `%M6.1` (Paso 2), `%M6.2` (Paso 3), `%M6.3` (Paso 4).

### 📐 Lógica sugerida (Estructura)

**Paso 1: Rojo (10s)**
* `Set %Q0.0` (Rojo), `Reset %Q0.1`, `Reset %Q0.2`.
* `TON` (Temporizador 10s).
* Al finalizar el `TON`, `Set %M6.1` y `Reset %M6.0`.

**Paso 2: Amarillo Destellante (2Hz, 3s)**
* Usar el **Clock Memory Byte** del PLC (ej. byte `MB1` bit `.2` para 2Hz).
* `Condición:` `(Paso_2 AND Clock_2Hz) -> Set %Q0.1`.
* `Condición:` `(Paso_2 AND NOT Clock_2Hz) -> Reset %Q0.1`.
* Al finalizar el `TON` de 3s, `Set %M6.2` y `Reset %M6.1`.

**Paso 3: Verde (7s)**
* `Set %Q0.2` (Verde), `Reset %Q0.0`, `Reset %Q0.1`.
* `TON` (Temporizador 7s).
* Al finalizar, `Set %M6.3` y `Reset %M6.2`.

**Paso 4: Verde + Amarillo (3s)**
* `Set %Q0.2`, `Set %Q0.1`.
* `TON` (Temporizador 3s).
* Al finalizar, Reset total de pasos para reiniciar el ciclo.

---

## ⚠️ Tips de Oro
1. **Verificación:** Una vez programado, **ejecuta las Referencias Cruzadas** sobre `%Q0.0`, `%Q0.1` y `%Q0.2`. Si ves más de una instrucción de escritura (Write/Set) activa al mismo tiempo sin una lógica de exclusión mutua, tendrás un error de funcionamiento.
2. **Memorias (M10.0 a M10.7):** Si necesitas capturar un flanco (ej. inicio de paso), usa estas marcas para guardar el estado anterior, tal como indica el ejemplo del D.F. (Detector de Flanco) en tu material.
3. **Orden:** Asegúrate de que los `Reset` de los pasos anteriores ocurran simultáneamente con el `Set` del paso actual para garantizar que solo un paso esté activo.
