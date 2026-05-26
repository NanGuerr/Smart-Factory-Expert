# 🧮 Operaciones y Conversiones con Números Binarios 💻

Este documento resume varios ejemplos de conversión entre sistemas numéricos (binario y decimal) y operaciones aritméticas básicas en binario.

---

## ➡️ Conversión de Binario a Decimal

Para convertir un número binario a decimal, multiplicamos cada dígito por la potencia de 2 correspondiente a su posición (empezando desde la derecha, con la posición 0) y sumamos los resultados.

### Ejemplo 1: Convertir `110101`

1.  **Desglose de potencias:** 2️⃣
    * $1 \times 2^5 = 1 \times 32 = 32$
    * $1 \times 2^4 = 1 \times 16 = 16$
    * $0 \times 2^3 = 0 \times 8 = 0$
    * $1 \times 2^2 = 1 \times 4 = 4$
    * $0 \times 2^1 = 0 \times 2 = 0$
    * $1 \times 2^0 = 1 \times 1 = 1$

2.  **Suma final:** ➕
    * $32 + 16 + 0 + 4 + 0 + 1 = \mathbf{53}$

✅ **Resultado:** El número binario `110101` es **53** en decimal.

---

### Ejemplo 2: Convertir `101010101`

Realizamos la suma de las potencias de 2 donde aparece el dígito 1:

* $1 \times 2^8 = 256$
* $0 \times 2^7 = 0$
* $1 \times 2^6 = 64$
* $0 \times 2^5 = 0$
* $1 \times 2^4 = 16$
* $0 \times 2^3 = 0$
* $1 \times 2^2 = 4$
* $0 \times 2^1 = 0$
* $1 \times 2^0 = 1$

🔢 **Suma:** $256 + 64 + 16 + 4 + 1 = \mathbf{341}$

✅ **Resultado:** El número binario `101010101` es **341** en decimal.

---

## ⬅️ Conversión de Decimal a Binario

Para convertir de decimal a binario, utilizamos el método de divisiones sucesivas entre 2, anotando los residuos. El número binario se forma leyendo los residuos de abajo hacia arriba.

### Ejemplo 3: Convertir `27`

1.  **Divisiones:** ➗
    * $27 \div 2 = 13$ (residuo **1**)
    * $13 \div 2 = 6$ (residuo **1**)
    * $6 \div 2 = 3$ (residuo **0**)
    * $3 \div 2 = 1$ (residuo **1**)
    * $1 \div 2 = 0$ (residuo **1**)

✅ **Resultado:** El número decimal `27` es **11011** en binario.

---

### Ejemplo 4: Convertir `100`

1.  **Divisiones:** ➗
    * $100 \div 2 = 50$ (residuo **0**)
    * $50 \div 2 = 25$ (residuo **0**)
    * $25 \div 2 = 12$ (residuo **1**)
    * $12 \div 2 = 6$ (residuo **0**)
    * $6 \div 2 = 3$ (residuo **0**)
    * $3 \div 2 = 1$ (residuo **1**)
    * $1 \div 2 = 0$ (residuo **1**)

✅ **Resultado:** El número decimal `100` es **1100100** en binario.

---

## ➕ Suma Binaria

La suma binaria sigue reglas similares a la decimal, pero solo con dos dígitos (0 y 1). Recordar: $1 + 1 = 10$ (escribimos 0 y llevamos 1 de acarreo).

### Ejemplo 5: Calcular `1010 + 1101`

**Paso a paso:** 🪜

```text
    (acarreo)  1 1 1 0  <-- 🚩
               1 0 1 0
             + 1 1 0 1
             ---------
             1 0 1 1 1
