def escalarValores(valor_analogico, minimo_ing=0, maximo_ing=32767, minimo=0.0, maximo=100.0):
    """
    Escala un valor desde un rango de entrada a un rango de salida.
    Equivalente a la función map() de Arduino.
    Calculamos la proporción del valor dentro del rango de entrada
    (valor - min_ing) / (max_ing - min_ing)
    """
    # Aplicamos la fórmula de interpolación lineal
    salida = (valor_analogico - minimo_ing) * (maximo - minimo) / (maximo_ing - minimo_ing) + minimo
    
    return salida

# --- Valor analógico a escalar ---

# Ejemplo 1

rango = escalarValores(16383) 
print(f"Ejemplo (Rango): {rango:.2f} %")

# Ejemplo 2

escalar = escalarValores(256, 0, 1023, 100, 0)
print(f"Ejemplo (Escalar): {escalar:.2f} %")

# Ejemplo 3

distancia = escalarValores(500, 0, 1000, 0, 5)
print(f"Ejemplo (Distancia): {distancia:.2f} cm")

