#1. El enfoque matemático (sum)
#Como True es igual a 1, la función sum() sumará todos los errores automáticamente. Es la forma más eficiente y elegante.
estadoSensores = [True, True, True, False, False, False, True, False, True, False, False, True, True, False, False, True, False, False, False, True,True, False, False, False, True, True, True, False, True, True, True, False, False, True, False, False, False, True,True, False]

# Sumamos los True (errores)
falla = sum(estadoSensores)
# El total de la lista menos los errores nos da los OK
ok = len(estadoSensores) - falla

print(f"OK: {ok}")
print(f"Falla: {falla}")

#2. El enfoque de filtrado (filter)
#Podemos usar la función filter() para crear una sublista que solo contenga los valores que sean True.

# Filtramos solo los elementos que son True
errores_lista = list(filter(None, estadoSensores)) # None usa el valor booleano por defecto

falla = len(errores_lista)
ok = len(estadoSensores) - falla

print(f"OK: {ok}")
print(f"Falla: {falla}")

#3. El enfoque de comprensión de listas
#Este método es muy "Pythonic". Creamos una nueva lista solo con los elementos que cumplen la condición de error y luego medimos su longitud.

# Creamos una lista solo con los elementos que son True
falla = len([s for s in estadoSensores if s is True])
ok = len([s for s in estadoSensores if s is False])

print(f"OK: {ok}")
print(f"Falla: {falla}")

# Imprimir resultados usando if y append
# Creamos listas vacías para separar los estados
lista_ok = []
lista_falla = []

# Recorremos la lista original
for sensor in estadoSensores:
    if sensor == True:
        lista_falla.append(sensor)
    else:
        lista_ok.append(sensor)

# Usamos len() para obtener las cantidades y armar el diccionario
resultados = {
    "OK": len(lista_ok),
    "Falla": len(lista_falla)
}

# Print final con formato textual
print(f"Hay {resultados['OK']} Sensores ok y {resultados['Falla']} Sensores en falla")
