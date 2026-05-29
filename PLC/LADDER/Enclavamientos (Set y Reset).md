# 🎛️ Enclavamientos (Set y Reset)

Este documento presenta un análisis profundo, descriptivo y secuencial sobre las estrategias de retención de señales eléctricas simuladas mediante el lenguaje de contactos (**Ladder Diagram - LD**), basado en el material oficial de **INGELEARN** dictado por Ignacio A. Lavaggi. 🚀

---

## 📚 1. Contexto 

Dentro de la arquitectura del lenguaje Ladder, el control de memorias y estados es un pilar fundamental. 

---

## 🔒 2. Enclavamiento Clásico (Estrategia por Contactos)

El objetivo primordial de un **Enclavamiento** es mantener encendida una señal de salida (por ejemplo, el arranque de un motor eléctrico) de manera permanente, incluso si el estímulo físico inicial (un pulsador mecánico de contacto momentáneo) duró una fracción de segundo.

### 🔌 A. Circuito de Enclavamiento Clásico (Set)
Para lograr la retención sin funciones especiales, se añade en paralelo al pulsador de **Arranque** un contacto Normal Abierto (NO) asociado directamente a la misma variable de la bobina de salida (**Motor**).

#### 🗺️ Diagrama Ladder de Arranque
```text
  Arranque               Motor
───┤ ├───┬───────────────( )───
         │
   Motor │
───┤ ├───┘

```

* **Mecánica Lógica:** Al presionar `Arranque`, la corriente lógica fluye y energiza al `Motor`. Al activarse el `Motor`, su contacto asociado en paralelo se cierra. Cuando el operador suelta el botón `Arranque`, el camino superior se abre, pero la corriente sigue fluyendo a través del contacto del `Motor`, autosustentando el circuito.

### 🛑 B. Circuito de Desactivación (Parada)

Para cortar la alimentación del enclavamiento anterior, es mandatorio introducir una condición de **Parada** en serie dentro de la línea principal del flujo eléctrico. Se utiliza un contacto Normal Cerrado (NC).

#### 🗺️ Diagrama Ladder Completo (Arranque / Parada Clásico)

```text
  Arranque    Parada     Motor
───┤ ├─────────┤/├───────( )───
         │
   Motor │
───┤ ├───┘

```

* **Mecánica Lógica:** Cuando se presiona `Parada`, el contacto `%I` se abre, interrumpiendo todo el camino conductor. La bobina `Motor` se desenergiza (pasa a 0) y su contacto de enclavamiento en paralelo se abre, asegurando que al soltar el botón de parada, el motor permanezca completamente apagado.

---

## 🧠 3. Enclavamientos Mediante Bobinas Especializadas (Set y Reset)

Es posible simplificar los diagramas Ladder y evitar ramificaciones en paralelo utilizando bobinas especializadas que retienen el estado de forma nativa en la memoria del PLC: la bobina **Set (S)** y la bobina **Reset (R)**.

```text
  Arranque         (S) Motor
───┤ ├─────────────[S]───

  Parada           (R) Motor
───┤ ├─────────────[R]───

```

### 🟢 A. Bobina Set (S)

* **Función:** Activa y enclava permanentemente en `1` lógico la variable asignada a ella en el momento exacto en que la línea recibe energía, sin importar si el pulso de entrada fue extremadamente corto.

### 🔴 B. Bobina Reset (R)

* **Función:** Desactiva y fuerza a `0` lógico la variable asignada, interrumpiendo cualquier estado de memoria previo cuando la línea de entrada es conmutada a verdadero.

### ⚖️ Prioridad de Instrucciones

Si tanto la señal de `Arranque` como la de `Parada` se activan de manera simultánea en el mismo ciclo de Scan (por ejemplo, ambos botones físicos presionados a la vez), el PLC resolverá el conflicto basándose en la **jerarquía de lectura**:

> 📐 **Regla de Ejecución:** Tomará prioridad de estado final la instrucción que aparezca posicionada **más abajo** en el diagrama de contactos, ya que el PLC lee los segmentos secuencialmente de arriba hacia abajo y de izquierda a derecha.

---

## 📦 4. Enclavamientos Mediante Bloques de Función (SR / RS)

Para un control visual e integrado de las memorias, la norma IEC 61131-3 define bloques biestables cerrados llamados funciones **SR** y **RS**. Su comportamiento y diferencia radican estrictamente en la prioridad interna ante entradas simultáneas.

### 🏢 A. Bloque SR (Prioridad al Set)

* **Estructura:** Dispone de dos entradas (`S1` y `R`) y una salida (`Q`).
* **Comportamiento Crítico:** Si las entradas de activación y desactivación se energizan en paralelo, el bloque le otorga **prioridad total a la instrucción Set**, manteniendo la salida en `1`.

```text
       ┌───────┐
  S1 ──┤  SR   ├── Q (Motor)
  R  ──┤       │
       └───────┘

```

### 🏢 B. Bloque RS (Prioridad al Reset / Sistema Seguro)

* **Estructura:** Dispone de las entradas (`S` y `R1`) y una salida (`Q`).
* **Comportamiento Crítico:** Si ambas entradas se activan al mismo tiempo, el bloque le otorga **prioridad total al comando Reset**, forzando la salida a `0`.
* 🛡️ **Nota Industrial:** Este bloque es el más utilizado en automatización de maquinaria pesada por motivos de seguridad, garantizando que una orden de parada siempre anule una orden de arranque.

```text
       ┌───────┐
  S  ──┤  RS   ├── Q (Motor)
  R1 ──┤       │
       └───────┘

```

---

## 📊 5. Tabla Comparativa de Comportamiento Dinámico

A continuación se resume el estado de la salida del motor frente a combinaciones simultáneas en los diferentes tipos de enclavamiento estudiados:

| Entrada Arranque (S) | Entrada Parada (R) | Salida (Enclaved Clásico) | Salida (Bloque SR) | Salida (Bloque RS) | ⚙️ Condición Operativa |
| --- | --- | --- | --- | --- | --- |
| `0` | `0` | Estado Anterior | Estado Anterior | Estado Anterior | Sistema estable en reposo o marcha. |
| `1` | `0` | `1` | `1` | `1` | Orden de Arranque procesada. |
| `0` | `1` | `0` | `0` | `0` | Orden de Parada procesada. |
| `1` | `1` | Depende del Orden | **`1` (Prioridad Set)** | **`0` (Prioridad Reset)** | **Entradas Simultáneas en Conflicto.** |

