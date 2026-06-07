# Lecturas del sensor
temperaturas = [28, 29, 31, 27, 33, 29, 30, 31, 32, 28]

# Límite crítico
umbral = 30

# --- COMPRENSIÓN DE LISTAS ---
# Estructura: [valor for valor in lista if condicion]
temperaturas_anormales = [t for t in temperaturas if t > umbral]

# Resultado para el operador
print("--- REPORTE ---\n")
if temperaturas_anormales:
    print(f"Hay {len(temperaturas_anormales)} valores que superan el límite:")
    print(f"Temperaturas: {temperaturas_anormales}")
else:
    print("Todos los sensores operan bajo el límite establecido.")
