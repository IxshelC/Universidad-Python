# Diccionario (key:vlaue)

diccionario = {
    "Nombre": "Carlos",
    "Edad" : 13,
    "Signo Zodiacal": "Virgo"
}

print(diccionario)

# Ver la cantidad de elementos
print(len(diccionario))

# Acceder a un elemento ( key)
print(diccionario['Nombre'])

# Otra forma
print(diccionario.get('Edad'))

# Modificar elemento
diccionario["Edad"] = 23
print(diccionario)

# Recorrer los elementos
for termino,valor in diccionario.items():
    print(termino,valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# Comprobar exitencia ede un elemento
print('Nombre' in diccionario)

# Agregar un elemento al diccionario
diccionario ['Color'] = 'Azul'
print(diccionario)

# Eliminar un elemento
diccionario.pop('Color')
print(diccionario)

# Limpiar
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario
print(diccionario)