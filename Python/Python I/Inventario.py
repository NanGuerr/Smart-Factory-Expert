# Diccionario de inventario actual
productos_stock = {
    'producto1': 15, 
    'producto2': 7, 
    'producto3': 11, 
    'producto4': 5
}

# Definimos el punto de reposición (umbral)
umbral_reposicion = 10

print("--- INVENTARIO ---\n")

# Variable para verificar si encontramos productos bajos
hay_alertas = False

# Recorremos el diccionario usando .items() para obtener clave y valor simultáneamente
for producto, cantidad in productos_stock.items():
    if cantidad < umbral_reposicion:
        print(f"El {producto} stock bajo con {cantidad} unidades.")
        hay_alertas = True

# Mensaje final si todo está en orden
if not hay_alertas:
    print("El stock se encuentra por encima del punto de reposición.")

print("-" * 40)
