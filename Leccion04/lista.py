# Creando lista
nombres = ['Juan', 'Carlos', 'Elena', 'María']

# Imprimiendo lista
print(nombres)

# accediendo a los elementos de la lsita
print(nombres[2])
print(nombres[-1])

# Imprimiendo rango
print(nombres[0:2])

# Ir del inicio de la lista sin incluirlo
print(nombres[:3])

# Desde el índice indicado hasta el final
print(nombres[1:])

# Cambiar un valor
nombres[3] = 'Ivonne'
print(nombres)

# Iterar una lista
for nombres in nombres:
    print(nombres)
else:
    print('No existen más nombres en la lista')

# Preguntar el largo de una lista
print(len(nombres))

# Agregar un elemento
nombres = ['Juan', 'Carlos', 'Elena', 'María']
nombres.append('Lorena')
print(nombres)

# Insertar un elemento en un índice en específico
nombres.insert(1, 'Octavio')
print(nombres)

#Remover un elemento
nombres.remove('Octavio')
print(nombres)

# Remover el último valor agregado
nombres.pop()
print(nombres)

# Eliminar en un índice indicado
del nombres[0]
print(nombres)

# Limpiar lista
nombres.clear()
print(nombres)

#  Eliminar de la memoria la lista
del nombres
print(nombres)


