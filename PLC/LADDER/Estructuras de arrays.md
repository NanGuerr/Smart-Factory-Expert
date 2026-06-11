# Estructuras de arrays ↪️

Lógica para inicializar un arreglo (`ArrayDatos`) con cuatro valores enteros y posteriormente realizar una operación de suma acumulada sobre ellos, guardando el resultado en la variable `iSuma`.

A continuación, presento la representación lógica en un diagrama de **Ladder (LD)** que traduce estas operaciones:

### Diagrama Ladder (LD)

El diagrama se divide conceptualmente en dos partes: la **inicialización** de los valores del arreglo y la **operación aritmética**.

```text
NETWORK 1: Inicialización de ArrayDatos
Se cargan los valores constantes en cada posición del arreglo.

     [MOV] INT#2  -----------> [ArrayDatos[0]]
     [MOV] INT#4  -----------> [ArrayDatos[1]]
     [MOV] INT#9  -----------> [ArrayDatos[2]]
     [MOV] INT#10 -----------> [ArrayDatos[3]]

─────────────────────────────────────────────────────────────

NETWORK 2: Suma de elementos
Se suman los elementos del arreglo y el resultado se guarda en iSuma.

     +---------------------------+
     |           ADD             |
     | IN1: ArrayDatos[0]        |
     | IN2: ArrayDatos[1]        |
     | IN3: ArrayDatos[2]        |
     | IN4: ArrayDatos[3]        |
     |                      OUT: |-----( ) iSuma
     +---------------------------+

```

### Explicación del funcionamiento:

1. **Inicialización (Network 1):** El código XML utiliza asignaciones directas de constantes (`INT#2`, `INT#4`, `INT#9`, `INT#10`) a las posiciones del arreglo `ArrayDatos[0]` al `ArrayDatos[3]`. En un entorno Ladder, esto se representa típicamente mediante bloques de transferencia o movimiento (`MOV`).

2. **Operación Aritmética (Network 2):** El bloque `ADD` (definido en el XML como `localId="13"`) toma las cuatro entradas del arreglo y realiza la suma.

3. **Resultado:** La salida del bloque `ADD` se asigna a la variable `iSuma` (`localId="14"`), la cual almacena el valor final de la operación (en este caso, 25).
