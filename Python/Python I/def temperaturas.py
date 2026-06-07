def analizar_temperaturas(lista_temps):
    # Calculamos el promedio
    promedio = sum(lista_temps) / len(lista_temps)
    
    # Obtenemos el mínimo y el máximo
    minima = min(lista_temps)
    maxima = max(lista_temps)
    
    # Contamos cuántas son menores a 22°C
    # Esto crea una sub-lista con los que cumplen la condición y mide su largo
    menores_22 = len([t for t in lista_temps if t < 22])
    
    return (promedio, minima, maxima, menores_22)

def imprimir_reporte(datos_tupla):
    promedio, minima, maxima, cantidad_bajas = datos_tupla
    
    print("--- Resultados ---")
    print(f"Promedio: {promedio:.2f}°C")
    print(f"Mínima:   {minima}°C")
    print(f"Máxima:   {maxima}°C")
    print(f"<22°C:    {cantidad_bajas} menores")
    print("-" * 20 + "\n")

# Listas de prueba proporcionadas
temperaturas1 = [27.1, 22.3, 26.8, 23.5, 22.7, 15.3, 26.6, 16.9, 18.1, 24.7, 23.8, 18.4, 26.1, 27.5, 27.3, 21.9, 25.4, 25.1, 20.4, 16.2, 27.5, 22.7, 25.9, 21.2]
temperaturas2 = [25.4, 21.5, 27.3, 25.5, 20.2, 26.6, 16.1, 27.7, 26.4, 24.0, 22.6, 19.4, 27.0, 18.3, 25.0, 24.3, 25.6, 27.1, 15.6, 27.1, 26.6, 22.7, 20.4, 23.3]
temperaturas3 = [16.4, 20.5, 23.5, 17.3, 26.2, 26.2, 22.9, 21.2, 24.2, 26.0, 18.7, 27.5, 25.0, 22.7, 21.7, 22.7, 23.3, 25.0, 26.7, 18.7, 19.6, 23.9, 20.0, 17.2]

# Ejecución de las pruebas
listas = [temperaturas1, temperaturas2, temperaturas3]

for i, lista in enumerate(listas, 1):
    print(f"Lista {i}:")
    resultados = analizar_temperaturas(lista)
    imprimir_reporte(resultados)
